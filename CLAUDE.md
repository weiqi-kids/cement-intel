# Cement Intel - 水泥供應鏈情報追蹤

## 專案狀態：初始化完成

### 系統架構

| 模組 | 說明 | 狀態 |
|------|------|------|
| **新聞爬蟲** | 待建立，涵蓋 16 家公司 | 待開發 |
| **規則引擎** | 關鍵字匹配、情緒分析、重要性評分、異常偵測 | 已設定 |
| **報告生成** | 每日報告、7 日報告 | 待測試 |
| **前端** | Dashboard | 待客製化 |
| **CI/CD** | daily-ingest.yml + deploy-pages.yml | 待設定 |

### 追蹤範圍

#### 公司 (16 家)

**上游 - 骨料/設備** (4 家)
- Vulcan Materials (骨料)
- Martin Marietta (骨料)
- Eagle Materials (水泥+石膏)
- thyssenkrupp 蒂森克虜伯 (設備)

**中游 - 水泥製造** (11 家)
- Holcim, CRH, CEMEX, Heidelberg Materials 海德堡材料
- Taiwan Cement 台泥, Asia Cement 亞泥
- Anhui Conch 海螺水泥, UltraTech
- Taiheiyo Cement 太平洋水泥, Siam Cement, CNBM 中國建材

**下游 - 銷售** (1 家)
- Asia Cement China 亞泥中國

**ETFs**: IGF, PKB

#### 主題 (10 個)

- 水泥價格、基建支出、碳排放
- 產能整合、原料能源成本
- 產能、財報、展望、資本支出、庫存

---

## 標準流程

```
fetch_news → enrich_event → generate_metrics → detect_anomalies →
generate_daily → generate_7d_report → update_baselines → deploy
```

## 快速啟動

```bash
cd repos/cement-intel
source .venv/bin/activate

# 啟動本地伺服器
python3 -m http.server 8000 -d site

# 瀏覽器開啟
open http://localhost:8000
```

## 資料夾結構

```
cement-intel/
├── lib/                        # 規則引擎
├── scripts/                    # 執行腳本
├── configs/                    # 設定檔
│   ├── companies.yml           # 16 家公司 + 上下游關係
│   ├── topics.yml              # 10 個主題 + 關鍵字
│   ├── site.yml                # 網站設定
│   ├── sentiment_rules.yml     # 情緒詞典
│   ├── importance_rules.yml    # 重要性規則
│   ├── anomaly_rules.yml       # 異常偵測規則
│   └── 7d_highlights_rules.yml # 7 日報告規則
├── fetchers/                   # 公司新聞爬蟲（待建立）
├── data/
│   ├── raw/                    # 原始抓取資料
│   ├── events/                 # 標準格式事件
│   ├── metrics/                # 每日指標
│   ├── baselines/              # 歷史基準線
│   ├── normalized/             # 股價資料
│   ├── financials/             # 財務數據
│   ├── holders/                # 持股資料
│   └── fund_flow/              # 資金流向
├── reports/
│   ├── daily/                  # 每日報告
│   └── 7d/                     # 7 日報告
├── site/
│   ├── index.html              # Dashboard
│   └── data/                   # 前端資料
└── CLAUDE.md
```

## 下一步

1. 建立各公司爬蟲 (`fetchers/*.py`)
2. 測試規則引擎標註
3. 設定 GitHub Actions
4. 客製化前端 Dashboard
