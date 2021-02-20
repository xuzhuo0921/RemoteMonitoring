from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator
from monitor.models import Host
from datetime import datetime
import paramiko
import json

# Create your views here.

def index(request,pIndex=1):
    ''' 首页 '''
    # return HttpResponse("Hello,world")
    print('------index-------')
    hostList = Host.objects.get_queryset().order_by('id')
    p = Paginator(hostList,6)
    # if pIndex == "":
    #     print("index=0")
    # else:
    #     print("index=",pIndex)
    aList = p.page(pIndex)
    pList = p.page_range
    pNum = p.num_pages
    # for host in aList:
    #     print(host.__dict__)    
    context = {"hostlist":aList,"pList":pList,"pIndex":int(pIndex),"pNum":int(pNum)}
    # print(context)
    return render(request,"monitor/index.html",context)

def add(request):
    ''' 添加远程主机 '''
    print('------add-------')
    return render(request,'monitor/add.html')   

def insert(request):
    ''' 执行添加远程主机 '''
    print('------insert-------')
    try:
        newhost = Host()
        newhost.tag = request.POST['tag']
        newhost.ip = request.POST['ip']
        newhost.cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        newhost.save()
        print("添加成功~")
        try:
            newdetail = json.loads(get_stat(newhost.ip))
            newhost.cpu = newdetail['cpu_count']
            newhost.mem = newdetail['mem_total']/1024/1024/1024
            newhost.disk = newdetail['disk_total']/1024/1024/1024
            newhost.stat = 1
            newhost.save()
        except Exception as err:
            newhost.stat = 0
            newhost.save()

    except Exception as err:
        print(err)
        print("添加失败~")
    return redirect(reverse('index'))

def details(request,hid):
    ''' 查看远程主机详情 '''
    print('------details-------')
    # ipaddr = request.GET.get('ip')
    # print(ipaddr)
    # print("id = %s" % hid)
    host = Host.objects.get(id=hid)
    # print(host)
    context = {"interval":5,"host":host}
    # print('context:',context)
    return render(request,"monitor/details.html",context)
    # return HttpResponse(context)

def edit(request,hid):
    ''' 编辑远程主机 '''
    print('------edit-------')
    try:
        host = Host.objects.get(id=hid)
        context = {'host': host}
        return render(request, "monitor/edit.html",context)
    except Exception as err:
        print(err)
        print("没有找到要修改的主机")
        return redirect(reverse('index'))
    # return HttpResponse("------edit-------")

def delete(request,hid):
    ''' 删除远程主机 '''
    print('------delete-------')
    try:
        host = Host.objects.get(id=hid)
        host.delete()
        print("删除成功~")
    except Exception as err:
        print(err)
        print("删除失败~")
    return redirect(reverse('index'))
    # return HttpResponse("------delete-------")

def update(request,hid):
    ''' 执行修改远程主机 '''
    print('------update-------')
    try:
        host = Host.objects.get(id=hid)
        print('tag:',request.POST['tag'])
        host.tag = request.POST['tag']
        host.ip = request.POST['ip']
        host.cpu = request.POST['cpu']
        host.mem = request.POST['mem']
        host.disk = request.POST['disk']
        host.save()
        print("修改成功~")
    except Exception as err:
        print(err)
        print("修改失败~")
    return redirect(reverse('index'))

    # return HttpResponse("------update-------")

def get_host_stat(request,ipaddr):

    data = get_stat(ipaddr)
    return HttpResponse(data, content_type="application/json")

def get_stat(ipaddr):
    ssh = paramiko.SSHClient()
    # 设置为接受不在known_hosts 列表的主机可以进行ssh连接
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ipaddr, username="root", timeout=4.5)
        cmd_file = open('./static/run.py',"r")
        cmd = cmd_file.read()
        stdin, stdout, stderr = ssh.exec_command(cmd)
        data = stdout.read().decode()
    except Exception as err:
        print(err)
        print('ssh 链接出错')
    return data

def test(request):
    context = {}
    context['hello'] = 'Hello zhuobabe!'
    return render(request, 'monitor/test.html', context)
