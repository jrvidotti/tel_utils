# language: pt-br

Funcionalidade: Tipos de telefone

    Cenario: Celulares
        Dado que meu DDD padrão é "65"
        E que eu tenho o número "<numero>"
        Quando eu criar o objeto PhoneNumber
        Então o tipo será "celular"

    Exemplos:
        | numero          |
        | 92236269        |
        | (065) 9223-6269 |
        | 82236269        |


    Cenario: Celulares
        Dado que meu DDD padrão é "65"
        E que eu tenho o número "<numero>"
        Quando eu criar o objeto PhoneNumber
        Então o tipo será "fixo"

    Exemplos:
        | numero          |
        | 30527415        |
        | (065) 3623-1213 |
        | 2125-0023       |
