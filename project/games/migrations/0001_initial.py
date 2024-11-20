# Generated by Django 5.1.3 on 2024-11-19 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_remove_customuser_profile_image_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('deposit', models.IntegerField()),
                ('monthly_rent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('salary', models.IntegerField()),
                ('profile_image', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('current_money', models.IntegerField(default=0)),
                ('current_month', models.IntegerField(default=1)),
                ('is_morning', models.IntegerField(default=1)),
                ('hospital_visited', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='accounts.customuser')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.house')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.job')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
