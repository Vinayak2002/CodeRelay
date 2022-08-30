from django.shortcuts import render, redirect
from .forms import RegisterHostelUserForm, ComplaintForm, UserInfoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import User_info
from .models import Complaint
import operator

@login_required(login_url="/login")
def home(request):
    complaints = Complaint.objects.all()
    user_specific = []
    for complaint in complaints:
        if complaint.person == request.user:
            user_specific.append(complaint)
        elif complaint.status == "pending" and request.user.username == "officer_1":
            user_specific.append(complaint)
        elif complaint.status == "issue escalted" and request.user.username == "officer_2":
            user_specific.append(complaint)
        elif complaint.status == "issue escalted further" and request.user.username == "officer_3":
            user_specific.append(complaint)
    
    complaints = user_specific
    filtered = None

    try:
        user_ = User_info.objects.get(user=request.user)
    except:
        user_ = None

    if request.method == "POST":

        filter_id = request.POST.get("filter-id")
        
        accept = request.POST.get("complaint-id-accept")
        reject = request.POST.get("complaint-id-reject")
        escalate = request.POST.get("complaint-id-escalate")

        delete = request.POST.get("complaint-id-delete")

        if filter_id == 'hostel_name' and request.user.has_perm("main.change_complaint"):
            filtered = sorted(complaints, key=operator.attrgetter('hostel_name'))

        elif filter_id == "category" and request.user.has_perm("main.change_complaint"):
            filtered = sorted(complaints, key=operator.attrgetter('category'))

        elif filter_id == 'availability' and request.user.has_perm("main.change_complaint"):
            filtered = sorted(complaints, key=operator.attrgetter('availability'))

        elif filter_id == 'created_at' and request.user.has_perm("main.change_complaint"):
            filtered = sorted(complaints, key=operator.attrgetter('created_at'))

        elif accept and request.user.has_perm("main.change_complaint"):
            complaint = Complaint.objects.filter(id=accept).first()
            if complaint and (request.user.has_perm("main.change_complaint")):
                complaint.status = "request accpeted"
                complaint.save()

        elif reject and request.user.has_perm("main.change_complaint"):
            complaint = Complaint.objects.filter(id=reject).first()
            if complaint and (request.user.has_perm("main.change_complaint")):
                complaint.status = "request rejected"
                complaint.save()

        elif escalate and request.user.has_perm("main.change_complaint"):
            complaint = Complaint.objects.filter(id=escalate).first()
            if complaint:
                if request.user.username == "officer_1":
                    complaint.status = "issue escalted"
                if request.user.username == "officer_2":
                    complaint.status = "issue escalted further"
                complaint.save()

        elif delete:
            complaint = Complaint.objects.filter(id=delete).first()
            if complaint and (complaint.person == request.user):
                complaint.delete()


    if filtered is None:
        return render(request, 'main/home.html', {"complaints": complaints, "length": len(complaints)})
    else:
        return render(request, 'main/home.html', {"complaints": filtered, "length": len(filtered)})
    

# @login_required(login_url="/login")
def dashboard(request):
    try:
        complaints = len(Complaint.objects.all())
    except:
        complaints = 216

    try:
        users = len(User.objects.all())
    except:
        users = 25

    return render(request, 'main/base.html', {"complaints": complaints, "users": users})


@login_required(login_url="/login")
@permission_required("main.add_complaint", login_url="/login", raise_exception=True)
def create_complaint(request):
    user_ = None
    try:
        user_ = User_info.objects.get(user=request.user)
    except:
        user_ = None

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
            complaint.status = "pending"
            complaint.save()
            return redirect("/home")
    else:
        form = ComplaintForm()

    return render(request, 'main/create_complaint.html', {"form": form, "users": user_})


@login_required(login_url="/login")
def update_profile(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect("/dashboard")
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
