#coding:utf-8
from django.db import models


#多余的文字和图片
class tImage(models.Model):
	name = models.CharField(max_length=30)
	data = models.CharField(max_length=350)
	img  = models.ImageField(upload_to = './img')
class Text(models.Model):
	test = models.CharField(max_length=1024)
	txt  = models.CharField(max_length=1024)
#首页
class Index(models.Model):
	name = models.CharField(max_length=500)
	intr = models.TextField()
	click = models.TextField()
	img  = models.ImageField(upload_to = './img')
class Item(models.Model):
	name = models.CharField(max_length=500)
	intr = models.TextField()
	click = models.TextField()
class GoodStudent(models.Model):
	click = models.TextField()
	name = models.CharField(max_length=500)
	img  = models.ImageField(upload_to = './img')



#公司页面
class Company(models.Model):
	name = models.CharField(max_length=64)
	intr = models.TextField()
	img  = models.ImageField(upload_to = './img')



#学生页面
class Student(models.Model):
	name = models.CharField(max_length=64)
	intr = models.TextField()
	img  = models.ImageField(upload_to = './img')


class Image(models.Model):
	img  = models.ImageField(upload_to = './img')

