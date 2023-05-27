from django.shortcuts import render
from .models import Feed

# Create your views here.
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all() # select * from content_feed;
        print(feed_list)
        return render(request, "jinstagram/main.html")