# Generated by Django 2.2.4 on 2019-08-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0014_auto_20190821_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='Skye-placeholder.jpg', null=True, upload_to=''),
        ),
    ]
