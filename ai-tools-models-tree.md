(Cheat Sheet)

General Chat / Writing
- light → qwen2.5:3b
- normal → mistral:7b q5
- high-quality writing or reasoning → llama3.1

Coding
- default / best local coder → qwen2.5-coder 7b q4
- deep refactors → cloud Claude Sonnet
- if struggling locally → llama3.1:8b

File Ops & CLI
- fastest agent → qwen2.5:3b

Agentic tool use (JSON, functions, workflows)
- best tool-use model → llama3.1:8b

┌──────────────────────────────────────────────────────────────────────────┐
│                         LOCAL MODEL DECISION TREE                        │
│                             (M1 Air – 16GB RAM)                          │
└──────────────────────────────────────────────────────────────────────────┘

                                      │
                                      ▼
                     ┌────────────────────────────────────┐
                     │ What are you trying to do right now?│
                     └──────────────┬───────────────┬──────┘
                                    │               │
                                    │               │
                ┌───────────────────┘               └─────────────────────┐
                ▼                                                         ▼
     ┌───────────────────────┐                                 ┌─────────────────────┐
     │   General Chat /      │                                 │  Coding / Dev Work  │
     │   Writing Tasks       │                                 └─────────────────────┘
     └──────────┬────────────┘                                           │
                │                                                        ▼
                ▼                                    ┌───────────────────────────────────┐
     ┌──────────────────────────┐                    │ Multi-file work? IDE-level?       │
     │ Need deep reasoning or   │─── Yes ──────────▶│ Complex APIs? Large diffs?         │
     │ structured writing?      │                    └──────────────────┬─────────────────┘
     └───────────┬─────────────┘                                       │
                 │                                                     │ No
                 │ No                                                 ▼
                 ▼                                    ┌────────────────────────────────────┐
     ┌────────────────────────────────┐               │ Use qwen2.5-coder:7b-instruct q4_K_M│
     │ Use mistral:7b instruct q5_K_M │               │  » Best local 7B coder              │
     │  » Balanced, reliable general  │               └────────────────────────────────────┘
     │    assistant                   │
     └──────────┬─────────────────────┘
                │
                ▼
     ┌────────────────────────────────┐
     │ Light chat / quick writing?    │── Yes ─────▶ Use qwen2.5:3b
     │ (No heavy thinking)            │              » Fastest smart 3B
     └──────────┬─────────────────────┘
                │ No
                ▼
     ┌────────────────────────────────────┐
     │ Use llama3.1:8b q4_K_M         │
     │  » Best local writing quality      │
     │  » Strongest reasoning under 10B   │
     └────────────────────────────────────┘


─────────────────────────────────────────────────────────────────────────────
                     FILE OPS / CLI / AUTOMATION BRANCH
─────────────────────────────────────────────────────────────────────────────

                                      │
                                      ▼
                     ┌───────────────────────────────────────┐
                     │ Are you doing file ops, scripting,     │
                     │ shell automation, or fast tasks?        │
                     └───────────────┬─────────────────────────┘
                                     │
                                     ▼
                     ┌─────────────────────────────────────────┐
                     │ Need fastest possible responses?         │
                     │ (latency > intelligence)                │
                     └───────────┬─────────────────────────────┘
                                 │ Yes
                                 ▼
                     ┌─────────────────────────────────────────┐
                     │ Use qwen2.5:3b                          │
                     │  » Fastest capable model locally        │
                     │  » Great for opencode + open-interpreter│
                     └─────────────────────────────────────────┘



─────────────────────────────────────────────────────────────────────────────
                           AGENTIC TOOL-USE BRANCH
─────────────────────────────────────────────────────────────────────────────

                                      │
                                      ▼
               ┌───────────────────────────────────────────────┐
               │ Are you doing agent-style tasks?              │
               │ (JSON outputs, calling tools, structured I/O) │
               └───────────────┬───────────────────────────────┘
                               │ Yes
                               ▼
               ┌───────────────────────────────────────────────┐
               │ Use Nomad-7B                                  │
               │  » Best 7B for tool use                       │
               │  » Extremely reliable JSON / function calling │
               └───────────────────────────────────────────────┘

                               │ No
                               ▼
               (Return to general or coding branches above)


─────────────────────────────────────────────────────────────────────────────
                           LOCAL MODEL STRUGGLE CHECK
─────────────────────────────────────────────────────────────────────────────

                                      │
                                      ▼
                 ┌───────────────────────────────────────┐
                 │ Is the local model hallucinating,     │
                 │ timing out, overheating, or stuck?    │
                 └──────────┬────────────────────────────┘
                            │ Yes
                            ▼
                 ┌───────────────────────────────────────────┐
                 │ Coding issue?                              │
                 └───────────┬────────────────────────────────┘
                             │ Yes
                             ▼
                 ┌───────────────────────────────────────────┐
                 │ Switch to Claude Sonnet 3.5                │
                 │  » Best cloud coder                       │
                 └───────────────────────────────────────────┘

                             │ No
                             ▼
                 ┌───────────────────────────────────────────┐
                 │ Switch to Gemini 2.5 Pro or Grok 4 Fast   │
                 │  » Best for reasoning / traceability      │
                 └───────────────────────────────────────────┘


─────────────────────────────────────────────────────────────────────────────
                          DO-NOT-USE ON M1 AIR 16GB
─────────────────────────────────────────────────────────────────────────────

     ┌──────────────────────────────────────────────────────────────────┐
     │ Avoid:                                                           │
     │   • Phi-3 14B (too slow, overheats, unstable)                    │
     │   • DeepSeek V2 16B (swaps immediately → unusable)               │
     │   • Anything >10B unless llama3 8B (Q4)                          │
     │   • CodeLlama 7B (inferior to Qwen/DeepSeek)                     │
     └──────────────────────────────────────────────────────────────────┘

