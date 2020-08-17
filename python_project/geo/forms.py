from django import forms

PREFECTURE_CHOICES = (
    ('01', '北海道'),
    ('02', '青森')
)
class SampleForm(forms.Form):

    prefectures = forms.ChoiceField(
        label='都道府県',
        widget=forms.Select,
        choices=PREFECTURE_CHOICES,
        required=False,
    )