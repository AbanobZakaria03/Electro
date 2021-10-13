from django import forms


class Userform(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Email', max_length = 100,widget=forms.EmailInput)
    phonenumber = forms.IntegerField(label='Phonenumber')
    address = forms.CharField(label='Address', max_length=2000)
    password = forms.CharField(label='Password', max_length = 100,widget=forms.PasswordInput)
    #repassword = forms.CharField(label='Re-enter password', max_length=100, widget=forms.PasswordInput)

class loginUser(forms.Form):
    email = forms.CharField(label='Email', max_length = 100,widget=forms.EmailInput)
    password = forms.CharField(label='Password', max_length = 100,widget=forms.PasswordInput)
