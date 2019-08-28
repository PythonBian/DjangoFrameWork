from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 32)
    age = models.IntegerField()
    gender = models.CharField(max_length = 32)
    birthday = models.DateField()
    email = models.EmailField()
    adress = models.TextField()
    photo = models.ImageField(upload_to = 'images')
    def __str__(self):
        return self.name

class ArticleType(models.Model):
    label = models.CharField(max_length = 32)
    description = models.TextField()
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
    description = models.TextField()
    content = models.TextField()
    article_type = models.ManyToManyField(to=ArticleType)
    public_time = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
# Create your models here.
