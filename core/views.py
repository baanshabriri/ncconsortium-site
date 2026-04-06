# core/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import ContactSubmission

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Save to DB
        ContactSubmission.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )

        # Send email
        send_mail(
            subject="New Contact Form Submission",
            message=f"""
                Name    : {name}
                Email   : {email}
                Phone   : {phone}
                Message : {message}
            """,
            from_email="no-reply@ncconsortium.in",
            recipient_list=["your-email@gmail.com"],
            fail_silently=False,
        )

        return redirect("/")  # or success page

    return render(request, "contact.html")