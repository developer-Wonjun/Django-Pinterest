from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        if LikeRecord.objects.filter(user=user, article=article).exists():
            messages.add_message(self.request, messages.ERROR, '이미 좋아요를 누르셨습니다.')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            messages.add_message(self.request, messages.SUCCESS, '좋아요 성공!')
            LikeRecord(user=user, article=article).save()

        article.like += 1
        article.save()

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)