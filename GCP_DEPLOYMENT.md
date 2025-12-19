# Google Cloud Run Deployment Guide

## 🚀 Quick Deploy to Google Cloud Run

### Prerequisites
1. **Google Cloud Account** with billing enabled
2. **gcloud CLI** installed: https://cloud.google.com/sdk/docs/install
3. **Docker** installed (optional - Cloud Build handles this)

### Step 1: Setup Google Cloud Project
```bash
# Login to Google Cloud
gcloud auth login

# Create new project (or use existing)
gcloud projects create digital-detox-weaver-demo
gcloud config set project digital-detox-weaver-demo

# Enable required APIs
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
```

### Step 2: Deploy with One Command
```bash
# Deploy directly from source
gcloud run deploy digital-detox-weaver \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080 \
  --memory 2Gi \
  --set-env-vars GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

### Step 3: Access Your Live Dashboard
After deployment, you'll get a URL like:
```
https://digital-detox-weaver-[hash]-uc.a.run.app
```

## 🔧 Alternative: Using Cloud Build
```bash
# Submit build
gcloud builds submit --tag gcr.io/PROJECT_ID/digital-detox-weaver

# Deploy from image
gcloud run deploy digital-detox-weaver \
  --image gcr.io/PROJECT_ID/digital-detox-weaver \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## 💰 Cost Estimate
- **Free Tier**: 2 million requests/month
- **Typical Cost**: $0.10-$2.00/month for demo usage
- **Auto-scaling**: Scales to zero when not in use

## 🎯 Benefits of Google Cloud Run
✅ **Reliable**: Enterprise-grade infrastructure
✅ **Fast**: Cold start < 2 seconds
✅ **Scalable**: Auto-scales 0 to 1000+ instances
✅ **Cost-effective**: Pay only for requests
✅ **Secure**: HTTPS by default

## 🔍 Monitoring & Logs
```bash
# View logs
gcloud run services logs tail digital-detox-weaver --region=us-central1

# Get service info
gcloud run services describe digital-detox-weaver --region=us-central1
```

## 🚨 Troubleshooting
- **Build fails**: Check Dockerfile and requirements.txt
- **App crashes**: Check logs with command above
- **API errors**: Verify GEMINI_API_KEY is set correctly