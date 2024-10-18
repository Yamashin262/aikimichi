from datetime import date
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
    name = models.CharField(max_length=40, verbose_name="道場名")
    address = models.CharField(max_length=200, verbose_name="住所")
    phone_number = models.CharField(max_length=20)
    introduction = models.TextField()
    picture = models.ImageField(blank=True)
    mailaddress = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "道場"
        verbose_name_plural = "道場"
    
class Rank(models.Model):
    rank = models.CharField(max_length=10,verbose_name="階級")
    
    def __str__(self):
        return self.rank
    
    class Meta:
        verbose_name = "階級"
        verbose_name_plural = "階級"

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    nickname = models.CharField(max_length=40, verbose_name="ニックネーム")
    gender = models.PositiveIntegerField(default=0, verbose_name="性別")
    date = models.DateField(default=date.today)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE, default=1)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.nickname
    
    class Meta:
        verbose_name = "ニックネーム"
        verbose_name_plural = "ニックネーム"

class Event(models.Model):
    name = models.CharField(max_length=40, verbose_name="イベント")
    date = models.DateField(verbose_name="日付")
    place = models.CharField(max_length=200, verbose_name="場所")
    teachername = models.CharField(max_length=50,verbose_name="指導者名")
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)
    contents = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "イベント"
        verbose_name_plural = "イベント"
    
class EventJoin(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.IntegerField(verbose_name="イベント参加情報")
    reservationdate = models.DateTimeField()
    canceldate = models.DateTimeField()
    updatedate = models.DateTimeField()
    
    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name = "イベント参加情報"
        verbose_name_plural = "イベント参加情報"
    
class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = "お気に入り"
        verbose_name_plural = "お気に入り"

class PracticeRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    practicedate = models.DateField(verbose_name="稽古日時")
    practicecontents = models.TextField(verbose_name="稽古内容")
    updatedate = models.DateTimeField(verbose_name="更新日")
    
    def __str__(self):
        return self.practicedate
    
    class Meta:
        verbose_name = "稽古記録"
        verbose_name_plural = "稽古記録"

class ExaminationResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    result = models.IntegerField(verbose_name="審査結果")
    examinationdate = models.DateTimeField(verbose_name="審査日")
    updatedate = models.DateTimeField(verbose_name="更新日")
    
    def __str__(self):
        return self.result
    
    class Meta:
        verbose_name = "審査結果"
        verbose_name_plural = "審査結果"


