# Review Paper: Memory-Efficient LLM Deployment on Microcontrollers ✅

## Generated File

📄 **[LLM_on_Microcontrollers_Review_Paper.docx](file:///Users/bidur/ncit/res/LLM_on_Microcontrollers_Review_Paper.docx)** (IEEE two-column format)

---

## 📚 6 Research Papers Referenced (with PDF Download Links)

| # | Paper Title | Authors | Year | PDF Download |
|---|------------|---------|------|-------------|
| 1 | **The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits (BitNet b1.58)** | S. Ma, H. Wang, L. Ma, et al. (Microsoft) | 2024 | [📥 Download PDF](https://arxiv.org/pdf/2402.17764) |
| 2 | **LLM in a Flash: Efficient Large Language Model Inference with Limited Memory** | K. Alizadeh, I. Mirzadeh, D. Belenko, et al. (Apple) | 2023 | [📥 Download PDF](https://arxiv.org/pdf/2312.11514) |
| 3 | **MCUNetV2: Memory-Efficient Patch-based Inference for Tiny Deep Learning** | J. Lin, W.-M. Chen, H. Cai, C. Gan, S. Han (MIT) | 2021 | [📥 Download PDF](https://arxiv.org/pdf/2110.15352) |
| 4 | **PowerInfer-2: Fast Large Language Model Inference on a Smartphone** | Z. Xue, Y. Song, Z. Mi, et al. (SJTU) | 2024 | [📥 Download PDF](https://arxiv.org/pdf/2406.06282) |
| 5 | **AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration (TinyChatEngine)** | J. Lin, J. Tang, H. Tang, S. Yang, et al. (MIT HAN Lab) — Best Paper, MLSys 2024 | 2024 | [📥 Download PDF](https://arxiv.org/pdf/2306.00978) \| [GitHub](https://github.com/mit-han-lab/TinyChatEngine) |
| 6 | **TinyLLM: Training and Deploying Language Models at the Edge** | S. V. Kandala, P. Medaranga, A. Varshney (NUS) | 2024 | [📥 Download PDF](https://arxiv.org/pdf/2412.15304) |

> [!TIP]
> Click the "📥 Download PDF" links above to directly download each paper from arXiv.

---

## 🔬 Research Gaps Identified (Highlighted in Yellow in DOCX)

| # | Research Gap | Description |
|---|-------------|-------------|
| 1 | **No LLM Architecture for Sub-1MB SRAM** | All existing LLMs use standard Transformers with KV caches; no architecture designed natively for MCU SRAM constraints (Mamba/RWKV unexplored for MCUs) |
| 2 | **No Ternary-Native MCU Hardware** | BitNet b1.58 eliminates FP math, but no MCU-class hardware accelerator or FPGA IP exists for ternary {-1,0,1} inference |
| 3 | **Flash Memory Bandwidth Bottleneck** | MCU QSPI flash (50–100 MB/s) is 30–100× slower than NVMe SSDs used by LLM in a Flash; impact on token latency unstudied |
| 4 | **No Standardized MCU Language Benchmarks** | MLPerf Tiny covers vision but no benchmark exists for language inference on MCUs (tokens/sec, tokens/joule, SRAM usage) |
| 5 | **On-Device Continual Learning Unexplored** | All works are inference-only; on-device fine-tuning/personalization on MCUs (e.g., LoRA with <10KB overhead) is entirely absent |
| 6 | **No End-to-End System Demonstration** | No bare-metal MCU demo with real-time guarantees; RTOS interaction, power profiling, and resource sharing with sensors/actuators unanswered |

---

## 📑 Paper Structure (IEEE Format)

- **Title & Author block** (centered, Times New Roman)
- **Abstract** with keywords
- **Section I**: Introduction — the 5-orders-of-magnitude memory gap
- **Section II**: Literature Review (6 papers, detailed analysis)
- **Section III**: Comparative Analysis (TABLE I: Paper Summary + TABLE II: Memory/Hardware Comparison)
- **Section IV**: Research Gaps (⚠️ **highlighted in yellow**)
- **Section V**: Discussion and Future Directions
- **Section VI**: Conclusion
- **References** (IEEE citation style)

---

## 🗂️ Both Review Papers in Workspace

| File | Topic |
|------|-------|
| [LLM_Review_Paper_2025_2026.docx](file:///Users/bidur/ncit/res/LLM_Review_Paper_2025_2026.docx) | Recent LLM Improvements (2025–2026) |
| [LLM_on_Microcontrollers_Review_Paper.docx](file:///Users/bidur/ncit/res/LLM_on_Microcontrollers_Review_Paper.docx) | LLMs on Microcontrollers — Memory Efficiency |
