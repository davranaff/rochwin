from users.querysets import basequeryset
from django.db.models import Count, F, Sum, Q



class EmployeeQueryset(basequeryset.BaseQueryset):
     
    def all_statistics(self, month, year):
        '''__doc__: Возвращает кол-во купленных товаров, общую сумму и username employee'''

        query = self.select_related('user')
        query = query.filter(
            Q(order__isnull=False) & 
            Q(order__created_at__month=month) & 
            Q(order__created_at__year=year)
        )
        query = query.annotate(
            product_count=Count('order__product'),
            total=Sum('order__total_price'),
            username=F('user__username'),
        )

        return query
     
    def get_one_statistic(self, id, month, year):
        '''__doc__: select sum(distinct total_price) as total, app_order.employee_id as id from users_employee
            join app_order on users_employee.id = app_order.employee_id 
            join app_order_product on app_order_product.order_id = app_order.id 
            where extract(month from app_order.created_at) = {month} and extract(year from app_order.created_at) = {year}
            group by app_order.employee_id 
            having app_order.employee_id = {id}'''
        

        # query_1 = self.raw(f"""
        #     select sum(distinct total_price) as total, app_order.employee_id as id
        #     from users_employee
        #     join app_order on users_employee.id = app_order.employee_id 
        #     where extract(month from app_order.created_at) = {month} and extract(year from app_order.created_at) = {year}
        #     group by app_order.employee_id 
        #     having app_order.employee_id = {id};
        # """)

        # query_2 = self.raw(f"""
            
        # """)

        # query = self.filter()

        # query = self.filter(
        #     Q(pk=id) &
        #     Q(order__isnull=False) & 
        #     Q(order__created_at__month=month) & 
        #     Q(order__created_at__year=year)
        # ).annotate(
        #     client_count=Count('order__client')
        # )

        # return query