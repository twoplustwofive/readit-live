# Generated by Django 3.0.2 on 2020-05-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='media/image/default.jpg', upload_to='images/'),
        ),
    ]
