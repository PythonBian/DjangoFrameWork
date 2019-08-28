from django.contrib import admin
from Article.models import *

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(ArticleType)

# Register your models here.
