from django.shortcuts import render, redirect
from .forms import RegisterHostelUserForm, ComplaintForm, UserInfoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import User_info
from .models import Complaint


@login_required(login_url="/login")
def home(request):
    complaints = Complaint.objects.all()

    try:
        user_ = User_info.objects.get(user=request.user)
    except:
        user_ = None

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Complaint.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'main/home.html', {"complaints": complaints})


@login_required(login_url="/login")
@permission_required("main.add_complaint", login_url="/login", raise_exception=True)
def create_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.person = request.user
            complaint.officer = "officer-1"
            user_info = User_info.objects.get(user=request.user)
            complaint.hostel_name = user_info.hostel_name
            complaint.phone = user_info.phone
            complaint.room = user_info.room
            complaint.save()
            return redirect("/home")
    else:
        form = ComplaintForm()

    return render(request, 'main/create_complaint.html', {"form": form})


@login_required(login_url="/login")
def update_profile(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect("/home")
    else:
        form = UserInfoForm()

    return render(request, 'main/update_profile.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterHostelUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/update_profile')
    else:
        form = RegisterHostelUserForm()

    return render(request, 'registration/sign_up.html', {"form": form})
