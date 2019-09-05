from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        # pass

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 查看首页
        self.browser.get(self.live_server_url)

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
        time.sleep(1)

        self.check_for_row_in_list_table('1. Buy peacock feathers')

        # 页面中又显示了一个文本框，可以输入其他待办事项
        # 他又输入了“Use peacock feathers to make a fly”
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table('2. Use peacock feathers to make a fly')

        self.fail('finish the test!')

        # 页面再次更新，出现两个待办事项

        # 网站生成了唯一的URL
        # 网页还带了一些文字说明

        # 他访问了那个URL，发现代办事项都还在
