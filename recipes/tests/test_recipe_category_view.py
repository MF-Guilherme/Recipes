from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_not_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
            )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse(
            'recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_category_template_doesnt_load_recipes_not_published(self):
        '''Tests if an 'not_published' recipe really doesn't appear on the page''' # noqa

        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        # Getting the Response HTTP from server
        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={'category_id': recipe.category.id})
            )

        self.assertEqual(response.status_code, 404)

