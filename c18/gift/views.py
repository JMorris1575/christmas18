from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import PermissionDenied

from .models import Gift, Comment

import utilities

class GiftListView(View):
    template = 'gift/gift_list.html'

    def get(self, request):
        gifts = Gift.objects.all()
        context = {'gifts': gifts, 'user_has_gift': utilities.user_has_gift(request.user),
                   'memory': utilities.get_random_memory()}
        return render(request, self.template, context)


class GiftSelectView(View):

    def post(self, request, gift_number):
        current_gift = Gift.objects.get(gift_number=gift_number)
        current_gift.selected = True
        current_gift.receiver = request.user
        current_gift.save()
        return redirect(reverse('gift:home'))


class GiftChangeMindView(View):

    def post(self, request, gift_number):
        current_gift = Gift.objects.get(gift_number=gift_number)
        current_gift.selected = False
        current_gift.receiver = None
        current_gift.save()
        return redirect(reverse('gift:home'))


class AddCommentView(View):
    template_name = 'gift/comment_create.html'

    def get(self, request, gift_number):
        gift = Gift.objects.get(gift_number=gift_number)
        comments = gift.comment_set.all()
        context = {'gift':gift, 'comments':comments, 'memory':utilities.get_random_memory()}
        return render(request, self.template_name, context)

    def post(self, request, gift_number):
        gift = Gift.objects.get(gift_number=gift_number)
        # Needs a check for an empty request.POST['comment_text']. Should only save comment if there is one.
        # Otherwise is should go back to the create_comment page with an error message
        # The create_comment page should also have a cancel button to escape without adding a comment.
        new_comment = Comment(gift=gift, user=request.user, comment=request.POST['comment_text'])
        new_comment.save()
        return redirect('gift:home')

class EditCommentView(View):
    template_name = 'gift/comment_edit.html'

    def get(self, request, gift_number, comment_id):
        gift= Gift.objects.get(gift_number=gift_number)
        comments = gift.comment_set.all()
        try:
            selected_comment = Comment.objects.get(pk=comment_id)
        except:
            return redirect('gift:home')
        if request.user == selected_comment.user:
            context = {'gift':gift, 'comments':comments, 'selected_comment':selected_comment,
                   'memory':utilities.get_random_memory()}
            return render(request, self.template_name, context)
        else:
            raise PermissionDenied

    def post(self, request, gift_number, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        if request.user == comment.user:
            comment.comment = request.POST['comment_text']
            comment.save()
            return redirect('gift:home')
        else:
            raise PermissionDenied


class DeleteCommentView(View):
    template_name = 'gift/comment_delete.html'

    def get(self, request, gift_number, comment_id):
        try:
            gift = Gift.objects.get(gift_number=gift_number)
            comment = Comment.objects.get(pk=comment_id)
        except:
            return redirect('gift:home')
        comments = gift.comment_set.all()
        if request.user == comment.user:
            context = {'gift':gift, 'comments':comments, 'selected_comment':comment,
                       'memory':utilities.get_random_memory()}
            return render(request, self.template_name, context)

    def post(self, request, gift_number, comment_id):
        try:
            gift = Gift.objects.get(gift_number=gift_number)
            comment = Comment.objects.get(pk=comment_id)
        except:
            return redirect('gift:home')
        if request.POST['button'] != 'delete':
            return redirect('gift:edit_comment', gift.gift_number, comment_id)
        else:
            if request.user == comment.user:
                comment.delete()
                return redirect('gift:home')
            else:
                raise PermissionDenied

