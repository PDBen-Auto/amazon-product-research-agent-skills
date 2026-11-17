# Viabilidade de fornecedores e amostras

`amazon-supplier-feasibility` · Português

## Objetivo e âmbito

Preparar RFQ, orçamentos comparáveis e critérios fundamentados para amostras; por defeito não contactar fábricas nem comprar.

## Fundamento e dependências

Especificação obrigatória; comparação exige orçamentos datados equivalentes. Conformidade, amostras e comunicação são condicionais. Contacto com a fábrica requer autorização separada.

## Entradas

Especificação/desenho com unidades/tolerâncias e hipóteses de quantidade/procura; moeda, Incoterm, ferramentas e pagamentos quando necessários; opcionais PDF/XLSX/CSV e provas de qualidade.

## Saídas

RFQ, comparação custo/prazo, registo de riscos e plano de amostras. Estados READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL ou INSUFFICIENT_EVIDENCE.

## Procedimento

1. Rever lacunas e requisitos essenciais
2. preparar RFQ
3. alinhar quantidade, moeda, Incoterm, inclusões e data
4. examinar ferramentas/capacidade/qualidade/conformidade/logística
5. definir testes antes da receção
6. comparar viabilidade total e passar custos ao modelo económico.

## Limites e condições de interrupção

Não classificar orçamentos incomparáveis nem aceitar certificação sem documentos. Falha crítica não é compensada por preço baixo. Não enviar, negociar ou encomendar sem permissão.

## Exemplo de pedido

Use `$amazon-supplier-feasibility` — Alinhar íman, adesivo, binário, ensaio térmico, propriedade dos moldes e embalagem antes de comparar suportes; responda em português e preserve as provas, os dados desconhecidos e os limites de autorização.

## Especificação completa

[Entrada do Skill e referências detalhadas](../../SKILL.md).

Use o idioma explicitamente solicitado; caso contrário, siga o idioma do pedido. Preserve comandos, identificadores, chaves JSON, valores enumerados, unidades e citações originais. Distinga traduções e originais. Não deduza país, moeda ou jurisdição pelo idioma. Leia as referências detalhadas relevantes e mantenha todas as verificações e autorizações existentes.

Antes da entrega, confira entradas, provas, valores em falta, ficheiros e critérios de conclusão originais. Assinale como não verificados os passos não executados; o sucesso de um script não valida conclusões comerciais.

## Cobertura linguística e validação

Este guia localizado cobre objetivo, requisitos, entradas, saídas, passos, exemplos e limites; não traduz todas as referências linha por linha. Referências técnicas detalhadas, casos históricos, erros de scripts, interfaces de exemplo e imagens mantêm o idioma original e podem ser explicados a pedido. Verificam-se estrutura, ligações e restrições essenciais; não se afirma revisão por falantes nativos de cada idioma.

