from homeassistant.components.climate import ClimateDevice
from homeassistant.components.climate.const import (
    ATTR_FAN_MODE,
    ATTR_HVAC_MODE,
    HVAC_MODE_OFF,
    HVAC_MODE_HEAT,
    HVAC_MODE_COOL,
    HVAC_MODE_DRY,
    FAN_AUTO,
    FAN_LOW,
    FAN_MEDIUM,
    FAN_HIGH,
    SUPPORT_FAN_MODE,
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
        self._fan_mode = FAN_AUTO

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

    @property
    def fan_mode(self):
        return self._fan_mode
    
    @property
    def fan_modes(self):
        return [
            FAN_AUTO,
            FAN_LOW,
            FAN_MEDIUM,
            FAN_HIGH
        ]

    def set_temperature(self, **kwargs):
        self._target_temp = kwargs.get(ATTR_TEMPERATURE)

    @property
    def target_temperature_step(self):
        return 1.0

    def set_fan_mode(self, fan_mode):
        self._fan_mode = fan_mode

    def set_hvac_mode(self, hvac_mode):
        self._hvac_mode = hvac_mode

    @property
    def supported_features(self):
        return SUPPORT_TARGET_TEMPERATURE | SUPPORT_FAN_MODE
    
    @property
    def min_temp(self):
        return 16.0
    
    @property
    def max_temp(self):
        return 31.0

    @property
    def name(self):
        return self._name
