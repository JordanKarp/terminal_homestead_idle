from random import randint

from src.data.natural_resource_data import natural_resources
from src.classes.natural_resource import NaturalResource


class Environment:
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

    def __str__(self):
        return "".join(
            str(resource) + "\n"
            for resource in self.natural_resources.values()
            if resource.count
        )
