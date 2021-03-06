import datetime
from haystack import indexes
from .models import Hack, HackSeries, HackCategory

# Check out this page for querying the whoosh_index!
# https://stackoverflow.com/questions/2395675/whoosh-index-viewer

class HackIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # title = indexes.CharField(model_attr='hack_title')
    title_auto = indexes.NgramField(model_attr='hack_title') # check to see if this causes titles to be indexed
    # content = indexes.CharField(model_attr='hack_content')
    # content_auto = indexes.EdgeNgramField(model_attr="hack_content") # replaces regular CharField index on line above
    content_auto = indexes.NgramField(model_attr="hack_content") # try this
    # pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Hack

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(hack_published__lte=datetime.datetime.now())


class HackSeriesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    hack_series = indexes.CharField(model_attr='hack_series')
    # series_summary = indexes.CharField(model_attr='series_summary')
    sersumm_auto = indexes.NgramField(model_attr="series_summary") # try this
    # pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return HackSeries

    # N/A for HackSeries (?)
    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(hack_published__lte=datetime.datetime.now())

class HackCategoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    hack_category = indexes.CharField(model_attr='hack_category')
    # category_summary = indexes.CharField(model_attr='category_summary')
    categsumm_auto = indexes.NgramField(model_attr="category_summary") # try this
    # pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return HackCategory

    # N/A for HackCategory (?)
    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(hack_published__lte=datetime.datetime.now())