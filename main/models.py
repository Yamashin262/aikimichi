from django.db import models

from django.contrib.auth.models import UserManager, AbstractUser

class CustomUserManager(UserManager):
    use_in_migrations = True
 
    def _create_user(self, email, username, password, **extra_fields):
        # create_user と create_superuser の共通処理
        if not email:
            raise ValueError('email must be set')
        if not username:
            raise ValueError('username must be set')
 
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
 
        return user
 
    def create_user(self, username, email=None, password=None, **extra_fields):
 
        if not email:
            raise ValueError('email must be set')
        if not username:
            raise ValueError('username must be set')
 
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
 
        return self._create_user(email, username, password, **extra_fields)
 
    def create_superuser(self, username, email=None, password=None, **extra_fields):
 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
 
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
 
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
 
        return self._create_user(email, username, password, **extra_fields)


class Dojo(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    introduction = models.TextField()
    picture = models.ImageField(blank=True)
    mailaddress = models.EmailField(max_length=100)
    
class Rank(models.Model):
    rank = models.CharField(max_length=10)

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    nickname = models.CharField(max_length=40)
    gender = models.PositiveIntegerField(default=0)
    date = models.DateField()
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)

class Event(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateField()
    place = models.CharField(max_length=200)
    teachername = models.CharField(max_length=50)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)
    contents = models.TextField()
    
class EventJoin(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.IntegerField()
    reservationdate = models.DateTimeField()
    canceldate = models.DateTimeField()
    updatedate = models.DateTimeField()
    
class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


    
class PracticeRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    practicedate = models.DateField()
    practicecontents = models.TextField()
    updatedate = models.DateTimeField()

class ExaminationResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    result = models.IntegerField()
    examinationdate = models.DateTimeField()
    updatedate = models.DateTimeField()


