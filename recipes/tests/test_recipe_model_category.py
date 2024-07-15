from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='Testing category str')
        return super().setUp()

    def test_recipe_category_model_string_representation(self):
        self.assertEqual(
            str(self.category),
            self.category.name,
            msg=f'Category string representation must'
                f'be "{self.category.name}" '
                f'but "{str(self.category)}" was received')

    def test_recipe_category_model_name_max_length_is_65_chars(self):
        self.category.name = 'A' * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
