from django.shortcuts import render , redirect
from .models import *
import random
from django.core.mail import send_mail
from myproject import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.http import JsonResponse,HttpResponse

def index(request):
    product = Product.objects.all()
    return render(request,'index.html',{'product': product })
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')
def detail(request):
    return render(request, 'detail.html')
def shop(request):
    return render(request, 'shop.html')
def signup(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            msg = "user already exist!!"
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password'],
                    profile = request.FILES['profile'],
                    usertype = request.POST['usertype']
                )
                msg1 = "Signup Successfully!!"
                return render(request,'signup.html',{'msg1':msg1})
            
            else:
                msg = "Password & confirm password does not match!!"
                return render(request,'signup.html',{'msg':msg})
            
    else:
        return render(request,'signup.html')
    
@csrf_exempt
def login(request):
    
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
            if user.password == request.POST['password']:
                request.session['email'] = user.email
                request.session['profile'] = user.profile.url
                if user.usertype=="buyer":
                    return redirect('index')
                else:
                    return redirect('sindex')

                
            else:
                msg = "Password is incorrect!!"
                return render(request, 'login.html', {'msg': msg})
        except:
            msg = "Email does not match!!"
            return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'login.html')

def logout(request):
    del request.session['email']
    del request.session['profile']
    return redirect('login')

def fpass(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            otp = random.randint(1001,9999)
            subject = 'OTP For Forgot Password'
            message = 'Hi ' + user.name + ' your OTP for Email Verification is :' + str(otp)
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [user.email,]
            send_mail(subject,message,email_from,recipient_list)
            request.session['email']=user.email
            request.session['otp']=otp
            return render(request,'otp.html')
        except:
            msg = "Email doesn't exist!" 
            return render(request,'fpass.html',{'msg':msg})
    else:
        return render(request,'fpass.html')
    
def otp(request):
    if request.method=='POST':
        try:
            otp = int(request.session['otp'])
            uotp = int(request.POST['uotp'])
            if otp==uotp:
                del request.session['otp']
                return redirect('newpass')
            else:
                msg = "Invalid OTP!!"
                return render(request, 'otp.html', {'msg': msg})
        except:
            pass
    else:
        return render(request,'otp.html')
    
def newpass(request):
    if request.method=='POST':
        try:
            user = User.objects.get(email=request.session['email'])
            if request.POST['npassword']==request.POST['cnpassword']:
                user.password = request.POST['npassword']
                user.save()
                del request.session['email']
                return redirect ('login')
            else:
                msg = "New password & confirm new password doesn't match "
                return render(request,'newpass.html',{'msg':msg})
        except:
            pass
    else:
       return render(request,'newpass.html')

def cpass(request):
    user = User.objects.get(email=request.session['email'])
    if request.method=='POST':
        try:
            
            if user.password==request.POST['opassword']:
                if request.POST['npassword']==request.POST['cnpassword']:
                    user.password = request.POST['npassword']
                    user.save()
                    return redirect ('logout')
                else:
                    msg = "New Password & Confirm New Password Doesn't Match!!"
                    if user.usertype=="buyer":
                       return render (request,'cpass.html',{'msg':msg})
                    else:
                       return render (request,'scpass.html',{'msg':msg})

            else:
                msg = "Old Password Doesn't match!!"
                if user.usertype=="buyer":
                    return render (request,'cpass.html',{'msg':msg})
                else:
                    return render (request,'scpass.html',{'msg':msg})

        except:
            pass
    else:
        if user.usertype=="buyer":
            return render(request,'cpass.html')
        else:
            return render(request,'scpass.html')
        
    
    
def uprofile(request):
    user = User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.name = request.POST['name']
        user.mobile = request.POST['mobile']
        try:
            user.profile = request.FILES['profile']
            user.save()
            request.session['profile']=user.profile.url
            if user.usertype == "buyer":
                return render(request, 'index.html', {'user': user})
            else:
                return render(request, 'sindex.html', {'user': user})

        except:
            if user.usertype == "buyer":
                return render(request, 'uprofile.html', {'user': user})
            else:
                return render(request, 'suprofile.html', {'user': user})

    else:
        if user.usertype == "buyer":
            return render(request, 'uprofile.html', {'user': user})
        else:
            return render(request, 'suprofile.html', {'user': user})



    
# def uprofile(request):
#     user = User.objects.get(email=request.session['email'])
#     if request.method=="POST":
#         user.name = request.POST['name']
#         user.mobile = request.POST['mobile']
#         try:
#             user.profile = request.FILES['profile']
#             user.save()
#             request.session['profile']=user.profile.url
#         except:
#             pass
#         user.save()
#         return redirect('index')
#     else:
#         return render(request,'uprofile.html',{'user':user})

def sindex(request):
    return render(request,'sindex.html')

def add(request):
    user=User.objects.get(email=request.session['email'])

    
    if request.method=="POST":
    
        try:
            Product.objects.create(
                user=user,
                pcategory=request.POST['pcategory'],
                pcompany=request.POST['pcompany'],
                pname=request.POST['pname'],
                pprice=request.POST['pprice'],
                pdesc=request.POST['pdesc'],
                pimage=request.FILES['pimage']

            )
            msg = "product added successfully"
            return render(request, 'add.html',{'msg':msg})
        except:
            msg = "Error in adding product."
            return render(request, 'add.html', {'msg': msg})
    else:
        return render(request,'add.html')
    
def view(request):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.filter(user=user)
    return render(request,'view.html',{'product': product})

def pdetails(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)
    return render(request,'pdetails.html',{'product': product})

def edit(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)
    
    if request.method=="POST":
        product.pname = request.POST['pname']
        product.pprice= request.POST['pprice']
        product.save()

        return redirect('view')
    else:
        return render(request,'edit.html',{'product': product})
    

def delete(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('view')

def addwish(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)

    try:
        Wishlist.objects.create(
            user = user,
            product = product
        )
        return redirect('wish')
    except:
        pass

def wish(request):
    user = User.objects.get(email=request.session['email'])
    wish = Wishlist.objects.filter(user=user)
    return render (request, 'wish.html',{'wish':wish})

def bpdetails(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)
    flag = False
    try:
       wish = Wishlist.objects.get(user=user,product=product)
       flag = True

    except:
        pass
    return render(request,'bpdetails.html',{'product': product,'flag':flag})



def deletewish(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)
    wish = Wishlist.objects.get(product=product)
    wish.delete()
    return redirect('wish')

def addcart(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)

    try:
        Cart.objects.create(
            user = user,
            product = product,
            total = product.pprice,
            qty=1,
            payment=False
        )
        return redirect('cart')
    except:
        pass


def cart(request):
    user = User.objects.get(email=request.session['email'])
    cart = Cart.objects.filter(user=user,payment=False)
    net = 0
    for i in cart:
        net+=i.total
    
    client = razorpay.Client(auth = (settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    payment = client.order.create({'amount': net * 100, 'currency': 'INR', 'payment_capture': 1})

    context = {
                    'payment' : payment,

                }
    return render (request, 'cart.html',{'cart':cart, 'context':context , 'net': net})


def deletecart(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)
    cart = Cart.objects.get(product=product)
    cart.delete()
    return redirect('cart')

def sucess(request):
   
    try:
        user = User.objects.get(email=request.session['email'])
        cart = Cart.objects.filter(user=user)
        for i in cart:
            i.payment=True
            i.save()
            return render(request,'sucess.html',{'cart': cart})
        
    except Exception as e:
        print("*************",e)
        return render(request,'sucess.html')
