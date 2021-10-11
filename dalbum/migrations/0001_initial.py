# Generated by Django 3.2.7 on 2021-10-11 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('disc', models.TextField()),
                ('image', models.ImageField(upload_to='albumphotos/')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
