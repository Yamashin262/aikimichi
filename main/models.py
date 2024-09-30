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

'''
class CustomUser(AbstractUser):
    pass
    objects = CustomUserManager()
 
    def __str__(self):
        return self.email
'''


class Dojo(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    introduction = models.CharField(max_length=200)
    picture = 
    mailaddress = models.CharField(max_length=200)

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    teachername = models.CharField(max_length=200)
    DojoID = 
    contents = models.CharField(max_length=200)
    
class EvebtJoin(models.Model):
    UserID = 
    EventID =
    status = 
    reservationdate = models.CharField(max_length=200)
    canceldate = models.CharField(max_length=200)
    updatedate = models.CharField(max_length=200)
    
class Favorite(models.Model):
    UserID = 
    EventID =
    
class PracticeRecord(models.Model):
    UserID = 
    RankID = 
    practicedate = models.CharField(max_length=200)
    practicecontents = models.CharField(max_length=200)
    updatedate = models.CharField(max_length=200)

class ExaminationResult(models.Model):
    UserID = 
    RankID = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    examinationdate = models.CharField(max_length=200)
    updatedate = models.CharField(max_length=200)

class Rank(models.Model):
    RankID = models.CharField(max_length=200)
