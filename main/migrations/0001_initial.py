# Generated by Django 4.2.16 on 2024-09-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dojo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('introduction', models.CharField(max_length=200)),
                ('picture', models.CharField(max_length=200)),
                ('mailaddress', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EvebtJoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=200)),
                ('EventID', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('reservationdate', models.CharField(max_length=200)),
                ('canceldate', models.CharField(max_length=200)),
                ('updatedate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('teachername', models.CharField(max_length=200)),
                ('DojoID', models.CharField(max_length=200)),
                ('contents', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ExaminationResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=200)),
                ('RankID', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=200)),
                ('examinationdate', models.CharField(max_length=200)),
                ('updatedate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=200)),
                ('EventID', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PracticeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=200)),
                ('RankID', models.CharField(max_length=200)),
                ('practicedate', models.CharField(max_length=200)),
                ('practicecontents', models.CharField(max_length=200)),
                ('updatedate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RankID', models.CharField(max_length=200)),
            ],
        ),
    ]