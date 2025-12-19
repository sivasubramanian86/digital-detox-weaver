# Digital Detox Weaver: Orchestration Framework

## Overview

The Digital Detox Weaver orchestration framework implements **SOURCE 4** of the 4-source data integration system. This framework manages AI agent workflows, multi-LLM routing, and comprehensive analysis generation for the Kiro Challenge.

## Architecture

### 4 Data Sources Integration

1. **SOURCE 1**: Epidemiological Data Generator (800+ records, 8 datasets)
2. **SOURCE 2**: AI-Generated Insights (25,000+ words, 4 specialized agents)
3. **SOURCE 3**: Original Project Foundation (Dashboard infrastructure)
4. **SOURCE 4**: Orchestration Framework (This system)

### Multi-LLM Support

- **Primary**: Claude 3.5 Sonnet
- **Fallback**: Gemini 2.0 Flash
- **Additional**: AWS Bedrock, OpenAI (configurable)
- **Automatic failover** between providers

### 4 Specialized AI Agents

1. **Data Analyst** (T=0.3): Statistical analysis, epidemiological insights
2. **Visualization Expert** (T=0.6): Dashboard design, accessibility
3. **Health Researcher** (T=0.5): Mechanistic pathways, literature synthesis
4. **Policy Advisor** (T=0.7): Implementation strategies, cost-benefit analysis

## Quick Start

### 1. Setup Environment

```bash
# Run setup script
python setup_kiro.py

# Edit .env.local and add your Claude API key
# Get key from: https://console.anthropic.com
```

### 2. Install Dependencies

```bash
pip install -r requirements-kiro.txt
```

### 3. Run Orchestrator

```bash
# Execute complete 10-step workflow (20-30 minutes)
python kiro_main.py
```

### 4. Launch Dashboard

```bash
# In separate terminal
streamlit run app.py
# Open: http://localhost:8501
```

## Workflow Pipeline

The orchestrator executes a 10-step pipeline:

1. **Initialize Project**: Research framework and methodology
2. **Generate Data**: Execute SOURCE 1 epidemiological data generation
3. **Analyze Data**: Statistical analysis with confidence intervals
4. **Design Visualizations** (PARALLEL): 8-tab dashboard specifications
5. **Generate Health Insights** (PARALLEL): Mechanistic pathways
6. **Generate Dashboard Code**: Integrate SOURCE 3 with SOURCE 1 data
7. **Policy Recommendations**: 3-phase implementation pathway
8. **Generate Report**: 3000+ word publication-ready analysis
9. **Document Data Lineage**: Source integration verification
10. **Finalize and Deploy**: System ready for use

## Output Artifacts

After execution, check `./outputs/` for:

- `01_initialization.md`: Research framework
- `03_analysis.md`: Statistical analysis
- `04_visualization_design.md`: Chart specifications
- `05_health_insights.md`: Mechanism analysis
- `06_policy_recommendations.md`: Policy pathway
- `FINAL_REPORT.md`: Comprehensive 3000+ word report

## Configuration

### Environment Variables (.env.local)

```bash
# Primary LLM
CLAUDE_API_KEY=sk-ant-your-key-here
LLM_PROVIDER=claude
PRIMARY_MODEL=claude-3-5-sonnet-20241022

# Fallback LLM
GEMINI_API_KEY=your-gemini-key
FALLBACK_MODEL=gemini-2.0-flash

# Optional: AWS Bedrock
AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
AWS_REGION=us-east-1

# Streaming & Performance
KIRO_ENABLE_STREAMING=true
MAX_WORKERS=4
TIMEOUT_SECONDS=300
```

### Agent Temperatures

- **Data Analyst**: 0.3 (Precise, analytical)
- **Visualization Expert**: 0.6 (Creative, design-focused)
- **Health Researcher**: 0.5 (Balanced, evidence-based)
- **Policy Advisor**: 0.7 (Creative, implementation-focused)

## File Structure

```
digital-detox-weaver/
├── .kiro/                          # Orchestration framework
│   ├── config/
│   │   ├── llm_config.py          # Multi-LLM configuration
│   │   ├── agent_config.py        # 4 agent specifications
│   │   └── workflow_config.yaml   # Pipeline definition
│   ├── agents/
│   │   └── llm_router.py          # Multi-provider routing
│   ├── prompts/
│   │   └── analysis_prompts.py    # Structured prompt templates
│   └── logs/                      # Execution logs
├── outputs/                       # Generated analysis files
├── .env.example                   # Environment template
├── .env.local                     # Your API keys (create this)
├── requirements-kiro.txt          # Orchestration dependencies
├── kiro_main.py                   # Main orchestrator
└── setup_kiro.py                  # Setup verification
```

## Data Lineage Tracking

The system automatically tracks data flow:

- **Input**: SOURCE 1 epidemiological data (800+ records)
- **Processing**: Multi-agent analysis pipeline
- **Output**: 6 markdown reports + dashboard integration
- **Verification**: `.kiro/data_lineage.md` documents complete flow

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all `.kiro/` files are created
2. **API Key Issues**: Check `.env.local` configuration
3. **Streaming Errors**: Verify network connectivity
4. **Memory Issues**: Reduce `MAX_WORKERS` in `.env.local`

### Logs

Check execution logs:
```bash
tail -f .kiro/logs/workflow_execution.log
```

### Verification

Run setup verification:
```bash
python setup_kiro.py
```

## Integration with Main Project

The orchestration framework integrates with the main Digital Detox Weaver project:

1. **SOURCE 1**: Uses `data_generators.py` for epidemiological data
2. **SOURCE 2**: Generates AI analysis through this framework
3. **SOURCE 3**: Integrates with existing `app.py`, `visualizations.py`
4. **SOURCE 4**: This orchestration system

## Performance

- **Execution Time**: 20-30 minutes for complete workflow
- **Output Size**: 25,000+ words of analysis
- **Memory Usage**: ~2GB during peak execution
- **API Calls**: ~50-100 LLM requests with streaming

## Success Metrics

✅ **Complete Integration**: All 4 data sources operational
✅ **AI Analysis**: 25,000+ words generated
✅ **Dashboard Ready**: 8-tab interface functional
✅ **Data Lineage**: Source integration documented
✅ **Production Ready**: Comprehensive documentation

## Support

For issues or questions:
1. Check logs in `.kiro/logs/`
2. Verify setup with `python setup_kiro.py`
3. Review configuration in `.env.local`
4. Check API key validity and quotas