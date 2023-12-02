from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_404_NOT_FOUND
from users.models import Employee
from users.serializers.employee import StatisticSerializer
from app.models import Order
from users.utils.check_date import check_date



class EmployeeStatistics(APIView):

    def get(self, request):

        month, year, error = check_date(request)

        if error:
            return Response({'error': 'month and year query is required!'}, HTTP_400_BAD_REQUEST)
        
        serializer = StatisticSerializer(data=Employee.objects.all_statistics(month, year), many=True)
        
        if serializer.is_valid():
            return Response({'error': 'validation error'}, HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            'clients_count': len(serializer.data),
            'data': serializer.data
        }, HTTP_200_OK)


class OneEmployeeStatistics(APIView):

    def get(self, request, id):

        
        month, year, error = check_date(request)

        if error:
            return Response({'error': 'month and year query is required!'}, HTTP_400_BAD_REQUEST)

        orders = Order.objects.get_employee_statistics(id, month, year)
        
        if len(orders):
            
            data = {
                'fullname': orders[0].get('first_name') + ' ' + orders[0].get('last_name'),
                'clients_count': len(orders),
                'products_count': 0,
                'total_price': 0,
            }


            for item in orders:
                data['products_count'] += item.get('products_count')
                data['total_price'] += item.get('total_price')
            
            return Response(data, HTTP_200_OK)

        return Response({'data': 'not found!'}, HTTP_404_NOT_FOUND)

class ClientStatistics(APIView):

    def get(self, request, id):

        month, year, error = check_date(request)

        if error:
            return Response({'error': 'month and year query is required!'}, HTTP_400_BAD_REQUEST)
        
        orders = Order.objects.get_client_statistics(id, month, year)

        if len(orders):

            products_count = Order.objects.get_products_count(id, month, year)

            data = {
                'fullname': orders[0].get('first_name') + ' ' + orders[0].get('last_name'),
                'client_id': orders[0].get('client_id'),
                'products_count': products_count,
                'total_price': 0,
            }


            for item in orders:
                data['total_price'] += item.get('total_price')

            return Response(data, HTTP_200_OK)

        return Response({'data': 'not found!'}, HTTP_404_NOT_FOUND)