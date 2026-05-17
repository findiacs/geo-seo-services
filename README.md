<p align="center">
  <img src="assets/banner.svg" alt="AI Visibility Intelligence Infrastructure" width="900"/>
</p>

<p align="center">
  <strong>AI Discoverability Infrastructure.</strong> Proprietary AI visibility intelligence assessment system<br/>
  (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) while maintaining foundational discovery accessibility.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Supported-blue?style=for-the-badge&logo=anthropic" alt="Claude Code Supported"/>
  <img src="https://img.shields.io/badge/Gemini_CLI-Supported-blue?style=for-the-badge&logo=google" alt="Gemini CLI Supported"/>
  <img src="https://img.shields.io/badge/Codex_CLI-Supported-blue?style=for-the-badge&logo=openai" alt="Codex CLI Supported"/>
  <img src="https://img.shields.io/badge/OpenCode-Supported-blue?style=for-the-badge" alt="OpenCode Supported"/>
  <img src="https://img.shields.io/badge/Antigravity_IDE-Supported-blue?style=for-the-badge" alt="Antigravity IDE Supported"/>
</p>

---

## 1. Executive Introduction

An AI Visibility Intelligence platform designed to assess how modern AI systems interpret, trust, and recommend businesses across digital discovery environments.

This executive-grade platform operates as a specialized intelligence infrastructure. It evaluates discoverability, recommendation readiness, AI perception gaps, and the underlying trust infrastructure necessary for entity inclusion in LLM-mediated discovery.

## 2. Platform Positioning

The platform transcends legacy search optimization by mapping the specific pathways AI models utilize to construct knowledge graphs. It answers a critical strategic question: *How do foundational models perceive and cite this entity?*

| Metric | Value |
|--------|-------|
| AI Visibility services market | $850M+ (projected $7.3B by 2031) |
| AI-referred traffic growth | +527% year-over-year |
| AI traffic conversion rate vs organic | 4.4x higher |
| Brand mentions vs backlinks for AI | 3x stronger correlation |
| Marketers investing in AI Discoverability | Only 23% |

## 3. Core Intelligence Capabilities

The intelligence layer is capable of conducting deep diagnostic sweeps across multiple visibility vectors:

- **AI Discoverability Assessments:** Comprehensive evaluations of how an entity is processed by LLM architectures.
- **Recommendation Readiness Analysis:** Scoring content blocks for AI citation extraction readiness and fact-density.
- **AI Trust Signal Evaluation:** Correlating distributed brand mentions across high-trust AI-cited platforms (e.g., YouTube, Reddit, LinkedIn).
- **Discovery Accessibility Diagnostics:** Analyzing server-side rendering pipelines and AI-crawler access controls to ensure seamless ingestion.
- **Explainability Infrastructure:** Validating and structuring entity-relationship data (JSON-LD) for precise model interpretation.

## 4. Assessment & Reporting Layer

The system aggregates visibility diagnostics into premium, institutional decision-oriented intelligence reports.

These outputs translate underlying capability gaps into a deterministic **AI Discoverability Readiness** score, framing technical deficiencies as business consequence and infrastructure risk. Reports are generated in both markdown and executive-ready PDF formats, featuring score gauges, platform readiness visualizations, and prioritized visibility remediation paths.

## 5. AI Visibility Infrastructure Assets

Beyond assessment, the system generates targeted remediation files designed to reinforce AI perception:
- Validated `llms.txt` schema files to guide crawler ingestion.
- Machine-readable structured data architectures mapping entity relationships.
- Targeted adjustments to crawler access governance.

## 6. Operational Architecture

The platform coordinates specialized parallel agents to handle distinct visibility vectors simultaneously without exposing complex underlying orchestration to the end-user.

```text
ai-visibility-intelligence/
├── geo/                          # Intelligence orchestrator
├── skills/                       # Specialized assessment and reporting modules
├── agents/                       # Parallel discovery and analysis agents
├── scripts/                      # Core assessment logic, PDF generation, and scoring
├── schema/                       # Base architectural templates for entity explainability
├── install.sh                    # One-command installer
├── install-win.sh                # Windows deployment module
└── requirements.txt              # Infrastructure dependencies
```

Data privacy is strictly maintained. Pipeline records, intelligence reports, and engagement proposals are stored locally in isolated runtime directories (`~/.geo-prospects/`), ensuring client confidentiality is structurally enforced.

---

## 7. Setup / Installation

### One-Command Install (macOS/Linux)

The installation script automatically detects and installs the intelligence modules to all supported AI coding assistants on your system.

```console
curl -fsSL https://raw.githubusercontent.com/Abderraouf-yt/ai-visibility-intelligence/main/install.sh > install.sh && chmod +x install.sh && ./install.sh
```

### Manual Install

```console
git clone https://github.com/Abderraouf-yt/ai-visibility-intelligence.git
cd ai-visibility-intelligence
./install.sh
```

### Windows (Git Bash)

Requires [Git for Windows](https://git-scm.com/downloads) which includes Git Bash.

```console
# Option 1: One-command install (run from Git Bash, not PowerShell/CMD)
curl -fsSL https://raw.githubusercontent.com/Abderraouf-yt/ai-visibility-intelligence/main/install-win.sh > install-win.sh && chmod +x install-win.sh && ./install-win.sh

# Option 2: Manual install
git clone https://github.com/Abderraouf-yt/ai-visibility-intelligence.git
cd ai-visibility-intelligence
./install-win.sh
```

> **Note:** Right-click the folder and select "Open Git Bash here", or open Git Bash and navigate to the directory. Do not use PowerShell or Command Prompt.

### Requirements

- Python 3.8+ (on Debian/Ubuntu also `python3-venv`)
- Claude Code CLI
- Git
- Optional: [`uv`](https://docs.astral.sh/uv/) — for accelerated dependency resolution
- Optional: Playwright — for rendering pipeline diagnostics

### Isolated Deployment

Dependencies are installed into a dedicated virtual environment at `~/.claude/skills/geo/.venv/`. Your system environment remains untouched. Uninstallation guarantees the complete removal of the runtime environment.

---

## 8. Usage

The intelligence assessment suite is executed via the command line interface:

| Command | Capability |
|---------|-------------|
| `/geo audit <url>` | Full AI visibility intelligence assessment with parallel subagents |
| `/geo quick <url>` | 60-second discovery accessibility snapshot |
| `/geo citability <url>` | Score content for AI reference eligibility |
| `/geo crawlers <url>` | Diagnose AI crawler access governance |
| `/geo llmstxt <url>` | Analyze or generate AI interpretation files |
| `/geo brands <url>` | Scan authority signals across AI-cited platforms |
| `/geo platforms <url>` | Cross-platform discovery optimization |
| `/geo schema <url>` | Explainability infrastructure analysis & generation |
| `/geo technical <url>` | Discovery accessibility audit |
| `/geo content <url>` | Knowledge clarity & entity assessment |

---

## 9. Report Generation

To generate executive deliverables after an assessment:

| Command | Output |
|---------|-------------|
| `/geo report <url>` | Generate executive intelligence report (Markdown) |
| `/geo report-pdf` | Generate professional PDF report with intelligence visualizations |

---

## 10. Security / Confidentiality Positioning

This infrastructure is engineered for professional advisory engagements. Client pipeline data, generated intelligence reports, and engagement files remain strictly localized on the host machine.

To remove the platform and all executable logic:
```console
./uninstall.sh
```
*(Note: Client records stored in `~/.geo-prospects/` must be manually archived or deleted to prevent accidental data loss.)*

---

**Proprietary Infrastructure**
Operated and maintained by Abderraouf-yt, AI Visibility Engineer.
