# Suite de pesquisa de produtos Amazon

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

Use o idioma explicitamente solicitado; caso contrário, siga o idioma do pedido. Preserve comandos, identificadores, chaves JSON, valores enumerados, unidades e citações originais. Distinga traduções e originais. Não deduza país, moeda ou jurisdição pelo idioma. Leia as referências detalhadas relevantes e mantenha todas as verificações e autorizações existentes.

## Instalação e utilização

Transfira ou clone o repositório e copie o diretório do Skill indicado, com as suas references, scripts, assets e demais dependências existentes, para o diretório de Skills do ambiente. Preserve o nome e SKILL.md. Mudar o idioma da documentação não exige outra instalação. Os comandos são opções, não provas de instalação ou ativação.

```sh
git clone https://github.com/PDBen-Auto/amazon-product-research-agent-skills.git
```

## Diferenciação de produto baseada em provas

`amazon-product-differentiation-rd`

Transformar dificuldades dos clientes em mecanismos, especificações mensuráveis, experiências económicas e critérios prévios de abandono.

Diretório do Skill: `skills/amazon-product-differentiation-rd`

**Fundamento e dependências**

Provas rastreáveis, produto de referência e tarefa principal do utilizador. Restrições comerciais para viabilidade; protótipos e revisão patente/fornecedor conforme necessário. Provas fornecidas dispensam serviço em direto.

**Entradas**

Obrigatórios: avaliações/entrevistas/devoluções, imagens/especificação de referência e tarefa. Condicionais preço, custo, dimensões, materiais, compatibilidade, MOQ e conformidade. Limiares propostos são hipóteses.

**Saídas**

Mapa prova-mecanismo, conceitos, especificações, experiências e riscos em Markdown/JSON/tabela. Cada recomendação exige prova, mecanismo, requisito e teste.

[Procedimento · Limites e condições de interrupção · Exemplo de pedido](skills/amazon-product-differentiation-rd/references/i18n/pt.md)

> Use `$amazon-product-differentiation-rd` — Para um suporte que escorrega, definir retenção, libertação, massa do aparelho e ensaios de vibração/temperatura, não apenas um íman mais forte; responda em português e preserve as provas, os dados desconhecidos e os limites de autorização.

## Suite de pesquisa de produtos Amazon

`amazon-product-research-suite`

Encaminhar decisões com dois ou mais domínios para o menor conjunto de Skills especializados; tarefas restritas seguem diretamente para o especialista.

Diretório do Skill: `skills/amazon-product-research-suite`

**Fundamento e dependências**

Ambiente Agent Skills e especialistas escolhidos instalados. Provas fornecidas permitem trabalho offline; recolha em direto exige rede/permissão. Python 3.10+ para utilitários opcionais.

**Entradas**

Decisão de produto obrigatória; conforme a tarefa ASIN/identidade, mercado, jurisdição, período e direitos. Opcionais CSV/JSON/XLSX/PDF/imagens, orçamentos e restrições. Desconhecidos ficam como lacunas.

**Saídas**

route-plan.json, contrato comum de provas, Skills/ordem, entradas em falta e destinos. O encaminhamento não instala nem contacta serviços.

[Procedimento · Limites e condições de interrupção · Exemplo de pedido](skills/amazon-product-research-suite/references/i18n/pt.md)

> Use `$amazon-product-research-suite` — Avaliar um suporte automóvel em mercado, avaliações, diferenciação, fornecimento e economia; acrescentar análise de desenhos quando há imagens; responda em português e preserve as provas, os dados desconhecidos e os limites de autorização.

## Viabilidade de fornecedores e amostras

`amazon-supplier-feasibility`

Preparar RFQ, orçamentos comparáveis e critérios fundamentados para amostras; por defeito não contactar fábricas nem comprar.

Diretório do Skill: `skills/amazon-supplier-feasibility`

**Fundamento e dependências**

Especificação obrigatória; comparação exige orçamentos datados equivalentes. Conformidade, amostras e comunicação são condicionais. Contacto com a fábrica requer autorização separada.

**Entradas**

Especificação/desenho com unidades/tolerâncias e hipóteses de quantidade/procura; moeda, Incoterm, ferramentas e pagamentos quando necessários; opcionais PDF/XLSX/CSV e provas de qualidade.

**Saídas**

RFQ, comparação custo/prazo, registo de riscos e plano de amostras. Estados READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL ou INSUFFICIENT_EVIDENCE.

[Procedimento · Limites e condições de interrupção · Exemplo de pedido](skills/amazon-supplier-feasibility/references/i18n/pt.md)

> Use `$amazon-supplier-feasibility` — Alinhar íman, adesivo, binário, ensaio térmico, propriedade dos moldes e embalagem antes de comparar suportes; responda em português e preserve as provas, os dados desconhecidos e os limites de autorização.

## Economia unitária e caixa inicial

`amazon-unit-economics-cashflow`

Calcular contribuição, ACOS de equilíbrio, sensibilidade a devoluções e caixa da primeira encomenda com hipóteses explícitas.

Diretório do Skill: `skills/amazon-unit-economics-cashflow`

**Fundamento e dependências**

Preços/custos numéricos e taxas documentadas. Python 3.10+ para calculadora sem pacotes externos. Caixa exige quantidades e calendário de pagamentos.

**Entradas**

JSON: preço, comissão, logística, custo entregue, taxa/perda de devolução, ACOS e variáveis adicionais. Caixa: unidades, moldes, arranque, entrada e reserva. Uma moeda, taxas entre0 e1.

**Saídas**

JSON/ficheiro escolhido com contribuição/margem, ACOS de equilíbrio, perdas, caixa inicial e cenários. Entradas inválidas devolvem erro; sem ações de rede/conta.

[Procedimento · Limites e condições de interrupção · Exemplo de pedido](skills/amazon-unit-economics-cashflow/references/i18n/pt.md)

> Use `$amazon-unit-economics-cashflow` — Com preços/custos fornecidos, comparar cenários de devoluções/ACOS e apresentar contribuição e caixa inicial separadamente; responda em português e preserve as provas, os dados desconhecidos e os limites de autorização.

## Cobertura linguística e validação

Este guia localizado cobre objetivo, requisitos, entradas, saídas, passos, exemplos e limites; não traduz todas as referências linha por linha. Referências técnicas detalhadas, casos históricos, erros de scripts, interfaces de exemplo e imagens mantêm o idioma original e podem ser explicados a pedido. Verificam-se estrutura, ligações e restrições essenciais; não se afirma revisão por falantes nativos de cada idioma.

Antes da entrega, confira entradas, provas, valores em falta, ficheiros e critérios de conclusão originais. Assinale como não verificados os passos não executados; o sucesso de um script não valida conclusões comerciais.
