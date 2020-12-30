from django.shortcuts import render,redirect
from .models import foodModel,CartModel,OrdersModel
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            aa = User.objects.get(username=username)
        except User.DoesNotExist:
            aa = None
        if aa is not None:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            else:
                return redirect(login)

    return render(request,'login.html')

        
    return render(request,'login.html')

def registerUser(request):
    if request.method=='POST':
        username = request.POST['username']
       
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password==confirmPassword:
            try:
                user = User.objects.get(username=username)
                messages.error(request,'EMAIL EXISTS, TRY ANOTHER')
            except User.DoesNotExist:
                User.objects.create_user(username=username,password=password)
                return redirect(login)
                
        else:
            messages.error(request,'passwords and confirm password does not match')
            return redirect('registerUser')
    return render(request,'registerUser.html')

def dashboard(request):
    try:
        user  = request.user
    except  User.DoesNotExist:
        user = None
    if user.id is not None:
        allFood = foodModel.objects.all()
        context = {
            'foods':allFood
        }
        return render(request,'dashboard.html',context)
    else:
        return redirect('login')
    
def addToCart(request,food_id):
    try:
        user = request.user
    except User.DoesNotExist:
        user = None
    if user.id is not None:
        food = foodModel.objects.get(id = food_id)
        cc = CartModel.objects.create(food_name=food.food_name,food_price=food.food_price,user=user)
        cc.save()
        return redirect('dashboard')

    else:
        return redirect('login')

    


def logout(request):
    auth.logout(request)
    return redirect('login')

def myCart(request):
    try:
        current_user = request.user
    except User.DoesNotExist:
        current_user  =None
    if current_user.id is not None:
        cartItems = CartModel.objects.filter(user = current_user).all()
    

        context  ={
            'cartItems':cartItems

        }
        return render(request,'myCart.html',context)

    else:
        return redirect('login')




def checkout(request):
    try:
        current_user = request.user
    except User.DoesNotExist:
        current_user  =None
    if current_user.id is not None:
        cart_items = CartModel.objects.filter(user = current_user)
        for i in cart_items:
            a = OrdersModel.objects.create(food_name=i.food_name,food_price=i.food_price,user = current_user)

            a.save()
        cart_items.delete()
        return redirect('myOrders')
    else:
        return redirect('login')

        

def myOrders(request):
    try:
        current_user = request.user
    except User.DoesNotExist:
        current_user  =None
    if current_user.id is not None:
        ordered_items = OrdersModel.objects.filter(user=current_user).all()
        context = {
            'ordered_items':ordered_items
        }
        return render(request,'myOrders.html',context)

    else:
        return redirect('login')


