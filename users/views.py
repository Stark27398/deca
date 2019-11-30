from django.shortcuts import render
from users.models import *
import json, requests, urllib
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.core import serializers
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.templatetags.staticfiles import static
import csv
import importlib
import sys
from django.views.decorators.csrf import csrf_exempt
import uuid
# Create your views here.
@csrf_exempt
def home(request):
    return render(request, 'users/home.html', {
        'sports': Sportsmaster.objects.all(),
        'options': Selection.objects.all(),
    })

@csrf_exempt
def index(request):
    return render(request,'users/index.html',{
        'sports':Sportsmaster.objects.all(),
        'options':Selection.objects.all(),
    })


@csrf_exempt
def createUser(request):
    gender = request.POST['gender_id']
    sportsId = request.POST['sports_id']
    sportsId = json.loads(sportsId)
    uid = uuid.uuid1()
    params = {
        "gender_id": gender,
        "sport_preferences": sportsId,
    }
    print(params)
    url = "https://deca-reco.azurewebsites.net/appdata_api/v1/users/"+str(uid)
    print(url)
    res = requests.post(url,json=params)
    print(res.status_code)
    return JsonResponse({'uuid':uid,'success':True},safe=False)

def error(request):
    try:
        uid = User.objects.get(email=request.GET.get('userid'))
    except:
        return HttpResponse(0)
    return HttpResponse(1)

def form(request):
    name=request.GET['selected']
    event = Selection.objects.get(name=name)
    template = Templates.objects.get(typeof='template')
    e = json.loads(serializers.serialize('json', [event, ]))
    t = json.loads(serializers.serialize('json', [template, ]))
    data =  json.dumps({
        'event':e,
        'template':t,
    })
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def recommendationPage(request):
    if request.method == 'POST':
        try:
            uid = request.POST.get('user_id')
            print(uid)
            # uid = User.objects.get(email='jayanth27398@gmail.com')
            # select = request.POST.get('selected')
            # if select != 'Events':
            #     return render(request,'users/recommend.html',{
            #         'req_err':'API is not available for '+select,
            #     })
            select='User'
            checked = []
            # gender = request.POST['gender_id']
            # sportsId = request.POST['sports_id']
            # sportsId = json.loads(sportsId)
            # uid = uuid.uuid1()
            # params = {
            #     "gender_id": gender,
            #     "sport_preferences": sportsId,
            # }
            # print(params)
            # url = "https://deca-reco.azurewebsites.net/appdata_api/v1/users/"+str(uid)
            # print(url)
            # res = requests.post(url, json=params)
            # print('Status code',res.status_code)
            selected = Selection.objects.get(name=select)
            if selected.notAvailable:
                return render(request,'users/recommend.html',{
                    'req_err':'API is not available for '+selected.name,
                })
            url = str(selected.url)+str(uid) + \
                '/'+str(selected.endpoint)+'?recompute=true&limit=20&offset=0'
            if selected.location:
                lat = 13.056
                lng = 77.5938
                if request.POST.get('geocode-lat'):
                    lat = request.POST.get('geocode-lat')
                if request.POST.get('geocode-lng'):
                    lng = request.POST.get('geocode-lng')
                url += '&latitude='+str(lat) + '&longitude='+str(lng)
            
            if selected.check:
                if(request.POST.get('event')):
                    checked.append(int(request.POST.get('event')))
                if(request.POST.get('class')):
                    checked.append(int(request.POST.get('class')))
                if(request.POST.get('facility')):
                    checked.append(int(request.POST.get('facility')))

            sport_id = request.POST['sport_id']
            sport_id = json.loads(sport_id)
            sport = []
            for s in sport_id:
                sport.append(s['sport_id'])
            print('checked',checked)
            print(sport)
            # print(checked)
            print(url)
            # url = 'https://preprodrecoengine.decathlon.in/recommend_api/v1/users/'+uid.userid + \
            #     '/eventsforyou?latitude='+str(lat)+'&longitude=' + \
            #     str(lng)+'&recompute=true&limit=20&offset=0&sports_id='+sportsid
            
            # url = 'https://preprodrecoengine.decathlon.in/recommend_api/v1/users/'+uid.userid + \
            #     '/eventsforyou?latitude='+str(lat)+'&longitude=' + \
            #     str(lng)+'&recompute=true&limit=20&offset=0'

            # url ='https://prodrecoengine.decathlon.in/recommend_api/v1/users/81b5b618-0d3b-437c-97c5-2bb0344bd757/foryou?recompute=true&limit=20&offset=0&latitude=12.9715987&longitude=77.59456269999998'
            # uid = User.objects.get(email='jayanth27398@gmail.com')
            # lat = 13.056
            # lng = 77.5938
            # sportsid=uid.userid
            # url = 'https://preprodrecoengine.decathlon.in/recommend_api/v1/users/'+uid.userid + \
            #     '/eventsforyou?latitude='+str(lat)+'&longitude=' + \
            #     str(lng)+'&recompute=true&limit=20&offset=0&sports_id='+sportsid
            try:
                response = urllib.request.urlopen(url)
                result = json.loads(response.read().decode(
                    response.info().get_param('charset') or 'utf-8'))
                events=[]
                sports=[]
                location=[]
                typeId=[]
                content=[]
                className=[]
                error_i=0
                for res in result:
                    try:
                        if (not checked) or (int(res['content_type_id']) in checked):
                            clsName = contentId.objects.get(
                                typeId=res['content_type_id'])
                            
                            if clsName not in content:
                                content.append(clsName)
                            # cls_ = getattr(importlib.import_module(
                            #     "users.models"), clsName.name)
                            # spt_ = getattr(importlib.import_module(
                            #     "users.models"), clsName.sport)
                            cls_ = str_to_class(clsName.name)
                            spt_ = str_to_class(clsName.sport)
                            # print(type(clsName),clsName.sport)
                            # print(cls_.objects.all())
                            # print(type(spt_))

                            sid = spt_.objects.filter(**{clsName.key:res[selected.keyId]})
                            # print(len(sid))
                            event = cls_.objects.get(**{clsName.key:res[selected.keyId]})
                            for i in range(len(sid)):
                                if str(sid[i].sport_id) in sport:
                                    # print(sid[i].sport_id)
                                    events.append(event)
                                    sports.append(Sportsmaster.objects.get(
                                        sport_id=(sid[i].sport_id)))
                                    try:
                                        location.append(reverseGeocode(event.latitude,event.longitude))
                                    except:
                                        location.append("")
                                    # location.append(StoreDetails.objects.get(storeId=event.businessId))
                                    typeId.append(clsName.typeId)
                                    className.append(clsName.classtype)
                            # print(className)
                    except Exception as e:  
                        print('error : %s' % e)
                        error_i+=1 
                print('no of error :',error_i)
                return render(request, 'users/recommend.html', {
                    'response': zip(events,sports,location,typeId,className),
                    'content':content,
                })
            except Exception as e:
                print(e)
                return render(request, 'users/recommend.html', {
                    'req_err':"Api error",
                })

        except Exception as e:
            print(e)
            return redirect('users:index')
    else:   
        return HttpResponseRedirect("/")



def reverseGeocode(latitude,longitude):

    apikey = 'AIzaSyA38JrOcxhg7v-JMeCY8T57UOhC7nmIauY'
    base = "https://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&key={key}".format(
        lat=latitude,
        lon=longitude,
        key=apikey
    )
    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url)
    response=json.loads(response.content)
    return response['results'][0]['formatted_address']

def upload(request):
    alert='None'
    if request.method == 'POST':
        global d
        csvfile = request.FILES['myfile']
        print(csvfile)
        f = (csvfile.read().decode('utf-8')).splitlines()
        data = csv.reader(f)
        d = None
        if "store" in str(csvfile).lower():
            d = StoreDetails()
        elif "sport" in str(csvfile).lower():
            if "event" in str(csvfile).lower():
                d = EventSport()
            elif "class" in str(csvfile).lower():
                d = ClassSport()
            elif "facility" in str(csvfile).lower():
                d= FacilitySport()
            else:
                d=SportsMaster()
        elif "master" in str(csvfile).lower():
            if "event" in str(csvfile).lower():
                d = EventMaster()
            elif "class" in str(csvfile).lower():
                d = ClassMaster()
            elif "facility" in str(csvfile).lower():
                d = FacilityMaster()
        elif "user" in str(csvfile).lower():
            d = User()
        print(d.__class__.__name__)
        class_ = getattr(importlib.import_module(
            "users.models"), d.__class__.__name__)
        print(type(d))
        att=[]
        for a in d.__dict__.keys():
            if (a!='_state') and (a!='id') :
                att.append(a)
        print(att)
        for row in data:
            dt=class_()
            for i in range(len(row)):
                if att[i] != '_state' or att[i] != 'id':
                    if row[i]=='TRUE':
                        setattr(dt,att[i],True)
                    elif row[i] == 'FALSE':
                        setattr(dt, att[i], False)
                    else:
                        if row[i]=='':
                            row[i]=None
                        setattr(dt,att[i],row[i])
            dt.save()
        alert='Success'
    return render(request,'users/upload.html',{
        'alert':alert,
    })


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)
