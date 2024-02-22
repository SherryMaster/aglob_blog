# APIs for app
from django.http import HttpResponseRedirect
from django.urls import reverse

from AGlob.models import Post


def like_post(request, pk):
    post = Post.objects.get(id=request.POST.get('post_id'))
    liked = int(request.POST.get('post_like'))
    if liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('AGlob:post_detail', args=[str(pk)]))