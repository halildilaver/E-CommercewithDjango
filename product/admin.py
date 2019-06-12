from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

# Register your models here.
from product.models import Category, Product

class ProductAdmin (admin.ModelAdmin):
    list_display = ('title', 'category', 'status')
    list_filter = ('category', 'status')

class ModelClass:
    detail = RichTextUploadingField()

class PostForm(forms.ModelForm):
    detail = forms.CharField(widget=CKEditorUploadingWidget())

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)