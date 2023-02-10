from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #first_name = forms.CharField(max_length=200)
    username = forms.CharField(label='First Name(username)')
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("username","email","photo","password1")

    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class VoteForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect(), empty_label=None)

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super(VoteForm, self).__init__(*args, **kwargs)
        self.fields['choice'].queryset = question.choice_set.all()