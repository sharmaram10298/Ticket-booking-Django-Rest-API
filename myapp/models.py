from django.db import models

# Create your models here.



class Theater(models.Model):
    seat = models.CharField(max_length=150, null=False,blank=False)
    a = models.CharField(max_length=150, name=False, blank=False)
    a_status = models.CharField(default=0,max_length=2)
    b = models.CharField(max_length=150, name=False, blank=False)
    b_status = models.CharField(default=0, max_length=2)
    c = models.CharField(max_length=150, name=False, blank=False)
    c_status = models.CharField(default=0, max_length=2)
    d = models.CharField(max_length=150, name=False, blank=False)
    d_status = models.CharField(default=0, max_length=2)
    e = models.CharField(max_length=150, name=False, blank=False)
    e_status = models.CharField(default=0, max_length=2)
    f = models.CharField(max_length=150, name=False, blank=False)
    f_status = models.CharField(default=0, max_length=2)
    g = models.CharField(max_length=150, name=False, blank=False)
    g_status = models.CharField(default=0, max_length=2)
    h = models.CharField(max_length=150, name=False, blank=False)
    h_status = models.CharField(default=0, max_length=2)
    j = models.CharField(max_length=150, name=False, blank=False)
    j_status = models.CharField(default=0, max_length=2)
    k = models.CharField(max_length=150, name=False, blank=False)
    k_status = models.CharField(default=0, max_length=2)
    l = models.CharField(max_length=150, name=False, blank=False)
    l_status = models.CharField(default=0, max_length=2)
