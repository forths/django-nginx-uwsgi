from django.http import JsonResponse
# Create your views here.
def result(request):
    return JsonResponse({"result":"OK"})
