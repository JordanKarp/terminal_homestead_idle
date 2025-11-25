from random import randint

from natural_resource_data import natural_resource_dict
from natural_resource import NaturalResource

class Environment:
    def __init__(self, nat_resources=None):
        if not nat_resources:
            nat_resources = self.generate_natural_resources()
        self.natural_resources = nat_resources

    
    def generate_natural_resources(self):
        resources = {}
        for resource_name, resource_data in natural_resource_dict.items():
            min = resource_data.get("minimum", 0)
            max = resource_data.get("maximum", 0)
            growth = resource_data.get("growth_rate", 0)
            count = randint(min, max)
            plural_name = resource_name.get("plural_name", resource_name)
            description = resource_name.get("description", "No Description Found")
            resource = NaturalResource(resource_name, plural_name,description, count, growth )
            resources[resource_name] = resource
        return resources