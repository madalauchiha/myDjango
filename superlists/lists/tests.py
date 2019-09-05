from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     # print(response.content)
    #     expected_html = render_to_string('home.html')
    #     # print(expected_html)
    #     # print(response.content.decode())
    #     self.assertEqual(response.content.decode(), expected_html)
    #     # self.assertTrue(response.content.startswith(b'<html>'))
    #     # self.assertTrue(response.content.endswith(b'</html>'))
    #     # self.assertIn(b'<title>To-Do lists</title>', response.content)
    #
    # def test_home_page_can_save_post_request(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = 'A new list item'
    #
    #     response = home_page(request)
    #     # self.assertIn('A new list item', response.content.decode())
    #
    #     expected_html = render_to_string('home.html',
    #                                      {'new_item_text': 'A new list item'})
    #
    #     print(expected_html)
    #     print(response.content.decode())
    #     self.assertEqual(response.content.decode(), expected_html)


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        self.assertEqual(saved_items[0].text, first_item.text)
        self.assertEqual(saved_items[1].text, second_item.text)
