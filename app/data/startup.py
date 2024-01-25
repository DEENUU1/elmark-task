import json

from config.database import get_categories_collection, get_parts_collection


def part_load_startup_data(file_path: str) -> None:
    try:
        with open(file_path, "r") as file:
            mockup_data = json.load(file)

        collection = get_parts_collection()
        for part in mockup_data:
            existing = collection.find_one({"serial_number": part["serial_number"]})
            if not existing:
                collection.insert_one(part)

    except Exception as e:
        print(e)


def category_load_startup_data(file_path: str) -> None:
    try:
        with open(file_path, "r") as file:
            mockup_data = json.load(file)

        collection = get_categories_collection()
        for category in mockup_data:
            existing = collection.find_one({"name": category["name"], "parent_name": category.get("parent_name", None)})
            if not existing:
                collection.insert_one(category)

    except Exception as e:
        print(e)