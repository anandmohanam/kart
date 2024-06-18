from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Category, Order
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_fun(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('account')
        else:
            messages.error(request, "Profile with this username or Password doesn't exist!")

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['email']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already in use!")
            else:
                user = User.objects.create_user(username=username, first_name=firstname,
                                                last_name=lastname, email=email,
                                                password=password)
                user.save()
                messages.success(request, "Profile created successfully.")
                return redirect('/')  # Redirect to login page after successful registration
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'register.html')


@login_required
def account(request):
    user = request.user
    categories = Category.objects.all()
    photos = Photo.objects.all()
    return render(request, 'account.html', {'user': user,'categories': categories, 'photos': photos})


@login_required
def payment(request):
    return render(request, 'payment.html')


def order(request, pk):
    # Retrieve a specific Photo instance by id
    myitem = get_object_or_404(Photo, id=pk)

    if request.method == 'POST':
        # Get quantity from form, default to 1 if not provided
        quantity = request.POST.get('quantity', 1)

        # Create and save the order
        Order.objects.create(
            user=request.user,
            photo=myitem,
            quantity=quantity
        )

        # Redirect to 'mycarts' after placing the order
        return redirect('mycarts')

    # Redirect to 'account' if the request method is not POST
    return redirect('account')


@login_required
def mycarts(request):
    myitem=Order.objects.all()
    print(myitem)

    return render(request,'mycart.html',{'myitem':myitem})


def logout_page(request):
    logout(request)
    return redirect('/')