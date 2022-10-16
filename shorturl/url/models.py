from django.db import models

# Create models here.


class Urls(models.Model):
    host_url = models.CharField('Host', max_length=150, default='url of the host')
    short_url = models.CharField('Short', max_length=150, default='short url', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='created time')

    def __str__(self):
        return self.host_url+self.short_url

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'