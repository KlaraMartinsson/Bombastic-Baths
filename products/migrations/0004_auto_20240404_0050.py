# Generated by Django 3.2.25 on 2024-04-03 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240401_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='gift',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
