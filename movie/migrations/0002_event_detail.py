# Generated by Django 2.0 on 2019-12-20 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.ImageField(upload_to='images/')),
                ('event_summary', models.CharField(max_length=200)),
            ],
        ),
    ]