from seleniumbase import BaseCase
from ..page_objects.main_page import MainPage as PageObjects


class WithoutValuesTest(BaseCase):

    def common_actions(self):
        self.click(PageObjects.btn_simular)
        # Verifica se as mensagens de erro aparecem
        self.assert_element(PageObjects.valorAplicar_error)
        self.assert_element(PageObjects.valorInvestir_error)
        self.assert_element(PageObjects.tempo_error)

    def test_with_no_values(self):
        self.open(PageObjects.url)
        self.common_actions()
        # Testar para empresa
        self.click(PageObjects.radio_btn_empresa)
        self.common_actions()
