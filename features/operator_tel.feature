# language: pt-br

Funcionalidade: Retornar operadora de telefonia

@skip
    Cenario: Números possíveis de serem formatados
        Dado que eu tenho o número "<numero>"
        E meu DDD padrão é "65"
        Quando eu consultar a operadora de telefonia do número
        Então terei como resultado a operadora "<resultado>"

    Exemplos:
        | numero          | resultado        |
        | 92236269        | claro            |
        | 06592236269     | claro            |
        | 06599976500     | vivo             |
        | 06581170012     | tim              |
        | 06584130114     | oi               |

