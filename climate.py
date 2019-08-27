from homeassistant.components.climate import ClimateDevice
from homeassistant.components.climate.const import (
    HVAC_MODE_OFF,
    HVAC_MODE_HEAT,
    HVAC_MODE_COOL,
    HVAC_MODE_DRY,
    SUPPORT_TARGET_TEMPERATURE
)
from homeassistant.const import (
    CONF_NAME,
    TEMP_CELSIUS
)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    async_add_entities([MyClimate(name)])
    

class MyClimate(ClimateDevice):

    def __init__(
        self,
        name,
    ):
        self._name = name
        self._hvac_mode = HVAC_MODE_OFF

    @property
    def temperature_unit(self):
        return TEMP_CELSIUS

    @property
    def hvac_mode(self):
        return self._hvac_mode
    
    @property
    def hvac_modes(self):
        return [
            HVAC_MODE_OFF,
            HVAC_MODE_HEAT,
            HVAC_MODE_COOL,
            HVAC_MODE_DRY,
        ]
    
    @property
    def supported_features(self):
        return SUPPORT_TARGET_TEMPERATURE

    @property
    def name(self):
        return self._name

    