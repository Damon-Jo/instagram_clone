import os
from uuid import uuid4
from django.shortcuts import render
from rest_framework.response import Response

from .models import Feed
from Jinstagram.settings import MEDIA_ROOT
from user.models import User
# Create your views here.
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed;

        # print('User logged in : ', request.session['email'])
        email = request.session.get('email', None)

        if email is None:
            return render(request, 'user/login.html')

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, 'user/login.html')

        return render(request, "jinstagram/main.html", context=dict(feeds=feed_list, user=user))

class UploadFeed(APIView):
    def post(self, request):

        #at first, read the file
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, like_count=0)

        return Response(status=200)

class Profile(APIView):
    def get(self, request):

        email = request.session.get('email', None)

        if email is None:
            return render(request, 'user/login.html')

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, 'user/login.html')

        return render(request, 'content/profile.html', context=dict(user=user))