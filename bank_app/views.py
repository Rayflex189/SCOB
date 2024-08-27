from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import authenticate, login, logout

from .decorators import *
from .forms import *
from .models import *
from .utilis import *


# Create your views here.

def home(request):
    return render(request, 'bank_app/index.html')

@login_required(login_url='loginview')
def analytics(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/analytics.html', context)

@login_required(login_url='loginview')
def bank_transfer(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('imf')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'bank_app/bank_transfer.html', context)

@unauthenticated_user
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('loginview')

    context = {'form': form}
    return render(request, 'bank_app/register.html', context)

@unauthenticated_user
def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('reset_profile')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'bank_app/login.html')

@login_required(login_url='loginview')
def dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user

    doubled_balance = user_profile.balance * 2

    # Check if account is linked
    if not user_profile.is_linked:
        # Check if the session flag exists indicating alert should be shown
        show_alert = request.session.get('show_alert', True)

        if show_alert:
            # Retrieve last refresh time from session and convert to datetime
            last_refresh_str = request.session.get('last_refresh', None)
            if last_refresh_str:
                last_refresh = timezone.datetime.fromisoformat(last_refresh_str)
            else:
                last_refresh = None

            # Check if enough time has passed since last refresh to show the alert
            if last_refresh is None or (timezone.now() - last_refresh) > timedelta(minutes=5):
                request.session['last_refresh'] = timezone.now().isoformat()
                request.session['show_alert'] = True  # Set the flag to show alert
                alert_message = "Link account with the payment system for secure transfer"
            else:
                alert_message = None
        else:
            alert_message = None
    else:
        # If account is linked, no alert message needed
        alert_message = None
        request.session['show_alert'] = False  # Ensure flag is False if account is linked

    # Handling the deposit form submission
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                if not user_profile.is_linked:
                    # If user tries to submit form without linking account, flag an error
                    form.add_error(None, "Please link your account before making a deposit.")
                else:
                    form.save()
                    return redirect('imf')  # Replace with your actual redirection logic
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'alert_message': alert_message,
        'doubled_balance':doubled_balance,
        'form': form,
    }
    return render(request, 'bank_app/dashboard.html', context)

@login_required(login_url='loginview')
@transaction.atomic
def reset_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
            form = UserProfileForm(request.POST,request.FILES, instance=request.user.userprofile)
            if form.is_valid():
                form.save()
                return redirect('otp')  # Redirect to the same page after successful update
            else:
                form = UserProfileForm(instance=request.user.userprofile)

    context = {
                'form': form
            }
    return render(request, 'bank_app/reset_profile.html', context)

@login_required(login_url='loginview')
def otp(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp_code_input = form.cleaned_data['otp']
            # Validate the OTP here (e.g., check if it matches the expected value)
            if validate_otp(otp_code_input, user_profile):  # Define this function based on your validation logic
                # Redirect to success page or dashboard
                return redirect('dashboard')
            else:
                # Handle invalid OTP case
                form.add_error(None, 'Invalid OTP code')
    else:
        form = OTPForm()

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'bank_app/otp.html', context)

@login_required(login_url='loginview')
def imf(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = IMFForm(request.POST)
        if form.is_valid():
            imf_code_input = form.cleaned_data['imf']
            # Validate the OTP here (e.g., check if it matches the expected value)
            if validate_imf(imf_code_input, user_profile):  # Define this function based on your validation logic
                # Redirect to success page or dashboard
                return redirect('aml')
            else:
                form.add_error(None, 'Invalid IMF code')
    else:
        form = IMFForm()

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'bank_app/imf.html', context)

@login_required(login_url='loginview')
def aml(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = AMLForm(request.POST)
        if form.is_valid():
            aml_code_input = form.cleaned_data['aml']
            # Validate the OTP here (e.g., check if it matches the expected value)
            if validate_aml(aml_code_input, user_profile):  # Define this function based on your validation logic
                # Redirect to success page or dashboard
                return redirect('tac')
            else:
                # Handle invalid OTP case
                form.add_error(None, 'Invalid AML code')
    else:
        form = AMLForm()

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'bank_app/aml.html', context)

@login_required(login_url='loginview')
def tac(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = TACForm(request.POST)
        if form.is_valid():
            tac_code_input = form.cleaned_data['tac']
            # Validate the OTP here (e.g., check if it matches the expected value)
            if validate_tac(tac_code_input, user_profile):  # Define this function based on your validation logic
                # Redirect to success page or dashboard
                return redirect('vat')
            else:
                # Handle invalid OTP case
                form.add_error(None, 'Invalid TAC code')
    else:
        form = TACForm()

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'bank_app/tac.html', context)

@login_required(login_url='loginview')
def loans(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/loans.html', context)

@login_required(login_url='loginview')
def vat(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = VATForm(request.POST)
        if form.is_valid():
            vat_code_input = form.cleaned_data['vat']
            # Validate the OTP here (e.g., check if it matches the expected value)
            if validate_vat(vat_code_input, user_profile):  # Define this function based on your validation logic
                # Redirect to success page or dashboard
                return redirect('pending')
            else:
                # Handle invalid OTP case
                form.add_error(None, 'Invalid VAT code')
    else:
        form = VATForm()

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'bank_app/vat.html', context)

@login_required(login_url='loginview')
def pending(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'bank_app/pending.html', context)

@login_required(login_url='loginview')
@transaction.atomic
def linking_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = LinkingCodeForm(request.POST)
        if form.is_valid():
            # Check if the linking code matches
            entered_code = form.cleaned_data['linking_code']
            if entered_code == profile.linking_code:
                messages.success(request, 'Account successfully linked.')
                # Handle linking logic here, e.g., set a flag in UserProfile
                profile.is_linked = True
                profile.save()
                return redirect('dashboard')  # Redirect to dashboard or another view
            else:
                messages.error(request, 'Invalid linking code. Please try again.')
        else:
            messages.error(request, 'Form validation failed. Please check the input.')

    else:
        form = LinkingCodeForm()

    context = {
        'form': form,
        'user_profile': profile
    }
    return render(request, 'bank_app/linking_page.html', context)

@login_required(login_url='loginview')
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/profile.html', context)

@login_required(login_url='loginview')
def kyc(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/kyc.html', context)

@login_required(login_url='loginview')
def coming_soon(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/coming_soon.html')

@login_required(login_url='loginview')
def LogOut(request):
    logout(request)
    return redirect('loginview')