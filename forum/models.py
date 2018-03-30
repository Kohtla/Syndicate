from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Theme(models.Model):
    creator = models.CharField(max_length = 250)
    theme_title = models.CharField(max_length = 1000)
    theme_image = models.CharField(max_length = 2000)
    def __str__(self):
        return self.creator + " - " +self.theme_title

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'pk':self.pk})

class Message(models.Model):
    theme  = models.ForeignKey(Theme, on_delete=models.CASCADE)
    author = models.CharField(max_length = 250)
    message_text = models.CharField(max_length = 2000)
    answer_to = models.CharField(max_length = 250)
    def __str__(self):
        return self.author + " : " +self.message_text

