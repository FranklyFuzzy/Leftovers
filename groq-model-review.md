| Recommendation | Best Model | Reason |
|:---|:---|:---|
| **⚡ Speed & Low-Latency Real-Time Applications** | llama-3.1-8b-instant | Fastest inference with 6K tokens/min, optimized for instant responses |
| **🎯 General-Purpose & Enterprise Applications** | llama-3.3-70b-versatile | Best balance of quality and capability for most use cases |
| **🛡️ Content Safety & Moderation** | llama-guard-4-12b | Detects harmful content; use alongside other models for input/output filtering |
| **🚨 Prompt Injection & Attack Detection** | llama-prompt-guard-2-86m | Filters adversarial prompts before they reach main models |
| **🧠 Complex Reasoning & Knowledge Tasks** | llama-3.3-70b-versatile or gpt-oss-120b | Superior reasoning for multi-step problems and specialized knowledge |
| **💡 Efficient Expert Routing** | llama-4-scout-17b or llama-4-maverick-17b | Mixture-of-experts for performance without full model overhead |
| **📚 Long Document Processing** | kimi-k2-instruct | Extended context window for document analysis |
| **💰 Cost-Efficient Mid-Scale** | gpt-oss-20b or qwen3-32b | Good quality without maximum computational requirements |

---

| Model | Example Tasks | Best Use Cases |
|:---|:---|:---|
| **allam-2-7b** | • Simple chatbot responses<br>• Basic text classification<br>• Quick sentiment analysis<br>• Lightweight summarization | Lightweight, efficient multilingual text generation; basic NLP tasks with minimal latency |
| **groq/compound** | • Multi-step decision trees<br>• Route customer queries<br>• Complex reasoning workflows<br>• Conditional logic chains | Specialized routing and decision-making for complex multi-step reasoning and compound queries requiring orchestration |
| **groq/compound-mini** | • Edge device inference<br>• Mobile app responses<br>• IoT text processing<br>• Resource-limited environments | Lightweight compound reasoning for resource-constrained environments while maintaining routing capabilities |
| **llama-3.1-8b-instant** | • Live chat support<br>• Real-time content filtering<br>• Quick data analysis<br>• Fast API responses<br>• Content classification | Fast, real-time conversational AI; content filtering; data analysis; text classification; sentiment analysis; translation requiring instant responses |
| **llama-3.3-70b-versatile** | • Blog/article generation<br>• Code generation & review<br>• Customer service chatbots<br>• Text summarization<br>• Complex Q&A systems<br>• Dialogue systems | General-purpose enterprise applications; content creation; code generation; complex reasoning; text summarization; dialogue systems; sophisticated language understanding |
| **llama-4-maverick-17b-128e** | • Multi-expert task routing<br>• Specialized domain reasoning<br>• High-throughput inference<br>• Balanced quality/speed tasks<br>• Production workflows | Advanced reasoning with mixture-of-experts efficiency; general-purpose tasks with improved performance over dense models; specialized domain handling |
| **llama-4-scout-17b-16e** | • Expert-selected task routing<br>• Specialized domain inference<br>• High-throughput production<br>• Dynamic model selection | Efficient expert routing for specialized domain tasks and high-throughput production inference with selective expert activation |
| **llama-guard-4-12b** | • Review user-generated content<br>• Filter chatbot outputs<br>• Moderate multimodal inputs<br>• Screen images + text<br>• Check for hate speech/violence | Content moderation detecting 14 categories (violence, hate, sexual content, misinformation, etc.); both text and image moderation; ensuring safe AI interactions |
| **llama-prompt-guard-2-22m** | • Pre-filter user inputs<br>• Detect jailbreak attempts<br>• Block injection attacks<br>• Lightweight input screening | Lightweight prompt injection detection and attack filtering at inference time; minimal overhead |
| **llama-prompt-guard-2-86m** | • Advanced jailbreak detection<br>• Sophisticated attack filtering<br>• Complex prompt analysis<br>• Enhanced security screening | Enhanced prompt injection filtering with larger model capacity for more sophisticated attack detection and complex prompt analysis |
| **kimi-k2-instruct** | • Process long research papers<br>• Analyze full legal documents<br>• Extended conversation history<br>• Long-form document Q&A<br>• Multilingual long documents | Long-context understanding; multilingual reasoning; complex document analysis; instruction-following tasks with extended context |
| **kimi-k2-instruct-0905** | • Updated long-context tasks<br>• Improved multilingual documents<br>• Better instruction adherence<br>• Enhanced reasoning tasks | Updated version with improved multilingual capabilities and refined instruction adherence for long-context applications |
| **gpt-oss-120b** | • Enterprise knowledge systems<br>• Complex research synthesis<br>• High-quality content creation<br>• Advanced reasoning tasks<br>• Scientific analysis | Enterprise-grade general-purpose tasks; complex reasoning; knowledge-intensive applications; high-quality text generation |
| **gpt-oss-20b** | • Standard business applications<br>• Content generation<br>• Code assistance<br>• General Q&A systems<br>• Production workloads | Balanced performance and speed for mid-scale production applications requiring good quality without maximum computational overhead |
| **gpt-oss-safeguard-20b** | • Safe content generation<br>• Enterprise compliance tasks<br>• Regulated industry applications<br>• Safety-critical workflows | Safety-focused variant with built-in content safety verification for compliance-heavy industries and regulated applications |
| **qwen3-32b** | • Multilingual content creation<br>• Code generation/debugging<br>• Math problem solving<br>• Instruction-following tasks<br>• Technical documentation | Multilingual tasks; coding assistance; math reasoning; instruction-following; general-purpose applications with good capability/efficiency balance |

