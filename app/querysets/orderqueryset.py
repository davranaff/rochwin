from django.db.models import QuerySet, Q, Sum, Count, F




class OrderQueryset(QuerySet):
    
    def get_employee_statistics(self, id, month, year):

        query = self.filter(Q(employee__id=id) & Q(created_at__month=month) & Q(created_at__year=year))
        query = query.values('total_price').annotate(
            products_count=Count('product'),
            first_name=F('employee__user__first_name'),
            last_name=F('employee__user__last_name'),
        )

        return query
    
    def get_client_statistics(self, id, month, year):

        query = self.filter(Q(client__id=id) & Q(created_at__month=month) & Q(created_at__year=year))
        query = query.values('total_price').annotate(
            client_id=F('client__user__id'),
            first_name=F('client__user__first_name'),
            last_name=F('client__user__last_name'),
        )

        return query
    
    def get_products_count(self, id, month, year):

        query = self.filter(Q(client__id=id) & Q(created_at__month=month) & Q(created_at__year=year))
        query = query.count()

        return query
