from django.db import models
from django.utils.text import slugify

class BlogCategory(models.Model):
    name = models.CharField(verbose_name="Blog Category", blank=False, unique=True, max_length=50)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(verbose_name="Status", default=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Blog Term"
        verbose_name_plural = "Blog Term"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify( self.name)
        super().save(*args, **kwargs)


class Blog(models.Model):
    categories = models.ManyToManyField(
        BlogCategory,        
        related_name="blogs",
        blank=True
    )
    name = models.CharField(verbose_name="Blog title", max_length=50, blank=False, unique=True)
    slug = models.SlugField(verbose_name="Blog title", max_length=50, blank=False, unique=True)
    status = models.BooleanField(verbose_name="Status", default=True)
    
    class Meta:
        ordering = ['-id']
        verbose_name = "Blog"
        verbose_name_plural = "Blog"
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
