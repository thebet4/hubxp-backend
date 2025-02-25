
def individual_category(category):
    return {
        "id": str(category["_id"]),
        "name": category["name"],
        "created_at": category["created_at"],
        "updated_at": category["updated_at"]
    }


def all_categories(categories):
    return [individual_category(category) for category in categories]
