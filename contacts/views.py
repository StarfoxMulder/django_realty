from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check to see if the user has made an inquiry on this listing previously

        if request.user.is_authenticated:
            user_id = request.POST['user_id']
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquery into this property.  If one of our realtors has not contacted you yet, please call us at (202)-555-5555')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Since we only want the email to send if the save was successful, include it after the .save() method.  Sends to the realtor and company account in the array.
        send_mail(
            'New inquery for '+listing,
            'Sign into the admin panel for more information regarding this listing.',
            'JudeP.Development@gmail.com',
            [realtor_email, 'JudeP.Development@gmail.com'],
            fail_silently=False
        )
        # Confirmation email for the front-end user

        messages.success(
            request, 'Your request has been submitted and one of our realtors will reach out to you shortly.  Thank you for your interest in our properties!')

        return redirect('/listings/'+listing_id)


# For front-end user email notification
"""
        send_mail(
            'Your inquiry for '+listing,
            'Hi '+name+'!  Thank you for yoru interest in our property at ' +
            listing+'.  One of our realtors will reach out to you shortly.',
            'JudeP.Development@gmail.com',
            [email, 'JudeP.Development@gmail.com'],
            fail_silently=False
        )
"""
