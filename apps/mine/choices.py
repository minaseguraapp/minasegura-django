from django.db import models


class MeasurementSiteChoice(models.TextChoices):
    """
    Measurement site choices
    """
    MINING_OPERATIONS = "MINING_OPERATIONS", "En labores o frentes de explotación"
    MAIN_AIR_RETURN = "MAIN_AIR_RETURN", "En los retornos principales de aire"
    AIR_RETURN_FROM_STALLS = "AIR_RETURN_FROM_STALLS", "En el retorno de aire de los tajos"
    AIR_RETURN_PREP_DEV = "AIR_RETURN_PREP_DEV", " En el retorno de aire de los frentes de preparación y desarrollo"


class MeasurementSiteCoalChoice(models.TextChoices):
    COAL_DUST_LEVEL = "COAL_DUST_LEVEL", "Nivel de polvo de carbón"
    PARTICLE_DUST_SIZE = "PARTICLE_DUST_SIZE", "Tamaño de partícula de polvo"
