from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("called get")
        return render(request, "jinstagram/main.html")

    def post(self, request):
        print("called post")
        return render(request, "jinstagram/main.html")