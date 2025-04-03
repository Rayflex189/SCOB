from django.contrib import admin
from .models import UserProfile, Transaction

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number', 'otp_code', 'imf_code', 'aml_code', 'tac_code', 'vat_code', 'linking_code', 'balance']  # Include balance in the admin list
    search_fields = ['user__username']  # Search by username

    def save_model(self, request, obj, form, change):
        if change:  # Check if the model instance is being updated, not created
            try:
                old_instance = UserProfile.objects.get(pk=obj.pk)
                if old_instance.balance != obj.balance:
                    amount = obj.balance - old_instance.balance
                    description = 'Credit' if amount > 0 else 'Debit'
                    
                    # Print statements for debugging
                    print(f"Admin updated balance for user: {obj.user.username}")
                    print(f"Old balance: {old_instance.balance}, New balance: {obj.balance}")
                    print(f"Transaction type: {description}, Amount: {abs(amount)}")

                    # Create a transaction record
                    Transaction.objects.create(
                        user=obj.user,
                        amount=abs(amount),  # Use absolute value for amount
                        balance_after=obj.balance,
                        description=description
                    )
            except UserProfile.DoesNotExist:
                pass
        super().save_model(request, obj, form, change)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'balance_after', 'timestamp', 'description']  # Specify fields to display in the admin list
    search_fields = ['user__username', 'description']  # Search by user and description
    list_filter = ['timestamp', 'user']  # Add filters for timestamp and user
    ordering = ['-timestamp']

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('image_display',)

    def image_display(self, obj):
        return obj.image.url if obj.image else None
