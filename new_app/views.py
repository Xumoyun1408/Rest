from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import TravelSerializer, MehmonhonaSerializer, KlassSerializer
from .models import Travel, Mehmonhona, Klass

class TravelView(APIView):
    def get(self,request:Response,pk:int=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                return Response(TravelSerializer(travel).data)
            except:
                return Response({'massage':'Topilmadi'})
      
        travel = Travel.objects.get(pk=pk)
        return Response({'travel':TravelSerializer(travel,many=True).data})
    
    def post(self,request:Response):
        serializer = TravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        travel = serializer.save()
        return Response(TravelSerializer(travel).data)

    def put(self,request:Request,pk:int=None):
        if not pk:
            return Response({'massage':'Method PUT not allowed'})
        try:
            travel = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(travel,data = request.data)
            serializer.is_valid()
            update_travel = serializer.save()
            return Response(TravelSerializer(update_travel).data)
        except:
            return Response({'massage':'Topilmadi'})
            
    def delete(self,request:Request,pk:int):
        if not pk:
            return Response({'massage':'Method Delete not allowed'})
        try:
            travel = Travel.objects.get(pk=pk)
            travel.delete()
            return Response({'massage':'success'})
        except:
            return Response({'massage':'Topilmadi'})
# ------------------------------------------------------------------------------------------------
class KlassView(APIView):
    def get(self,request:Response,pk:int=None):
        if pk:
            try:
                klass = Klass.objects.get(pk=pk)
                return Response(KlassSerializer(klass).data)
            except:
                return Response({'massage':'Topilmadi'})
      
        klass = Klass.objects.get(pk=pk)
        return Response({'klass':KlassSerializer(klass,many=True).data})
      
    def post(self,request:Response):
        serializer = KlassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        klass = serializer.save()
        return Response(KlassSerializer(klass).data)

    def put(self,request:Request,pk:int=None):
        if not pk:
            return Response({'massage':'Method PUT not allowed'})
        try:
            klass = Klass.objects.get(pk=pk)
            serializer = KlassSerializer(klass,data = request.data)
            serializer.is_valid()
            update_klass = serializer.save()
            return Response(klass(update_klass).data)
        except:
            return Response({'massage':'Topilmadi'})
            
    def delete(self,request:Request,pk:int):
        if not pk:
            return Response({'massage':'Method Delete not allowed'})
        try:
            klass = Klass.objects.get(pk=pk)
            klass.delete()
            return Response({'massage':'success'})
        except:
            return Response({'massage':'Topilmadi'})
# ------------------------------------------------------------------------------------------------
class MehmonhonaView(APIView):
    def get(self,request:Response,pk:int=None):
        if pk:
            try:
                mehmonhona = Mehmonhona.objects.get(pk=pk)
                return Response(MehmonhonaSerializer(mehmonhona).data)
            except:
                return Response({'massage':'Topilmadi'})
      
        mehmonhona = Mehmonhona.objects.get(pk=pk)
        return Response({'mehmonhona':MehmonhonaSerializer(mehmonhona,many=True).data})
      
    def post(self,request:Response):
        serializer = MehmonhonaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mehmonhona = serializer.save()
        return Response(MehmonhonaSerializer(mehmonhona).data)
     
    def put(self,request:Request,pk:int=None):
        if not pk:
            return Response({'massage':'Method PUT not allowed'})
        try:
            mehmonhona = Mehmonhona.objects.get(pk=pk)
            serializer = MehmonhonaSerializer(mehmonhona,data = request.data)
            serializer.is_valid()
            update_mehmonhona = serializer.save()
            return Response(Mehmonhona(update_mehmonhona).data)
        except:
            return Response({'massage':'Topilmadi'})
            
    def delete(self,request:Request,pk:int):
        if not pk:
            return Response({'massage':'Method Delete not allowed'})
        try:
            mehmonhona = Mehmonhona.objects.get(pk=pk)
            mehmonhona.delete()
            return Response({'massage':'success'})
        except:
            return Response({'massage':'Topilmadi'})