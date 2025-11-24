from dataclasses import dataclass


@dataclass(frozen=True)
class NaturalResource:
    name: str
    plural_name: str
    description: str
    minimum: int
    maximum: int
    groth_rate: float
