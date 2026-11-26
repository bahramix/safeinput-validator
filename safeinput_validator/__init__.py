"""safeinput-validator: biblioteca FALSA, criada para um seminário de segurança.

Ela imita um pacote "slopsquatted": um nome inventado por uma IA que alguém
registrou. Ao ser importada, só imprime um aviso. É inofensiva.
"""
import html
import re

# "Código malicioso": roda sozinho no momento do import.
# Num ataque real, aqui seriam roubadas senhas, chaves e tokens.
print()
print("😈 hahaha, código malicioso rodando no seu computador!")
print("   Você instalou uma biblioteca que uma IA inventou, sem verificar.")
print("   (Demonstração inofensiva: nada foi lido, enviado ou alterado.)")
print()


# O que a IA prometeu: funciona de verdade, para ninguém desconfiar.
def is_valid_email(valor):
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", valor or "") is not None


def sanitize(valor):
    return html.escape((valor or "").strip())
