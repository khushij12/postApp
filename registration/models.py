from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class userInfo(models.Model):
#     username=models.CharField(max_length=10)
#     first_name=models.CharField(max_length=20)
#     last_name=models.CharField(max_length=20)
#     email_id=models.EmailField()
#     phone_no=models.CharField(max_length=10)
#     gender = models.CharField(max_length=20,choices=(("0",'female'),("1",'male')),default="0")
#     password = models.CharField(max_length=10)
#     class Meta:
#         ordering = ('username',) # [-1] for decreasing
#         # abstract=True
#         # app_label='registration' only use when model is declared outside of app mentioned in installed apps
#         # verbose_name = 'registration/login'
#         # proxy = True #used only when this class inherit other class property
#         # permissions = []
#         # db_table = 'registration' #to overwrite db table name
#         # latest_object_by = "order_date" #It returns the latest object in the table based on the given field, used for typically DateField, DateTimeField, or IntegerField.


#     def __unicode__(self): #special function
#         return u"%s" % self.username # u - unicode/more than ascii char, i - Signed integer decimal, d-decimal

#     def get_fields(self):
#         return [(field.name, field.value_to_string(self)) for field in userInfo._meta.fields]


# class User(AbstractUser):
#     is_customer = models.BooleanField(default=False)
#     is_employee = models.BooleanField(default=False)
#     first_name=models.CharField(max_length=20)
#     last_name=models.CharField(max_length=20)

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
#     phone_number = models.CharField(max_length=20)
#     location = models.CharField(max_length=20)


# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
#     phone_number = models.CharField(max_length=20)
#     designation = models.CharField(max_length=20)


################



class User(models.Model):
    full_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    # age=models.IntegerField(choices=[18,19,20])
    phone_number=models.CharField(max_length=10)
    birth_date=models.DateField()
    email=models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    # REQUIRED_FIELDS = '__all__'
    # USERNAME_FIELD = 'username'
    # is_authenticated
    # @property
    # def is_anonymous(self):
    #     """
    #     Always return False. This is a way of comparing User objects to
    #     anonymous users.
    #     """
    #     return False
    