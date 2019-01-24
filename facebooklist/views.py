from django.shortcuts import render,redirect
from .models import FacebookList, Category
import datetime

def login(request):  
    facebooks = FacebookList.objects.all() 
    categories = Category.objects.all() 
    if request.method == "POST": 
        if "taskAdd" in request.POST: 
            title = request.POST["description"] 
            date = str(request.POST["date"]) 
            category = request.POST["category_select"] 
            content = title + " -- " + date + " " + category 
            Facebook = FacebookList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Facebook.save()  
            return redirect("/") 

        if "taskDelete" in request.POST: 
            checkedlist = request.POST["checkedbox"] 
            for facebook_id in checkedlist:
                facebook = facebookList.objects.get(id=int(facebook_id)) 
                facebook.delete() 
    return render(request, "login.html", {"facebooks": facebooks, "categories":categories})
