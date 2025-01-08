from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def home(request):
	return render(request,"index.html")

# CRUD

#Create
def addemployee(request):
	try:
		Name=request.POST['name']   
		Address=request.POST['address'] 
		Age=int(request.POST['age']	)	
		empobj=Employee.objects.create(name=Name,address=Address,age=Age)
		empobj.save()
		return render(request,"index.html",{"msg":"Employee added"})
	
	except Exception as e:
		print(e)   
		return render(request,"index.html",{"msg":"Employee can't be added"})




#Read 
def display(request):	
	empdtls=Employee.objects.all()
	return render(request,"index.html",{'empdtls':empdtls})

#Delete using name
def delemployee(request):
	empname=request.POST['name']
	empdtls = Employee.objects.filter(name=empname)
	if empdtls.exists():
		empdtls.delete()
		return render(request, 'index.html', {"msg1": "Deleted successfully"})
	else:
		return render(request, 'index.html', {"msg1": "No records found"})

def updatename(request):
	#Update using filter
	try:		
		oldname=request.POST["oldname"]  
		newname=request.POST["newname"]
		emp=Employee.objects.filter(name=oldname)
		if emp.exists():
			emp.update(name=newname)
			return render(request,"index.html",{'msg1':"Updated"})
		else:
			return render(request,"index.html",{'msg1':"No records found"})
	except Exception as e:
		print(e)
		return render(request,"index.html",{'msg1':"Not Updated"})

'''	
#Update using get()
	eid=request.POST["empid"]
	newname=request.POST["newname"]
	emp=Employee.objects.get(id=eid)   //single object
	emp.name=newname
	emp.save()
	return render(request,"index.html",{'msg':"Updated"})
'''







		
	



	


