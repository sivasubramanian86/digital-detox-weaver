#!/bin/bash
# Google Cloud Run Deployment Script

echo "🚀 Deploying Digital Detox Weaver to Google Cloud Run..."

# Set project ID (replace with your project)
PROJECT_ID="your-gcp-project-id"
SERVICE_NAME="digital-detox-weaver"
REGION="us-central1"

# Build and deploy
gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME

gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --port 8080 \
  --memory 2Gi \
  --cpu 1 \
  --set-env-vars GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE

echo "✅ Deployment complete!"
echo "🌐 Your app will be available at:"
gcloud run services describe $SERVICE_NAME --region=$REGION --format="value(status.url)"