from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Complaint, User_info
from django.contrib.admin.widgets import AdminDateWidget

HOSTEL_CHOICES = (
    ('hostel-1','Hostel-1'),
    ('hostel-2', 'Hostel-2'),
    ('hostel-3','Hostel-3'),
)

CATEGORY_CHOICES = (
    ('Electrical','Electrical'),
    ('Cleanliness', 'Cleanliness'),
    ('Security','Security'),
    ('Water','Water'),
)

class RegisterHostelUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserInfoForm(forms.ModelForm):
    hostel_name = forms.TypedChoiceField(choices=HOSTEL_CHOICES, coerce=str, initial='hostel-1', required=True)
    phone = forms.CharField(max_length=10, required=True)
    room = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User_info
        fields = ["name", "phone", "room", "hostel_name"]

class ComplaintForm(forms.ModelForm):
    category = forms.TypedChoiceField(choices=CATEGORY_CHOICES, coerce=str, initial='hostel-1', required=True)
    # availability = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': '%Y-%M-%D %H:%M'}))
    availability = forms.DateTimeField(widget=forms.SelectDateWidget)


    class Meta:
        model = Complaint
        fields = ["category", "availability", "description" ]


