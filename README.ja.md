# Amazon 商品調査スイート

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

ユーザーが明示した言語で出力し、指定がなければ依頼文の言語に従います。コマンド、スキル ID、JSON キー、列挙値、単位、引用原文は保持します。翻訳と原文を分け、言語から国・通貨・法域を推定しません。詳細仕様の該当資料を読み、既存の検証と権限確認を適用します。

## 導入と利用

リポジトリを取得し、下記のスキルディレクトリを既存の references、scripts、assets などと一緒にホストのスキル用ディレクトリへコピーします。名前と SKILL.md は変更しません。説明言語を変えるだけなら再導入は不要です。導入用コマンドの掲載は、導入済みや有効化済みを意味しません。

```sh
git clone https://github.com/PDBen-Auto/amazon-product-research-agent-skills.git
```

## 根拠に基づく商品差別化

`amazon-product-differentiation-rd`

顧客の不満を製品機構、測定可能な仕様、低コスト実験、事前の中止基準へ変換します。

スキルディレクトリ: `skills/amazon-product-differentiation-rd`

**実装の根拠と依存関係**

追跡できる顧客根拠、基準製品、主要な利用目的が必須。実現性には事業制約、検証には試作品や専門レビューが必要に応じて求められます。

**入力**

必須：レビュー・面談・返品根拠、製品画像や仕様、対象者の目的。条件付き：価格、原価、寸法、材料、適合、MOQ、規制。提案する閾値は仮定と明記します。

**出力**

根拠と機構の対応、案の比較、数値仕様、実験計画、未解決リスクを Markdown/JSON/表で出力。各推奨には根拠・機構・要件・試験が必要です。

[実行手順 · 制約と停止条件 · 依頼例](skills/amazon-product-differentiation-rd/references/i18n/ja.md)

> 次のスキルを使用してください： `$amazon-product-differentiation-rd` — 滑るホルダーなら磁力だけでなく保持・解除力、端末重量、振動・温度試験を定義します。日本語で回答し、根拠、不明点、操作権限を維持してください。

## Amazon 商品調査スイート

`amazon-product-research-suite`

二つ以上の調査領域にまたがる判断を最小限の専門 Skill に振り分けます。単一課題は専門手順へ直接回します。

スキルディレクトリ: `skills/amazon-product-research-suite`

**実装の根拠と依存関係**

Agent Skills 対応環境と選択した専門 Skill。手持ち資料ならオフライン可。オンライン取得には通信と許可が必要です。Python 3.10+ は補助ツール利用時に必要です。

**入力**

商品判断は必須。必要に応じ ASIN、商品、市場、法域、期間、操作権限。任意：CSV/JSON/XLSX/PDF/画像、見積、事業条件。不明事項は不足として残します。

**出力**

route-plan.json、共通根拠契約、Skill と順序、不足項目、成果先。振り分け自体はインストールやサービス接続をしません。

[実行手順 · 制約と停止条件 · 依頼例](skills/amazon-product-research-suite/references/i18n/ja.md)

> 次のスキルを使用してください： `$amazon-product-research-suite` — 車載ホルダーを市場、レビュー、差別化、供給者、採算の順に調べ、外観資料があれば意匠予備調査を追加します。日本語で回答し、根拠、不明点、操作権限を維持してください。

## 供給者の実現性と試作判定

`amazon-supplier-feasibility`

RFQ、見積の同条件比較、根拠付き試作品合格基準を作成します。標準では工場連絡や発注をしません。

スキルディレクトリ: `skills/amazon-supplier-feasibility`

**実装の根拠と依存関係**

製品仕様が必須。比較には日付付きの比較可能な見積が必要です。規制、試作品、通信権限は条件付きで確認し、工場への連絡には別途許可が必要です。

**入力**

単位・公差付き仕様や図面、数量・需要仮定。条件付き：通貨、Incoterm、金型予算、支払条件。任意：PDF/XLSX/CSV 見積、品質資料。

**出力**

RFQ、費用・納期比較、製造リスク表、試験計画。状態は READY_FOR_RFQ、READY_FOR_SAMPLE、CONDITIONAL、INSUFFICIENT_EVIDENCE。

[実行手順 · 制約と停止条件 · 依頼例](skills/amazon-supplier-feasibility/references/i18n/ja.md)

> 次のスキルを使用してください： `$amazon-supplier-feasibility` — ホルダーの磁石等級、接着剤、トルク、温度試験、金型所有、包装をそろえて見積を比較します。日本語で回答し、根拠、不明点、操作権限を維持してください。

## 単位採算と初回資金

`amazon-unit-economics-cashflow`

明示した仮定から限界利益、広告損益分岐点、返品感度、初回必要資金を計算します。

スキルディレクトリ: `skills/amazon-unit-economics-cashflow`

**実装の根拠と依存関係**

数値の価格・原価と根拠ある市場手数料が必要です。標準ライブラリ計算器は Python 3.10+。資金分析には注文数量と支払時期も必要です。

**入力**

JSON：価格、販売・配送手数料、着地原価、返品率・損失、広告 ACOS、その他変動費。資金には数量、金型、準備費、前金、余裕資金。単一通貨、率は0～1。

**出力**

利益・利益率、損益分岐 ACOS、返品損失、初回資金、シナリオの JSON または指定ファイル。不正入力は非ゼロ終了、通信・アカウント操作なし。

[実行手順 · 制約と停止条件 · 依頼例](skills/amazon-unit-economics-cashflow/references/i18n/ja.md)

> 次のスキルを使用してください： `$amazon-unit-economics-cashflow` — 提供されたホルダー価格・原価で返品率と ACOS を比較し、利益と初回資金を併記します。日本語で回答し、根拠、不明点、操作権限を維持してください。

## 言語対応と検証

本書は目的、前提、入出力、手順、例、制約をまとめた日本語運用ガイドです。全参考資料の逐語訳ではありません。詳細技術資料、過去事例、スクリプトのエラー、サンプル画面、画像は原言語のままです。必要に応じて日本語で説明できます。構造・リンク・重要制約を確認していますが、各言語の母語話者による校閲は未実施です。

納品前に入力、根拠、欠損、出力ファイルと元の完了条件を照合します。未実行の工程は未検証とし、終了コードの成功を業務上の検証成功と混同しません。
