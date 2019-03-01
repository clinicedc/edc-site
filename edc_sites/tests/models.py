from django.db import models

from ..model_mixins import SiteModelMixin


class TestModelWithSite(SiteModelMixin, models.Model):

    f1 = models.CharField(max_length=10, default="1")