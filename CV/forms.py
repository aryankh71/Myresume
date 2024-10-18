from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="شماره تلفن نامعتبر است.")


class CurriculumForm(forms.Form):
    # author = forms.ModelChoiceField(queryset=User.objects.all(), label='نویسنده')
    gender = forms.ChoiceField(choices=Person.STATUS_CHOICES, required=False, label='جنسیت')
    summary = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), label='خلاصه حرفه ای')
    address = forms.CharField(label='آدرس')
    phone = PhoneNumberField(label='تلفن همراه', validators=[phone_regex])
    telephone = PhoneNumberField(label='تلفن منزل', validators=[phone_regex])
    instagram_url = forms.URLField(label='آدرس اینستاگرام')
    linkedin_url = forms.URLField(label='آدرس لینکدین')
    github_url = forms.URLField(label='آدرس گیت هاب')
    skype_url = forms.URLField(label='آدرس اسکایپ')
    telegram_url = forms.URLField(label='آدرس تلگرام')
    person_image = forms.ImageField(label='بارگذاری تصویر')
    birthday = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    skills = forms.CharField(label='مهارت')
    experience = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), label='تجربیات')
    languages = forms.ModelChoiceField(queryset=Languages.objects.all(), label='زبان‌ها')
    education = forms.ModelChoiceField(queryset=Education.objects.all(), label='تحصیلات')

    company_name = forms.CharField(label='نام شرکت')
    job_title = forms.CharField(label='عنوان شغلی')
    start_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}), label='تاریخ شروع همکاری')
    end_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}), label='تاریخ پایان همکاری', required=False)
    is_current_job = forms.BooleanField(label='فعالیت در این شغل', required=False)
    responsibilities = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), label='مسئولیت‌ها')
    location = forms.CharField(label='آدرس محل کار')
    employment_type = forms.ChoiceField(choices=JobHistory.EMPLOYMENT_TYPE_CHOICES, required=False, label='نوع استخدام')

    degree = forms.ChoiceField(choices=Education.DEGREE_CHOICES, required=False, label='مدرک تحصیلی')


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'message']