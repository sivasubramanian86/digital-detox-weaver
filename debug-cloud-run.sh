#!/bin/bash
# Debug Cloud Run deployment

echo "🔍 Checking Cloud Run logs..."

# Get recent logs
gcloud run services logs tail digital-detox-weaver --region=us-central1 --limit=50

echo ""
echo "🔍 Checking service configuration..."

# Get service details
gcloud run services describe digital-detox-weaver --region=us-central1 --format="export"