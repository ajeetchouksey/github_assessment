# AI Assessment with Intelligent Fallback - Setup Guide

## Overview

This enhanced workflow provides **intelligent AI fallback** for repository assessments:

1. **🥇 Claude Sonnet 3.5** (Preferred - Best analysis quality)
2. **🥈 OpenAI GPT-4** (Fallback - Excellent alternative)  
3. **🥉 GitHub Copilot** (Future integration - When available)

The workflow automatically detects available AI providers and uses the best one available, ensuring your assessments always run successfully.

## Quick Setup

### Step 1: Configure AI API Keys (Choose One or More)

**Option A: Claude (Recommended)**
```
Repository Settings → Secrets → New secret
Name: ANTHROPIC_API_KEY
Value: [Your Claude API key from console.anthropic.com]
```

**Option B: OpenAI (Great Fallback)**
```
Repository Settings → Secrets → New secret  
Name: OPENAI_API_KEY
Value: [Your OpenAI API key from platform.openai.com]
```

**Option C: Both (Best Coverage)**
- Configure both secrets above
- Workflow will prefer Claude, fallback to OpenAI automatically

### Step 2: Deploy the Workflow

1. **Replace the old workflow file**:
   - Delete: `.github/workflows/claude-assessment.yml`
   - Use: `.github/workflows/ai-assessment-with-fallback.yml`

2. **Commit and push** the new workflow file

### Step 3: Test the Setup

**Manual Test:**
```
Actions → AI Repository Assessment → Run workflow

Settings:
✅ Assessment Type: comprehensive
✅ AI Preference: claude-preferred  
✅ Output Version: 1.0.0
```

## AI Provider Preferences

### claude-preferred (Default)
- **Priority**: Claude → OpenAI → GitHub
- **Best for**: Comprehensive analysis, technical accuracy
- **Fallback**: Automatic to OpenAI if Claude unavailable

### openai-preferred
- **Priority**: OpenAI → Claude → GitHub  
- **Best for**: Consistent formatting, cost optimization
- **Fallback**: Automatic to Claude if OpenAI unavailable

### auto-detect-best
- **Priority**: Dynamic based on availability
- **Best for**: Maximum reliability, any API key works
- **Fallback**: Uses any working provider

## Cost Comparison

**Per Assessment (Estimated):**

| Provider | Small Repo | Medium Repo | Large Repo |
|----------|------------|-------------|------------|
| Claude 3.5 Sonnet | $3-5 | $8-12 | $15-25 |
| OpenAI GPT-4 | $2-4 | $6-10 | $12-20 |

**💡 Tip**: Use OpenAI for frequent assessments, Claude for critical reviews

## Benefits of This Approach

### ✅ Reliability
- **Never fails**: Always has a working AI provider
- **Automatic fallback**: No manual intervention needed
- **Graceful degradation**: Best available option always used

### ✅ Flexibility  
- **Multiple providers**: Choose based on your subscriptions
- **Cost optimization**: Use cheaper provider for routine checks
- **Quality optimization**: Use Claude for important assessments

### ✅ Future-Proof
- **GitHub Copilot ready**: When API becomes available
- **New providers**: Easy to add more AI options
- **Preference evolution**: Change preferences without workflow edits

## Usage Examples

### Example 1: Claude Preferred with OpenAI Fallback
```yaml
# Secrets configured:
ANTHROPIC_API_KEY: sk-ant-...
OPENAI_API_KEY: sk-...

# Workflow selection: claude-preferred
# Result: Uses Claude, falls back to OpenAI if needed
```

### Example 2: OpenAI Only
```yaml
# Secrets configured:
OPENAI_API_KEY: sk-...

# Workflow selection: any preference
# Result: Uses OpenAI (only available option)
```

### Example 3: Maximum Coverage
```yaml
# Secrets configured:
ANTHROPIC_API_KEY: sk-ant-...
OPENAI_API_KEY: sk-...

# Workflow selection: auto-detect-best
# Result: Automatically picks best available option
```

## Troubleshooting

### Common Issues

**Issue: "All AI providers failed"**
```
Solution: Configure at least one API key:
- ANTHROPIC_API_KEY (for Claude)
- OPENAI_API_KEY (for OpenAI)
```

**Issue: "Assessment too expensive"**
```
Solution: Switch to OpenAI preference:
- Use openai-preferred in workflow inputs
- ~30-40% cost reduction vs Claude
```

**Issue: "Claude API rate limited"**
```
Automatic handling: Workflow falls back to OpenAI
Manual solution: Configure OPENAI_API_KEY as backup
```

### Quality Differences

**Claude Advantages:**
- Superior Terraform/Infrastructure analysis
- Better Azure-specific recommendations  
- More detailed security assessments
- Advanced code pattern recognition

**OpenAI Advantages:**
- Consistent markdown formatting
- Faster response times
- Lower API costs
- Broader general knowledge

## Migration from Old Workflow

### If You're Using claude-assessment.yml:

1. **Backup existing reports**:
   ```bash
   cp docs/gh-assessment-report-*.md backup/
   ```

2. **Replace workflow file**:
   ```bash
   rm .github/workflows/claude-assessment.yml
   cp ai-assessment-with-fallback.yml .github/workflows/
   ```

3. **Update secrets** (if needed):
   - Keep existing ANTHROPIC_API_KEY
   - Optionally add OPENAI_API_KEY for fallback

4. **Test new workflow**:
   ```
   Actions → AI Repository Assessment → Run workflow
   ```

### Compatibility

✅ **Assessment reports**: Same format, same versioning
✅ **Framework files**: No changes needed  
✅ **Existing secrets**: All work with new workflow
✅ **Scheduling**: Same schedule (weekly Monday 9 AM UTC)

## Best Practices

### For Production Use
- **Configure both APIs**: Claude + OpenAI for reliability
- **Use claude-preferred**: Best analysis quality
- **Monitor costs**: Set up billing alerts

### For Development/Testing  
- **Single API**: OpenAI for cost efficiency
- **Frequent runs**: Use auto-increment versioning
- **Focus on specific areas**: Use security-focused assessments

### For Compliance/Audit
- **Claude preferred**: Superior analysis depth
- **Manual versioning**: Explicit version control
- **Comprehensive type**: Full repository assessment

---

## API Key Setup Details

### Claude API (Anthropic)
1. Visit [console.anthropic.com](https://console.anthropic.com)
2. Create account or sign in
3. Go to API keys section
4. Create new key with sufficient credits
5. Add as ANTHROPIC_API_KEY secret

### OpenAI API
1. Visit [platform.openai.com](https://platform.openai.com)  
2. Create account or sign in
3. Go to API keys section
4. Create new key with GPT-4 access
5. Add as OPENAI_API_KEY secret

### GitHub Token (Auto-provided)
- GITHUB_TOKEN is automatically available
- No additional configuration needed
- Used for issue creation and repository access

---

**Ready to Use!** 🚀

Your repository now has intelligent AI-powered assessments with automatic fallback. The workflow will always find a working AI provider and generate high-quality assessment reports.
