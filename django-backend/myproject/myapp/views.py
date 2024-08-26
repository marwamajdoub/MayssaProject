from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_KEY = "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"

class QueryView(APIView):
    def post(self, request):
        prompt = request.data.get('inputs', '')
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        return Response(response.json(), status=status.HTTP_200_OK)
