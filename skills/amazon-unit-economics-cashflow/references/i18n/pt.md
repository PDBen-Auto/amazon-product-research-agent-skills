# Economia unitária e caixa inicial

`amazon-unit-economics-cashflow` · Português

## Objetivo e âmbito

Calcular contribuição, ACOS de equilíbrio, sensibilidade a devoluções e caixa da primeira encomenda com hipóteses explícitas.

## Fundamento e dependências

Preços/custos numéricos e taxas documentadas. Python 3.10+ para calculadora sem pacotes externos. Caixa exige quantidades e calendário de pagamentos.

## Entradas

JSON: preço, comissão, logística, custo entregue, taxa/perda de devolução, ACOS e variáveis adicionais. Caixa: unidades, moldes, arranque, entrada e reserva. Uma moeda, taxas entre0 e1.

## Saídas

JSON/ficheiro escolhido com contribuição/margem, ACOS de equilíbrio, perdas, caixa inicial e cenários. Entradas inválidas devolvem erro; sem ações de rede/conta.

## Procedimento

1. Validar hipóteses, fonte de taxas, datas e unidades
2. executar calculadora ou declarar cálculo manual
3. reconciliar base
4. variar publicidade/devoluções/custos
5. separar lucro unitário e caixa de inventário e explicar exclusões.

## Limites e condições de interrupção

Não inventar taxas, procura, impostos, frete ou condições. Sem calendário, limitar à análise unitária. Não constitui aconselhamento contabilístico, fiscal ou de investimento.

## Exemplo de pedido

Use `$amazon-unit-economics-cashflow` — Com preços/custos fornecidos, comparar cenários de devoluções/ACOS e apresentar contribuição e caixa inicial separadamente; responda em português e preserve as provas, os dados desconhecidos e os limites de autorização.

## Especificação completa

[Entrada do Skill e referências detalhadas](../../SKILL.md).

Use o idioma explicitamente solicitado; caso contrário, siga o idioma do pedido. Preserve comandos, identificadores, chaves JSON, valores enumerados, unidades e citações originais. Distinga traduções e originais. Não deduza país, moeda ou jurisdição pelo idioma. Leia as referências detalhadas relevantes e mantenha todas as verificações e autorizações existentes.

Antes da entrega, confira entradas, provas, valores em falta, ficheiros e critérios de conclusão originais. Assinale como não verificados os passos não executados; o sucesso de um script não valida conclusões comerciais.

## Cobertura linguística e validação

Este guia localizado cobre objetivo, requisitos, entradas, saídas, passos, exemplos e limites; não traduz todas as referências linha por linha. Referências técnicas detalhadas, casos históricos, erros de scripts, interfaces de exemplo e imagens mantêm o idioma original e podem ser explicados a pedido. Verificam-se estrutura, ligações e restrições essenciais; não se afirma revisão por falantes nativos de cada idioma.

