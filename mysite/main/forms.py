from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from haystack.forms import SearchForm
from .models import Hack

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
    
    
class AutocompleteSearchForm(SearchForm):

    def search(self):
        query = self.cleaned_data["q"]
        
        if not self.is_valid():
            return self.no_query_found()
        if not query:
            return self.no_query_found() 
        
        # sqs = self.searchqueryset.filter(content_auto=self.cleaned_data["q"]) # works for hack content but no results from other fields
        # sqs = self.searchqueryset.filter(title_auto=self.cleaned_data["q"]) # works for hack title but no results from other fields
        # sqs = self.searchqueryset.filter(content=query) # Gets results from all indexed fields in all models BUT no partial text search. Full words, which behaves more like EdgeNgramField(?) NB: "content" is a special field in haystack to reference all fields/models in index.
        sqs = self.searchqueryset.filter(content=query).models(Hack) # as above but only Hack models passed. So searching on a Series works but only the Hacks in the Series are returned, not the Series itself. Stemming is implemented by default so can search for "train" to return trains.

        if self.load_all:
            sqs = sqs.load_all()

        return sqs

