# coding:utf-8
from datetime import date

import django.utils.timezone as timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import hashlib

import blockchain.checkdata

from .models import Block,CommonUser

#from .forms import TransactionForm, IndexQueryForm
from .forms import IdQueryForm

from .generate_chain import create_new_block

sha = hashlib.sha256()

# Create your views here.
def home(request):
    return render(request, 'home.html')

def gene_block(request):
    if Block.objects.exists():
        return_message = "区块链非空！请勿重复创建创世区块！"
    else:
        new_block = Block(index=0)
        new_block.timestamp = timezone.now()

        new_block.trackNum = '这是创世区块！'
        new_block.deviceId = '这是创世区块！'
        new_block.deviceName = '这是创世区块！'
        new_block.dpCreationTime = timezone.now() - date.timedelta(days=3650)  # 随便设置一个很久以前的日期作为初始日期。
        new_block.location = '这是创世区块！'
        new_block.image = '这是创世区块！'

        new_block.previous_hash = "0" * 64
        sha.update(str(new_block.index).encode("utf8") +
                   str(new_block.timestamp).encode("utf8") +
                   str(new_block.trackNum).encode("utf8") +
                   str(new_block.deviceId).encode("utf8") +
                   str(new_block.deviceName).encode("utf8") +
                   str(new_block.dpCreationTime).encode("utf8") +
                   str(new_block.location).encode("utf8") +
                   str(new_block.image).encode("utf8") +
                   str(new_block.previous_hash).encode("utf8")
                   )
        new_block.self_hash = sha.hexdigest()
        new_block.save()
        return_message = "创世区块建立成功！"

    return HttpResponse(str(return_message))
# def add_block(request):
#     return render(request, 'add_block.html')


def query_id(request):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IdQueryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            uid = form.cleaned_data['uid']
            try:
                object_user = CommonUser.objects.get(uid = uid)
                blockchain.checkdata.check_new_data()
            except:
                return HttpResponse("所查询的用户不存在！")

            if object_user in CommonUser.objects.all():
                return HttpResponseRedirect("/query_id_result/?uid="+str(object_user.uid))
            else:
                return HttpResponse("所查询的用户不存在！")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IdQueryForm()

    return render(request, 'query_id.html', {'form': form})

#
def query_id_result(request):
    uid = request.GET['uid']
    info_dict = {}#用来存运单号的数据，自动创建1234...个key
    info_data = {}
    object_user = CommonUser.objects.get(uid = uid)
    info_dict['name'] = object_user.name
    info_dict['uid'] = object_user.uid
    #取出运单号字段进行处理
    trackNumListStr = object_user.trackNumSet
    #trackNumList = trackNumListStr.split(',')
    trackNumListInt=int(trackNumListStr)
#简单的筛选以显示每个身份证对应多个订单
    for block in Block.objects.all():
        if block.index%10 == trackNumListInt:
            keyname = str(block.index)
            info_data[keyname] = block.trackNum
        else:
            index = block.index%10
            if index%10 == trackNumListInt:
                keyname = str(block.index)
                info_data[keyname] = block.trackNum
    return render(request, 'query_id_result.html', {'info_dict': info_dict,'info_data':info_data})

def testfunc(request):
    return HttpResponse(str(blockchain.checkdata.check_new_data()))
#详细信息页
def moremess(request,index):
    object_block = Block.objects.get(index=index)
    info_dict={}
    info_dict['image_ID']= object_block.self_hash
    info_dict['index']= object_block.index
    info_dict['timestamp']= object_block.timestamp
    info_dict['trackname']= object_block.trackNum
    return render(request,'moremessage.html',{'info_dict':info_dict})

def theory(request,index):
    object_block = Block.objects.get(index=index)
    info_dict = {}
    info_dict['previous_hash'] = object_block.previous_hash
    info_dict['index'] = object_block.index
    info_dict['timestamp'] = object_block.timestamp
    info_dict['self_hash'] = object_block.self_hash
    return render(request,'theory.html',{'info_dict':info_dict})

