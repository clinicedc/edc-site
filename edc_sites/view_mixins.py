from __future__ import annotations

from django.core.exceptions import ObjectDoesNotExist

from .auths import view_auditallsites_codename
from .models import SiteProfile
from .site import SiteNotRegistered, sites


class SiteViewMixin:
    def get_context_data(self, **kwargs) -> dict:
        try:
            site_profile = SiteProfile.objects.get(site__id=self.request.site.id)
        except ObjectDoesNotExist:
            site_profile = None
        kwargs.update(site_profile=site_profile)
        try:
            kwargs.update(site_title=site_profile.title)
        except AttributeError:
            if not sites.all():
                raise SiteNotRegistered(
                    "Unable to determine site profile 'title'. No sites have been registered! "
                )
            raise
        codename = f"edc_sites.{view_auditallsites_codename}"
        kwargs.update(has_view_auditallsites=self.request.user.has_perm(codename))
        return super().get_context_data(**kwargs)
