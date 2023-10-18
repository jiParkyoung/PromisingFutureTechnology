from cProfile import label
from django.shortcuts import render
from pip import main

# Create your views here.
from .models import Total
from .models import ThesisUse
from .models import market
from .models import link
import json
from django.http import JsonResponse
from . import model_USE
from kss import split_sentences
import numpy as np

def index(request):
    print("page1")
    totals =Total.objects.order_by('key')
    totals_key = totals.values_list('key',flat=True).distinct()
    keys=[]
    for i in totals_key:
        totals_orderT =Total.objects.order_by('title')
        totals_title = totals_orderT.values_list('title',flat=True).filter(key=i).distinct()
        keys.append([i,totals_title.count()])
   
    keys.sort(key=lambda x: (x[1], x[0]),reverse=True)
    key_list=[i[0] for i in keys]

    keys=[]
    for i in key_list:
        keys.append([Total.objects.filter(key=i),Total.objects.filter(key=i).values_list('title',flat=True).distinct()])
    # print(key_list)  
    data=""
    for i in key_list:
        data += i+","+str(Total.objects.filter(key=i).values_list('title',flat=True).distinct().count())+","
    data=data[:-1]    
    return render(request,'main/index.html',{'totals':keys, 'data':data})

def second(request,key):
    print("page2")
    totals =Total.objects.filter(key=key).order_by('title')
    totals_title = totals.values_list('title',flat=True).distinct()
    titles_s=[]
    for i in totals_title:
            totals_orderT =Total.objects.order_by('title')
            totals_title1 = totals_orderT.values_list('label',flat=True).filter(title=i,label='1')
            titles_s.append([i,totals_title1.count()])
    titles_s.sort(key=lambda x: (x[1], x[0]),reverse=True)
    titles_list_s=[i[0] for i in titles_s]

    mid_count =totals_title.count()
    all=Total.objects.all().order_by('title')
    all=all.values_list('title',flat=True).distinct()
    
    market_content=market.objects.filter(key__iexact=key)
    market_content=market_content.values()[0]['contents']

    #년도 그래프

    y_2019=Total.objects.filter(key=key,year=2019).order_by('title').values_list('title',flat=True).distinct()
    y_2020=Total.objects.filter(key=key,year=2020).order_by('title').values_list('title',flat=True).distinct()
    y_2021=Total.objects.filter(key=key,year=2021).order_by('title').values_list('title',flat=True).distinct()
    return render(request,'main/second.html',{'mid_key':key,'mid_count':mid_count, 'all':all,
                                              'y_2019':y_2019, 'y_2020':y_2020, 'y_2021':y_2021, 'market_content':market_content,'titles_s':titles_list_s})

def third(request,title,key):
    print("page3")
    goods = Total.objects.filter(title__iexact=title,label=1)
    bads = Total.objects.filter(title__iexact=title,label=2)
    year= ThesisUse.objects.filter(title__iexact=title+'.pdf').values_list('year','month','use')
    data=""
    # print(type(year.))
    for i in reversed(year):
        data += ','.join(map(str, i))+','
    data=data[:-1] 
    
    links=link.objects.filter(title__iexact=title)
    url=links.values()[0]['URL']


    # good_per=[i.percentage*100 for i in goods]
    # bad_per=[i.percentage*100 for i in bads]
    return render(request,'main/third.html',{'mid_key':key, 'title':title, 'goods':goods, 'bads':bads,'data':data,'url':url})


def model(request):
    return render(request,'main/model.html')
def first(request):
    return render(request,'main/firstpage.html')

def model_use(request):
    jsonObject= json.loads(request.body)
    user_text=jsonObject.get('content')
    text_split=split_sentences(user_text)
    #######예측

    test_eval=[]
    for i in text_split:
        data = [i, '0']
        dataset_another = [data]
        another_test = model_USE.BERTDataset(dataset_another, 0, 1, model_USE.tok, model_USE.max_len, True, False)
        test_dataloader = model_USE.torch.utils.data.DataLoader(another_test, batch_size=model_USE.batch_size, num_workers=5)

        for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
            token_ids = token_ids.long().to(model_USE.device)
            segment_ids = segment_ids.long().to(model_USE.device)

            valid_length= valid_length
            label = label.long().to(model_USE.device)

            out = model_USE.model(token_ids, valid_length, segment_ids)
            soft=out.detach().cpu().numpy()
            a=np.array(list(soft[0]))
            a=list(model_USE.softmax(a))
            #test_eval.append(a.index(max(a)))
            if max(a)>=0.7:
                test_eval.append(a.index(max(a)))
            else:
                test_eval.append(3)

    for i,v in enumerate(test_eval):
        if v==1:
            test_eval[i]='촉진'
        elif v==2:
            test_eval[i]='저해'
        else:
            test_eval[i]='중립'

    result_dict={'data':[]}
    for i in range(len(text_split)):
        result_dict['data'].append({'text':text_split[i], 'value':test_eval[i]})
    
    #result=json.dumps(result_dict)
    #print(result)
    return JsonResponse(result_dict)