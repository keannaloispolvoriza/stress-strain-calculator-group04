def main():
    print("=== Stress and Strain Calculator ===")
    print()

    # Get user inputs and convert to float data types
    force = float(input("Enter applied force (in Newtons, N): "))
    area = float(input("Enter cross-sectional area (in square meters, m²): "))
    original_length = float(input("Enter original length (in meters, m): "))
    change_in_length = float(input("Enter change in length (in meters, m): "))

    # Perform calculations using arithmetic operators
    stress = force / area
    strain = change_in_length / original_length

    # Display inputs and formatted output using f-strings
    print()
    print("=== Input Summary ===")
    print(f"Applied Force (F): {force:,.2f} N")
    print(f"Cross-Sectional Area (A): {area:,.6f} m²")
    print(f"Original Length (L₀): {original_length:,.4f} m")
    print(f"Change in Length (ΔL): {change_in_length:,.6f} m")

    print()
    print("=== Calculated Results ===")
    print(f"Stress (σ): {stress:,.2f} Pa")
    print(f"Strain (ε): {strain:,.6f} (dimensionless)")

if __name__ == "__main__":
    main()
