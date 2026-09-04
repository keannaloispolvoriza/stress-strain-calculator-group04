from properties import MaterialProperties


class Material:
    """Base class for all materials."""

    def __init__(
        self,
        name: str,
        properties: MaterialProperties
    ):
        self.name = name
        self.properties = properties

    @property
    def density(self) -> float:
        """Get material density."""
        return self.properties.density

    @property
    def yield_strength(self) -> float:
        """Get material yield strength."""
        return self.properties.yield_strength

    @property
    def typical_youngs_modulus(self) -> float:
        """Get typical Young's modulus."""
        return self.properties.typical_youngs_modulus

    def can_withstand_stress(
        self,
        stress: float
    ) -> bool:
        """Check whether the material can withstand stress."""
        return stress < self.yield_strength

    def __str__(self) -> str:
        return (
            f"{self.name} "
            f"(Density: {self.density} kg/m³)"
        )


class Metal(Material):
    """A metal material."""

    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        is_ferrous: bool = False
    ):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous

    def __str__(self) -> str:
        if self.is_ferrous:
            metal_type = "Ferrous"
        else:
            metal_type = "Non-ferrous"

        return (
            f"{self.name} "
            f"({metal_type} metal, "
            f"Density: {self.density} kg/m³)"
        )


class Plastic(Material):
    """A plastic material."""

    def __str__(self) -> str:
        return (
            f"{self.name} "
            f"(Plastic, "
            f"Density: {self.density} kg/m³)"
        )


class Composite(Material):
    """A composite material."""

    def __str__(self) -> str:
        return (
            f"{self.name} "
            f"(Composite, "
            f"Density: {self.density} kg/m³)"
        )
