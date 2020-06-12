from ckeditor.fields import RichTextField
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from datetime import datetime

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    key = models.SlugField('slug', editable=False)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    description = RichTextField()
    imageUrl = models.ImageField('image', upload_to='%d-%m-%Y/images')


# create a new slug and save


    def save(self, *args, **kwargs):
        if not self.key:
            self.key = slugify(self.title)
            self.key = datetime.now().strftime('%Y-%m-')+self.key
        return super().save(*args, **kwargs)

     # delete the image from file system
    def delete(self, *args, **kwargs):
        if self.imageUrl:
            self.imageUrl.delete()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        pass
        return reverse('articles-key', args=[str(self.key)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
