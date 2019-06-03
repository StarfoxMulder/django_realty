from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password matches
        if password == password2:
            # Check database for a match to the username variable set above
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, 'That username is taken.  Please try again with a different username.')
                return redirect('register')
            else:
              # Checking database to see if the email is unique
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, 'That email is taken.  Please try again with a different email.')
                    return redirect('register')
                else:
                    # Everything has passed -- additional logic to follow
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after registration
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')

                    # Redirect user to login page after registration
                    user.save()
                    messages.success(
                        request, 'You are now registered and may log in')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # Default code for initial testing of error message
        # These two lines are the totality of the above 'if' conditional
        # messages.error(request, 'Testing error message')
        # return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(
                request, 'Invalid credentials. Username not found or password is incorrect.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
