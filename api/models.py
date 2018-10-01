from django.db import models


# Create your models here.

class UserGroup(models.Model):
    title = models.CharField(max_length=66)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    user_type_choices = [
        (1, '普通用户'),
        (2, 'vipUser'),
        (3, 'svipUser'),
    ]
    user_type = models.IntegerField(choices=user_type_choices)

    user_name = models.CharField(max_length=66, unique=True)
    password = models.CharField(max_length=66)

    user_group = models.ForeignKey(to='UserGroup')
    user_Role = models.ManyToManyField(to='Role')

    def __str__(self):
        return self.user_name

class UserToker(models.Model):
    user_to = models.OneToOneField(to=UserInfo)
    token = models.CharField(max_length=66, null=True)


class Role(models.Model):
    title = models.CharField(max_length=66)

    def __str__(self):
        return self.title