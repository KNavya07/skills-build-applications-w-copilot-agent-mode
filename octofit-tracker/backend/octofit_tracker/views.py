from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "url": "https://super-space-trout-wrrwgwx6q4xjc5qg6-8000.app.github.dev"
    })