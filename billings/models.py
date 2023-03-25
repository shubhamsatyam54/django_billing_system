from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
STATE_CHOICES = (
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Delhi", "Delhi"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Ladakh", "Ladakh"),
    ("Lakshadweep", "Lakshadweep"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Pondicherry", "Pondicherry"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal")
)


class Client(models.Model):
    pincode_regex = RegexValidator(
        regex=r'^\d{6}$',
        message='Pincode must be a 6-digit number.',
        code='invalid_pincode'
    )

    gst_regex = RegexValidator(
        regex=r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d{1}[Z]{1}[A-Z\d]{1}$',
        message='Invalid GST number.',
        code='invalid_gst_number'
    )

    license_regex = RegexValidator(
        regex=r'^[A-Z]{2}/\d{5}$',
        message='Invalid drug license number.',
        code='invalid_license_number'
    )

    name = models.CharField(max_length=255,primary_key=True)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, choices=STATE_CHOICES, default="Bihar")
    pincode = models.CharField(
        max_length=6,
        validators=[pincode_regex]
    )

    gst_number = models.CharField(
        max_length=15,
        validators=[gst_regex],
        verbose_name="GST Number",
    )

    dl_number = models.CharField(
        max_length=8,
        validators=[license_regex],
        verbose_name="DL Number"
    )

    amount_due = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name='Amount due (INR`)'
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255,primary_key=True,)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title

class Batch(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mfd = models.DateField(verbose_name='Manufacturing Date')
    expdt = models.DateField(verbose_name='Expiry Date')
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'name')

    def __str__(self):
        return self.name
