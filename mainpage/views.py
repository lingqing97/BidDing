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
from django.http import HttpResponseRedirect
from .models import UserInfo
from .models import Task
from django.contrib.auth.models import User


# Create your views here.
def ShowHomePage(request):
    template = get_template('homePage.html')
    html = template.render(locals())
    return HttpResponse(html)


def Login(request):
    template = get_template('loginauth.html')
    username = None
    if request.user.is_authenticated():
        user = request.user
        submitTask = Task.objects.filter(pusher=user)
        receiveTask = Task.objects.filter(receiver=request.user.username)
        messages.add_message(request, messages.INFO, "welcome %s" % request.user.username)
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
                    user = User.objects.filter(username=username)
                    submitTask = Task.objects.filter(pusher=user)
                    receiveTask = Task.objects.filter(receiver=username)
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


def Logout(request):
    template = get_template('homePage.html')
    auth.logout(request)
    messages.add_message(request, messages.INFO, '成功注销了')
    html = template.render(locals(), request)
    return HttpResponse(html)


def ShowUserHomePage(request):
    if request.user.is_authenticated():
        username = request.user.username
        user = request.user
        submitTask = Task.objects.filter(pusher=user)
        receiveTask = Task.objects.filter(receiver=request.user.username)
        template = get_template('UserHomePage.html')
        html = template.render(locals())
    else:
        return HttpResponseRedirect('/')
    return HttpResponse(html)


def ShowUserBiddingPage(request):
    if request.user.is_authenticated():
        template = get_template('UserBiddingPage.html')
        username = request.user.username
        if request.method == 'GET':
            user = request.user
            tasks = Task.objects.exclude(pusher=user).filter(status=False)
            html = template.render(locals())
        else:
            pusher_name = request.POST.get('pusher')
            pusher=User.objects.filter(username=pusher_name)
            date = request.POST.get('date',None)
            task = request.POST.get('task',None)
            pay = request.POST.get('pay',None)
            bidTask = Task.objects.filter(pusher=pusher,task=task,pay=pay)
            if bidTask:
                messages.add_message(request, messages.INFO, '接单成功')
                bidTask.update(status=True, receiver=username)
                html = template.render(locals(), request)
            else:
                messages.add_message(request, messages.INFO, '接单失败')
                html = template.render(locals(), request)
            return HttpResponse(html)
    else:
        return HttpResponseRedirect('/')
    return HttpResponse(html)


def ShowUserSubmitPage(request):
    if request.user.is_authenticated():
        template = get_template('UserSubmitPage.html')
        if request.method == 'GET':
            newtask = NewTask()
            html = template.render(locals(), request)
        else:
            user = request.user
            task_form = Task(pusher=user)
            newtask = NewTask(request.POST, instance=task_form)
            if newtask.is_valid():
                messages.add_message(request, messages.INFO, '提交成功')
                newtask.save()
                html = template.render(locals(), request)
            else:
                messages.add_message(request, messages.INFO, '提交失败')
                html = template.render(locals(), request)
        return HttpResponse(html)
    else:
        return HttpResponseRedirect('/')


def ShowUserInfoPage(request):
    if request.user.is_authenticated():
        username = User.objects.get(username=request.user.username).username
        email = User.objects.get(username=request.user.username).email
        if UserInfo.objects.filter(user=request.user).exists():
            user = UserInfo.objects.get(user=request.user)
        else:
            user = None
        if request.method == 'GET':
            newuser_info = userinfo()
            template = get_template('UserInfoPage.html')
            html = template.render(locals(), request)
            return HttpResponse(html)
        else:
            newuser_info = userinfo(request.POST)
            if newuser_info.is_valid():
                messages.add_message(request, messages.INFO, '修改成功')
                UserInfo.objects.filter(user=request.user).update(age=newuser_info.cleaned_data['age'] \
                                                                  , phone=newuser_info.cleaned_data['phone'],
                                                                  apartment=newuser_info.cleaned_data['apartment'] \
                                                                  , address=newuser_info.cleaned_data['address'],
                                                                  interest=newuser_info.cleaned_data['interest'])
                return HttpResponseRedirect('/userInfo/')
            else:
                messages.add_message(request, messages.WARNING, '修改失败')
                return HttpResponseRedirect('/userInfo/')
    else:
        return HttpResponseRedirect('/')
