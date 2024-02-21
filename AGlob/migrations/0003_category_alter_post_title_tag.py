# Generated by Django 5.0 on 2024-01-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AGlob', '0002_post_title_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=100),
        ),
    ]
