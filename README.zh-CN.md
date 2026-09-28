# Amazon 产品研究 Agent Skills 套件

面向 Amazon 产品团队的一站式 Skill 入口：市场边界、评论洞察、外观专利预筛、供应链可行性和 Go/No-Go 立项决策。

## 5 分钟开始

安装统一路由 Skill：

```bash
npx skills add PDBen-Auto/amazon-product-research-agent-skills --skill amazon-product-research-suite
```

然后告诉 Agent：

```text
使用 $amazon-product-research-suite。我正在评估一个 Amazon US 新产品。
请先把问题路由到合适的 Skill，列出缺失证据，再给出执行计划。
```

也可以直接安装单项 Skill：

```bash
npx skills add PDBen-Auto/amazon-review-intelligence-skill
npx skills add PDBen-Auto/design-patent-design-around-skill --skill design-patent-search-and-design-around
npx skills add PDBen-Auto/sellersprite-amazon-market-research-bi-skill --skill sellersprite-bi-market-research
npx skills add PDBen-Auto/amazon-product-decision-suite --skill amazon-product-decision-gateway
```

## 如何选择

| 你要回答的问题 | 使用 Skill | 得到的结果 |
| --- | --- | --- |
| 用户到底在抱怨什么，产品该改什么？ | [Amazon Review Intelligence](https://github.com/PDBen-Auto/amazon-review-intelligence-skill) | 保留原文证据的评论数据、Excel、JSON、离线 HTML VOC 报告和产品假设 |
| 产品是否接近已有外观设计权，如何改款？ | [Design Patent Search and Design-around](https://github.com/PDBen-Auto/design-patent-design-around-skill) | 搜索日志、官方图纸分析、风险拆分、结构性设计规避方案和打样门槛 |
| 真实直接市场有多大，哪些 ASIN 可以进入分母？ | [SellerSprite Market Research BI](https://github.com/PDBen-Auto/sellersprite-amazon-market-research-bi-skill) | 候选清单、相关性判断、父 ASIN 去重、覆盖闸门和离线 BI 仪表板 |
| 该不该投入、打样、询盘，还是停止？ | [Amazon Product Decision Gateway](https://github.com/PDBen-Auto/amazon-product-decision-suite) | 证据契约、阶段门状态、GO / CONDITIONAL_GO / NO_GO / INSUFFICIENT_EVIDENCE 交接 |

## 解决什么问题

市场 BI 能说明需求，评论分析能说明痛点，专利搜索能提示风险，但它们单独都不能证明产品可生产、能赚钱、适合当前团队投入。本套件把这些任务组织成一条可复核的决策链：

```text
市场边界 -> 用户证据 -> 设计/IP 风险 -> 供应链可行性 -> 单位经济与现金 -> 阶段门决策
```

它不是替代所有专业 Skill，而是提供一个能被搜索、能被安装、能被路由和能被复盘的统一入口。

## 核心差异

- 按产品问题路由，不要求用户先理解工具目录；
- 明确区分事实、计算、模型、推断和假设；
- 输出 JSON、XLSX、HTML、搜索日志、候选清单和签名交接包；
- CAPTCHA、缺失数据、法律不确定性和关键成本缺口会成为显式阻断；
- 公开仓库不包含私有 Engine、客户数据、凭证、内部阈值和签名私钥；
- 单项仓库可独立安装，也可以作为套件的一部分使用。

## 安全与隐私

安装脚本没有遥测、隐藏追踪、后门、提示词混淆或凭证收集逻辑。不要把 Amazon Cookie、SellerSprite 私有导出、供应商联系人、客户评论、API Token 或签名私钥提交到公开仓库。

更多输入、输出、依赖和边界见 [SKILL.md](SKILL.md) 与各子仓库文档。
