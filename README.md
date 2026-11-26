# safeinput-validator

> ⚠️ **Biblioteca FALSA, criada para uma demonstração acadêmica de segurança (AI slopsquatting).**
> Ao ser importada, ela só imprime um aviso. Não lê, não envia e não altera nada.
> Não use em projetos reais.

## O que ela demonstra

Uma IA recomendou a biblioteca `safeinput-validator`, que não existia. Este repositório faz o papel do atacante que registrou esse nome: quem copiar e colar a recomendação da IA instala este código, e ele roda sozinho no `import`.

## Instalação (como a IA "recomenda")

```bash
pip install git+https://github.com/bahramix/safeinput-validator.git
```

## Uso

```python
from safeinput_validator import is_valid_email, sanitize

print(is_valid_email("usuario@exemplo.com"))  # True
print(sanitize("<script>alert('x')</script>"))  # texto escapado
```

Ao importar, aparece:

```
😈 hahaha, código malicioso rodando no seu computador!
```

## Remover

```bash
pip uninstall -y safeinput-validator
```
