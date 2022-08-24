import requests
import json
Employee={
    'eno':1003,
    'name':'Eswaramma',
    'age':42,
    'salary':75000,
    'address':'Venkatagiri'
}
#response = requests.post('http://127.0.0.1:8000/Employee/Employee_cr/',data=json.dumps(Employee))
#response = requests.get('http://127.0.0.1:8000/Employee/Employee_cr/')
#response = requests.put('http://127.0.0.1:8000/Employee/Employee_rud/3',data=json.dumps(Employee))
response = requests.delete('http://127.0.0.1:8000/Employee/Employee_rud/62')
print(response.json())
