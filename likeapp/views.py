from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord

@transaction.atomic #함수안에서 일어나는 모든 db상호작용은 트랜잭션화
def db_transaction(user, article):
    article.like += 1
    article.save()
    
    if LikeRecord.objects.filter(user=user, article=article).exists():
        raise ValidationError('Like already exists')
    else:
        LikeRecord(user=user, article=article).save()




@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])
        try:

            db_transaction(user, article)
            messages.add_message(self.request, messages.SUCCESS, '좋아요 성공!')

        except ValidationError:
            messages.add_message(self.request, messages.ERROR, '이미 좋아요를 누르셨습니다.')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        return super(LikeArticleView, self).get(self.request, *args, **kwargs)