from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'frontends/index.html')

def choice(request):
    return render(request, 'frontends/choice.html')

def trailer(request):
    return render(request, 'frontends/trailer.html')

def result(request):
    return render(request, 'frontends/result.html') 

def detail(request):
    return render(request, 'frontends/detail.html') 

# # @require_POST
# def create_comment(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.review = review
#         comment.user = request.user
#         comment.save()
#         return redirect('community:detail', review.pk)
#     context = {
#         'comment_form': comment_form,
#         'review': review,
#         'comments': review.comment_set.all(),
#     }
#     return render(request, 'community/detail.html', context)