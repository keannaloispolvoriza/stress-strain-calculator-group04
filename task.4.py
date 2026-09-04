# TASK 4 - FUNCTIONS AND MODULAR PROGRAMMING

# Predef mats
materials = {
    "1": {"name": "Steel", "yield_strength": 250e6},
    "2": {"name": "Aluminum", "yield_strength": 150e6},
    "3": {"name": "Copper", "yield_strength": 78e6}
}

# Min factor of safety
required_safety_factor = 1.5

# CALCULATION FUNCTIONS

def calculate_stress(force, area):
    return force / area
"""calculate stress using force and area."""


def calculate_strain(change_in_length, original_length):
    return change_in_length / original_length
"""calculate strain using change in length and original length."""


def calculate_youngs_modulus(stress, strain):
    if strain == 0:
        return None
    return stress / strain
"""calculate young's modulus using stress and strain."""


def calculate_factor_of_safety(yield_strength, stress):
    if stress == 0:
        return None
    return yield_strength / stress
"""calculate the factor of safety."""


# VALIDATION FUNCTIONS

def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value
            else:
                print("Value must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")
"""get a number greater than zero."""


def get_non_negative_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value >= 0:
                return value
            else:
                print("Value cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")
"""get a number that is zero or greater."""


# MATERIAL MANAGEMENT

def select_material():
    
    while True:
        print("\n=== Material Selection ===")
        print("1. Steel")
        print("2. Aluminum")
        print("3. Copper")
        print("4. Custom Material")

        choice = input("Choose a material: ").strip()

        if choice in materials:
            material_name = materials[choice]["name"]
            yield_strength = materials[choice]["yield_strength"]

            return material_name, yield_strength

        elif choice == "4":
            material_name = input("Enter material name: ").strip()

            if material_name == "":
                print("Material name cannot be empty.")
                continue

            yield_strength_mpa = get_positive_number(
                "Enter yield strength (MPa): "
            )

            yield_strength = yield_strength_mpa * 1_000_000

            return material_name, yield_strength

        else:
            print("Invalid material choice. Please try again.")

"""allows the user to select a material."""


# SAFETY ANALYSIS

def analyze_safety(factor_of_safety):    
    if factor_of_safety >= required_safety_factor:
        return "SAFE"
    else:
        return "UNSAFE"

"""determines whether the material is safe."""


# DISPLAY FUNCTION

def display_results(
        material_name,
        stress,
        strain,
        youngs_modulus,
        yield_strength,
        factor_of_safety,
        safety_result):

    print("\n=== Analysis Results ===")
    print(f"Material: {material_name}")
    print(f"Stress: {stress:,.2f} Pa")
    print(f"Strain: {strain:.6f}")

    if youngs_modulus is None:
        print("Young's Modulus: Undefined (strain is zero)")
    else:
        print(f"Young's Modulus: {youngs_modulus:,.2f} Pa")

    print(f"Yield Strength: {yield_strength:,.2f} Pa")
    print(f"Factor of Safety: {factor_of_safety:.2f}")
    print(f"Safety Result: {safety_result}")

"""displays the stress and strain analysis results."""


calculation_history = []

materials_used = set()


def record_calculation(
        material_name,
        force,
        area,
        original_length,
        change_in_length,
        stress,
        strain,
        youngs_modulus,
        yield_strength,
        factor_of_safety,
        safety_result):

    test_record = {
        "material": material_name,
        "force": force,
        "area": area,
        "original_length": original_length,
        "change_in_length": change_in_length,
        "stress": stress,
        "strain": strain,
        "youngs_modulus": youngs_modulus,
        "yield_strength": yield_strength,
        "factor_of_safety": factor_of_safety,
        "safety_result": safety_result
    }

    calculation_history.append(test_record)
    materials_used.add(material_name)


def display_session_summary():
    print("\n=== Session Summary ===")

    if len(calculation_history) == 0:
        print("No calculations were recorded.")
        return

    stress_values = []
    strain_values = []

    for record in calculation_history:
        stress_values.append(record["stress"])
        strain_values.append(record["strain"])

    average_stress = sum(stress_values) / len(stress_values)
    average_strain = sum(strain_values) / len(strain_values)

    highest_stress = max(stress_values)
    lowest_stress = min(stress_values)

    print(f"Total tests: {len(calculation_history)}")
    print(f"Materials used: {', '.join(sorted(materials_used))}")
    print(f"Average Stress: {average_stress:,.2f} Pa")
    print(f"Average Strain: {average_strain:.6f}")
    print(f"Highest Stress: {highest_stress:,.2f} Pa")
    print(f"Lowest Stress: {lowest_stress:,.2f} Pa")

"""display a summary of all calculations."""

# MAIN FUNCTION
"""run the Stress and Strain Analysis System."""
def main():
    print("=== Stress and Strain Analysis System ===")

    while True:

        material_data = select_material()

        if material_data is None:
            break

        material_name, yield_strength = material_data

        print(f"\nMaterial selected: {material_name}")

        force = get_positive_number(
            "Enter applied force (N): "
        )

        area = get_positive_number(
            "Enter cross-sectional area (m^2): "
        )

        original_length = get_positive_number(
            "Enter original length (m): "
        )

        change_in_length = get_non_negative_number(
            "Enter change in length (m): "
        )

        stress = calculate_stress(
            force,
            area
        )

        strain = calculate_strain(
            change_in_length,
            original_length
        )

        youngs_modulus = calculate_youngs_modulus(
            stress,
            strain
        )

        factor_of_safety = calculate_factor_of_safety(
            yield_strength,
            stress
        )

        safety_result = analyze_safety(
            factor_of_safety
        )

        record_calculation(
            material_name,
            force,
            area,
            original_length,
            change_in_length,
            stress,
            strain,
            youngs_modulus,
            yield_strength,
            factor_of_safety,
            safety_result
        )

        display_results(
            material_name,
            stress,
            strain,
            youngs_modulus,
            yield_strength,
            factor_of_safety,
            safety_result
        )

        while True:

            again = input(
                "\nDo you want to perform another calculation? (y/n): "
            ).strip().lower()

            if again == "y":
                break

            elif again == "n":
                display_session_summary()
                print("\nProgram ended. Thank you!")
                return

            else:
                print("Kindly enter y or n.")

    display_session_summary()
    print("\nProgram ended. Thank you!")


# Program start
if __name__ == "__main__":
    main()