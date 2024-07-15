from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_registered_yet_if_not_recipes(self):  # noqa
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes registered yet',
            response.content.decode('utf-8'),
            )

    def test_recipe_home_template_loads_recipes(self):
        # Need a recipe for this test
        self.make_recipe()

        # Getting the Response HTTP from server
        response = self.client.get(reverse('recipes:home'))
        # Getting just the content and convert to string
        content = response.content.decode('utf-8')
        # Getting the recipes QuerySet
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_doesnt_load_recipes_not_published(self):
        '''Tests if an 'not_published' recipe really doesn't appear on the page''' # noqa

        # Need a recipe for this test
        self.make_recipe(is_published=False)

        # Getting the Response HTTP from server
        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            'No recipes registered yet',
            response.content.decode('utf-8'),
            )
