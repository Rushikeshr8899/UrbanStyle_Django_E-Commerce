# Generated by Django 4.2 on 2023-04-22 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(upload_to='Photos/categories'),
        ),
    ]
