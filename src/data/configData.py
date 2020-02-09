def get_default_value_by_type(value_type):
    if value_type == bool:
        return False
    elif value_type == str:
        return ""
    elif value_type == float:
        return 0.0
    elif value_type == int:
        return 0


def bool_type_converter(value):
    if isinstance(value, str):
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        raise ValueError
    else:
        return bool(value)


def int_type_converter(value):
    return int(value)


def float_type_converter(value):
    return float(value)


def str_type_converter(value):
    return str(value)


def get_type_converter(config_type):
    if config_type == bool:
        return bool_type_converter
    elif config_type == int:
        return int_type_converter
    elif config_type == float:
        return float_type_converter
    elif config_type == str:
        return str_type_converter


class ConfigData:
    def __init__(self, config_type, default_value=None):
        self.config_type = config_type
        self.value = None
        self.default_value = default_value
        self.set_value(default_value)

    def set_value(self, value):
        if value is not None:
            type_converter = get_type_converter(self.config_type)
            self.value = type_converter(value)
        else:
            self.value = get_default_value_by_type(self.config_type)
