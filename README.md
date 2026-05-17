# AI Visibility Intelligence

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status Active"/>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License MIT"/>
</p>

## AI Visibility Assessment Infrastructure

AI Visibility Intelligence platform for assessing how modern AI systems interpret, trust, and recommend businesses across digital discovery environments.

The platform provides comprehensive readiness assessments to ensure brand discoverability across large language models, AI search engines, and emerging conversational discovery platforms.

---

## Strategic Significance

| Metric | Context |
|--------|---------|
| Emerging Discoverability | Rapid shifts in user discovery toward conversational AI interfaces. |
| AI-referred Traffic | Increasing importance of structured data and entity recognition for AI models. |
| Visibility Benchmarks | Brand mentions and semantic relevance correlate strongly with AI retrieval. |
| Authority Signals | Demonstrable expertise and clear structural context influence recommendation algorithms. |

---

## Deployment Options

### One-Command Deployment (macOS/Linux)

The installation script automatically detects and installs the necessary components.

```shell
curl -fsSL https://raw.githubusercontent.com/findiacs/ai-visibility-intelligence/main/install.sh | source /dev/stdin
```

### Manual Deployment

```shell
git clone https://github.com/findiacs/ai-visibility-intelligence.git
cd ai-visibility-intelligence
./install.sh
```

### Windows Shell

Requires Git for Windows.

```shell
# Option 1: One-command deployment
curl -fsSL https://raw.githubusercontent.com/findiacs/ai-visibility-intelligence/main/install-win.sh | source /dev/stdin

# Option 2: Manual deployment
git clone https://github.com/findiacs/ai-visibility-intelligence.git
cd ai-visibility-intelligence
./install-win.sh
```

### Requirements

- Python 3.8+ (on Debian/Ubuntu also `python3-venv`)
- Git
- Optional: `uv` — if present, the installer uses it for faster dependency installation
- Optional: Playwright (for execution requiring rendering)

### Isolated Environment

Python dependencies are installed into a dedicated virtual environment at
`~/.claude/skills/geo/.venv/`. Your system Python is **not** touched, and
uninstalling the platform removes the venv together with the rest of the files.

---

## Intelligence Modules

| Module | Execution |
|---------|-------------|
| **Comprehensive Analysis** | Full visibility and readiness assessment across all vectors. |
| **Visibility Snapshot** | Rapid assessment of current AI discoverability. |
| **Retrieval Readiness** | Score content structure for AI citation compatibility. |
| **Crawler Access** | Validate AI bot access protocols and restrictions. |
| **Contextual Directives** | Analyze or generate `llms.txt` standard files. |
| **Entity Recognition** | Scan brand presence across platforms heavily weighted by AI models. |
| **Platform Readiness** | Optimization assessment for specific AI discovery platforms. |
| **Structural Context** | Structured data analysis and validation. |
| **Technical Assessment** | Technical foundation analysis for optimal machine readability. |
| **Authority Analysis** | Content quality, structure, and E-E-A-T alignment. |
| **Intelligence Report** | Generate comprehensive executive assessment report. |

---

## System Architecture

```text
ai-visibility-intelligence/
├── geo/                          # Primary orchestrator
│   └── SKILL.md                  # Routing definitions
├── skills/                       # Specialized intelligence modules
│   ├── geo-audit/                # Comprehensive assessment
│   ├── geo-citability/           # Retrieval Readiness scoring
│   ├── geo-crawlers/             # Crawler access analysis
│   ├── geo-llmstxt/              # Contextual directive management
│   ├── geo-brand-mentions/       # Entity recognition scanning
│   ├── geo-platform-optimizer/   # Platform-specific optimization
│   ├── geo-schema/               # Structural context analysis
│   ├── geo-technical/            # Technical foundation assessment
│   ├── geo-content/              # Authority and structural analysis
│   ├── geo-report/               # Executive summary generation
│   ├── geo-report-pdf/           # Formal intelligence report generation
│   ├── geo-prospect/             # Pipeline management
│   ├── geo-proposal/             # Proposal generation
│   └── geo-compare/              # Longitudinal delta tracking
├── agents/                       # Parallel processing units
│   ├── geo-ai-visibility.md      # Visibility and entity processing
│   ├── geo-platform-analysis.md  # Platform readiness processing
│   ├── geo-technical.md          # Technical analysis processing
│   ├── geo-content.md            # Content and authority processing
│   └── geo-schema.md             # Structural data processing
├── scripts/                      # Core analytical utilities
│   ├── fetch_page.py             # Acquisition engine
│   ├── citability_scorer.py      # Retrieval readiness logic
│   ├── brand_scanner.py          # Entity presence detection
│   ├── llmstxt_generator.py      # Contextual directive logic
│   └── generate_pdf_report.py    # Report rendering engine
├── schema/                       # Structural templates
│   ├── organization.json
│   ├── local-business.json
│   ├── article-author.json
│   ├── software-saas.json
│   ├── product-ecommerce.json
│   └── website-searchaction.json
├── install.sh                    # Deployment utility
├── uninstall.sh                  # Teardown utility
├── requirements.txt              # Environment dependencies
└── README.md                     # Documentation
```

---

## Data Segregation

The system stores operational data locally, segregated from the execution codebase:

```text
~/.geo-prospects/
├── prospects.json              # Assessment pipeline state
├── proposals/                  # Generated documentation
└── reports/                    # Intelligence summaries
```

This directory is preserved during standard teardown procedures.

---

## Operational Workflow

### Comprehensive Assessment Sequence

1. **Discovery & Ingestion** — Validates endpoint, determines structural taxonomy, analyzes topology.
2. **Parallel Processing** — Engages analytical sub-systems:
   - Visibility & Entity Readiness
   - Discovery Platform Compatibility
   - Technical Foundation
   - Structural & Authority Assessment
   - Schema & Metadata Validation
3. **Synthesis** — Aggregates metrics and determines composite readiness scoring.
4. **Executive Reporting** — Outputs prioritized strategic and technical recommendations.

---

## Key Capabilities

### Retrieval Readiness Evaluation
Analyzes content structures for compatibility with AI extraction models, favoring self-contained, high-density informational blocks.

### Crawler Protocol Validation
Validates access configurations across major AI ingestion bots to ensure appropriate indexing while preserving security posture.

### Entity Presence Detection
Assesses brand footprint across authoritative domains frequently utilized as training data or live-retrieval sources by AI models.

### Contextual Directives (`llms.txt`)
Supports the implementation of standardized contextual files that guide AI understanding of organizational structures and data hierarchies.

### Executive Reporting
Generates professional assessments, detailing readiness scores, platform compatibility, and strategic technical recommendations.

---

## Application Scenarios

- **Strategic Assessment** — Evaluate organizational readiness for emerging AI search modalities.
- **Brand Intelligence** — Monitor how language models perceive and represent specific entities.
- **Technical Validation** — Ensure optimal machine readability of critical digital assets.
- **Platform Strategy** — Align digital infrastructure with conversational discovery requirements.

---

## Teardown

```shell
./uninstall.sh
```

---

## License

MIT License

---

Proprietary Intelligence Infrastructure.
