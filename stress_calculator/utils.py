def validate_positive_number(value, parameter_name):
    """Validate that a number is positive."""
    if value <= 0:
        raise ValueError(
            f"{parameter_name} must be greater than zero."
        )

    return value

def calculate_stress(force, area):
    """Calculate stress using force and area."""
    validate_positive_number(area, "Area")

    if force < 0:
        raise ValueError("Force cannot be negative.")

    return force / area

def calculate_strain(original_length, change_in_length):
    """Calculate strain."""
    validate_positive_number(
        original_length,
        "Original length"
    )

    return change_in_length / original_length

def calculate_youngs_modulus(stress, strain):
    """Calculate Young's modulus."""
    if strain == 0:
        return None

    return stress / strain

def calculate_factor_of_safety(yield_strength, stress):
    """Calculate factor of safety."""
    if stress == 0:
        return None

    return yield_strength / stress

def pascal_to_mpa(value):
    """Convert Pa to MPa."""
    return value / 1_000_000

def mpa_to_pascal(value):
    """Convert MPa to Pa."""
    return value * 1_000_000

def pascal_to_gpa(value):
    """Convert Pa to GPa."""
    return value / 1_000_000_000
