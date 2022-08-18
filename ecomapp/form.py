from allauth.account.forms import SignupForm
from django import forms
 
 
class CustomSignupForm(SignupForm):

    users = (
    ('admin', 'admin'),
    ('shopuser', 'shopuser'),
    ('customer','customer')
)

    full_name = forms.CharField(max_length=30, label='First Name')
    # DOB = forms.DateField()
    gender = forms.CharField(max_length=30, label='Gender')
    usertype = forms.ChoiceField(choices=users)
    def save(self, request):
        # breakpoint()
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['full_name']
        user.user_type = self.cleaned_data['usertype']
        # user.DOB = self.clened_data['DOB']
        user.gender = self.cleaned_data['gender']
        user.save()
        return user


# from django import forms
# from .models import Customuser
# class SignForm(forms.ModelForm):

#     username = forms.CharField(
#         max_length=30,
#     )
    
#     def myclean():
#         pass
#     def signup(self, request, user):
#         """You signup function."""

#     class Meta:
#         model = Customuser
#         fields = [
#             'usertype'
#         ]