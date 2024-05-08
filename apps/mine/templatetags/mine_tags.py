import datetime

from django import template

from apps.mine.choices import MeasurementSiteChoice, MeasurementSiteCoalChoice
from apps.mine.models import Zone

register = template.Library()


@register.filter('timestamp_to_time')
def convert_timestamp_to_time(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp))


@register.filter('measurement_site')
def measurement_site(value):
    label = MeasurementSiteChoice(value).label
    return label if label else value


@register.filter('measurement_site_coal')
def measurement_site_coal(value):
    label = MeasurementSiteCoalChoice(value).label
    return label if label else value


@register.simple_tag
def get_zone(zone_id):
    zone = Zone.objects.filter(id=zone_id).first()
    if zone:
        return zone
    return f"Zone {zone_id}"
