from ast import Sub
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking


from .models import Booking, Subject
# Create your views here.

def index(request):
    # who
    user = User.objects.get(pk=request.user.id)

    # enrolled subject
    enrolled_subjects = Booking.objects.filter(user=user)

    id = []
    for subject in enrolled_subjects:
        id.append(subject.course_number.id)
    subjects = Subject.objects.exclude(pk__in=id)

    return render(request, "booking/index.html",{
        'subjects': subjects
    })

def bookings(request, subject_id):
    user = User.objects.get(pk=request.user.id)
    subject = Subject.objects.get(id=subject_id)

    check = Booking.objects.filter(user=user, course_number=subject).first()

    if check is None:
        booking = Booking.objects.create(user=user, course_number=subject)

        subjects = Booking.objects.filter(user=user)
        print(subject)
        return render(request,'booking/booking.html', {
            'subjects': subjects,
        })

    # try:
    #     user = User.objects.get(pk=request.user.id)
    #     subject = Subject.objects.get(id=subject_id)

    #     check = Booking.objects.get(user=user, course_number=subject)
    #     print('check:', check)
    #     if not check:
    #         booking = Booking.objects.create(user=user, course_number=subject)
    #     ##showbooking = Booking.objects.filter(user=user) 

    #         subject = Booking.objects.filter(user=user)
    #         print(subject)
    #         return render(request,'booking/booking.html', {
    #             'bookings': bookings,
    #         })
    # except Exception as e:
    #     print("Error on booking : ", e)
    # return index(request)

   
        

# def showbooking(request):
#     try:
#         user = User.objects.get(pk=request.user.id)
#         showbooking = Booking.objects.values_list('course_number')
#         return render(request, 'booking/showbooking.html', {
#             'showbookings' : showbooking,
#         })
#     except Exception as e:
#         print("Error on showing : ", e)
#     return index(request)

    
    


#def index(request):
#   return render(request, "subject/index.html",{
#       'subject': Subject.objects.all()
#   })

