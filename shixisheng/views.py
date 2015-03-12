#coding:utf-8
from django.http import HttpResponse#这个函数用来处理返回
from django.shortcuts import render_to_response,redirect
from .models import Text,tImage,Index,Item,GoodStudent,Company,Student,Image
import datetime
from django.forms.models import modelform_factory
from django.template import RequestContext
from django.template.response import TemplateResponse as TR
def home(request):
	a = Text.objects.get(id = 1)
	b = tImage.objects.get(id = 1)
	c = Company.objects.all()[:8]
	e = Index.objects.all()[:8]
	g = Item.objects.all()
	h = Item.objects.all()[5:]
	d = {'a':a,'b':b,'c':c,'e':e,'g':g,'h':h}
	all_text = Text.objects.all() 
	all_img = tImage.objects.all()
	for i in all_text:
		d[i.txt] = i.test
	for i in all_img:
		d[i.name] = i.img
	return render_to_response('index.html',d,context_instance=RequestContext(request))
def goodstudent(request):
	f = GoodStudent.objects.all()
	d = {'f':f}
	all_text = Text.objects.all()
	for i in all_text:
		d[i.txt] = i.test
	return render_to_response('goodstudent.html',d)

def theme(request):
	return render_to_response('theme.html')
def indextw(request):
	return render_to_response('indextwo.html')
def item(request):
	return render_to_response('item.html')
def liucheng(request):
	return render_to_response('flow.html')


def companys(request):
	a = Text.objects.get(id = 1)
	b = tImage.objects.get(id = 1)
	c = Company.objects.all()[:8]
	d = {'a':a,'b':b,'c':c}
	all_text = Text.objects.all()
	all_img = tImage.objects.all()
	for i in all_text:
		d[i.txt] = i.test
	for i in all_img:
		d[i.name] = i.img
	return render_to_response('company.html',d)
def comone(request):
	return render_to_response('companyone.html')
def comsec(request):
	return render_to_response('comsec.html')
def comthr(request):
	return render_to_response('comthree.html')



def students(request):
	c = Company.objects.all()[:8]
	d = {'c':c}
	return render_to_response('student.html',d)

def daoshi(request):
	return render_to_response('daoshi.html')

def register(request):
	a = {}
	all_img = tImage.objects.all()
	for i in all_img:
		a[i.name] = i.img
	return render_to_response('zhuce.html',a)





def lc(request):
	return render_to_response('lc.html')
def fd(request):
	all_img = tImage.objects.all()
	d = {}
	for i in all_img:
		d[i.name] = i.img
	return render_to_response('fd.html',d)
def time(request):
	return HttpResponse(str(datetime.datetime.now()))

#上面4和6行声明
def upload(request):
	conta_form = modelform_factory(GoodStudent)
	print request.POST
	a = conta_form(request.POST,request.FILES)  #POST里面是文件名，内容在FILE里
	if a.is_valid():
		#a.name = request.POST['name']
		#a.click = request.POST['click']	
		#a.img = request.POST['img']
		a.save()
	print a
	#return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('/media/%s').closest('.mce-window').find('.mce-primary').click();</script>"%img.img)
	#return HttpResponse(str(img.img))
	return redirect("/index")
