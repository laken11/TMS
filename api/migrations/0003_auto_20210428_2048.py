# Generated by Django 3.2 on 2021-04-28 19:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210428_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0d18470d-96cc-4969-adb4-0b1dfd668c97'), primary_key=True, serialize=False, verbose_name='Address id'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.UUIDField(default=uuid.UUID('934c8090-224c-41e5-849f-e17f58c49c3d'), primary_key=True, serialize=False, verbose_name='Booking id'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='id',
            field=models.UUIDField(default=uuid.UUID('384a34a0-e1ac-4212-982d-8702850caf4e'), primary_key=True, serialize=False, verbose_name='Destination Id'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9faa5835-e953-4ade-88cd-e905ebb86b68'), primary_key=True, serialize=False, verbose_name='Journey id'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5bb4de8f-5eeb-4479-97f2-07f31cef4a5e'), primary_key=True, serialize=False, verbose_name='Payment id'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='id',
            field=models.UUIDField(default=uuid.UUID('85a464e6-a9f5-4ba3-905e-86e177791343'), primary_key=True, serialize=False, verbose_name='Permission id'),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4fd17574-76a7-4107-83fa-c0b38992f53a'), primary_key=True, serialize=False, verbose_name='Person unique id'),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.UUIDField(default=uuid.UUID('396c32a8-241a-4377-a4c2-70e08bcba076'), primary_key=True, serialize=False, verbose_name='Role id'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ec5ed873-ec07-431a-95ec-82b360cba678'), primary_key=True, serialize=False, verbose_name='Bus id'),
        ),
    ]