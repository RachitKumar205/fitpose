# Generated by Django 3.1.2 on 2021-04-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_detail_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='gif_2',
        ),
        migrations.AlterField(
            model_name='detail',
            name='gif_1',
            field=models.ImageField(default='none', upload_to='exercises/'),
        ),
    ]