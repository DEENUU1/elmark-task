from app.models.categories import Category


def test_create_base_category_object():
    category = Category(name="Tools")
    assert category.name == "Tools"
    assert category.parent_name is None
