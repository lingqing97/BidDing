# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import *
from django.template.loader import get_template
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from froms import *
from django.contrib import auth
# Create your views here.
def ShowHomePage(request):
    template=get_template('homePage.html')
    html=template.render(locals())
    return HttpResponse(html)

def Login(request):
    template = get_template('loginauth.html')
    username = None
    if request.user.is_authenticated():
        user = request.user
        # diaries = Diary.objects.filter(user=user)
        messages.add_message(request,messages.INFO,"welcome %s"%request.user.username)
        template = get_template('UserHomePage.html')
        username = request.user.username
    else:
        if request.method == 'GET':
            loginform = LoginForm()
        else:
            loginform = LoginForm(request.POST)
            if loginform.is_valid():
                username = auth.authenticate(request, username=loginform.cleaned_data['username'],
                                             password=loginform.cleaned_data['password'], age=0, interest='',
                                             birthday='', phone='')
                if username and username.is_active:
                    # user = User.objects.filter(username=username)
                    # diaries = Diary.objects.filter(user=user)
                    messages.add_message(request, messages.INFO, "welcome %s" % request.user.username)
                    template = get_template('UserHomePage.html')
                    auth.login(request, username)
                else:
                    username = None
                    messages.add_message(request, messages.WARNING, '密码错误或账号未注册')
            else:
                username = None
                messages.add_message(request, messages.WARNING, '请输入完整的账号和密码')
    html = template.render(locals(), request)
    return HttpResponse(html)