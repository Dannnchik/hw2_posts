from django.shortcuts import render
from django.http import HttpResponse

def text_response_view(request):
    return HttpResponse("это текстовый ответ от сервера")

def html_response_view(request):
    return render(request, 'my_template.html')

# myapp/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Post
from django.views import View

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        data = [
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "rate": post.rate,
                "created_at": post.created_at,
                "updated_at": post.updated_at,
            }
            for post in posts
        ]
        return JsonResponse(data, safe=False)

class PostDetailView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        data = {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "rate": post.rate,
            "created_at": post.created_at,
            "updated_at": post.updated_at,
        }
        return JsonResponse(data)
