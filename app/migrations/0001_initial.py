# Generated by Django 5.0.3 on 2025-03-12 02:24

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('level', models.IntegerField(choices=[(0, 'Debug'), (1, 'Info'), (2, 'Warning'), (3, 'Error')], default=1)),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(default='', max_length=256)),
                ('country', models.CharField(default='', max_length=256)),
                ('ref', models.CharField(default='', max_length=256)),
                ('sid', models.CharField(default='', max_length=256)),
                ('url', models.CharField(default='', max_length=256)),
                ('val1', models.CharField(default='', max_length=256)),
                ('val2', models.CharField(default='', max_length=256)),
                ('val3', models.CharField(default='', max_length=256)),
                ('ip', models.CharField(default='', max_length=256)),
                ('body', models.TextField(default='{}')),
                ('user_agent', models.CharField(default='', max_length=1024)),
                ('device', models.CharField(default='', max_length=256)),
                ('browser', models.CharField(default='', max_length=256)),
                ('browser_family', models.CharField(default='', max_length=256)),
                ('is_mobile', models.BooleanField(default=False)),
                ('is_tablet', models.BooleanField(default=False)),
                ('is_touch_capable', models.BooleanField(default=False)),
                ('is_pc', models.BooleanField(default=False)),
                ('is_bot', models.BooleanField(default=False)),
                ('os', models.CharField(default='', max_length=256)),
                ('os_family', models.CharField(default='', max_length=256)),
                ('os_version', models.CharField(default='', max_length=256)),
                ('device_family', models.CharField(default='', max_length=256)),
                ('device_brand', models.CharField(default='', max_length=256)),
                ('device_model', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-created'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
