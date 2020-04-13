from seleniumbase import BaseCase
from ..page_objects.main_page import MainPage as PageObjects


class HappyPathTest(BaseCase):

    def common_actions(self):
        # Preenche valor para aplicar com 20,00
        self.update_text(PageObjects.input_valor_aplicar, '20,00')
        # Preenche valor que você quer poupar com 20,00
        self.update_text(PageObjects.input_valor_investir, '20,00')
        # Por quanto tempo você quer poupar com 20
        self.update_text(PageObjects.input_quanto_tempo, '20')

        self.click(PageObjects.btn_simular)
        self.assert_element(PageObjects.table)
        self.click(PageObjects.btn_repeat_simulation)

    def test_happy_path_para_voce(self):
        self.open(PageObjects.url)
        self.common_actions()
        # Testar para empresa
        self.click(PageObjects.radio_btn_empresa)
        self.common_actions()
