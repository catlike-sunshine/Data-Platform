from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

#单独建立的用户模型
class  users(models.Model):
  id = models.AutoField(primary_key = True)
  name =  models.CharField(max_length = 100)
  info = models.CharField(max_length = 200, default = "na")

# 文章模型
class article(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField("标题",max_length = 100)
    content = models.TextField("正文")

    """Determine the length of a specified textfield length. If its length exceeds our
        predefined one, then the part of that text that exceeds will display in ellipsis."""

    def truncated_content(self):
        if len(str(self.content))>65:
            return '{}......'.format(str(self.content[0:65]))
        else:
            return str(self.content)

#将article的title属性返回, 作为article的显示
    def __str__(self):
        return (self.title)

#机型数据模型
class acmodels(models.Model):
    id = models.AutoField(primary_key = True)
    basic_acmodels = models.CharField("基本型号", max_length = 100)
    expanded_acmodels = models.CharField("扩展型号", max_length = 100)
    if_intra_ac = models.BooleanField(default = False)

    def __str__(self):
        return (self.basic_acmodels)

#事故数据模型
class accident(models.Model):
  id = models.AutoField(primary_key = True)
  title = models.CharField("标题", max_length=200)
  date = models.DateField("发生时间")
  content = models.TextField("事件描述")
  acmodels = models.ForeignKey(acmodels, on_delete = models.CASCADE)

  def __str__(self):
    return (self.title)

#评论数据模型
class comment(models.Model):
    post = models.ForeignKey(article, on_delete = models.CASCADE, related_name = 'comment')
    name = models.CharField(max_length = 100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name,self.post)


#术语定义部分内容
class terms(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField("概词条念", max_length = 200)
    content = models.TextField("词条说明")
    acmodels = models.ForeignKey(acmodels, on_delete = models.CASCADE, limit_choices_to={'if_intra_ac': True})
    tags = TaggableManager("标签",blank=True)
    source = models.TextField("词条来源",blank=True)

    def __str__(self):
        return (self.title)