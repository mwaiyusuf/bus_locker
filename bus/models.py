 from  __future__ import unicode_literals #allows you to schedule invocation of callables at a given time
from django.db import models
from django.db.models.signals import post_save 
from django.contrib.auth.models import User 
from django.db.models import Avg,Max,Min 
import datetime as dt 
import numpy as np 
# Create your models here.


class Bus(models.Model):
    title = models.TextField(max_length=200, null=True, blank=True, default="title")
    # project_image = models.ImageField(upload_to='picture/', null=True, blank=True)
    description = models.TextField()
    bus_url=models.URLField(max_length=250)

    def average_design(self):
        design_ratings = list(map(lambda x: x.design_rating, self.reviews.all()))
        return np.mean(design_ratings)

    def average_usability(self):
        usability_ratings = list(map(lambda x: x.usability_rating, self.reviews.all()))
        return np.mean(usability_ratings)

    def average_content(self):
        content_ratings = list(map(lambda x: x.content_rating, self.reviews.all()))
        return np.mean(content_ratings)

    def save_bus(self):
        self.save()
    @classmethod
    def delete_bus_by_id(cls, id):
        bus = cls.objects.filter(pk=id)
        bus.delete()

    @classmethod
    def get_bus_by_id(cls, id):
        bus = cls.objects.get(pk=id)
        return bus

    @classmethod
    def search_bus(cls, search_term):
        bus = cls.objects.filter(title__icontains=search_term)
        return bus

    @classmethod
    def update_bus(cls, id):
        bus = cls.objects.filter(id=id).update(id=id)
        return bus
    @classmethod
    def update_description(cls, id):
      bus = cls.objects.filter(id=id).update(id=id)
        return bus

    def __str__(self):
        return self.title
class Profile(models.Model):
    class Meta:
        db_table = 'profile'

    bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
    profile_pic = models.ImageField(upload_to='picture/', null=True, blank=True, default= 0)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="profile")
    bus=models.ForeignKey(Project, null=True)
    contact=models.IntegerField(default=0)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)


    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()


    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    @property
    def image_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    def __str__(self):
        return self.user.username