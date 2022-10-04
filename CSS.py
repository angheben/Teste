"""
O mínimo que você precisa saber sobre CSS

CSS é a sigla para Cascading Style Sheets, ou Folha de Estilo em Cascata e é usado para aplicar estilos nas páginas HTML

Desenvolvido pelo W3C em 1996 para formatar as páginas HTML, já que as tags HTML foram projetadas para realizar
marcações das páginas.

A relação entre HTML e CSS é bem forte. Como o HTML é uma linguagem de marcação (o alicerce de um site) e o CSS é focado
no estilo (toda a estética do site), eles andam juntos.

Basicamente existem 2 formas de se adicionar estilos CSS em uma página HTML:
1 - Inline, ou seja, diretamente na página HTML (não recomendado);
2 -
"""
import random


class Pessoa:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = self.gerar_idade()

    def gerar_idade(self):
        idade = random.randint(1, 100)
        return idade