# Generated by Django 4.1.3 on 2022-11-30 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_login_rename_age_reg_age_rename_email_reg_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='reg',
            name='password',
            field=models.CharField(max_length=15),
        ),
    ]
