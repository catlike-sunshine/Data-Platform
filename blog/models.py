from django.db import models

# Create your models here.

#单独建立的用户模型
class  users(models.Model):
  id = models.AutoField(primary_key = True)
  name =  models.CharField(max_length = 100)
  info = models.CharField(max_length = 200, default = "na")


class acmodels(models.Model):
    id = models.AutoField(primary_key = True)
    basic_acmodels = models.CharField("基本型号", max_length = 100)
    expanded_acmodels = models.CharField("扩展型号", max_length = 100)

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

