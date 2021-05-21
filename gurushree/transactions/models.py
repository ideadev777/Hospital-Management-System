from django.db import models

class patient_registration(models.Model):
    reg_type=models.CharField(max_length=32, null=True)
    title=models.CharField(max_length=32, null=True)
    gender=models.CharField(max_length=32, null=True)
    p_name=models.CharField(max_length=32, null=True)
    year=models.IntegerField(null=True)
    month=models.IntegerField(null=True)
    day=models.IntegerField(null=True)
    mobile_number=models.CharField(max_length=32, null=True)
    address=models.CharField(max_length=32, null=True)
    email_id=models.CharField(max_length=32, null=True)
    address2=models.CharField(max_length=32, null=True)
    location=models.CharField(max_length=32, null=True)
    pincode=models.CharField(max_length=32, null=True)
    alternateContact=models.CharField(max_length=32, null=True)
    marital=models.CharField(max_length=32, null=True)
    occupation=models.CharField(max_length=32, null=True)
    religion=models.CharField(max_length=32, null=True)
    father_name=models.CharField(max_length=32, null=True)
    blood_group=models.CharField(max_length=32, null=True)
    nationality=models.CharField(max_length=32, null=True)
    id_type=models.CharField(max_length=32, null=True)
    id_number=models.CharField(max_length=32, null=True)
    p_photo = models.FileField(max_length=355, null=True)
    a_photo = models.FileField(max_length=355, null=True)
    isActive=models.BooleanField(default=True)
    AddedBY =models.CharField(max_length=32, null=True)
    Addeddate = models.DateTimeField(auto_now_add=True)
    editedby =models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.p_name