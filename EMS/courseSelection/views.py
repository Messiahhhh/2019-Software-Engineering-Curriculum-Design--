from django.shortcuts import render
import pymysql
# Create your views here.
import numpy
import cv2
def welcome(request):
    return render(request, 'Welcome.html')  # 引入欢迎页
