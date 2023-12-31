# Generated by Django 4.2.3 on 2023-07-09 07:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, error_messages={'unique': 'Bu telefon raqamga ega foydalanuvchi oldindan mavjud'}, help_text='Required. 12 characters or fewer. Digits only.', max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed.", regex='^998[0-9]{9}$')]),
        ),
    ]
