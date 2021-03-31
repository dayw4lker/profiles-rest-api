from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """returns a list of apiview features"""
        an_apiview = [
        'Uses HTTP methods as function (get, push, patch, put, delete)',
        'is similar to a traditional django view',
        'gives you yo the most control over your application logic',
        'is mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


        
