from models.categories import Category


class CategorySchema(Category):
    pass


class CategoryUpdateSchema(CategorySchema):
    name: str = None

    class Config:
        orm_mode = True

