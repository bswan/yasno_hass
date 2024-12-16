from homeassistant.const import Platform


DOMAIN = "yasno_hass"

CONF_CITY = "city"
CONF_GROUPS = "groups"

YASNO_GROUPS = 6
YASNO_SUBGROUPS = 2
CITIES = ["kiev", "dnipro"]

PLATFORMS = [Platform.BINARY_SENSOR, Platform.CALENDAR]
