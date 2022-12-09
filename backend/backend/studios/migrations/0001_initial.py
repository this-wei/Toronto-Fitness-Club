# Generated by Django 4.0.1 on 2022-12-09 01:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=120, null=True)),
                ('postal_code', models.CharField(max_length=120, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=15, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=15, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Studio',
                'verbose_name_plural': 'Studios',
            },
        ),
        migrations.CreateModel(
            name='StudioImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studios.studio')),
            ],
            options={
                'verbose_name': 'Studio Image',
                'verbose_name_plural': 'Studio Images',
            },
        ),
        migrations.CreateModel(
            name='StudioAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120, null=True)),
                ('quantity', models.IntegerField()),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studios.studio')),
            ],
            options={
                'verbose_name': 'Studio Amenity',
                'verbose_name_plural': 'Studio Amenities',
            },
        ),
    ]