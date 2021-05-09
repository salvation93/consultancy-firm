from django.db import models
# from django.db.models.BigAutoField import DEFAULT_AUTO_FIELD 
import random
from django.urls import reverse
from django.utils import timezone
import time
from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    thumb = models.ImageField()

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hrms:dept_detail", kwargs={"pk": self.pk})

   
class BusinessLogic(models.Model):
    DUTIES = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.DUTIES
  

class Employee(models.Model):
    LANGUAGE = (('english','ENGLISH'),('french','FRENCH'),('arabic','ARABIC'),('spanich','SPANISH'))
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    emp_id = models.CharField(max_length=70, default='emp'+str(random.randrange(100,999,1)))
    thumb = models.ImageField(blank=True,null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=125, null=False)
    address = models.TextField(max_length=100, default='')
    emergency = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER, max_length=10)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    # work = models.ForeignKey(BusinessLogic, on_delete=models.CASCADE, default='select')
    joined = models.DateTimeField(default=timezone.now)
    language = models.CharField(choices=LANGUAGE, max_length=10, default='english')
    account = models.CharField(max_length=10, default='Your bank details')
    bank = models.CharField(max_length=25, default='bank name')
    salary = models.CharField(max_length=16,default='00,000.00')      
    def __str__(self):
        return self.first_name
        
    def get_absolute_url(self):
        return reverse("hrms:employee_view", kwargs={"pk": self.pk})


class Kin(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    occupation = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.first_name+'-'+self.last_name
    
    def get_absolute_url(self):
        return reverse("hrms:employee_view",kwargs={'pk':self.employee.pk})
    

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class Job(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    category = models.CharField(choices=JOB_TYPE, max_length=20)
    date = models.DateTimeField(default=timezone.now)
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="")
    update = models.DateTimeField()
    filled = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.get_full_name()
class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
    date = models.DateField(auto_now_add=True)
    first_in = models.TimeField()
    last_out = models.TimeField(null=True)
    status = models.CharField(choices=STATUS, max_length=15 )
    staff = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def save(self,*args, **kwargs):
        self.first_in = timezone.localtime()
        super(Attendance,self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Attendance -> '+str(self.date) + ' -> ' + str(self.staff)

class Leave (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)

    def __str__(self):
        return self.employee + ' ' + self.start

class Recruitment(models.Model):
    first_name = models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    position = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name +' - '+self.position

class Training(models.Model):
    train_in = models.CharField(max_length=90)

    def __str__(self):
        return self.train_in


class CourseStatus(models.Model):
    specify = models.ForeignKey(Training, on_delete=models.CASCADE, blank=False)
    status = (('active','ACTIVE'),('finished','FINISHED'))

class Course(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    start =  models.DateField(auto_now_add=True)
    end = models.CharField(blank=False, max_length=15)
    deliver_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    statu = models.ForeignKey(CourseStatus, on_delete=models.CASCADE)



