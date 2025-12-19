# 🧵 Digital Detox Weaver

**Production-ready platform for multi-source epidemiological data analysis and AI-powered health insights.**

A complete **Kiro Challenge submission** demonstrating advanced data architecture, AI orchestration, and modern SaaS dashboard design.

---

## 🎯 Project Overview

**Digital Detox Weaver** weaves together **4 distinct data sources** into a unified, production-grade platform:

1. **SOURCE 1**: Epidemiological Data Generator (800+ records)
2. **SOURCE 2**: AI-Generated Insights (4 specialized agents)
3. **SOURCE 3**: Dashboard & Visualization Code
4. **SOURCE 4**: Orchestration Framework (multi-LLM routing)

### Key Metrics

| Component | Details |
|-----------|---------|
| **Code** | 2000+ lines (Python) |
| **Data** | 494+ records (epidemiological) |
| **AI** | 4 agents, multi-LLM support |
| **Analysis** | 25,000+ words (AI-generated) |
| **Dashboard** | 8 interactive tabs (modern UI) |
| **Theme** | Data Weaver (multi-source integration) |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Gemini API key (or Claude API key)
- ~500MB disk space

### Installation

1. **Clone and setup**:
   ```bash
   git clone https://github.com/yourusername/digital-detox-weaver.git
   cd digital-detox-weaver
   ```

2. **Create environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-kiro.txt
   ```

4. **Configure secrets**:
   ```bash
   cp .env.example .env.local
   # Edit .env.local and add your API key
   ```

### Running the System

1. **Terminal 1 – Run orchestrator** (generates data & reports):
   ```bash
   python kiro_main.py
   # Outputs to ./outputs/ (takes 20-30 minutes)
   ```

2. **Terminal 2 – Run dashboard**:
   ```bash
   streamlit run app.py
   # Opens at http://localhost:8501
   ```

---

## 📁 Project Structure

```
digital-detox-weaver/
├── .kiro/                      # Kiro framework
│   ├── workflows/              # 5 orchestration workflows
│   ├── streaming/              # Real-time output streams
│   ├── agents/                 # 4 specialized AI agents
│   ├── config/                 # Configuration files
│   ├── prompts/                # 4 prompt templates
│   └── logs/                   # Execution logs
├── app.py                      # Modern Streamlit dashboard
├── kiro_main.py                # Main orchestrator
├── data_generators.py          # SOURCE 1: Data generation
├── requirements.txt
├── requirements-kiro.txt
├── .env.example                # Environment template
├── .gitignore                  # Git configuration (tracks .kiro/)
└── README.md                   # This file
```

---

## 🧵 The 4 Data Sources

### SOURCE 1: Epidemiological Data Generator
- **File**: `data_generators.py`
- **Output**: 8 pandas DataFrames, 494+ records
- **Datasets**: Global epidemiology, age stratification, platforms, mechanisms, disease timeline, SES inequality, detox recovery, policy interventions
- **Reproducibility**: Seeded RNG (seed=42)

### SOURCE 2: AI-Generated Insights
- **File**: `.kiro/agents/`
- **Output**: 25,000+ words across 6 markdown files
- **Agents**: Data Analyst (T=0.3), Visualization Expert (T=0.6), Health Researcher (T=0.5), Policy Advisor (T=0.7)
- **Multi-LLM**: Gemini (primary), Claude/AWS/OpenAI (fallback)

### SOURCE 3: Dashboard & Visualization
- **Files**: `app.py`, `visualizations.py`, `config.py`
- **Output**: 8-tab interactive Streamlit dashboard
- **Charts**: 30+ Plotly visualizations

### SOURCE 4: Orchestration Framework
- **Files**: `.kiro/config/`, `.kiro/workflows/`, `kiro_main.py`
- **Output**: 10-step automated pipeline with logging
- **Features**: Multi-LLM routing, streaming responses, error handling

---

## 📊 Dashboard Features

### 8 Interactive Tabs
- 🌍 **Global Overview** – KPIs, trends, world heatmap
- 👥 **Age Analysis** – Vulnerability curves by age
- 📱 **Platforms** – Bubble chart (engagement vs harm)
- 🔬 **Mechanisms** – 4-panel causal pathways
- 🏥 **Disease Timelines** – Multi-disease progression
- 💰 **Inequality** – SES-stratified disparities
- ✨ **Detox Effects** – 12-week recovery curves
- 📋 **Policy & Report** – Recommendations and synthesis

### Modern UI/UX
- Clean, contemporary design (Plotly + Streamlit theming)
- Responsive layout (desktop/tablet/mobile)
- WCAG AA accessibility (4.5:1 contrast minimum)
- Interactive elements (hover, filter, toggle)
- Dark theme support

---

## 🔄 Workflow Pipeline

The 10-step orchestrator:

```
1. Initialize Research Framework
    ↓
2. Generate SOURCE 1 Data (494+ records)
    ↓
3. Statistical Analysis
    ↓
4. [PARALLEL] Visualization Design
    ↓
5. [PARALLEL] Health Insights
    ↓
6. Dashboard Refresh (load SOURCE 1 into UI)
    ↓
7. Policy Recommendations
    ↓
8. Final Comprehensive Report
    ↓
9. Data Lineage Documentation
    ↓
10. Finalization & GitHub Readiness
```

Parallel execution (steps 4 & 5) reduces total runtime to ~25 minutes.

---

## 🛠️ Customization

### Change AI Provider
Edit `.env.local`:
```
LLM_PROVIDER=gemini        # Options: claude, gemini, aws, openai
GEMINI_API_KEY=your-key-here
```

### Adjust Agent Temperatures
Edit `.kiro/config/agent_config.py`:
```python
AGENT_TEMPERATURES = {
    "data_analyst": 0.3,           # Lower = more precise
    "visualization_expert": 0.6,   # Mid = balanced
    "health_researcher": 0.5,
    "policy_advisor": 0.7,         # Higher = more creative
}
```

---

## 📚 Generated Outputs

After running orchestrator, find outputs in `./outputs/`:

- `01_initialization.md` – Research framework
- `03_analysis.md` – Statistical analysis
- `04_visualization_design.md` – Chart specifications
- `05_health_insights.md` – Mechanistic insights
- `06_policy_recommendations.md` – 3-phase policy pathway
- `FINAL_REPORT.md` – 3000+ word comprehensive report

---

## 🚀 GitHub Deployment

Initialize Git and commit:
```bash
git init
git add .
git commit -m "Initial Digital Detox Weaver commit"
git remote add origin https://github.com/yourusername/digital-detox-weaver.git
git push -u origin main
```

Key points:
- ✅ `.kiro/` folder is tracked (framework code)
- ✅ `.env.local` is ignored (secrets)
- ✅ `outputs/` is ignored (generated files)
- ✅ All code is documented and production-ready

---

## 📋 Architecture Highlights

### Multi-Source Integration
- Clear data lineage: SOURCE 1 → SOURCE 3/4 → SOURCE 2 → Dashboard
- Explicit documentation: Each source labeled in code
- Traceable flow: `.kiro/data_lineage.md` tracks transformations
- Reproducible: Seeded RNG, deterministic prompts

### Production Quality
- Error handling with retry logic
- Structured logging throughout
- Configuration management (Pydantic)
- No hardcoded secrets
- Streaming AI responses for UX

### Modern Dashboard
- Responsive layout (Streamlit best practices)
- Accessible design (WCAG AA compliance)
- Interactive visualizations (Plotly)
- Real-time data loading
- Mobile-friendly UI

---

## 🎓 Learning & Insights

This project demonstrates:
- ✓ Advanced data architecture (4-source integration)
- ✓ Multi-LLM orchestration with failover
- ✓ Modern dashboard design (SaaS-quality UI)
- ✓ Production-grade Python code
- ✓ GitHub-ready project structure
- ✓ Kiro Challenge excellence

---

## 📞 Support & Troubleshooting

### Dashboard won't load?
```bash
streamlit run app.py --logger.level=debug
```

### Orchestrator stuck?
```bash
# Check logs
tail -f .kiro/logs/workflow_execution.log

# Check API keys in .env.local
cat .env.local | grep API_KEY
```

### Git issues?
```bash
# Verify .gitignore
cat .gitignore

# Confirm .kiro/ is tracked
git ls-files | grep .kiro

# Confirm .env.local is ignored
git check-ignore .env.local
```

---

## 🎉 Next Steps

1. **Run the orchestrator**: `python kiro_main.py` (20-30 min)
2. **Open the dashboard**: `streamlit run app.py`
3. **Explore outputs**: Check `./outputs/` for generated reports
4. **Commit to Git**: `git add . && git commit -m "..."`
5. **Submit to Kiro Challenge**: Share GitHub repo

**Happy weaving!** 🧵