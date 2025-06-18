from django.shortcuts import render, redirect
from .forms import ProposalForm
from django.core.mail import send_mail

PARTNERS = [
    {"name": "BrandX Media", "focus": "Visual Design"},
    {"name": "ContentForge", "focus": "Copywriting"},
    {"name": "Filmify Studios", "focus": "Ad Film Production"},
    {"name": "SEO Experts LLP", "focus": "Digital Marketing"},
]

def home(request):
    services = ["SEO", "Branding", "Rebranding", "Visual Branding", "Ad Film Making", "Content Writing"]
    return render(request, 'core/home.html', {'services': services})

def partners(request):
    return render(request, 'core/partners.html', {'partners': PARTNERS})

def proposal(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'New Proposal Submitted',
                f"Proposal from {form.cleaned_data['name']}, {form.cleaned_data['company']}",
                'noreply@kreatify.com',
                ['admin@kreatify.com'],
                fail_silently=True,
            )
            return redirect('success')
    else:
        form = ProposalForm()
    return render(request, 'core/proposal.html', {'form': form})

def success(request):
    return render(request, 'core/success.html')