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
    SUPPORT_SWING_MODE,
    SUPPORT_TARGET_TEMPERATURE
)
from homeassistant.const import (
    ATTR_TEMPERATURE,
    CONF_NAME,
    TEMP_CELSIUS
)

FAN_DIRECTION_AUTO = "auto"
FAN_DIRECTION_HIGH = "high"
FAN_DIRECTION_MEDIUMHIGH = "medium high"
FAN_DIRECTION_MEDIUM = "medium"
FAN_DIRECTION_MEDIUMLOW = "medium low"
FAN_DIRECTION_LOW = "low"
FAN_DIRECTION_SWING = "swing"

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
        self._swing_mode = FAN_DIRECTION_AUTO

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

    @property
    def swing_mode(self):
        return self._swing_mode

    @property
    def swing_modes(self):
        return [
            FAN_DIRECTION_AUTO,
            FAN_DIRECTION_HIGH,
            FAN_DIRECTION_MEDIUMHIGH,
            FAN_DIRECTION_MEDIUM,
            FAN_DIRECTION_MEDIUMLOW,
            FAN_DIRECTION_LOW,
            FAN_DIRECTION_SWING
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

    def set_swing_mode(self, swing_mode):
        self._swing_mode = swing_mode

    @property
    def supported_features(self):
        return SUPPORT_TARGET_TEMPERATURE | SUPPORT_FAN_MODE | SUPPORT_SWING_MODE
    
    @property
    def min_temp(self):
        return 16.0
    
    @property
    def max_temp(self):
        return 31.0

    @property
    def name(self):
        return self._name
