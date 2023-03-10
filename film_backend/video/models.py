from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField('语境', max_length=150, help_text='语境')
    context=models.CharField('真语境',max_length=30,default=1,help_text='真语境')
    equation=models.CharField('公式',max_length=180,default=1,help_text='公式')
    example=models.CharField('例子',max_length=200,default=1,help_text='例子')
    cover_url = models.URLField('封面url', help_text='封面url')
    video_url = models.URLField('视频url', help_text='视频url')
    knowledge=models.CharField('知识链接',max_length=100,default=1,help_text='知识链接')
    
    class Meta:
        db_table = 'video'
        verbose_name = 'video'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class mainPage(models.Model):
    context=models.CharField('真语境',max_length=30,default=1,help_text='真语境')
    equation=models.CharField('公式',max_length=180,default=1,help_text='公式')
    example=models.CharField('例子',max_length=200,default=1,help_text='例子')
    cover_url = models.URLField('封面url', help_text='封面url')
    video_url = models.URLField('视频url', help_text='视频url')
    knowledge=models.CharField('知识链接',max_length=100,default=1,help_text='知识链接')
    class Meta:
        db_table = 'mainPage'
        verbose_name = 'mainPage'
        verbose_name_plural = verbose_name