from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150,
                             verbose_name='Name of news')

    content = models.TextField(blank=True,
                               verbose_name='content fo article')

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Date of create')

    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Date of update')

    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',
                              verbose_name='Photo of article',
                              blank=True)

    is_published = models.BooleanField(default=True,
                                       verbose_name='Published Yes/No')

    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT,
                                 null=True,
                                 )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150,
                             db_index=True,
                             verbose_name='Name of category',
                             )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
