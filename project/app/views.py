from django.shortcuts import render

# Create your views here


def home (request):
    try:
        data=request.session['name']
        return render(request,'app/home.html',{'data1':data})
    except:
        return render(request,'app/home.html')
   
def about (request):
    try:
        data=request.session['name']
        return render(request,'app/about.html',{'data1':data})
    except:
        return render(request,'app/about.html')
    
def menu (request):
    try:
        data=request.session['name']
        return render(request,'app/menu.html',{'data1':data})
    except:
        return render(request,'app/menu.html')

def products (request):
    try:
        data=request.session['name']
        return render(request,'app/products.html',{'data1':data})
    except:
        return render(request,'app/products.html')

def review (request):
    try:
        data=request.session['name']
        return render(request,'app/review.html',{'data1':data})
    except:
        return render(request,'app/review.html')

def contact (request):
    try:
        data=request.session['name']
        return render(request,'app/contact.html',{'data1':data})
    except:
        return render(request,'app/contact.html')

def blogs (request):
    try:
        data=request.session['name']
        return render(request,'app/blogs.html',{'data1':data})
    except:
        return render(request,'app/blogs.html')


# def home (request,Data=None):
#     if Data:
#         return render(request,'app/home.html',{'data1':Data})
#     else:
#         return render(request,'app/home.html')

# def about (request,Data=None):
#     if Data:
#         return render(request,'app/about.html',{'data1':Data})
#     else:
#         return render(request,'app/about.html')

# def menu (request,Data=None):
#     if Data:
#         return render(request,'app/menu.html',{'data1':Data})
#     else:
#         return render(request,'app/menu.html')

# def products (request,Data=None):
#     if Data:
#         return render(request,'app/products.html',{'data1':Data})
#     else:
#         return render(request,'app/products.html')

# def review (request,Data=None):
#     if Data:
#         return render(request,'app/review.html',{'data1':Data})
#     else:
#         return render(request,'app/review.html')

# def contact (request,Data=None):
#     if Data:
#         return render(request,'app/contact.html',{'data1':Data})
#     else:
#         return render(request,'app/contact.html')

# def blogs (request,Data=None):
#     if Data:
#         return render(request,'app/blogs.html',{'data1':Data})
#     else:
#         return render(request,'app/blogs.html')

def register (request):
    return render(request,'app/register.html')

def savedata(request):
    Name=request.POST['name']
    Email=request.POST['email']
    Contact=request.POST['contact']
    City=request.POST['city']
    Password=request.POST['password']
    cpassowrd=request.POST['cpassword']
    print(Email)
    print(Contact)
    print(City)
    print(Password)
    print(cpassowrd)
    request.session['name']=Name
    request.session['Email']=Email
    request.session['contact']=Contact
    request.session['city']=City
    request.session['Password']=Password
    request.session['cpass']=cpassowrd
    return render(request,"app/login.html")

def login (request):
    return render(request,'app/login.html')

def logindata (request):
    try:
        emailid=request.POST['email']
        passid=request.POST['password']

        SaveEmailid=request.session['Email']
        SavePasswordid=request.session['Password']
    
        if emailid == SaveEmailid and passid == SavePasswordid :
            savedata=request.session['name']
            request.session.modified=True
            return render(request,'app/home.html',{'data1':savedata})
        else:
            name='details not matched'
            return render(request,'app/login.html', {'data':name})
    except:
        msg='session expiredd .......... !!'
        return render(request,'app/register.html',{'msg':msg})


def logout (request):
    del request.session['Email']
    del request.session['name']
    del request.session['contact']
    del request.session['city']
    del request.session['Password']
    del request.session['cpass']
    request.session.flush() #completly remove from our system
    return render(request,'app/home.html')
