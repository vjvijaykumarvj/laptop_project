import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.core.serializers import serialize
# Create your views here.
from django.views.generic import View
class Employee_CR(View):
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            emp_json = request.body
            #convert the Employee Record From Dict format By Using Loads()
            try:
                emp_dict = json.loads(emp_json)
            except:
                return HttpResponse(json.dumps({'messege':'Please Fill Details Perfectly'}))
            emp_list = Employee(eno=emp_dict['eno'],name=emp_dict['name'],age=emp_dict['age'],salary=emp_dict['salary'],address=emp_dict['address'])
            emp_list.save()
            #send response from Client
            response_msg = {'messege':'Employee Create Successfully Completed'}
            return HttpResponse(json.dumps(response_msg),content_type='application/json')
    def get(self,request,*args,**kwargs):
        if request.method == 'GET':
#           get the all Employee From Database
            emp_db = Employee.objects.all()
            #this is complex objects so convert one by one details
            emp_json = serialize('json',emp_db)
            temp_dict = json.loads(emp_json)
            final_emp=[]
            for obj in temp_dict:
                emp = obj['fields']
                emp['id']=obj['pk']
                final_emp.append(emp)
            return HttpResponse(json.dumps(final_emp),content_type='application/json')
class Employee_RUD(View):
    def get(self,request,pk,*args,**kwargs):
        if request.method=='GET':
            try:
                employee = Employee.objects.get(id=pk)
            except:
                return HttpResponse(json.dumps({'messege':'Employee Record Not Found Please Fill Valid details'}))
            emp_dict={
                'id':employee.id,
                'eno':employee.eno,
                'name':employee.name,
                'age':employee.age,
                'salary':employee.salary,
                'address':employee.address
            }
            return HttpResponse(json.dumps(emp_dict),content_type='application/json')
#     def put(self,request,pk,*args,**kwargs):
# #       get the Employee Record from database
#         emp_json = request.body
#         #convert the dict format
#         try:
#             emp_input = json.loads(emp_json)
#         except:
#             return HttpResponse(json.dumps({'messege': 'Flise fill details perfectly some mistakes'}))
#         try:
#             employee =Employee.objects.get(id=pk)
#         except:
#             return HttpResponse(json.dumps({'messege': 'Employee Record id={pk} not found'}))
#         employee = EmployeeForm(emp_input,instance=employee)
#         if employee.is_valid():
#             employee.save()
#         return HttpResponse(json.dumps({'messege':'update Employee Record Successfully Completed'}))

    def delete(self,request,pk,*args,**kwargs):
        try:
             employee = Employee.objects.get(id=pk)
        except:
            return HttpResponse(json.dumps({'messege':'Employee id={} not valid'}),content_type='application/json')
        employee.delete()
        return HttpResponse(json.dumps({'messege':'Delete Emplotee Successfully'}),content_type='application/json')
