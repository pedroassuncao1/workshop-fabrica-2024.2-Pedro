# telefone/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # URLs que não requerem autenticação
        exempt_urls = [
            reverse('login'),
            reverse('register'),
            reverse('home'),
            reverse('consultar_telefone'),
        ]

        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect(reverse('login'))

        response = self.get_response(request)
        return response