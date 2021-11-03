# Generated by Django 3.2.8 on 2021-10-27 12:33

from django.db import migrations, models
import my_blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=300, null=True)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(null=True, upload_to='', verbose_name=my_blog.models.article_directory_path)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
