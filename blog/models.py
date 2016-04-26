from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    photo = models.ImageField()
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
   #글제목 보기게 함 
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    ##외래키의 역활
    post = models.ForeignKey(Post)
    message = models.TextField()
