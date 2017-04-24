from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension
from django.core.urlresolvers import reverse
import os
from django.conf import settings

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    no_of_songs = models.IntegerField(default=0)

    def get_absoulte_url(self):
        return reverse('composer:project',kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + ' ' + str(self.no_of_songs)

class Song(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    file = models.FileField(upload_to='songs/',validators=[validate_file_extension])
    name = models.CharField(max_length=250,default='')

    def __str__(self):
        return self.name

    def save(self, *args,**kwargs):

        basename, extension = os.path.splitext(os.path.basename(self.file.url))
        self.name = basename
        super(Song,self).save(*args,**kwargs)

    def delete(self):

        pk = self.project.pk
        no_of_songs = self.project.no_of_songs - 1

        Project.objects.filter(pk=pk).update(no_of_songs=no_of_songs)

        os.remove("F:\Licenta\music_processing" + self.file.url)
        return super(Song,self).delete()