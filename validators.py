def validate_int(value, min_value=None, max_value=None, required=False):
    if not value:
        if required:
            raise TypeError('required value is None')
        return

    try:
        value = int(value)
    except ValueError:
        raise ValueError('value is not numeric')

    if (min_value is not None and max_value is not None and
            min_value > max_value):
        raise ValueError(f'minimum value {min_value} is greater than maximum value {max_value}')

    if min_value is not None and value < min_value:
        raise ValueError(f"expected value less than {min_value}, but got {value}")

    if max_value is not None and value > max_value:
        raise ValueError(f"expected value greater than {max_value}, but got {value}")

    return True


def validate_list_int(values, min_value=None, max_value=None, required=False):
    if not values:
        if required:
            raise TypeError('required value is None')
        return

    for value in values:
        validate_int(value, min_value, max_value, required)

    return True
