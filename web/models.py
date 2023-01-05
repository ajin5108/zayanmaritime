from django.db import models
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField 

# Create your models here.

class Services(models.Model):
    image = VersatileImageField('service image',upload_to='image/testimagemodel/')
    heading = models.CharField(max_length=100)
    discription = models.TextField()
    image2 = VersatileImageField('service image2',upload_to='image/testimagemodel/',null=True,blank=True)
    image3 = VersatileImageField('service image3',upload_to='image/testimagemodel/',null=True,blank=True)
    contenttitle = models.CharField(max_length=100,null=True)
    content = models.TextField()

    def __str__(self):
        return self.heading
    

class AdminNumber(models.Model):
    name = models.CharField(max_length=20)
    phone_number=models.CharField(max_length=12) 



class Gallery(models.Model):
    galleryimage = VersatileImageField('gallery image',upload_to='image/testmoedel/',null=True,blank=True)


class Career(models.Model):
    jobname = models.CharField(max_length=100)
    discription = HTMLField()    
    location = models.CharField(max_length=50, null=True, blank=True)
    salary = models.CharField(max_length=50, null=True, blank=True)
    vaccancy = models.IntegerField(null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)   
    job_responsibility = HTMLField(null=True, blank=True)
    educational_requirments = HTMLField(null=True,blank=True)

    def __str__(self):
        return self.jobname
        

class CareerData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    jobs = models.CharField(max_length=100)
    resume = models.FileField(upload_to='image/testmoedel/')

    def __str__(self):
        return self.name