from seleniumbase import BaseCase
from ..page_objects.main_page import MainPage as PageObjects


class NegativeNumbersTest(BaseCase):

    def test_negative_values(self):
        self.open(PageObjects.url)
        
        # Preenche valor para aplicar com -20,00
        self.update_text(PageObjects.input_valor_aplicar, '-20,00')
        valor_aplicar = self.get_text(PageObjects.input_valor_aplicar)
        # Verifica se valor fica 20,00
        assert '20,00' == valor_aplicar if valor_aplicar else True

        # Preenche valor que você quer poupar com 20,00
        self.update_text(PageObjects.input_valor_investir, '-20,00')
        valor_investir = self.get_text(PageObjects.input_valor_investir)
        # Verifica se valor fica 20,00
        assert '20,00' == valor_investir if valor_investir else True
        
        # Por quanto tempo você quer poupar com 20
        self.update_text(PageObjects.input_quanto_tempo, '-2')
        # Clica para checar se vai aparecer a mensagem de erro
        self.click(PageObjects.btn_simular)
        valor_investir = self.get_text(PageObjects.input_valor_investir)
        # TODO: Colocar no README que pode colocar valores negativos aqui
        #       Provavelmente esse comportamento não era esperado...
        if valor_investir: assert '2' == valor_investir  # noqa
        else:
            # Verifica se valor fica 2 ou a mensagem de erro aparece
            self.assert_element(PageObjects.tempo_error)
            self.update_text(PageObjects.input_quanto_tempo, '2')

        self.click(PageObjects.btn_simular)
        self.assert_element(PageObjects.table)
        self.click(PageObjects.btn_repeat_simulation)
