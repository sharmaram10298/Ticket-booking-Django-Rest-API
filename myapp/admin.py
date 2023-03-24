from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Theater)
class Theater(admin.ModelAdmin):
    list_display = ['id','seat','a','a_status', 'b', 'b_status','c','c_status','d','d_status','e','e_status','f','f_status','g','g_status','h','h_status','j','j_status','k','k_status','l','l_status']
