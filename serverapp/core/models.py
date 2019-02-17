# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Django class to manage users
class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
 
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

# Main user class
class User(AbstractBaseUser, PermissionsMixin):
    # Model fields
    email = models.EmailField(unique=True, null=True, blank=False)
    first_name = models.CharField(max_length=80, unique=False, null=True, blank=False)
    last_name = models.CharField(max_length=80, unique=False, null=True, blank=False)
    age = models.IntegerField(unique=False, null=True, blank=False)
    school = models.CharField(max_length=80, unique=False, null=True, blank=False)
    
    # Cannot be chosen on signup
    classification = models.CharField(max_length=80, unique=False, null=True, blank=False)
    role = models.CharField(max_length=80, unique=False, null=True, blank=False)

    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Is the user allowed to have access to the admin',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text= 'Is the user account currently active',
    )
    USERNAME_FIELD = 'email'
    objects = MyUserManager()
 
    def __str__(self):
        return self.email
 
    def get_full_name(self):
        return self.email
 
    def get_short_name(self):
        return self.email

# Model to hold information about a Question
class Question(models.Model):
    contest = models.ForeignKey(
        'Contest',
        on_delete = models.CASCADE,
    )
    text = models.CharField(max_length=80, unique=False, null=True, blank=False)
    solution = models.CharField(max_length=80, unique=False, null=True, blank=False)

# Model to hold contest information
class Contest(models.Model):
    contest_name = models.CharField(max_length=80, unique=False, null=True, blank=False)

# Model to hold user score information
class ParticipantScore(models.Model):
    user_id = models.ForeignKey(
        'User',
        on_delete = models.CASCADE,
    )
    contest_id = models.ForeignKey(
        'Contest',
        on_delete = models.CASCADE,
    )
    user_points = models.FloatField(unique=False, null=True, blank=False)
    total_points = models.FloatField(unique=False, null=True, blank=False)
>>>>>>> be88eb75850d02ca1c0d8df7f334efed3f94c361
