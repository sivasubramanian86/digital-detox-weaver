# 🚀 Deploy Your Live Dashboard NOW

## Step 1: Install Google Cloud CLI
Download and install: https://cloud.google.com/sdk/docs/install

## Step 2: Login and Setup
```bash
# Login to Google Cloud
gcloud auth login

# Set your project (create one if needed)
gcloud config set project YOUR_PROJECT_ID

# Enable required services
gcloud services enable run.googleapis.com cloudbuild.googleapis.com
```

## Step 3: Deploy with ONE Command
```bash
cd c:\Users\USER\OneDrive\Documents\digital-detox-weaver

gcloud run deploy digital-detox-weaver \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080 \
  --memory 2Gi \
  --set-env-vars GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

## 🎯 What Happens Next:
1. **Cloud Build** builds your Docker image
2. **Cloud Run** deploys your app
3. **You get a live URL** like: `https://digital-detox-weaver-xyz-uc.a.run.app`

## ⚡ Alternative: Railway (Faster Setup)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway link
railway up

# Add environment variable
railway variables set GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

## 🔥 Fastest Option: Render
1. Go to https://render.com
2. Connect GitHub repo: `sivasubramanian86/digital-detox-weaver`
3. Add environment variable: `GEMINI_API_KEY`
4. Deploy!

Your dashboard will be live in 5-10 minutes! 🎉