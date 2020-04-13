# teste-selenium
Uma aplicação simples usando Selenium para teste de API e E2E

## Rodando testes
* Passo 1: instale Python e certifique que o pip está em suas variaveis de ambiente. (no terminal digite: pip --version)
* Passo Opcional (para não deixar arquivos no teu computador): Instale o virtualenv (pip install virtualenv) depois no terminal digite use(Linux):
```bash
    virtualenv venv
    . venv/bin/activate
```
para windows:
https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais

* Passo 2: primeiro: cd teste_selenium, depois: pip install -r requirements.txt
* Passo3: rode no terminal/cmd
```bash
    pytest --browser=firefox
```

## Tecnicas de teste escolhidas
* Teste de contrato com JSONSchema - Como dito antes, sinceramente achei que faltava explicação na parte da API, testei alguns POST, queries e levei um bom tempo até perceber que poderia tratava de um teste de contrato (lendo bastante), não tem muitos "corner cases então foi a parte mais simples"

* Teste End to end - Como o caso de aceitação dizia para fazer testes em uma UI e preenchendo campos, testes e2e são perfeitos pra isso.

### Planejamento
* Primeiramente, comecei usando Cypress como pode ver nesse repositório: https://github.com/lucasstd/teste-simulador. E foi incrivelmente mais simples e bonito, logo após uma conversa com a avaliadora ficou acertado que faria com Selenium e em Java, então comecei com o Java como pode ver: https://github.com/lucasstd/teste-selenium/tree/java-version. Achei incrívelmente irritante usar o JsonSchema de lá (everit) e pegar um arquivo JSON, mas até tinha conseguido fazer e montar o projeto com Maven sem saber nada, porém, comecei no computador do trabalho com Java e lá funcionava, e no meu computador pessoal não, só depois de quase terminar o projeto em Python que descobri o motivo (Driver do chrome estava com problema), então peguei os arquivos de lá por ssh e coloquei em outra Branch, para fazer no Python usei a biblioteca SeleniumBase para não precisar reescrever muitos códigos, fazer uma factory para driver e tudo que já tinha pronto lá(embora o código fonte deles não foi muito bem feito) e foi relativamente facil para terminar o projeto (tenho um projeto que criei antes sem o seleniumBase se quiserem).
Já havia criado os testes, pensado na historia e "corner cases" pelo outro teste com Cypress que havia feito, então precisei apenas olhar o código fonte do SeleniumBase e do selenium para entender o funcionamento, com isso em mente montei um JsonValidator com draft7 bem generico para que eu possa usar no futuro em outros projetos.

## Criado com
- [x] [Selenium](https://selenium-python.readthedocs.io/) - Pois foi acordado que usaria.

- [x] [JSONSchema](https://json-schema.org/implementations.html) - Escolhi o JSONSchema para teste de contrato pois já havia utilizado com Python e Java antes, porém, me poderia ter feito sem essa ferramenta, mas ela pode agregar mais no futuro, por isso foi escolhida

- [x] [Python](https://www.python.org/) - Pois é uma linguagem de script, simples e rápido para criar um projeto, embora não seja relativamente performatico comparado com uma linguagem compilada.

### Ferramentas testadas e não utilizadas
- [ ] Cucumber - fiz alguns testes com cucumber antes de escolher deixa-lo de lado pois já haviam critério de aceitação, e deveria ser um projeto simples (posso criar uma branch e colocar, mas decidi não encher de coisas o github)
``` 
Feature: Testar campos do formulario de investimentos

    Background: Acesso o site de simulação de investimentos da Sicredi
        Given acesso o site da Sicredi

    Scenario: Preencher o formulario de investimentos com informações certas
        Then visualizar a tabela de resultado com Mês e Valor. 

    Scenario Outline: Preencher o formulario de investimentos com informações incorretas
        When informar <Qual o valor que você quer aplicar?> abaixo de 20,00
        When informar <Por quanto tempo você quer poupar?> abaixo de 20,00
        And Mudar o foco do campo
        Then devo visualizar a mensagem de erro

    Scenario Outline: Preencher o formulario de investimentos com informações incorretas e clicar em simular
        When informar <Qual o valor que você quer aplicar> abaixo de 20,00
        When informar <Por quanto tempo você quer poupar?> abaixo de 20,00
        And clicar em simular
        Then não devo visualizar a tabela de resultado com Mês e Valor.
```

- [ ] Docker - No geral, meus projetos são feitos utilizando Docker, porém como era para fazer uma coisa bem simples, preferi não complicar


## Aprendido
Aprendi que é incrivelmente diferente usar diversas ferramentas de teste, várias coisas não estão prontas no Selenium, e com Java principalmente... Os projetos com Java no geral são divertidos, porém não sei porque dificultaram tanto para Jsonschema (tudo bem que não é uma linguagem de script, mas...), mas aprendi que selenium tem várias limitações, como componentes que não aparecem e precisa ser esperado e não se pode abrir o console, entre outras coisas, que no Cypress possui.
