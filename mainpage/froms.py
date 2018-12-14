# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from mainpage.models import UserInfo
from mainpage.models import Task
from django.forms import Textarea
class LoginForm(forms.Form):
    username=forms.CharField(label='姓名',max_length=20)
    password=forms.CharField(label='密码',max_length=20,widget=forms.PasswordInput())

class userinfo(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=['age','phone','apartment','address','interest']
    def __init__(self,*args,**argv):
        forms.ModelForm.__init__(self,*args,**argv)
        self.fields['age'].label='年龄:'
        self.fields['phone'].label='手机号:'
        self.fields['apartment'].label='部门:'
        self.fields['address'].label='住址:'
        self.fields['interest'].label='兴趣:'

class NewTask(forms.ModelForm):
    class Meta:
        model=Task
        fields=['task','pay','img']
        widgets={'task':Textarea(attrs={'cols':80,'rows':10,'vertical-align':'bottom'}),
                 }
    def __init__(self,*args,**argv):
        forms.ModelForm.__init__(self,*args,**argv)
        self.fields['task'].textarea='任务描述:'
        self.fields['pay'].label='任务定价:'
        self.fields['img'].label='任务图片:'