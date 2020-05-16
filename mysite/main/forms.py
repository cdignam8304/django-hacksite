from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from haystack.forms import ModelSearchForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    model = User
    fields = ("username",
              "email",
              "password1",
              "password2")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
    
# THERE IS A PROBLEM WITH THE CODE BELOW - SEE SYNTAX ERROR
# class AutocompleteModelSearchForm(ModelSearchForm):

#     def search(self):
#         if not self.is_valid():
#             return self.no_query_found()
#         if not self.cleaned_data.get("q")
#             return self.no_query_found()
#         sqs = self.searchqueryset.filter(first_name_auto=self.cleaned_data["q"])

#         if self.load_all
#             sqs = sqs.load_all()

#         return sqs

