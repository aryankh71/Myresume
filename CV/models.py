from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date


class Person(models.Model):
    STATUS_CHOICES = (
        ('male', 'آقا'),
        ('female', 'خانم')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    gender = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='جنسیت')
    summary = models.TextField(verbose_name='خلاصه حرفه‌ای', blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name='آدرس')
    phone = PhoneNumberField(blank=True, null=True, verbose_name='تلفن همراه')
    telephone = PhoneNumberField(blank=True, null=True, verbose_name='تلفن ثابت')
    # instagram_url = models.URLField(max_length=200, blank=True, null=True, verbose_name='لینک اینستاگرام')
    linkedin_url = models.URLField(max_length=200, blank=True, null=True, verbose_name='لینک لینکدین')
    github_url = models.URLField(max_length=200, blank=True, null=True, verbose_name='لینک گیت هاب')
    instagram_url = models.URLField(max_length=200, blank=True, null=True, verbose_name='لینک اینستاگرام')
    skype_url = models.URLField(max_length=200, blank=True, null=True, verbose_name='لینک اسکایپ')
    telegram_url = models.URLField(max_length=200, blank=True, null=True, verbose_name='لینک تلگرام')
    person_image = models.ImageField(upload_to='%Y-%m-%d', null=True,verbose_name='تصویر پروفایل')
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.author}"

    @property
    def age(self):
        if self.birthday:
            today = date.today()
            age = today.year - self.birthday.year - (
                        (today.month, today.day) < (self.birthday.month, self.birthday.day))
            return age
        return None


class Education(models.Model):
    DEGREE_CHOICES = [
        ('high_school', 'High School'),
        ('associate', 'Associate Degree'),
        ('bachelor', 'Bachelor Degree'),
        ('master', 'Master Degree'),
        ('doctorate', 'Doctorate Degree'),
    ]
    institution = models.CharField(max_length=255, null=True)
    field_of_study = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"


class Languages(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class ProfessionalSummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='professional', default=None)
    skills = models.CharField(max_length=255, verbose_name='مهارت‌ها', blank=True, null=True)
    experience = models.TextField(verbose_name='تجربیات',  null=True)
    career_goals = models.TextField(verbose_name='اهداف حرفه‌ای', null=True)
    # languages = models.TextField(verbose_name='زبان‌ها', blank=True, null=True)
    languages = models.ForeignKey(Languages, on_delete=models.CASCADE, null=True, blank=True,verbose_name='زبان ها')
    education = models.ForeignKey(Education, on_delete=models.CASCADE, verbose_name='تحصیلات', blank=True, null=True)
    summary_image = models.ImageField(upload_to='%Y-%m-%d', blank=True, null=True, verbose_name='تصویر رزومه')

    def __str__(self):
        return f"{self.user}"


class JobHistory(models.Model):
    EMPLOYMENT_TYPE_CHOICES = (
        ('full_time', 'تمام وقت'),
        ('part_time', 'پاره‌وقت'),
        ('contract', 'قراردادی'),
        ('internship', 'کارآموزی'),
        ('telecommuting', 'دورکاری'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_histories', default=None)
    company_name = models.CharField(max_length=255, verbose_name='نام شرکت')
    job_title = models.CharField(max_length=255, verbose_name='عنوان شغلی')
    start_date = models.DateField(verbose_name='تاریخ شروع')
    end_date = models.DateField(verbose_name='تاریخ پایان', blank=True, null=True)
    is_current_job = models.BooleanField(default=False, verbose_name='شغل فعلی')
    responsibilities = models.TextField(verbose_name='مسئولیت‌ها و وظایف', blank=True, null=True)
    achievements = models.TextField(verbose_name='دستاوردها و موفقیت‌ها', blank=True, null=True)
    location = models.CharField(max_length=255, verbose_name='محل کار', blank=True, null=True)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE_CHOICES, verbose_name='نوع استخدام', blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title}"


class Comment(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"