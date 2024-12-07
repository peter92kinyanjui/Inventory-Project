from .import views
from django.urls import path,include






app_name = 'items'

urlpatterns = [

    path('layout/',views.layout,name='layout.html'),
    path('layout1/',views.layout1,name='layout1.html'),
    

    path('index/', views.index, name='index'),
    path('', views.homepage, name='homepage'),
    path('confirmdelete/',views.confirmdelete,name='confirmdelete'),
    path('confirmdelete/<id>/', views.confirmdelete, name='confirmdelete'),






    #Asset Paths
    path('update_asset/',views.update_asset,name='update_asset'),
    path('insert/',views.insert,name='insert'),
    path('insert_data/',views.insert_data,name='insert_data'),
    # path('delete_asset/',views.delete_asset,name='delete_asset'),
    path('view_assets/',views.view_asset,name='view_assets'),
    path('details/<id>/',views.get_asset,name='details'),
    path('view_asset/<id>/',views.get_asset,name='view_asset'),
    path('update_asset/<id>/',views.update_asset,name='update_asset'),
    # path('delete_asset/<id>/',views.delete_asset,name='delete_asset'),
    path('details/',views.details, name='details'),

    

    #Excel report generation paths
    path('export_assets/', views.export_assets_to_excel, name='export_assets'),
    path('export_requests/', views.export_requests_to_excel, name='export_requests'),
    # path('export_asset_to_excel/<id>/', views.export_asset_to_excel, name='export_asset_to_excel'),
   
    #Requests paths
    path('requests/',views.requests,name='requests'),
    path('update_request/',views.update_request,name='update_request'),
    path('view_requests/',views.view_requests,name='view_requests'),
    path('request_insert/',views.request_insert,name='request_insert'),
    path('view_request/<id>/',views.get_request,name='view_request'),
    path('request_details/<id>/', views.get_request,name='request_details'),
    path('delete_request/',views.delete_request,name='delete_request'),
    path('update_request/<id>/',views.update_request,name='update_request'),
    path('delete_request/<id>/',views.delete_request,name='delete_request'),

   

]