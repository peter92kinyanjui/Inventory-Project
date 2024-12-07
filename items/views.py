
from django.shortcuts import render,redirect
from items.models import Asset
import pandas as pd
from .models import Asset
from .models import Request
from django.http import HttpResponse
# from .models import User
from members import views
from django.contrib import messages


#Generate Report function
def export_assets_to_excel(request):
    # Query the Person model to get all records
    assets = Asset.objects.all().values()
        
    # Convert the QuerySet to a DataFrame
    df = pd.DataFrame(list(assets))

    # Define the Excel file response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=assets.xlsx'

    # Use Pandas to write the DataFrame to an Excel file
    df.to_excel(response, index=False, engine='openpyxl')

    return response



# def export_asset_to_excel(request,id):

#     asset = Asset.objects.get(id=id).values()
#     df = pd.DataFrame(list(asset))

#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename=asset.xlsx'
#     df.to_excel(response, index=False, engine='openpyxl')

#     return response




#Asset funtions

def homepage(request):
    return render(request,'homepage.html')

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def layout(request):
    return render(request,'layout.html')

def layout1(request):
    return render(request,'layout1.html')

def insert(request):
    return render(request,'insert.html')

def insert_data(request):
    if request.method == 'POST':
        asset_name = request.POST['asset_name']
        unit_cost = request.POST['unit_cost']
        inv_value = request.POST['inv_value']
        department = request.POST['department']
        asset_qty = request.POST['asset_qty']
        asset_specs = request.POST['asset_specs']
        # asset_img = request.FILES['asset_img']

        asset = Asset(
                          asset_name=asset_name,
                          unit_cost= unit_cost,
                          inv_value = inv_value,
                          department=department,
                          asset_qty=asset_qty,
                          asset_specs=asset_specs,
                        #   asset_img=asset_img
        )
        asset.save()

        return redirect('/view_assets/')

    return render(request,'insert.html')

def view_asset(request):
    assets = Asset.objects.all()
    return render(request,'view_assets.html',{'assets':assets})



def details(request):
    return render(request,name='details.html')

#retrieving single asset
def get_asset(request,id):
    asset=Asset.objects.get(id=id)
    return render(request,'details.html',{'asset':asset})

#update an entry
def update_asset(request,id):
    asset=Asset.objects.get(id=id)
    if request.method == 'POST':
        #getting the new values
        asset_name = request.POST['asset_name']
        unit_cost = request.POST['unit_cost']
        inv_value = request.POST['inv_value']
        department = request.POST['department']
        asset_qty = request.POST['asset_qty']
        asset_specs = request.POST['asset_specs']
        # asset_img = request.FILES['asset_img']

        #Reassigning the new values
        asset.asset_name = asset_name
        asset.unit_cost = unit_cost
        asset.inv_value = inv_value
        asset.department = department
        asset.asset_qty = asset_qty
        asset.asset_specs = asset_specs
        # asset.asset_img = asset_img

        asset.save()
        return redirect('/view_assets/')

    return render(request,'update_asset.html',{'asset':asset})




def confirmdelete(request,id):
    asset = Asset.objects.get(id=id)
    if request.method == 'POST':
        asset.delete()
        messages.success(request, 'Asset successfully deleted')
        return redirect('/view_assets/')
    return  render(request,'confirmdelete.html')





# def delete_asset(request,id):
#     asset = Asset.objects.get(id=id)
#     if request.method == 'POST':
#         asset.delete()
#         messages.success(request,'Asset successfully deleted')
#         return redirect('/view_assets/')
#
#     return render(request,'confirmDelete.html')






# def view_users(request):
#     users = User.objects.all()
#     return render(request,'view_users.html',{'users':users})

# def regform(request):
#     return render(request,'regform.html')


# def insert_users(request):
#     if request.method == 'POST':
#         staff_no = request.POST['staff_no']
#         staff_fname = request.POST['staff_fname']
#         staff_sname = request.POST['staff_sname']
#         staff_email = request.POST['staff_email']
#         password = request.POST['password']
        
        

#         user = User(
#                           staff_no = staff_no,
#                           staff_fname = staff_fname,
#                           staff_sname = staff_sname,
#                           staff_email = staff_email,
#                           password = password,
                          
                        
#         )
#         user.save()

#         return redirect('/view_users/')

#     return render(request,'regform.html')

#retrieving single request
def get_request(request,id):
    request_detail=Request.objects.get(id=id)
    return render(request,'request_details.html',{'request_detail':request_detail})





#Requests functions 
def requests(request):
    return render(request,'requests.html')

    


def view_requests(request):
    requests = Request.objects.all()
    return render(request,'view_requests.html',{'requests':requests})


def request_insert(request):
    if request.method == 'POST':
        staff_no = request.POST['staff_no']
        staff_fname = request.POST['staff_fname']
        staff_sname = request.POST['staff_sname']
        asset_name = request.POST['asset_name']
        department = request.POST['department']
        asset_qty = request.POST['asset_qty']
        asset_specs = request.POST['asset_specs']
        allocation_status = request.POST['allocation_status']
        

        request_asset = Request(
                          staff_no = staff_no,
                          staff_fname = staff_fname,
                          staff_sname = staff_sname,
                          asset_name = asset_name,
                          department = department,
                          asset_qty = asset_qty,
                          asset_specs = asset_specs,
                          allocation_status = allocation_status,
                        
        )
        request_asset.save()

        return redirect('/view_requests/')

    return render(request,'requests.html')

#retrieving single request
def get_request(request,id):
    request_detail=Request.objects.get(id=id)
    return render(request,'request_details.html',{'request_detail':request_detail})



#update an entry
def update_request(request,id):
    request_asset=Request.objects.get(id=id)
    if request.method == 'POST':
        #getting the new values
        staff_no = request.POST['staff_no']
        staff_fname = request.POST['staff_fname']
        staff_sname = request.POST['staff_sname']
        asset_name = request.POST['asset_name']
        department = request.POST['department']
        asset_qty = request.POST['asset_qty']
        asset_specs = request.POST['asset_specs']
        allocation_status = request.POST['allocation_status']

        #Reassigning the new values
        request_asset.staff_no = staff_no
        request_asset.staff_fname = staff_fname
        request_asset.staff_sname = staff_sname
        request_asset.asset_name = asset_name
        request_asset.department = department
        request_asset.asset_qty = asset_qty
        request_asset.asset_specs = asset_specs
        request_asset.allocation_status = allocation_status

        request_asset.save()
        return redirect('/view_requests/')

    return render(request,'update_request.html',{'request_asset':request_asset})






def delete_request(request,id):
    request_asset = Request.objects.get(id=id)

    # pag.alert(text="Hello World", title="The Hello World Box")
    # pag.prompt(text="Are you sure you want to delete")


    request_asset.delete()
    return redirect('/view_requests/')


def export_requests_to_excel(request):
    # Query the Person model to get all records
    requests_made = Request.objects.all().values()

    # Convert the QuerySet to a DataFrame
    df = pd.DataFrame(list(requests_made))

    # Define the Excel file response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Requests_made.xlsx'

    # Use Pandas to write the DataFrame to an Excel file
    df.to_excel(response, index=False, engine='openpyxl')

    return response





