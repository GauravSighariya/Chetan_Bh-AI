# Generated by Django 4.0.5 on 2022-06-22 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('keywords', models.CharField(blank=True, max_length=300, null=True)),
                ('wordCount', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=300, null=True)),
                ('wordCount', models.CharField(blank=True, max_length=100, null=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.blog')),
            ],
        ),
    ]
