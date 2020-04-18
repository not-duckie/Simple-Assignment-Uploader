from django.shortcuts import render
from .forms import Profile_Form
from .models import User_Profile
import time

IMAGE_FILE_TYPES = ['pdf']


def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.Assignment = request.FILES['Assignment']
            file_type = user_pr.Assignment.url.split('.')[-1]
            file_type = file_type.lower()
            
            #user_pr.Assignment.name = 'ass.pdf'
            print (user_pr.Assignment.url)
            
            name = user_pr.Name
            roll = user_pr.RollNo
            user_pr.Assignment.name = name + '_' + str(roll) + '_____' + str(time.time()) + '.pdf'
            print (user_pr.Assignment.url)

            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            
            user_pr.save()

            return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'profile_maker/create.html', context)