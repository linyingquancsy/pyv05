# Generated by Django 2.2.1 on 2019-11-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pacon_datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=32, unique=True)),
                ('urls_news', models.URLField()),
                ('title_news', models.TextField()),
                ('times_news', models.TextField()),
                ('reads_news', models.CharField(max_length=32)),
                ('body_news', models.TextField()),
                ('images', models.TextField()),
            ],
        ),
    ]