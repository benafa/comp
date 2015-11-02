from django.contrib import admin

from .models import Content, Article, Image, Contributor

from django.forms import *
from django.db.models import *
from tinymce.widgets import TinyMCE

# class ProductionForm(forms.ModelForm):
#     some_field = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

#     class Meta:
#         model = Production

# class ProductionAdmin(admin.ModelAdmin):
#     form = ProductionForm

admin.site.register(Content)

class ArticleAdmin(admin.ModelAdmin):
    # ...
    list_display = ('title', 'subtitle', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)


admin.site.register(Image)


admin.site.register(Contributor)


# Register your models here.
