# Generated by Django 4.1.2 on 2022-10-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urls',
            options={'verbose_name': 'Url', 'verbose_name_plural': 'Urls'},
        ),
        migrations.AlterField(
            model_name='urls',
            name='host_url',
            field=models.CharField(default='url of the host', max_length=150, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='urls',
            name='short_url',
            field=models.CharField(blank=True, default='short url', max_length=150, verbose_name='Short'),
        ),
    ]
