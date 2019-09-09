from django.shortcuts import render
from users.models import User, EventMaster, EventSport, SportsMaster, Templates, Selection
from users.forms import EmailForm
import json, requests, urllib
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.core import serializers

# Create your views here.


def index(request):
    return render(request,'users/index.html',{
        'sports':SportsMaster.objects.all(),
        'options':Selection.objects.all(),
    })

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

def recommendationPage(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST.get('userid'))
            # uid = User.objects.get(email='jayanth27398@gmail.com')
            select = request.POST.get('selected')
            if select != 'Events':
                return render(request,'users/recommend.html',{
                    'req_err':'API is not available for '+select,
                })
            selected = Selection.objects.get(name=select)
            url = str(selected.url)+str(uid.userid) + \
                '/'+str(selected.endpoint)+'?recompute=true&limit=20&offset=0'

            if selected.location:
                lat = 13.056
                lng = 77.5938
                if request.POST.get('geocode-lat'):
                    lat = request.POST.get('geocode-lat')
                if request.POST.get('geocode-lng'):
                    lng = request.POST.get('geocode-lng')
                url += '&latitude='+str(lat) + '&longitude='+str(lng)
            
            sportsid = request.POST.get('sportid')
            if sportsid:
                url+= '&sports_id='+str(sportsid)

            # print(url)
            # url = 'https://preprodrecoengine.decathlon.in/recommend_api/v1/users/'+uid.userid + \
            #     '/eventsforyou?latitude='+str(lat)+'&longitude=' + \
            #     str(lng)+'&recompute=true&limit=20&offset=0&sports_id='+sportsid
            
            # url = 'https://preprodrecoengine.decathlon.in/recommend_api/v1/users/'+uid.userid + \
            #     '/eventsforyou?latitude='+str(lat)+'&longitude=' + \
            #     str(lng)+'&recompute=true&limit=20&offset=0'

            url ='https://preprodrecoengine.decathlon.in/recommend_api/v1/users/924afe9c-0991-4d6c-9443-cd75afe5e5c6/eventsforyou?latitude=13.056&longitude=77.5938&recompute=true&limit=20&offset=0'
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
                i=0
                for res in result:
                    try:
                        sid = EventSport.objects.filter(
                            eventId=res['event_id'])
                        # print(len(sid))
                        event = EventMaster.objects.get(uuid=res['event_id'])
                        for i in range(len(sid)):
                            events.append(event)
                            sports.append(SportsMaster.objects.get(
                                uuid=(sid[i].sportsId)))
                            # location.append(reverseGeocode(event.lat,event.lng))
                            location.append("Location")
                    except Exception as e:  
                        print(e) 
                # print(result)
                return render(request, 'users/recommend.html', {
                    'response': zip(events,sports,location),
                })
            except:
                return render(request, 'users/recommend.html', {
                    'req_err':"Api error",
                })

        except:
            return redirect('users:index')
    else:   
        return HttpResponseRedirect("/")


def reverseGeocode(latitude,longitude):

    apikey = 'AIzaSyDUO1omLbgXEl7XwDeeuP_2JtvmSKg98Q0'
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
