# Generated by Django 5.1.3 on 2024-11-30 19:01

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('difficulty_level', models.CharField(choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced')], default='BEGINNER', max_length=20)),
                ('time_commitment', models.PositiveIntegerField(help_text='Required minutes per day')),
                ('price_range', models.CharField(max_length=50)),
                ('required_equipment', models.JSONField(blank=True, default=list)),
                ('minimum_age', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hobbies.category')),
                ('related_hobbies', models.ManyToManyField(blank=True, to='hobbies.hobby')),
                ('tags', models.ManyToManyField(related_name='hobbies', to='hobbies.tag')),
            ],
            options={
                'verbose_name_plural': 'hobbies',
            },
        ),
        migrations.CreateModel(
            name='HobbyTasting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('duration', models.PositiveIntegerField(default=15, help_text='Duration in minutes')),
                ('equipment_needed', models.JSONField(blank=True, default=list)),
                ('instructions', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tastings', to='hobbies.hobby')),
            ],
        ),
        migrations.CreateModel(
            name='UserHobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active'), ('favorite', 'Favorite'), ('completed', 'Completed')], max_length=10)),
                ('notes', models.TextField(blank=True)),
                ('resources_links', models.JSONField(blank=True, default=list)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('last_activity', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_hobbies', to='hobbies.hobby')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_hobbies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]