from random import randint

from src.data.natural_resource_data import natural_resources
from src.classes.natural_resource import NaturalResource
from src.utility.utility_functions import get_number


class Environment:
    """Represents the natural resources available around the homestead.

    Provides helpers to query availability, adjust resource counts and
    generate defaults from static data.
    """
    def __init__(self, nat_resources=None):
        if not nat_resources:
            nat_resources = self.generate_natural_resources()
        self.natural_resources = nat_resources

    def has(self, resource_name, count=1):
        return (
            resource_name in self.natural_resources
            and self.natural_resources[resource_name].count >= count
        )

    def adjust_natural_resource_amount(self, resource, amount):
        if self.natural_resources.get(resource, None):
            self.natural_resources[resource].count += amount

    def generate_natural_resources(self):
        """Create resource objects using defaults from the data files."""
        resources = {}
        for resource_name, resource_data in natural_resources.items():
            minimum = resource_data.get("minimum", 0)
            maximum = resource_data.get("maximum", 0)
            growth = resource_data.get("growth_rate", 0)
            count = randint(minimum, maximum)
            plural_name = resource_data.get("plural_name", resource_name)
            description = resource_data.get("description", "No Description Found")
            resource = NaturalResource(
                resource_name, plural_name, description, count, growth
            )
            resources[resource_name] = resource
        return resources

    @staticmethod
    def prompt_custom_resources():
        """Interactively prompt the user to specify counts for each resource."""
        resources = {}
        for resource_name, resource_data in natural_resources.items():
            plural_name = resource_data.get("plural_name", resource_name)
            growth = resource_data.get("growth_rate", 0)
            description = resource_data.get("description", "No Description Found")
            number = get_number(f"How many {plural_name}: ")
            resource = NaturalResource(
                resource_name, plural_name, description, number, growth
            )
            resources[resource_name] = resource
        return resources


    def __str__(self):
        return "".join(
            str(resource) + "\n"
            for resource in self.natural_resources.values()
            if resource.count
        )
