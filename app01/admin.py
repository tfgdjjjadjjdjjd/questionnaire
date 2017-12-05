from django.contrib import admin

from . import models
admin.site.register(models.Userinfo)
admin.site.register(models.ClassList)
admin.site.register(models.Student)
admin.site.register(models.Questionnaire)
admin.site.register(models.Question)
admin.site.register(models.Option)
admin.site.register(models.Answer)
