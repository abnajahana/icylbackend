from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import generics


class ListBanners(generics.GenericAPIView):
    serializer_class=BannersSerializer        
    def get(self, request):
        queryset = Banners.objects.all()
        serializer = BannersSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class ListBannerbyid(generics.GenericAPIView):
    serializer_class=BannersSerializer        
    def get(self, request ,pk):
        queryset = Banners.objects.filter(id=pk)
        serializer = BannersSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class ListPrayers(generics.GenericAPIView):
    serializer_class=PrayerSerializer        
    def get(self, request):
        queryset = Prayer.objects.all()
        serializer = PrayerSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class ListEvent(generics.GenericAPIView):
    serializer_class=EventSerializer        
    def get(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})
            
class ListEventbyid(generics.GenericAPIView):
    serializer_class=EventSerializer        
    def get(self, request,pk):
        queryset = Event.objects.filter(id=pk)
        serializer = EventSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class ListVideo(generics.GenericAPIView):
    serializer_class=VideoSerializer        
    def get(self, request):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class ListVideobyid(generics.GenericAPIView):
    serializer_class=VideoSerializer        
    def get(self, request,pk):
        queryset = Video.objects.filter(id=pk)
        serializer = VideoSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class ListAgegroup(generics.GenericAPIView):
    serializer_class=AgegroupSerializer        
    def get(self, request):
        queryset = Agegroup.objects.all()
        serializer = AgegroupSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class ListCommittee(generics.GenericAPIView):
    serializer_class=CommitteeSerializer        
    def get(self, request):
        queryset = Committee.objects.all()
        serializer = CommitteeSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class AddForm(generics.CreateAPIView):
    serializer_class=FormSerializer        
    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})

class Addduaandspecialrequests(generics.CreateAPIView):
    serializer_class=duaandspecialrequestsSerializer        
    def post(self, request):
        serializer = duaandspecialrequestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})        


class Addfeedbackandquestions(generics.CreateAPIView):
    serializer_class=feedbackandquestionsSerializer        
    def post(self, request):
        serializer = feedbackandquestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})        

class Addsubscribeandnewsletter(generics.CreateAPIView):
    serializer_class=subscribeandnewsletterSerializer        
    def post(self, request):
        serializer = subscribeandnewsletterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})        


class ListCard(generics.GenericAPIView):
    serializer_class=CardSerializer        
    def get(self, request):
        queryset = Card.objects.all()
        serializer = CardSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class ListIndex(generics.GenericAPIView):
    serializer_class=IndexSerializer        
    def get(self, request):
        queryset = Index.objects.all()
        serializer = IndexSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})




class Listbannercard1(generics.GenericAPIView):
    serializer_class=BannerCard1Serializer        
    def get(self, request):
        queryset = CardBanner1.objects.all()
        serializer = BannerCard1Serializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})



class Listbannercard2(generics.GenericAPIView):
    serializer_class=BannerCard2Serializer        
    def get(self, request):
        queryset = CardBanner2.objects.all()
        serializer = BannerCard2Serializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class Listbannercard3(generics.GenericAPIView):
    serializer_class=BannerCard3Serializer        
    def get(self, request):
        queryset = CardBanner3.objects.all()
        serializer = BannerCard3Serializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class okview(generics.GenericAPIView):
    def get(self, request):

        return Response({"ok"})

# class reverse(generics.GenericAPIView):
       
#     def get(self, request):

#         number = int(input("Enter the integer number: "))  

#         # a=revs_number
#         # print(oct(number),"octal number of number is")
#         def decimal_to_octal(decimal):
#             octal = 0
#             i = 1
#             while (decimal != 0):
#                 octal = octal + (decimal % 8) * i
#                 decimal = int(decimal / 8)
#                 i = i * 10;

#             return octal;

#         print("Equivalent octal number : ",decimal_to_octal(number))     #n nte octal

#         h=decimal_to_octal(number)    #n nte octal  ----------------------------------------

#         revs_number = 0  
  
 
  
#         while (number > 0):  
 
#             remainder = number % 10  
#             revs_number = (revs_number * 10) + remainder  
#             number = number // 10  

#         print("reverse number : ",revs_number)  

#         b=revs_number      #n nte reverse
        
#         print("Equivalent octal number of reverse : ",decimal_to_octal(b))

#         c=decimal_to_octal(b)    #reversinte octal        #----------------------------------





#         def countEvenOdd(n):
     
#             even_count = 0
#             odd_count = 0
#             while (n > 0):
#                 rem = n % 10
#                 if (rem % 2 == 0):
#                     even_count += 1
#                 else:
#                     odd_count += 1
             
#                 n = int(n / 10)
     
#             print( "Even count of reverse octal : " , even_count)
#         n = c;
#         t = countEvenOdd(n);



            

#         def countEvenOdd(n):
     
#             even_number_count = 0
#             odd_count = 0
#             while (n > 0):
#                 rem = n % 10
#                 if (rem % 2 == 0):
#                     even_number_count += 1
#                 else:
#                     odd_count += 1
             
#                 n = int(n / 10)
     
#             print( "Even count of octal: " , even_number_count)
 

#         n = h;
#         w = countEvenOdd(n);

        

#         # if(t == w):
#         #     if(t % 2 == 0):
#         #         print("even",t)
#         #     else:
#         #         print("odd",t)

#         while t == w:
#             if (t % 2 == 0):
#                 print("even")
#             else:
#                 print("odd")
#         else:
#             print("Different")

#         return Response({})     






#         # m = h;
#         # l = countEvenOdd(m);

        
#         # if (l == t):
#         #     num=l
#         #     if(l % 2 == 0):
#         #         print("{0} is Even number".format(num))

#         #     else:
#         #         print("odd")
#         # else:
#         #     print("different")


#         # num = int(input("Enter a number: "))  
#         # if (num % 2) == 0:  
#         #     print("{0} is Even number".format(num))  
#         # else:  
#         #     print("{0} is Odd number".format(num))  



#         # print("Different")

        

