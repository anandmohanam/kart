from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Category, Order, Payment
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
def login_fun(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('account')
        else:
            messages.error(request, "Profile with this email or Password doesn't exist!")

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=email).exists():
                messages.error(request, "Username already taken!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already in use!")
            else:
                user = User.objects.create_user(username=email, first_name=firstname,
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
    return render(request, 'account.html', {'user': user, 'categories': categories, 'photos': photos})


@login_required
def accounts(request,pk):

    user = request.user
    categories = Category.objects.all()
    c = get_object_or_404(Category, id=pk)
    photos = Photo.objects.filter(name=c)
    return render(request, 'account.html', {'user': user, 'categories': categories, 'photos': photos})


@login_required
def order(request, pk):
    myitem = get_object_or_404(Photo, id=pk)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        Order.objects.create(
            user=request.user,
            photo=myitem,
            quantity=quantity,
            ordered_at=datetime.datetime.now()
        )
        return redirect('account')

    return redirect('account')

@login_required
def payment_confirmation(request):
    return render(request, 'payment_confirmation')


@login_required
def payment(request):
    if request.method == 'POST':
        orders = Order.objects.filter(user=request.user)
        total_amount = sum(order.photo.price * order.quantity for order in orders)

        if total_amount > 0:
            payment_method = request.POST.get('paymentMethod')
            shipping_address = request.POST.get('shippingAddress')
            state = request.POST.get('state')
            pin_code = request.POST.get('pinCode')
            phone_number = request.POST.get('phoneNumber')
            landmark = request.POST.get('landmark')
            reminder_note = request.POST.get('reminderNote')

            payment_data = {
                'user': request.user,
                'payment_method': payment_method,
                'shipping_address': shipping_address,
                'state': state,
                'pin_code': pin_code,
                'phone_number': phone_number,
                'landmark': landmark,
                'reminder_note': reminder_note,
                'total_amount': total_amount,
            }

            if payment_method == 'Card':
                payment_data.update({
                    'card_name': request.POST.get('cardName'),
                    'card_number': request.POST.get('cardNumber'),
                    'expiry_date': request.POST.get('expiryDate'),
                    'cvv': request.POST.get('cvv'),
                })
            elif payment_method == 'UPI':
                payment_data.update({'upi_id': request.POST.get('upiId')})

            Payment.objects.create(**payment_data)

            return redirect('success_page')
        else:
            # If total_amount is 0, redirect to account page
            return redirect('account_page')

    # If request.method is not POST, render the payment page with orders and cart total
    orders = Order.objects.filter(user=request.user)
    cart_total = sum(order.photo.price * order.quantity for order in orders)

    return render(request, 'payment.html', {'orders': orders, 'cart_total': cart_total})

@login_required
def mycarts(request):
    orders = Order.objects.filter(user=request.user)

    items_in_cart = {}
    for order in orders:
        photo_id = order.photo.id
        if photo_id in items_in_cart:
            items_in_cart[photo_id]['quantity'] += order.quantity
        else:
            items_in_cart[photo_id] = {
                'photo': order.photo,
                'quantity': order.quantity,
                'price': order.photo.price,
                'ordered_at': order.ordered_at
            }

    cart_total = sum(item['price'] * item['quantity'] for item in items_in_cart.values())

    return render(request, 'mycart.html', {'items_in_cart': items_in_cart.values(), 'cart_total': cart_total})


@login_required
def update(request):
    if request.method == 'POST':
        photo_id = request.POST['photo_id']
        quantity = int(request.POST['quantity'])

        order = Order.objects.filter(user=request.user, photo_id=photo_id).first()
        if order:
            order.quantity = quantity
            order.save()

    return redirect('mycarts')

@login_required
def success_page(request):
    return render(request, 'success_page.html')

@login_required
def delete(request):
    if request.method == 'POST':
        photo_id = request.POST['photo_id']

        order = Order.objects.filter(user=request.user, photo_id=photo_id).first()
        if order:
            order.delete()

    return redirect('mycarts')


def logout_page(request):
    logout(request)
    return redirect('/')
