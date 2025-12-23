from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

emial_validators = RegexValidator(
    regex=r"^[a-zA-Z0-9]+@[a-zA-Z]+\.(com|eur|net)$",
    message = 'emial is not correct'
)

password_validators = RegexValidator( 
    regex=r'^(?=*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
    message='كلمة السر يجب أن تكون 8 أحرف على الأقل وتحتوي على حرف ورقم'
)

# Create your models here
class Login(models.Model): 
    username = models.CharField(max_length=55)
    emial = models.CharField(max_length=55,validators=[emial_validators])
    password = models.CharField(max_length =55,validators=[password_validators])

class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    created_at = models.DateTimeField(verbose_name='CreatedTime',default=datetime.now)
    author = models.ForeignKey(User,default=User.first_name,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%y/%m/%d')

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    