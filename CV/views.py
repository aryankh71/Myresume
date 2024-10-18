from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage


def myresume(request):
    if request.method == 'POST':
        form = CurriculumForm(request.POST, request.FILES)

        if form.is_valid():
            # ذخیره اطلاعات فرم
            person = Person(
                author=request.user,
                gender=form.cleaned_data['gender'],
                summary=form.cleaned_data['summary'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone'],
                telephone=form.cleaned_data['telephone'],
                linkedin_url=form.cleaned_data['linkedin_url'],
                image=form.cleaned_data['image'],
            )
            person.save()

            professional_summary = ProfessionalSummary(
                user=request.user,
                skills=form.cleaned_data['skills'],
                experience=form.cleaned_data['experience'],
                languages=form.cleaned_data['languages'],
                education=form.cleaned_data['education'],
            )
            professional_summary.save()

            job_history = JobHistory(
                user=request.user,
                company_name=form.cleaned_data['company_name'],
                job_title=form.cleaned_data['job_title'],
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                is_current_job=form.cleaned_data['is_current_job'],
                responsibilities=form.cleaned_data['responsibilities'],
                location=form.cleaned_data['location'],
                employment_type=form.cleaned_data['employment_type'],
            )
            job_history.save()

            return redirect('profile', user_id=request.user.id)  # بازگشت به پروفایل کاربر

    else:
        form = CurriculumForm()
    context = {
        'form': form,
        'person' : Person.objects.get(id=1)
    }
    return render(request, 'panel.html', context)


@login_required
def profile(request):
    user = request.user

    resume = ProfessionalSummary.objects.filter(user=user)
    job_history = JobHistory.objects.filter(user=user)
    testimonials_users = User.objects.all()

    success_message = None

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            user_email = user.email

            full_message = f"Message from {user_email}:\n\n{message}"

            email = EmailMessage(
                subject=subject,
                body=full_message,
                from_email=user_email,
                to=['aryankhodakhah@gmail.com'],
                reply_to=[user_email],
            )
            email.send(fail_silently=False)

            success_message = "Message successfully sent!"  # پیام موفقیت پس از ارسال ایمیل

    else:
        form = CommentForm()
    person = Person.objects.filter(author=user)
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'resume': resume,
        'job_history': job_history,
        'person': person,
        'education': Education.objects.all(),
        'testimonials_users': testimonials_users,
        'form': form,  # فرم برای ارسال کامنت
        'success_message': success_message  # پیام موفقیت
    }

    return render(request, 'profile.html', context)


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success_url')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success_url')
            else:
                messages.error(request, "نام کاربری یا رمز عبور نادرست است")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('success_url')

# @login_required
# def Comment(request):
#     success_message = None
#
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             user_email = request.user.email
#
#
#             full_message = f"Message from {user_email}:\n\n{message}"
#
#
#             email = EmailMessage(
#                 subject=subject,
#                 body=full_message,
#                 from_email=user_email,
#                 to=['aryankhodakhah@gmail.com'],
#                 reply_to=[user_email],
#             )
#             email.send(fail_silently=False)
#
#             success_message = "Message successfully sent!"
#
#     else:
#         form = CommentForm()
#
#     return render(request, 'profile.html', {'form': form, 'success_message': success_message})
