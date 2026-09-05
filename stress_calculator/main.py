from database import (
    material,
    MATERIALS,
    REQUIRED_SAFETY_FACTOR,
    get_material,
    create_custom_material,
    save_results_to_json,
    export_results_to_csv
)

from tests import StressStrainTest, TestAnalysis
from utils import calculate_stress, calculate_strain, calculate_youngs_modulus


def get_positive_number(prompt):
    """Get a positive number from the user."""

    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Value must be greater than 0.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number.")


def get_non_negative_number(prompt):
    """Get a non-negative number from the user."""

    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Value cannot be negative.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number.")


def display_materials():
    """Display available materials."""

    print("\n=== Material Selection ===")

    for key, material in MATERIALS.items():
        print(f"{key}. {material.name}")

    print("C. Custom Material")
    print("Q. Quit")


def select_material():
    """Allow the user to select a material."""

    while True:
        display_materials()

        choice = input(
            "Choose a material: "
        ).strip().lower()

        if choice == "q":
            return None

        if choice == "c":
            try:
                return create_material_database()
            except ValueError as error:
                print(f"Invalid material: {error}")
                continue

        material = get_material(MATERIALS, choice)

        if material is not None:
            return material

        print("Invalid material choice.")


def display_test_results(test):
    """Display the results of a stress-strain test."""

    print("\n=== Test Results ===")
    print(f"Material: {test.material.name}")
    print(f"Force: {test.force:,.2f} N")
    print(f"Area: {test.area:,.6f} m²")
    print(
        f"Original Length: "
        f"{test.original_length:,.4f} m"
    )
    print(
        f"Change in Length: "
        f"{test.change_in_length:,.6f} m"
    )
    print(f"Stress: {test.stress:,.2f} Pa")
    print(f"Strain: {test.strain:.6f}")

    if test.youngs_modulus is None:
        print("Young's Modulus: Undefined")
    else:
        print(
            f"Young's Modulus: "
            f"{test.youngs_modulus:,.2f} Pa"
        )

    print(
        f"Factor of Safety: "
        f"{test.factor_of_safety():.2f}"
    )

    if test.factor_of_safety() >= REQUIRED_SAFETY_FACTOR:
        print("Safety Result: SAFE")
    else:
        print("Safety Result: UNSAFE")


def main():
    """Run the Stress and Strain Analysis System."""

    print("=== Stress and Strain Analysis System ===")

    analysis = TestAnalysis()

    while True:
        material = select_material()

        if material is None:
            break

        print(f"\nMaterial selected: {material.name}")

        force = get_positive_number(
            "Enter applied force (N): "
        )

        area = get_positive_number(
            "Enter cross-sectional area (m²): "
        )

        original_length = get_positive_number(
            "Enter original length (m): "
        )

        change_in_length = get_non_negative_number(
            "Enter change in length (m): "
        )

        try:
            stress = calculate_stress(force, area)
            strain = calculate_strain(original_length, change_in_length)
            youngs_modulus = calculate_youngs_modulus(stress, strain)
            
            test = StressStrainTest(
                material,
                force,
                area,
                original_length,
                change_in_length,
                youngs_modulus
            )

            analysis.add_test(test)

            display_test_results(test)

        except ValueError as error:
            print(f"Error: {error}")
            continue

        while True:
            again = input(
                "\nPerform another calculation? (y/n): "
            ).strip().lower()

            if again == "y":
                break

            if again == "n":
                print("\n=== Session Summary ===")
                print(analysis.summary())
                print("\nProgram ended. Thank you!")
                return

            print("Please enter y or n.")


    print("\n=== Session Summary ===")
    print(analysis.summary())
    print("\nProgram ended. Thank you!")


if __name__ == "__main__":
    main()
