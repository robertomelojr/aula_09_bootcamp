# Decorator e Logging

## Principais Pontos:
### Decoradores (decorators) são como um "envoltório" (wrap) que "emprestam" sua capacidade de processamento a outra função quando esta é invocada. Sua utilização é essencial para manter o conceito de DRY (Don't Repeat Yourself) sempre em mente!

### Pontos Abordados:
- **Loguru**: Avalia e armazena logs de erros, informações, e outros de maneira personalizada. É muito útil para entender a causa de falhas no código durante as fases de homologação/produção. A grande vantagem é que não é necessário debugar o código constantemente.
- **Sentry**: Possui um conceito similar ao Loguru e DataDog. Salva os logs em um servidor, porém, cobra pelo uso. Se configurado de forma incorreta, pode gerar altos custos para o projeto.
- **Time**: Muito útil para criar decoradores que, por exemplo, avaliem qual pipeline é mais eficiente e qual é menos eficiente.
- **Tenacity**: Útil para implementar retries no processamento de informações.
