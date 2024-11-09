from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Stu_Data
# Create your views here.



#First step in CRUD Project: This function will add new data and show all data
def add_show(request):
    """
    The `add_show` function in Python handles form submission, validation, saving data to the database,
    and rendering a template with form data and student records.
    
    :param request: The `request` parameter in the `add_show` function is an object that contains
    information about the current HTTP request. It includes details such as the request method (GET,
    POST, etc.), any data sent in the request, user session information, and more. In this function, it
    is used
    :return: The `add_show` function returns a rendered HTML template named 'addandshow.html' along with
    a form object `FormObj` and a queryset `stuData` containing all instances of `Stu_Data` model
    objects.
    """
    if request.method == 'POST':
        FormObj = StudentRegistration(request.POST)
        if FormObj.is_valid():
            name = FormObj.cleaned_data['name']
            age = FormObj.cleaned_data['age']
            email = FormObj.cleaned_data['email']
            password = FormObj.cleaned_data['password']
            address = FormObj.cleaned_data['address']
            reg = Stu_Data(name=name, age=age, email=email, password=password, address=address)
            reg.save()
            FormObj = StudentRegistration()
            # FormObj.save()
            # return render(request, 'APP1/addandshow.html')
    else:
        FormObj = StudentRegistration()
    stuData = Stu_Data.objects.all()
    return render(request, 'APP1/addandshow.html',{'form':FormObj,'stuData':stuData})









#Second step in CRUD Project: deletion of a particular data
def delete_data(request,id):
    """
    The function `delete_data` deletes a record from the `Stu_Data` model based on the provided ID when
    the request method is POST.
    
    :param request: The `request` parameter in the `delete_data` function is typically an HttpRequest
    object that represents the current HTTP request. It contains information about the request, such as
    the method used (GET, POST, etc.), headers, and data. In this context, the function is checking if
    the request method
    :param id: The `id` parameter in the `delete_data` function is used to identify the specific record
    in the `Stu_Data` model that needs to be deleted. It is typically the primary key (pk) of the record
    that uniquely identifies it in the database
    :return: The function `delete_data` is returning an `HttpResponseRedirect` object that redirects the
    user to the root URL `'/'`.
    """
    if request.method == 'POST':
        pi = Stu_Data.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    




# Third step in CRUD Project: Update/Edit
def Update_data(request,id):
    if request.method == 'POST':
        pi = Stu_Data.objects.get(pk=id)
        FormObj = StudentRegistration(request.POST, instance=pi)
        if FormObj.is_valid():
            FormObj.save()
    else:
        pi = Stu_Data.objects.get(pk=id)
        FormObj = StudentRegistration(instance=pi)
    return render(request, 'APP1/updatedata.html',{'form':FormObj})