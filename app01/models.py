from django.db import models

# Create your models here.
class Userinfo(models.Model):
    """
    员工表
    """
    name=models.CharField(max_length=32,verbose_name="员工姓名")

    def __str__(self):
        return self.name

class ClassList(models.Model):
    """
    班级表
    """
    name=models.CharField(max_length=32,verbose_name="班级名")

    def __str__(self):
        return self.name

class Student(models.Model):
    """
    学生表
    """
    user=models.CharField(max_length=16,verbose_name="学生姓名")
    pwd=models.CharField(max_length=32,verbose_name="密码",unique=True)
    classlist=models.ForeignKey(to="ClassList")

    def __str__(self):
        return self.user

class Questionnaire(models.Model):
    """
    调查问卷表
    """
    title=models.CharField(max_length=64,verbose_name="调查问卷表名")
    classlist=models.ForeignKey(to="ClassList")
    userinfo=models.ForeignKey(to="Userinfo")
    def __str__(self):
        return self.title


class  Question(models.Model):
    """
    问题表
    """
    caption=models.CharField(max_length=64,verbose_name="问题表名")      # caption 标题

    question_types=(
        (1,"打分(1~10)分"),
        (2,"单选"),
        (3,"评价"),
    )
    type=models.IntegerField(choices=question_types)
    def __str__(self):
        return self.caption

class Option(models.Model):
    """
    单选题的选项表
    """
    name=models.CharField(max_length=32,verbose_name="选项名称")
    score = models.IntegerField(verbose_name='选项对应的分值')
    question = models.ForeignKey(to=Question)
    def __str__(self):
        return self.name

class Answer(models.Model):
    """
    回答表
    """
    student=models.ForeignKey(to="Student")
    question = models.ForeignKey(to=Question)

    option = models.ForeignKey(to="Option", null=True, blank=True)
    val = models.IntegerField(null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
