# My Favorite Tools
| Name             | Use case         | Thoughts                                                                     |
| ---------------- | ---------------- | ---------------------------------------------------------------------------- |
| Ollama           | LLM download mgr | Easy to use                                                                  |
| opencode         | CLI              | Free access to Grok and PkL.        |
| open-interpreter | CLI              | Nice agentic interaction                                                     |
| LM Studio        | GUI              | Pretty interface with chat history and OpenAI-compatible. (Requires gollama to find/link ollama models). |

# Favorite Models
## Local

| Name                        | Use case                            | Thoughts          |
| --------------------------- | ----------------------------------- | ----------------- |
| mistral:7b-instruct-q5_K_M  | General chatting and writing helper | Fine for chatting |
| qwen2.5:3b                 | Quick file operation                | only semi functional option  |
| llama3.1:8b-instruct-q5_K_M | General/Writing                     | Best writing/reasoning  |
| qwen2.5-coder:1.5b          | Autocomplete in VS Code             | Works well enough |

## Cloud

| Name                  | Use case                 | Thoughts                                        |
| --------------------- | ------------------------ | ----------------------------------------------- |
| Claude Sonnet 2.5     | Coding                   | Excels at coding                                |
| Gemini 2.5 pro        | Complex/Multimodal tasks | You have headroom, might excel at complex tasks |
| GPT-5 (free)          | General                  | -                                               |
| Grok 4 Fast reasoning | Fast Reasoning           | -                                               |

# Tested tools & models and their issues

| Name                               | Use case         | Thoughts                                                           |
| ---------------------------------- | ---------------- | ------------------------------------------------------------------ |
| phi3:14b-medium-4k-instruct-q4_K_M | agentic/tool use | Poor response quality with code issues when interacting with files |
| DeepSeek-Coder-V2 Lite 16B Q4      | Coding           | Too large for existing host; caused lag and crashing               |
| llama3.2:3b                | File ops           | terrible, unusable results                                                            |
| codellama:7b                       | Coding           | inferior to qwen/deepseek                                                    |
| qwen2.5-coder:7b-instruct-q5_K_M   | Coding           | Testing                                                            |
| deepseek-coder:6.7b                | Coding           | Testing                                                            |


## Inference/API Providers

Companies that host models (often open source ones) and provide API access.

|Name|Pricing|Notes|Privacy & Data Concerns|
|---|---|---|---|
|Groq|Pay-per-token (varies by model). Example: Llama 3.1 70B ~$0.59/$0.79 per 1M tokens (input/output)|Free tier with account, very fast inference with LPU architecture|**Not used for training** without explicit opt-in consent. User data owned by you, not retained except to perform services. SOC 2 compliant. 30-day retention for abuse monitoring. Terms state data is not used to train models.|
|Together AI|Pay-per-token (varies by model). Generally competitive with other providers|$25 free credits for new users|**Not used for training** without explicit opt-in. You can disable data retention entirely in privacy settings (Settings > Profile). SOC 2 and HIPAA compliant. Enterprise options with VPC deployment for enhanced security.|
|Replicate|Pay-per-second based on hardware used. CPU: $0.0001/sec, GPU ranges from $0.000225/sec (T4) to $0.0058/sec (8x A40)|Pay-as-you-go, only pay when code is running, free tier with limited credits|Limited public information on training policies. Inputs/outputs processed for service provision. Check their terms for specific retention policies.|
|Fireworks AI|Pay-per-token. Example: Llama models range from $0.20-$3.00 per 1M input tokens|Free tier with credits, very fast inference, supports fine-tuning|SOC 2 compliant. Enterprise features available. Data handling follows standard cloud provider practices. Check specific terms for training and retention policies.|
|Raycast|Pro: $8/month (or $10/month), Team: $12/user/month. Advanced AI add-on: additional ~$4-8/month|Pro and Advanced tiers. Mac-only productivity tool with AI integration|Routes requests through various AI providers (OpenAI, Anthropic, etc). Privacy depends on which underlying provider is used. Check Raycast privacy policy for specifics on data routing and storage.|

## Foundational Providers

Advanced, state-of-the-art models pushing the boundaries of AI capabilities

|Name|Pricing|CLI?|CLI Access|Notes|Privacy & Data Concerns|
|---|---|---|---|---|---|
|Google Gemini|Free tier: 1.5 Flash (15 RPM, 1M TPM, 1500 RPD), 1.5 Pro (2 RPM, 32K TPM, 50 RPD). Paid: Flash $0.075-$0.30/1M, Pro $1.25-$10/1M (varies by context)|Yes (Gemini CLI - official, open source)|Free with Google account or API key|Free tier with Google account via AI Studio, 60 RPM/1000 RPD free limits, pay-as-you-go for production|**Free tier (AI Studio)**: Data MAY be used for training and reviewed by humans. **Paid API (Vertex AI)**: NOT used for training. 30-day retention for abuse monitoring, 24-hour caching by default (can disable). Zero data retention available. **Workspace**: NOT used for training. HIPAA/GDPR compliant with BAA. Regional data residency available (EU).|
|Anthropic Claude|Haiku 4.5: $1/$5 per 1M tokens. Sonnet 4.5: $3/$15 per 1M. Opus 4: $15/$75 per 1M (input/output)|Yes (Claude Code)|Requires Pro/Max subscription OR API key with billing|Pro ($20/mo) or Max ($100-200/mo) subscription includes CLI, OR use separate pay-as-you-go API|**Consumer (Free/Pro/Max)**: Opt-in for training (5-year retention if opted in, 30-day if not). **API/Enterprise**: NEVER used for training. 7-day retention (changing from 30-day). Zero Data Retention (ZDR) available for Enterprise. Flagged content: 2-year retention, scores 7 years. Does not sell data. GDPR/SOC 2 compliant.|
|OpenAI GPT|GPT-4o: $3/$10 per 1M. GPT-4.1: $10/$30 per 1M. GPT-5: $15/$60 per 1M. o4-mini: $4/$16 per 1M (input/output)|Yes (Codex CLI for coding, openai command for API)|Free to install, requires API key with billing|Pay-as-you-go API pricing only, subscriptions (Plus $20/mo) are separate and don't include API access|**API**: NOT used for training. 30-day retention for abuse monitoring. Zero retention available with BAA for PHI. **ChatGPT Free/Plus**: MAY be used for training unless opted out. Enterprise plans have stricter guarantees. SOC 2, GDPR compliant. No EU data residency for consumer plans.|
|Alibaba Qwen|Qwen3-Max: $0.459/$1.836 per 1M (50% price cut). Qwen2.5: $0.525+ per 1M|Yes (official CLI)|Free to install, requires Alibaba Cloud API key|Very competitive pricing. Free tier in Singapore region. Many models open-source under Apache 2.0|Subject to Chinese data laws. Data handling follows Alibaba Cloud policies. Open-source models available under Apache 2.0 can be self-hosted for full control. Check Alibaba Cloud terms for specifics on retention and training.|
|Moonshot Kimi|Kimi K2: $0.16/$2.63 per 1M tokens|Yes (Kimi CLI)|Free to install, requires Moonshot API key|1T parameter MoE model. Known for long-context (200K+ tokens) and agentic capabilities|Subject to Chinese data laws. Limited English documentation on privacy policies. Data handling follows Moonshot AI platform policies. Check platform.moonshot.ai terms for retention and training policies.|
