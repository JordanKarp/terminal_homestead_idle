from task import Task
from item_data import items
tasks = {
    "Chop Tree": Task(message="Chop Trees", duration=60, add_items=[items['Log']] remove_resources=['tree'], add_resources='Stump'),
}
