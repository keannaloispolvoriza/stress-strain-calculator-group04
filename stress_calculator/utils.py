def validate_input(force, area, original_length, change_in_length):    
    if force < 0:
        return False
    if area <= 0:
        return False
    if original_length <= 0:
        return False
    if change_in_length < 0:
        return False 
    return True
    
"""validate if all inputs are valid for calculations."""

def calculate_stress(force, area):    
    return force / area
"""calculate stress using force and area."""

def calculate_strain(original_length, change_in_length):    
    return change_in_length / original_length
"""calculate strain using original length and change in length."""

def calculate_youngs_modulus(stress, strain):    
    if strain == 0:
        return None
    return stress / strain
"""calculate Young's modulus using stress and strain."""

def main_calculator(material, force, area, original_length, change_in_length):    
    if not validate_input(force, area, original_length, change_in_length):
        return "Invalid input values."
    
    stress = calculate_stress(force, area)
    strain = calculate_strain(original_length, change_in_length)
    youngs_modulus = calculate_youngs_modulus(stress, strain)
    
    return {
        "material": material,
        "stress": stress,
        "strain": strain,
        "youngs_modulus": youngs_modulus
    }
"""main function to organize the stress-strain calculations."""
