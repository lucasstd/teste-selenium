from ..settings import configs

class MainPage:
    url = configs['BASE_URL']
    input_quanto_tempo = "#tempo"
    input_valor_aplicar = "#valorAplicar"
    input_valor_investir = "#valorInvestir"
    drop_num_meses = '''//*[@id=\"formInvestimento\"]/div[4]/div[2]/div[2]/a'''
    btn_simular = '''//*[@id=\"formInvestimento\"]/div[5]/ul/li[2]/button'''
    radio_btn_empresa = '''//*[@id=\"formInvestimento\"]/div[1]/input[2]'''
    # pagina da tabela
    table = '''/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/table'''
    btn_repeat_simulation = '''/html/body/div[3]/div/div/div[1]/div/div[2]/a'''
    # mensagens de erro
    tempo_error = "#tempo-error"
    valorAplicar_error = "#valorAplicar-error"
    valorInvestir_error = "#valorInvestir-error"
