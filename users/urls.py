from django.urls import path, include
from users.views import *

urlpatterns = [
    path('statistics/', include([
        path('employee/', EmployeeStatistics.as_view(), name='employee'),
        path('employee/<id>/', OneEmployeeStatistics.as_view(), name='employee_with_id'),
        path('client/<id>/', ClientStatistics.as_view(), name='client_with_id'),
    ])),
]
