from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update({
            "type":"text",
            "class":"form-control",
            "id":"inputComment",
            "placeholder":"리뷰를 남겨주세요! 스포일러는 삼가주세요💕",
            "maxlength":"140",
        })

    class Meta:
        model = Comment
        exclude = ['movie', 'user', 'rating']