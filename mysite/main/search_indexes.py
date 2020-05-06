import datetime
from haystack import indexes
from .models import Hack


class HackIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='hack_title')
    content = indexes.CharField(model_attr='hack_content')
    # pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Hack

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(hack_published__lte=datetime.datetime.now())

