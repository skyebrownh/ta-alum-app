# Generated by Django 2.2.4 on 2019-08-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0012_auto_20190821_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, default='Skye-placeholder.jpg', upload_to=''),
        ),
    ]
