

def check_date(request):
    month, year = request.query_params.get('month'), request.query_params.get('year')

    if not month or not year:
        return None, None, True
    
    return month, year, False