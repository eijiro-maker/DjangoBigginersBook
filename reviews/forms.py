from django import forms
from .models import Review
from django.utils import timezone

class ReviewCreateForm(forms.ModelForm):

    years = [x for x in range(1991,2031)]
    months = {
        1:'睦月', 2:'如月', 3:'弥生', 4:'卯月',
        5:'皐月', 6:'水無月', 7:'文月', 8:'葉月',
        9:'長月', 10:'神無月', 11:'霜月', 12:'師走'
    }

#    create_at = forms.DateField(label='日時', widget=forms.SelectDateWidget(years=years,months=months))
    create_at = forms.SplitDateTimeField(label='日時・時間', initial=timezone.now)
    class Meta:
        model = Review
        #fields = '__all__'
        exclude = ('created_at',)