from homeassistant.components.climate import ClimateDevice
from homeassistant.components.climate.const import (
    HVAC_MODE_OFF,
    HVAC_MODE_HEAT,
    HVAC_MODE_COOL,
    HVAC_MODE_DRY,
    SUPPORT_TARGET_TEMPERATURE
)
from homeassistant.const import (
    ATTR_TEMPERATURE,
    CONF_NAME,
    TEMP_CELSIUS
)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    target_temp = config.get(ATTR_TEMPERATURE)
    async_add_entities([MyClimate(name, target_temp)])
    
class MyClimate(ClimateDevice):

    def __init__(
        self,
        name,
        target_temp
    ):
        self._name = name
        self._hvac_mode = HVAC_MODE_OFF
        self._target_temp = 25

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
    def target_temperature(self):
        return self._target_temp

    def set_temperature(self, **kwargs):
        self._target_temp = kwargs.get(ATTR_TEMPERATURE)

    @property
    def target_temperature_step(self):
        return 1.0
    
    @property
    def supported_features(self):
        return SUPPORT_TARGET_TEMPERATURE
    
    @property
    def min_temp(self):
        return 16.0
    
    @property
    def max_temp(self):
        return 31.0

    @property
    def name(self):
        return self._name
