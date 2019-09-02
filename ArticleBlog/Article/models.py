from django.db import models
from ckeditor.fields import RichTextField

class Author(models.Model):
    name = models.CharField(max_length = 32)
    age = models.IntegerField()
    gender = models.CharField(max_length = 32)
    birthday = models.DateField()
    email = models.EmailField()
    adress = RichTextField()
    photo = models.ImageField(upload_to = 'images')
    def __str__(self):
        return self.name

class ArticleType(models.Model):
    label = models.CharField(max_length = 32)
    description = RichTextField()
    def __str__(self):
        return self.label

class Article(models.Model):
    """
    文章和作者 多对一
    文章和类型 多对多
    """
    title = models.CharField(max_length = 32)
    article_author = models.ForeignKey(to = Author,on_delete = models.CASCADE)
        #models.CASCADE 级联删除，作者删除，文章删除
        #models.SET_NULL 设置空，作者删除，文章的作者设置为null
        #models.SET_DEFAULT 设置默认值，作者删除，文章的作者设置为默认值，需要配合default参数使用
    description = RichTextField()
    content = RichTextField()
    article_type = models.ManyToManyField(to=ArticleType)
    public_time = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to='images')
    click = models.IntegerField() #点击率
    recommend = models.IntegerField(default=0) #推荐 0位默认，1位推荐

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length = 32)
    password = models.CharField(max_length = 32)
# Create your models here.
