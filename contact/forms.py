from django import forms
from django.forms import EmailField


class ContactForm(forms.Form):
    CATEGORIES = (
        ('1', 'お仕事の依頼'),
        ('2', 'サイトに関するお話'),
    )

    name = forms.CharField(
        label='お名前', max_length=50,
        required=False, help_text='＊任意'
    )
    email = forms.EmailField(
        label='メールアドレス', required=False, help_text='＊任意'
    )
    text = forms.CharField(label='問い合わせ内容', widget=forms.Textarea)
#    category = forms.ChoiceField(label='カテゴリ', choices=CATEGORIES)
#    category = forms.ChoiceField(label= 'カテゴリ', choices=CATEGORIES, widget=forms.RadioSelect)
#    category = forms.MultipleChoiceField(label='カテゴリ', choices=CATEGORIES)
    category = forms.MultipleChoiceField(label='カテゴリ', choices=CATEGORIES, widget=forms.CheckboxSelectMultiple)

    created_at = forms.DateTimeField(label='日付・時間')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label