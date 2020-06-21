from django.shortcuts import render

# Create your views here.

from collections import Counter
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def lambda_function(request):
    req_data = request.data.get('question')

    counter = Counter()
    for number in req_data:
        counter[number] += 1

    solution = []

    for item in counter.most_common():
        for _ in range(item[1]):
            solution.append(item[0])

    print(solution)
    return Response({'solution': solution})
