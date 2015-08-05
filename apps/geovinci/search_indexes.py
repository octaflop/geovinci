from haystack import indexes

from nearme.models import CampusLocation


class CampusLocationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    location = indexes.LocationField(model_attr='point')

    def get_model(self):
        return CampusLocation
