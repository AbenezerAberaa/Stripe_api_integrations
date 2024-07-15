
from django.urls import path,include
from . import views

urlpatterns = [
    path('customers/<str:account_name>',views.getCustomers),
    path('subscriptions/<str:account_name>',views.getSubscriptions),
    path('events/<str:account_name>',views.getEvents),
    path('invoices/<str:account_name>',views.getInvoices),
    path('payments/<str:account_name>',views.getPayments),
    path('admins/',views.getAdmins),
    path('register/',views.createAccount),
    path('delete/<str:account_name>',views.account_delete)
    
]