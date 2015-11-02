from django.db import models

from django.core.urlresolvers import reverse


# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.title


class Article(Content):
    text = models.TextField(max_length=2000)

    def show(self):
    	return self.title + "\n" + self.subtitle + "\n" + "On " + str(self.pub_date.month) + "."  + str(self.pub_date.day) + "." 
    	+ str(self.pub_date.year) + "\n" + self.text 


class Image(Content):
    path = models.FilePathField(max_length=500)

    def info(self):
    	return self.title + self.subtitle + "on " + str(self.pub_date.month) + "."  + str(self.pub_date.day) + "."
    	+ str(self.pub_date.year) + self.path 

class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    house = models.CharField(max_length=500)
    contents = models.ManyToManyField('Content',related_name='contributor', blank = True)
    # Another way to create a collection of Content objects that this contributor has made, 
    # is to use Content.objects.filter(contributors__first_name = 'name', contributors__last_name ="name")
    def die(self):
    	dead = Contributor.objects.get(first_name = self.first_name, last_name = self.last_name)
    	dead.delete()
    def __str__(self):              # __unicode__ on Python 2
        return self.first_name + " "+ self.last_name


