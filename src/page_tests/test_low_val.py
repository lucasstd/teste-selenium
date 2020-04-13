from seleniumbase import BaseCase
from ..page_objects.main_page import MainPage as PageObjects


class LowValuesTest(BaseCase):

    def test_low_values(self):
        self.open(PageObjects.url)
        # Preenche valor para aplicar com 2,00
        self.update_text(PageObjects.input_valor_aplicar, '2,00')
        # Preenche valor que você quer poupar com 20,00
        self.update_text(PageObjects.input_valor_investir, '2,00')
        # Por quanto tempo você quer poupar com 20
        self.update_text(PageObjects.input_quanto_tempo, '0')
        self.click(PageObjects.btn_simular)
        # Verifica se as mensagens de erro aparecem
        self.assert_element(PageObjects.valorAplicar_error)
        self.assert_element(PageObjects.valorInvestir_error)
        self.assert_element(PageObjects.tempo_error)
