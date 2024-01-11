from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import SavePost
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,'index.html')

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return HttpResponse('Wrong Credentials')
        
    return render(request,'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        users = User.objects.create_user(name,email,password)
        users.save()
        return redirect("login")
    return render(request,'register.html')

def home(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == 'POST':
        if 'delete' in request.POST:
            post_id = request.POST.get('delete')
            post_to_delete = get_object_or_404(SavePost, id=post_id, author=request.user)
            post_to_delete.delete()
        else:
            title = request.POST.get('title')
            author = request.user
            content = request.POST.get('content')

            post = SavePost(title=title, author=author, content=content)
            post.save()

        return redirect('home')

    saveposts = SavePost.objects.filter(author=request.user).order_by('-post_date')

    return render(request, 'home.html', {'saveposts': saveposts})

def blogs(request):
    blog_posts = SavePost.objects.all()
    return render(request, 'blogs.html', {'blog_posts': blog_posts})

def blog_detail(request, post_id):
    post = get_object_or_404(SavePost, id=post_id)
    return render(request, 'blog_detail.html', {'post': post})

def logout_view(request):
    logout(request)
    return redirect('index') 

