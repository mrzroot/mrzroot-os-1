<div align="center">

<!-- Hero Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,25,45&height=200&section=header&text=MRZROOT-OS-1&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=%E2%9A%A1%20Lightweight%20Python%20Async%20Task%20Runner%20%26%20Scheduler&descFontSize=16&descAlignY=58&descAlign=50" alt="MRZROOT OS 1 Banner" width="100%" />

<!-- Animated Typist -->
<a href="https://github.com/mrzroot/mrzroot-os-1">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&duration=2800&pause=1000&color=00D2FF&center=true&vCenter=true&width=650&lines=Simple+Async+Task+Runner+in+Python;Clean+Background+Job+Execution+with+asyncio;Zero+External+Dependencies+%7C+Beginner-Friendly" alt="Typing SVG" />
</a>

<br />

<!-- Live Status Badges -->
<p align="center">
  <a href="https://github.com/mrzroot/mrzroot-os-1/stargazers">
    <img src="https://img.shields.io/github/stars/mrzroot/mrzroot-os-1?style=for-the-badge&logo=github&color=00D2FF" alt="GitHub Stars" />
  </a>
  <a href="https://github.com/mrzroot/mrzroot-os-1/network/members">
    <img src="https://img.shields.io/github/forks/mrzroot/mrzroot-os-1?style=for-the-badge&logo=github&color=38BDF8" alt="GitHub Forks" />
  </a>
  <a href="https://github.com/mrzroot/mrzroot-os-1/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge" alt="License" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome" />
</p>

<p align="center">
  <strong>⭐ If you find this project useful, please consider starring the repository to support development! ⭐</strong>
</p>

</div>

---

### 📖 Overview

**MRZROOT-OS-1** is an easy-to-use, lightweight asynchronous task runner built with Python's built-in `asyncio`. It demonstrates how to run multiple background tasks concurrently without complicated setups or heavy third-party libraries.

```
┌─────────────────────────────────────────────────────────────┐
│  ⚡ MRZROOT-OS-1 Async Task Runner                         │
│  [Core] Concurrent • Clean • Easy to Learn • Zero Deps     │
└─────────────────────────────────────────────────────────────┘
```

---

### ✨ Key Features

- ⚡ **Built with Pure `asyncio`**: No Celery or Redis needed for small scripts and local experiments.
- ⏱️ **Concurrent Execution**: Run multiple tasks simultaneously with minimal code.
- 📖 **Clear & Commented Code**: Perfect for learning asynchronous programming in Python.
- 🚀 **Instant Setup**: Clone and run immediately.

---

### 🚀 Quick Start & Installation

```bash
# Clone the repository
git clone https://github.com/mrzroot/mrzroot-os-1.git
cd mrzroot-os-1

# Run the task engine
python main.py
```

---

### 💻 Architecture Flow

```mermaid
graph LR
    classDef input fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef engine fill:#0284c7,stroke:#00D2FF,stroke-width:2px,color:#fff;
    classDef output fill:#0f766e,stroke:#2dd4bf,stroke-width:2px,color:#fff;

    Tasks["📋 Task Queue (Async FIFO)"]:::input
    Scheduler["⏱️ Micro-Scheduler Engine"]:::engine
    Worker["⚡ Concurrent Async Workers"]:::engine
    Results["📊 Telemetry & Results"]:::output

    Tasks --> Scheduler
    Scheduler --> Worker
    Worker --> Results
```

---

### 🌟 Star History & Community Support

Support our open-source journey! If you like what we're building, leave a star ⭐:

<div align="center">
  <a href="https://star-history.com/#mrzroot/mrzroot-os-1&Date">
    <img src="https://api.star-history.com/svg?repos=mrzroot/mrzroot-os-1&type=Date" alt="Star History Chart" width="70%" />
  </a>
</div>

---

### 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/mrzroot/mrzroot-os-1/issues).

### 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).
