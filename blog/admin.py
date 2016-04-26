from django.contrib import admin
from .models import Post, Comment


#사진 보이게 함
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_dislay = ('title','photo_tag')
    
    def photo_tag(self,post):
        return '<img src="{}" style="width =100px;" />'.format(post.photo.url)
    photo_tag.allow_tags = True
##Django model을 admin에 설정
admin.site.register(Comment)
