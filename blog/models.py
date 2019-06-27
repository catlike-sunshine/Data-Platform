from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

#单独建立的用户模型
class  users(models.Model):
  id = models.AutoField(primary_key = True)
  name =  models.CharField(max_length = 100)
  info = models.CharField(max_length = 200, default = "na")


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

<<<<<<< HEAD
=======

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
>>>>>>> b62a42baaa96e7f09ee92cbe27dc5d71a0eda923
