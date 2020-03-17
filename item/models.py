from django.db import models
from django.utils import timezone
from pytils.translit import slugify
from PIL import Image
from django.db.models.signals import post_save, post_delete, pre_save
import uuid
from random import choices
import string
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.utils.safestring import mark_safe
#from laskshmi import settings
from itertools import chain
from ideaHome.settings import BASE_DIR
import os


def format_number(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num



class Category(models.Model):
    name = models.CharField('Название категории', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение категории', upload_to='category_img/', blank=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    page_title = models.CharField('Title страницы', max_length=255, blank=True, null=True)
    page_description = models.CharField('Description страницы', max_length=255, blank=True, null=True)
    page_keywords = models.TextField('Keywords', blank=True, null=True)
    short_description = models.TextField('Краткое описание для главной', blank=True,)
    description = RichTextUploadingField('Описание категории', blank=True, null=True)
    is_active = models.BooleanField('Отображать ?', default=True, db_index=True)
    is_in_index_catalog = models.BooleanField('Показывать в каталоге на главной ?', default=False, db_index=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.name_slug:
            testSlug = Category.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom

        super(Category, self).save(*args, **kwargs)

    def get_all_manufactors(self):
        all_manufactors = []
        #result = list()
        for subcat in self.subcategory.all():
            for m in Manufactor.objects.filter(subcategory=subcat):
                if m not in all_manufactors:
                    all_manufactors.append(m)
        # for i in all_manufactors:
        #     result = list(chain(result, i))
        return all_manufactors

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL,verbose_name='Категория',
                                 related_name='subcategory')
    name = models.CharField('Название подкатегории', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    page_title = models.CharField('Title страницы', max_length=255, blank=True, null=True)
    page_description = models.CharField('Description страницы', max_length=255, blank=True, null=True)
    page_keywords = models.TextField('Keywords', blank=True, null=True)
    description = RichTextUploadingField('Описание подкатегории', blank=True, null=True)
    discount = models.IntegerField('Скидка на все товары в подкатегории %', blank=True, default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.name_slug:
            testSlug = SubCategory.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        # all_items = self.item_set.all()
        # for item in all_items:
        #     item.discount = self.discount
        #     item.save()

        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

class Manufactor(models.Model):
    subcategory = models.ManyToManyField(SubCategory, blank=False, verbose_name='Отностится к подкатегориям', db_index=True)
    name = models.CharField('Название производителя', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Лого', upload_to='manufactor_img/', blank=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    page_title = models.CharField('Title страницы', max_length=255, blank=True, null=True)
    page_description = models.CharField('Description страницы', max_length=255, blank=True, null=True)
    page_keywords = models.TextField('Keywords', blank=True, null=True)
    description = RichTextUploadingField('Описание на странице', blank=True, null=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.name_slug:
            testSlug = Manufactor.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        super(Manufactor, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

class Tag(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True,on_delete=models.SET_NULL, verbose_name='Относится к категории')
    name = models.CharField('Название тега', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    seoText = RichTextUploadingField('Текст для СЕО', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} , категория {self.category.name}'

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"



class Item(models.Model):
    # collection = models.ManyToManyField(Collection, blank=True, verbose_name='Коллекция',db_index=True)
    tag = models.ManyToManyField(Tag, blank=True, db_index=True, verbose_name='Теги')
    manufactor = models.ForeignKey(Manufactor, blank=True, null=True, verbose_name='Производитель',
                                 on_delete=models.SET_NULL, db_index=True)
    category = models.ForeignKey(Category,verbose_name='Категории',on_delete=models.SET_NULL, db_index=True)
    subcategory = models.ForeignKey(SubCategory, verbose_name='Подкатегории',on_delete=models.SET_NULL,db_index=True)
    name = models.CharField('Название товара', max_length=255, blank=True, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True,default='')
    name_slug = models.CharField(max_length=255, blank=True, null=True,db_index=True)
    price = models.IntegerField('Цена', blank=True, default=0, db_index=True)
    article = models.CharField('Артикул', max_length=50, blank=True, null=True)
    discount = models.IntegerField('Скидка %', blank=True, default=0, db_index=True)
    units = models.CharField('Ед.Измерения', max_length=50, blank=True, null=True, default='не указано')
    material = models.CharField('Материал', max_length=50, blank=True, null=True, default='не указано')
    size = models.CharField('Размер', max_length=15, blank=True, null=True)
    weight = models.CharField('Вес', max_length=15, blank=True, null=True)
    complect = models.CharField('Комплект', max_length=15, blank=True, null=True)
    thickness = models.CharField('Толщина', max_length=15, blank=True, null=True)

    description = RichTextUploadingField('Описание товара', blank=True, null=True)
    page_title = models.CharField('Title страницы', max_length=255, blank=True, null=True)
    page_description = models.TextField('Description страницы',  blank=True, null=True)
    is_active = models.BooleanField('Отображать товар ?', default=True, db_index=True)
    is_present = models.BooleanField('Товар в наличии ?', default=True, db_index=True)
    is_new = models.BooleanField('Товар новинка ?', default=False, db_index=True)
    buys = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.name_slug:
            testSlug = Item.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(Item, self).save(*args, **kwargs)

    def get_small_image(self):
        if self.itemimage_set.first().image_small:
            return self.itemimage_set.first().image_small
        else:
            return 'http://placehold.it/200'

    def get_absolute_url(self):
        return f'/category/{self.category.name_slug}/{self.subcategory.name_slug}/{self.name_slug}'

    def get_full_image(self):
        if self.itemimage_set.first().image.url:
            return self.itemimage_set.first().image.url
        else:
            return 'http://placehold.it/700'
    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        if self.get_small_image():
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.get_small_image()))
        else:
            return mark_safe('<span>НЕТ МИНИАТЮРЫ</span>')

    image_tag.short_description = 'Основная картинка'



    @property
    def discount_value(self):
        if self.discount > 0:
            dis_val = self.price - (self.price * self.discount / 100)
        else:
            dis_val = 0
        return (format_number(dis_val))


    def __str__(self):
        return f'id:{self.id}  {self.name}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"



class ItemImage(models.Model):
    upload_to = 'items/%d/%s'


    def _get_upload_to(self, filename):
        ext = filename.split('.')[-1]

        filename = '{}.{}'.format(self.item.pk, ext)

        return self.upload_to % (self.item.id, filename)

    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField('Изображение товара', upload_to='items/', blank=True)
    image_small = models.CharField(max_length=255, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s Изображение для товара : %s ' % (self.id, self.item.name)

    class Meta:
        verbose_name = "Изображение для товара"
        verbose_name_plural = "Изображения для товара"

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        if self.image_small:
            return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image_small))
        else:
            return mark_safe('<span>НЕТ МИНИАТЮРЫ</span>')

    image_tag.short_description = 'Картинка'


    def save(self, *args, **kwargs):
        fill_color = '#fff'
        image = Image.open(self.image)

        if image.mode in ('RGBA', 'LA'):
            background = Image.new(image.mode[:-1], image.size, fill_color)
            background.paste(image, image.split()[-1])
            image = background
        image.thumbnail((175, 175), Image.ANTIALIAS)
        small_name = 'media/items/{}/{}'.format(self.item.id, str(uuid.uuid4()) + '.jpg')
        # if settings.DEBUG:
        #     os.makedirs('media/items/{}'.format(self.item.id), exist_ok=True)
        #     image.save(small_name, 'JPEG', quality=100)
        # else:
        os.makedirs(BASE_DIR + '/media/items/{}'.format(self.item.id), exist_ok=True)
        image.save(BASE_DIR + '/' + small_name, 'JPEG', quality=100)
        self.image_small = '/' + small_name




        super(ItemImage, self).save(*args, **kwargs)



class PromoCode(models.Model):
    promo_code = models.CharField('Промокод (для создания рандомного значения оставить пустым)', max_length=255, blank=True, null=True)
    promo_discount = models.IntegerField('Скидка на заказ', blank=True, default=0)
    use_counts = models.IntegerField('Кол-во использований', blank=True, default=1)
    is_unlimited = models.BooleanField('Неограниченное кол-во использований', default=False)
    is_active = models.BooleanField('Активен?', default=True)
    expiry = models.DateTimeField('Срок действия безлимитного кода', blank=True,null=True)

    def __str__(self):
        if self.is_unlimited:
            return 'Неограниченный промокод со скидкой : %s . Срок действия до : %s' % (self.promo_discount, self.expiry)
        else:
            return 'Ограниченный промокод со скидкой : %s . Оставшееся кол-во использований : %s' % (self.promo_discount, self.use_counts)

    class Meta:
        verbose_name = "Промокод"
        verbose_name_plural = "Промокоды"

    def save(self, *args, **kwargs):
        if self.is_unlimited:
            if not self.promo_code:
                self.promo_code = "LM-"+''.join(choices(string.ascii_uppercase + string.digits, k=5))
                self.use_counts = 0
        else:
            if not self.promo_code:
                self.promo_code = "LM-" + ''.join(choices(string.ascii_uppercase + string.digits, k=5))


        super(PromoCode, self).save(*args, **kwargs)




def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        os.remove(instance.image.path)
        os.remove(BASE_DIR + instance.image_small)

def auto_delete_file_on_change_itemimage(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = ItemImage.objects.get(pk=instance.pk).image
        image_small = ItemImage.objects.get(pk=instance.pk).image_small
    except ItemImage.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
            os.remove(BASE_DIR + image_small)


post_delete.connect(auto_delete_file_on_delete, sender=ItemImage)
pre_save.connect(auto_delete_file_on_change_itemimage, sender=ItemImage)