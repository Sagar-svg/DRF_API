from django.shortcuts import render



from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes

from apiclient.discovery import build
API_KEY = "AIzaSyDAT4w2gVsDI0RJc35wVoBE71ouMbl2Zv4"

@api_view(('GET',))
def snippet_list(request, qu):
    yt = build('youtube', 'v3', developerKey = API_KEY)
    req = yt.search().list(q = qu, part='snippet', type='video', maxResults=10)
    res = req.execute()
    res_dict = {'id':[], "data":[]}
    for item in res['items']:
        res_dict['id'].append(item['id'])
        res_dict["data"].append(item["snippet"])
    
    return Response(res_dict)

