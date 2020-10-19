from django.urls import path
from emp.views import *

urlpatterns = [

    path('', IndexView.as_view(), name='index'),

    path('add_emp/', EmpAddView.as_view(), name='add_emp'),
    path('edit_emp/<str:id>/', EmpUpdateView.as_view(), name='edit_emp'),
    path('view_emp/', EmpView.as_view(), name='view_emp'),
    path('details_emp/<str:id>', EmpDetails.as_view(), name='details_emp'),
    path('delete_emp/<str:id>', DeleteEmp.as_view(), name='delete_emp'),

]