def last_login(request):
    return {
        'last_login': request.COOKIES.get('last_login', 'N/A')
    }
