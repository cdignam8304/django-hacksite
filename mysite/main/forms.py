from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet


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
    

class AutoCompleteSearchForm(SearchForm):
    
    def search(self):
        if not self.is_valid():
            return self.no_query_found()
        # if not self.cleaned_data.get("q"):
        if not self.cleaned_data["q"]:
            return self.no_query_found()
        # sqs = super(AutoCompleteSearchForm, self).search()
        # sqs = self.searchqueryset.filter(first_name_auto=self.cleaned_data["q"])
        sqs = SearchQuerySet().autocomplete(content_auto=self.cleaned_data["q"])

        # if self.load_all
        #     sqs = sqs.load_all()

        return sqs
    

