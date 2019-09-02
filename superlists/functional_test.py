from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 查看首页
        self.browser.get('http://localhost:8000')

        # 首页和标题都包含“To-Do”
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请输入待办事项
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'),
                         'Enter a to-do item')

        # 文本框中输入“Buy peacock feathers”
        input_box.send_keys('Buy peacock feathers')

        # 回车后页面更新了
        # 代办事项表格中显示“1. Buy peacock feathers”
        input_box.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1. Buy peacock feathers' for row in rows))

        # 页面中又显示了一个文本框，可以输入其他待办事项
        # 他又输入了“Use peacock feathers to make a fly”
        self.fail('finish the test!')

        # 页面再次更新，出现两个待办事项

        # 网站生成了唯一的URL
        # 网页还带了一些文字说明

        # 他访问了那个URL，发现代办事项都还在


if '__main__' == __name__:
    unittest.main()
