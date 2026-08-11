# 
Vanguard Labs Portfolio – Full Stack Django Project Prompt

Build a modern, production-ready portfolio website called Vanguard Labs using the following stack:

- Backend: Django 5.x
- Database: PostgreSQL (SQLite for local development is acceptable)
- Frontend: HTML5
- Styling: Tailwind CSS
- JavaScript: Vanilla JavaScript (no React, Vue, Angular, or Alpine)
- Icons: Heroicons or Font Awesome
- Animations: CSS animations and Intersection Observer API
- Deployment Ready: Gunicorn + WhiteNoise
- Image optimization and lazy loading enabled

The overall design should feel premium, modern, futuristic, minimal, and creative, inspired by award-winning digital agencies. It should emphasize storytelling rather than simply displaying projects.

---

Branding

Company Name:
Vanguard Labs

Tagline:

«Building Tomorrow's Digital Experiences.»

Theme:

- Dark interface
- Black background
- Soft blue and violet gradients
- White typography
- Smooth glassmorphism cards
- Rounded corners
- Clean spacing
- Responsive on all devices
- Elegant hover animations
- Smooth scrolling
- Animated page transitions
- Custom cursor effects (desktop only)
- Particle background on the landing page
- Professional loading animation

---

Project Structure

Create a scalable Django project.

vanguard_labs/
│
├── core/
├── portfolio/
├── services/
├── team/
├── contact/
├── blog/
├── testimonials/
├── media/
├── static/
├── templates/
├── accounts/
└── dashboard/

Follow Django best practices.

Use:

- Class Based Views where appropriate
- Function Based Views where simpler
- Reusable template partials
- Environment variables
- Custom template tags
- Custom context processors
- Modular CSS organization
- SEO optimization
- Sitemap
- robots.txt
- Open Graph metadata

---

Landing Page

The homepage should include:

Hero Section

Large fullscreen hero.

Animated headline.

Typing animation.

Background particles.

CTA Buttons

- View Projects
- Work With Us

Floating statistics.

Example:

Projects Completed

Clients Served

Years of Experience

Technologies Mastered

---

About Vanguard Labs

Explain the mission.

Animated timeline.

Values section.

Vision section.

Cards with hover animations.

---

Services

Display services as interactive cards.

Examples:

- Web Development
- LMS Development
- CBT Systems
- UI/UX Design
- AI Integration
- Brand Identity
- Business Automation
- Mobile Applications
- API Development
- Cloud Deployment

Each card should have:

Icon

Description

Learn More button

Hover animation

---

Portfolio Section

Dynamic projects loaded from Django Admin.

Each project contains:

- Title
- Slug
- Description
- Client
- Category
- Technologies
- Completion Date
- Cover Image
- Gallery Images
- Live Demo Link
- GitHub Link
- Featured Flag
- Project Duration
- Team Members
- Testimonial
- Results
- Problem Statement
- Solution
- Process
- Lessons Learned

Display using animated masonry/grid layout.

Filtering by:

- Web
- Branding
- AI
- LMS
- CBT
- UI/UX
- Mobile

Search projects instantly with JavaScript.

---

Case Study Page

Each project opens into a beautiful case study page containing:

Hero banner

Overview

Problem

Research

Wireframes

Development Process

Technology Stack

Challenges

Solutions

Results

Gallery

Client Feedback

Next Project navigation

Related Projects

---

Meet the Crew

Dynamic team members.

Each profile contains:

Photo

Name

Role

Biography

Skills

Experience

GitHub

LinkedIn

Portfolio

Social media

Hover animation.

---

Our Process

Timeline:

1. Discovery

2. Research

3. Design

4. Prototype

5. Development

6. Testing

7. Deployment

8. Support

Animated while scrolling.

---

Testimonials

Carousel built using Vanilla JavaScript.

Editable from Django Admin.

Include:

Photo

Client Name

Company

Review

Rating

---

Technologies

Display animated icons for:

Python

Django

PostgreSQL

Docker

AWS

GitHub

JavaScript

Tailwind

HTML

CSS

REST API

Redis

---

Blog

Simple CMS.

Articles editable from admin.

Markdown support.

Categories.

Tags.

Reading time estimation.

Related posts.

---

Contact

Beautiful contact page.

Fields:

Name

Email

Company

Phone

Project Budget

Service Interested In

Project Description

Timeline

File Upload

Form validation using JavaScript.

Store inquiries inside Django Admin.

Optional email notification architecture should be modular so it can be enabled later.

---

Dashboard

Simple admin dashboard showing:

Projects

Messages

Testimonials

Blog posts

Team Members

Analytics cards

Recent activities

Quick actions

---

Search

Global search using Django.

Search:

Projects

Services

Blog

Team

Instant suggestions with JavaScript.

---

Footer

Company information.

Quick links.

Newsletter.

Social icons.

Copyright.

---

Models

Create models for:

Project

ProjectImage

Service

TeamMember

Technology

Category

BlogPost

Tag

ContactMessage

Testimonial

Client

CompanyStats

FAQ

NewsletterSubscriber

SiteSettings

---

Admin

Customize Django Admin.

Use:

Search

Filters

Image previews

Bulk actions

Ordering

Fieldsets

Custom dashboard branding

---

JavaScript Features

Implement using pure JavaScript:

Sticky navigation

Scroll progress bar

Back to top button

Animated counters

Typing effect

Filtering

Project search

Carousel

Lazy loading

Image modal

Theme persistence

Smooth scrolling

Reveal on scroll

Form validation

Loading animation

Notification system

Accordion FAQ

---

Performance

Lazy load images

Compressed assets

Minified CSS

Minified JS

Caching

Static file optimization

Accessibility best practices

SEO optimization

Responsive images

---

Security

CSRF protection

XSS protection

Secure forms

Rate limiting architecture

Environment variables

Proper Django settings separation

---

Deliverables

Generate:

- Complete Django project
- Models
- Views
- URLs
- Templates
- Tailwind integration
- Static assets
- JavaScript modules
- Forms
- Admin customization
- Seed data for demo projects
- Dummy team members
- Example case studies
- README.md with setup instructions
- Clean folder structure
- Well-commented code
- Professional coding standards

The code should be modular, reusable, scalable, easy to maintain, and structured as if it were being built by a senior software engineering team for a real digital agency.
