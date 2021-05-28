from django.db import models


# declare a new model with a name "GeeksModel"
class PragatishilModel(models.Model):
    # fields of the model
    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    admission_year=models.CharField(max_length=30)
    your_department=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=13)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class PepTalksUserModel(models.Model):

    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    admission_year=models.CharField(max_length=30)
    your_department=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=13)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class AriettaUserModel(models.Model):

    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    admission_year=models.CharField(max_length=30)
    your_department=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=13)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class DebateUserModel(models.Model):

    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    admission_year=models.CharField(max_length=30)
    your_department=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=13)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class LiterarryUserModel(models.Model):

    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    admission_year=models.CharField(max_length=30)
    your_department=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=13)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class RongmilantiUserModel(models.Model):

    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    admission_year=models.CharField(max_length=30)
    your_department=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=13)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name
        
class PratibimbaUserModel(models.Model):

    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    admission_year=models.CharField(max_length=30)
    your_department=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=13)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class TechonicsUserModel(models.Model):

    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    admission_year=models.CharField(max_length=30)
    your_department=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=13)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name