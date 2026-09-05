from material import Material


class StressStrainTest:
    """Represents one stress-strain test."""

    def __init__(
        self,
        material: Material,
        force: float,
        area: float,
        original_length: float,
        change_in_length: float,
        youngs_modulus: float
    ):
        self.material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length
        self._youngs_modulus = youngs_modulus

        self._validate_inputs()

    def _validate_inputs(self):
        """Validate test inputs."""

        if self._force <= 0:
            raise ValueError("Force must be positive.")

        if self._area <= 0:
            raise ValueError("Area must be positive.")

        if self._original_length <= 0:
            raise ValueError(
                "Original length must be positive."
            )

        if self._change_in_length < 0:
            raise ValueError(
                "Change in length cannot be negative."
            )

        if self._youngs_modulus <= 0:
            raise ValueError(
                "Young's modulus must be positive."
            )

    @property
    def force(self):
        return self._force

    @property
    def area(self):
        return self._area

    @property
    def original_length(self):
        return self._original_length

    @property
    def change_in_length(self):
        return self._change_in_length

    @property
    def stress(self):
        """Calculate stress in Pa."""
        return self.force / self.area

    @property
    def strain(self):
        """Calculate strain."""
        return self.change_in_length / self.original_length

    @property
    def youngs_modulus(self):
        """Return Young's modulus."""

        if self.strain == 0:
            return None

        return self._youngs_modulus

    def factor_of_safety(self):
        """Calculate factor of safety."""

        return self.material.yield_strength / self.stress

    def safety_result(self, required_safety_factor=1.5):
        """Determine if the test is safe."""

        if self.factor_of_safety() >= required_safety_factor:
            return "SAFE"

        return "UNSAFE"

    def to_dictionary(self):
        """
        Store test information as a dictionary.
        This satisfies the Task 3 dictionary requirement.
        """

        return {
            "material": self.material.name,
            "force": self.force,
            "area": self.area,
            "original_length": self.original_length,
            "change_in_length": self.change_in_length,
            "stress": self.stress,
            "strain": self.strain,
            "youngs_modulus": self.youngs_modulus,
            "safety_result": self.safety_result()
        }

    def __str__(self):
        modulus = self.youngs_modulus

        if modulus is None:
            modulus_text = "Undefined"
        else:
            modulus_text = f"{modulus:,.2f} Pa"

        return (
            f"Test on {self.material.name}: "
            f"Stress={self.stress:,.2f} Pa, "
            f"Strain={self.strain:.6f}, "
            f"Young's Modulus={modulus_text}"
        )


class TestAnalysis:
    """Store and analyze multiple stress-strain tests."""

    def __init__(self):
        # TASK 3: List
        # Stores all stress-strain test records.
        self._tests = []

        # TASK 3: Set
        # Stores unique materials used.
        self._materials_used = set()

        # TASK 3: Tuple
        # Constant measurement units.
        self._units = ("N", "m^2", "m", "Pa")

    def add_test(self, test: StressStrainTest):
        """Add a test to the calculation history."""

        if not isinstance(test, StressStrainTest):
            raise TypeError(
                "Only StressStrainTest objects are allowed."
            )

        # Add test to the LIST.
        self._tests.append(test)

        # Add material to the SET.
        self._materials_used.add(test.material.name)

    @property
    def tests(self):
        """Return all tests."""

        return tuple(self._tests)

    @property
    def materials_used(self):
        """Return unique materials used."""

        return self._materials_used

    @property
    def units(self):
        """Return constant measurement units."""

        return self._units

    def calculation_history(self):
        """
        Return calculation history as a list of dictionaries.
        """

        return [
            test.to_dictionary()
            for test in self._tests
        ]

    def highest_stress(self):
        """Find the test with the highest stress."""

        if not self._tests:
            return None

        return max(
            self._tests,
            key=lambda test: test.stress
        )

    def lowest_stress(self):
        """Find the test with the lowest stress."""

        if not self._tests:
            return None

        return min(
            self._tests,
            key=lambda test: test.stress
        )

    def average_stress(self):
        """Calculate average stress."""

        if not self._tests:
            return 0

        return (
            sum(test.stress for test in self._tests)
            / len(self._tests)
        )

    def average_strain(self):
        """Calculate average strain."""

        if not self._tests:
            return 0

        return (
            sum(test.strain for test in self._tests)
            / len(self._tests)
        )

    def summary(self):
        """Generate a session summary."""

        if not self._tests:
            return "No calculations were recorded."

        highest = self.highest_stress()
        lowest = self.lowest_stress()

        return (
            f"Total tests: {len(self._tests)}\n"
            f"Materials used: "
            f"{', '.join(sorted(self._materials_used))}\n"
            f"Average Stress: "
            f"{self.average_stress():,.2f} Pa\n"
            f"Average Strain: "
            f"{self.average_strain():.6f}\n"
            f"Highest Stress: "
            f"{highest.stress:,.2f} Pa "
            f"({highest.material.name})\n"
            f"Lowest Stress: "
            f"{lowest.stress:,.2f} Pa "
            f"({lowest.material.name})"
        )
