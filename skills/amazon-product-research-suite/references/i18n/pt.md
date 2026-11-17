# Suite de pesquisa de produtos Amazon

`amazon-product-research-suite` · Português

## Objetivo e âmbito

Encaminhar decisões com dois ou mais domínios para o menor conjunto de Skills especializados; tarefas restritas seguem diretamente para o especialista.

## Fundamento e dependências

Ambiente Agent Skills e especialistas escolhidos instalados. Provas fornecidas permitem trabalho offline; recolha em direto exige rede/permissão. Python 3.10+ para utilitários opcionais.

## Entradas

Decisão de produto obrigatória; conforme a tarefa ASIN/identidade, mercado, jurisdição, período e direitos. Opcionais CSV/JSON/XLSX/PDF/imagens, orçamentos e restrições. Desconhecidos ficam como lacunas.

## Saídas

route-plan.json, contrato comum de provas, Skills/ordem, entradas em falta e destinos. O encaminhamento não instala nem contacta serviços.

## Procedimento

1. Definir decisão/âmbito
2. selecionar e verificar Skills
3. criar plano/contrato
4. executar só fases autorizadas
5. distinguir observado/calculado/modelado/inferido/suposto
6. validar schemas e ficheiros
7. preservar resultados parciais perante bloqueios.

## Limites e condições de interrupção

Não inventar denominadores, taxas, compromissos de fornecedores, conclusões jurídicas ou pontuações privadas. CAPTCHA, acesso ausente, envio sensível ou hipóteses financeiras insuficientes interrompem a fase afetada.

## Exemplo de pedido

Use `$amazon-product-research-suite` — Avaliar um suporte automóvel em mercado, avaliações, diferenciação, fornecimento e economia; acrescentar análise de desenhos quando há imagens; responda em português e preserve as provas, os dados desconhecidos e os limites de autorização.

## Especificação completa

[Entrada do Skill e referências detalhadas](../../SKILL.md).

Use o idioma explicitamente solicitado; caso contrário, siga o idioma do pedido. Preserve comandos, identificadores, chaves JSON, valores enumerados, unidades e citações originais. Distinga traduções e originais. Não deduza país, moeda ou jurisdição pelo idioma. Leia as referências detalhadas relevantes e mantenha todas as verificações e autorizações existentes.

Antes da entrega, confira entradas, provas, valores em falta, ficheiros e critérios de conclusão originais. Assinale como não verificados os passos não executados; o sucesso de um script não valida conclusões comerciais.

## Cobertura linguística e validação

Este guia localizado cobre objetivo, requisitos, entradas, saídas, passos, exemplos e limites; não traduz todas as referências linha por linha. Referências técnicas detalhadas, casos históricos, erros de scripts, interfaces de exemplo e imagens mantêm o idioma original e podem ser explicados a pedido. Verificam-se estrutura, ligações e restrições essenciais; não se afirma revisão por falantes nativos de cada idioma.

