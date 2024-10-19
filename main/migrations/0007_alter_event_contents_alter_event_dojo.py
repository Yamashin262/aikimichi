# Generated by Django 4.2.16 on 2024-10-19 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_favorite_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contents',
            field=models.TextField(verbose_name='イベント内容'),
        ),
        migrations.AlterField(
            model_name='event',
            name='dojo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dojo', verbose_name='道場名'),
        ),
    ]
