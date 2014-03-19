# coding: utf-8
from lettuce import *
from tel_utils import PhoneNumber

@step(u'Dado que meu DDD padrão é "(.*)"')
def dado_que_meu_ddd_padrao_e(step, default_ddd):
    world.default_ddd = default_ddd

@step(u'E que eu tenho o número "(.*)"')
def e_que_eu_tenho_o_numero(step, number):
    world.number = number

@step(u'Quando eu criar o objeto PhoneNumber')
def quando_eu_criar_o_objeto_phonenumber(step):
    world.phone_number = PhoneNumber(world.number, world.default_ddd)

@step(u'Então o numero formatado será "(.*)"')
def entao_o_numero_formatado_sera(step, number):
    assert world.phone_number.number == number, '%s != %s' % (world.phone_number.number, number)

@step(u'Então o numero será vazio')
def entao_o_numero_sera_vazio(step):
    assert not world.phone_number.number, '%s' % world.novo_numero

@step(u'Então o tipo será "(.*)"')
def entao_o_tipo_sera(step, type_):
    assert world.phone_number.type() == type_, '%s != %s' % (world.phone_number.type(), type_)


'''

@step(u'Dado que meu DDD padrão é "(\d{2})"')
def e_meu_ddd_padrao_e(step, default_ddd):
    world.default_ddd = default_ddd

@step(u'E que eu tenho o número "(.+)"')
def dado_que_eu_tenho_o_numero_numero(step, number):
    world.phone_number = PhoneNumber(number, default_ddd)

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

@step(u'Quando eu verificar o tipo do telefone')
def quando_eu_verificar_o_tipo_do_telefone(step):
    world.tipo = tel_type(world.numero, world.ddd)

@step(u'Então o tipo será "(.+)"')
def entao_o_tipo_sera(step, tipo):
    assert world.tipo == tipo, '%s != %s' % (world.tipo, tipo)

'''