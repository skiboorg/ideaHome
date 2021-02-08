from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
import string

class BlogPost(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение превью (555 x 390)', upload_to='blog_img/', blank=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=False, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=False, null=True)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=False, null=True)
    short_description = models.TextField('Краткое описание ', blank=False)
    description = RichTextUploadingField('Статья', blank=False, null=True)
    views = models.IntegerField('Просмотров', default=0)
    is_active = models.BooleanField('Отображать статью ?', default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        testSlug = BlogPost.objects.filter(name_slug=slug)
        slugRandom = ''
        if not testSlug:
            slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
        self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(BlogPost, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return f'/post/{self.name_slug}/'

    def __str__(self):
        return 'Статья : %s ' % self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

