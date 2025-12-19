# 🧹 Clean Repository Setup Guide

## 🚨 CRITICAL: Complete Git History Cleanup Required

Your repository currently has API keys exposed in git history. This guide will help you create a completely clean repository.

## 🔥 Nuclear Option (Recommended)

### Step 1: Run the Cleanup Script
```bash
# Windows
NUCLEAR_CLEANUP.bat

# Or manually:
git branch backup-original-history
git update-ref -d HEAD
git add .
git commit -m "Initial commit - Digital Detox Weaver (clean history)"
```

### Step 2: Force Push Clean History
```bash
git push --force-with-lease origin main
```

## 🆕 Alternative: Create New Repository

If the nuclear option doesn't work, create a completely new repository:

### Step 1: Create New GitHub Repository
1. Go to GitHub and create a new repository: `digital-detox-weaver-clean`
2. **DO NOT** initialize with README, .gitignore, or license

### Step 2: Prepare Clean Local Copy
```bash
# Create new directory
mkdir digital-detox-weaver-clean
cd digital-detox-weaver-clean

# Initialize new git repo
git init
git branch -M main

# Copy only clean files (excluding problematic ones)
# Copy from your current directory, but skip:
# - SECURITY_CLEANUP.md
# - clean-git-history.sh  
# - replacements.txt
# - Any files with API keys
```

### Step 3: Set Up Clean Repository
```bash
# Add clean files
git add .
git commit -m "feat: Digital Detox Weaver - Production-ready health analytics platform

- 4-source data integration (epidemiological, AI, dashboard, orchestration)
- 8-tab interactive Streamlit dashboard  
- Multi-LLM routing with failover (Claude, Gemini, AWS, OpenAI)
- 25,000+ words of AI-generated analysis
- Production-grade security and deployment configs
- Complete Kiro Challenge submission"

# Connect to new remote
git remote add origin https://github.com/yourusername/digital-detox-weaver-clean.git
git push -u origin main
```

## ✅ Verification Checklist

After cleanup, verify:

- [ ] No API keys in any file
- [ ] `.env.local` is gitignored
- [ ] `.env.example` has placeholders only
- [ ] `SECURITY.md` has proper guidelines
- [ ] All deployment scripts use environment variables
- [ ] GitHub secret scanning shows no alerts

## 🔒 Security Best Practices Going Forward

### 1. Environment Variables Only
```bash
# .env.local (gitignored)
GEMINI_API_KEY=your-actual-key-here
CLAUDE_API_KEY=your-actual-key-here
```

### 2. Pre-commit Hooks
```bash
pip install pre-commit detect-secrets
pre-commit install
```

### 3. GitHub Settings
- Enable secret scanning
- Enable push protection
- Set up security alerts

## 🚨 IMMEDIATE ACTIONS

1. **Revoke exposed API keys** in Google AI Studio/Anthropic Console
2. **Generate new API keys**
3. **Run cleanup script** or create new repository
4. **Update deployment configs** with new keys
5. **Enable GitHub security features**

## 📞 Support

If you encounter issues:
1. Check GitHub's guide on removing sensitive data
2. Use BFG Repo Cleaner for complex cases
3. Contact GitHub support for persistent issues

---

**Remember**: Once something is in git history, assume it's compromised. Always revoke and regenerate exposed credentials.