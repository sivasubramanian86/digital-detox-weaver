# Live Dashboard Deployment Options

## 🎯 Quick Deploy (Choose One)

### 1. Streamlit Cloud ⭐ (Easiest)
```bash
# Already configured - just deploy at:
# https://share.streamlit.io
# Repository: sivasubramanian86/digital-detox-weaver
# Add GEMINI_API_KEY in secrets
```

### 2. Railway 🚂 (Most Reliable)
```bash
npm install -g @railway/cli
railway login
railway link sivasubramanian86/digital-detox-weaver
railway up
# Add GEMINI_API_KEY environment variable
```

### 3. Hugging Face Spaces 🤗 (AI-Focused)
```bash
# Create new Space at: https://huggingface.co/spaces
# Type: Streamlit
# Upload: streamlit_app.py + requirements.txt
# Add GEMINI_API_KEY in settings
```

### 4. Google Cloud Run ☁️ (Enterprise)
```bash
gcloud run deploy digital-detox-weaver \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## 🔑 Required Environment Variables
- `GEMINI_API_KEY`: Your Google AI API key
- `LLM_PROVIDER`: Set to "gemini"

## 📊 Dashboard Features
✅ 8 Interactive Tabs
✅ Real-time Data Generation  
✅ AI Report Integration
✅ Modern Dark Theme
✅ Mobile Responsive
✅ Plotly Visualizations

## 🎉 Live URLs (Once Deployed)
- **Streamlit Cloud**: `https://digital-detox-weaver.streamlit.app`
- **Railway**: `https://digital-detox-weaver.railway.app`  
- **HF Spaces**: `https://huggingface.co/spaces/username/digital-detox-weaver`