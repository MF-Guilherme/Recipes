from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeDetailViewTest(RecipeTestBase):
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_not_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
            )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It loads just one recipe'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_detail_template_doesnt_load_recipe_not_published(self):
        '''Tests if an 'not_published' recipe really doesn't appear on the page''' # noqa

        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        # Getting the Response HTTP from server
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={'id': recipe.id})
            )

        self.assertEqual(response.status_code, 404)

