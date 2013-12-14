# coding: utf-8
from lettuce import *
from tel_utils import tel_clean, tel_operator

@step(u'Dado que eu tenho o número "(.+)"')
def dado_que_eu_tenho_o_numero_numero(step, numero):
    world.numero = numero

@step(u'E meu DDD padrão é "(\d{2})"')
def e_meu_ddd_padrao_e(step, ddd):
    world.ddd = ddd

@step(u'Quando eu formatar o número')
def quando_eu_aplicar_o_formatar_o_numero_no_padrao_brasileiro(step):
    world.novo_numero = tel_clean(world.numero, world.ddd)

@step(u'Então terei como resultado o número "(.+)"')
def entao_terei_como_resultado_o_numero_resultado(step, novo_numero):
    assert world.novo_numero == novo_numero, '%s != %s' % (world.novo_numero, novo_numero)

@step(u'Então deverá ocorrer um erro')
def entao_devera_ocorrer_um_erro(step):
    assert not world.novo_numero, '%s' % world.novo_numero

@step(u'Quando eu consultar a operadora de telefonia do número')
def quando_eu_consultar_a_operadora_de_telefonia_do_numero(step):
    world.operadora = tel_operator(world.numero, world.ddd)

@step(u'Então terei como resultado a operadora "(.+)"')
def entao_terei_como_resultado_a_operadora(step, operadora):
    assert world.novo_numero == novo_numero, '%s != %s' % (world.novo_numero, novo_numero)
