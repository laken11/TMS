import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


# Create your models here.


class Person(AbstractBaseUser):
    id = models.UUIDField("Person unique id", primary_key=True, default=uuid.uuid4(), null=False)
    email = models.EmailField("Person email", null=False, unique=True, blank=False)
    last_name = models.CharField("Person last name", max_length=50, null=False, blank=False)
    first_name = models.CharField("Person first name", max_length=50, null=True, blank=True)
    password = models.CharField("Person password", max_length=150, null=False, blank=False)
    address = models.OneToOneField("Address", on_delete=models.RESTRICT)
    telephone = models.CharField("Person phone number", max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    role = models.ManyToManyField("Role")
    permission = models.ManyToManyField("Permission")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["email", "password"]


class Role(models.Model):
    id = models.UUIDField("Role id", primary_key=True, default=uuid.uuid4(), null=False)
    name = models.CharField("Role name", max_length=20, null=False, blank=False, unique=True)
    description = models.CharField("Role description", max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    permission = models.ManyToManyField("Permission")


class Permission(models.Model):
    id = models.UUIDField("Permission id", primary_key=True, default=uuid.uuid4(), null=False)
    name = models.CharField("Permission name", unique=True, null=False, blank=False, max_length=20)
    description = models.CharField("Permission description", null=False, blank=False, max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Address(models.Model):
    id = models.UUIDField("Address id", primary_key=True, default=uuid.uuid4(), null=False)
    line = models.CharField(max_length=20, null=False, blank=False)
    postal_code = models.IntegerField(null=True, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    state = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Vehicle(models.Model):
    id = models.UUIDField("Bus id", primary_key=True, default=uuid.uuid4(), null=False)
    name = models.CharField("Bus name", max_length=20, null=False, unique=True, blank=False)
    registration_number = models.IntegerField(null=False, blank=False)
    capacity = models.IntegerField( null=False, blank=False)
    status = models.CharField(max_length=20, null=False, blank=False, default="available")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Journey(models.Model):
    id = models.UUIDField("Journey id", primary_key=True, default=uuid.uuid4(), null=False)
    name = models.CharField("Journey name", null=False, blank=False, max_length=20)
    description = models.CharField("Journey information", null=True, blank=True, max_length=500)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.RESTRICT)
    price = models.DecimalField(max_length=10000000, max_digits=6, decimal_places=6)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Destination(models.Model):
    id = models.UUIDField("Destination Id", primary_key=True, default=uuid.uuid4(), null=False)
    location = models.CharField("Destination location or area", null=False, blank=False, max_length=50)
    description = models.CharField("Destination information", null=True, blank=True, max_length=500)
    journey = models.ManyToManyField(Journey)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    id = models.UUIDField("Booking id", primary_key=True, default=uuid.uuid4(), null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    reference = models.CharField(max_length=20, null=False, blank=False)
    status = models.CharField(max_length=20, null=False, blank=False, default="inactive")
    pay = models.CharField(max_length=20, null=False, blank=False, default="unpaid")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    id = models.UUIDField("Payment id", primary_key=True, default=uuid.uuid4(), null=False)
    booking = models.OneToOneField(Booking, on_delete=models.RESTRICT)
    amount = models.DecimalField(max_digits=6, decimal_places=6)
    status = models.CharField(max_length=20, null=False, blank=False, default="unpaid")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
