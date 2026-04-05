# 🐍 Python Mastery Curriculum

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Exercises](https://img.shields.io/badge/exercises-72-green.svg)](#)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Một lộ trình học Python thực chiến, được thiết kế để thu hẹp khoảng cách giữa kiến thức học thuật và kỹ thuật phần mềm thực tế tại các công ty công nghệ ở Việt Nam.

---

## 🚀 Quick Start (5 phút setup)

### Bước 1 — Clone repo và cài dependencies
```bash
git clone https://github.com/dyltran3/Pyt-Work-Guide.git
cd Pyt-Work-Guide

# Cài thư viện cho tracker (bắt buộc)
pip install rich
```

### Bước 2 — Khởi tạo Tracker
```bash
python python_curriculum/tracker.py --init
```

### Bước 3 — Bắt đầu lộ trình
```bash
# Xem dashboard tổng quan
python python_curriculum/tracker.py

# Xem lộ trình Career Track (Backend)
python python_curriculum/tracker.py roadmap backend

# Đánh dấu bắt đầu làm bài A-01
python python_curriculum/tracker.py start A-01
```

---

## 🎯 Lộ trình Career Roadmaps

Chọn lộ trình phù hợp với mục tiêu nghề nghiệp của bạn. Tracker sẽ tự động gợi ý bài học tiếp theo.

| Roadmap | Trọng tâm | Thời gian |
| :--- | :--- | :--- |
| **🖥️ Backend Engineer** | REST APIs, Async, DB Pools, Task Queues | ~8 tuần |
| **📊 Data Engineer** | ETL Pipelines, Streaming, Schema, Parquet | ~9 tuần |
| **🔐 Security Engineer** | Network, Crypto, Forensics, Compliance | ~8 tuần |
| **🤖 AI/ML Engineer** | LLM Agents, RAG, Tool Orchestration | ~7 tuần |
| **🛠️ DevOps Engineer** | Docker, CI/CD, Observability, Automation | ~6 tuần |

---

## 📦 Dependency Management

Cài đặt thư viện theo từng Career Track bạn theo đuổi:

<details>
<summary><b>Click để xem danh sách lệnh cài đặt</b></summary>

### Backend
```bash
pip install fastapi uvicorn pydantic pydantic-settings httpx
```

### Data & Analytics
```bash
pip install pandas numpy
```

### Cybersecurity
```bash
pip install pycryptodome cryptography pyyaml
```

### AI Agent / Computer Vision
```bash
pip install requests Pillow opencv-python sentence-transformers
```

### Infrastructure & QA
```bash
pip install pytest pytest-cov prometheus_client aiohttp
```
</details>

---

## 📚 Curriculum Detail (72 Bài tập)

### 📖 Book 1: Learn Python The Hard Way (Applied)
Lớp nền tảng vững chắc về CLI, logic xử lý và tư duy lập trình hệ thống.

| ID | Bài tập | Skill chính | Độ khó |
| :--- | :--- | :--- | :--- |
| A-01 | CLI Environment Inspector | `os.environ`, `f-strings` | ★★☆☆☆ |
| A-02 | Structured Log Parser | `Regex`, `Generators` | ★★★☆☆ |
| A-03 | Config File Generator | `String formatting` | ★★☆☆☆ |
| A-04 | Binary File Inspector | `bytes`, `struct`, `hex` | ★★★☆☆ |
| A-05 | API Request Validator | `Recursion`, `Dicts` | ★★★☆☆ |
| A-06 | HTTP Status Decision Tree | `Guard clauses` | ★★☆☆☆ |
| A-07 | Retry Logic with Backoff | `Decorators`, `Backoff` | ★★★★☆ |
| A-08 | Chunked File Processor | `itertools.islice` | ★★★☆☆ |
| A-09 | Rate Limiter Queue | `time`, `collections.deque` | ★★★☆☆ |
| A-10 | Dependency Resolver | `DFS`, `Topological sort` | ★★★★☆ |
| A-11 | Plugin Architecture | `OOP`, `Composition` | ★★★☆☆ |
| A-12 | ORM-lite Table Mapper | `Dict comprehension` | ★★★☆☆ |
| A-13 | Service Health Monitor | `Inheritance`, `Polymorphism` | ★★★☆☆ |
| A-14 | Project Scaffolding | `pathlib.Path` | ★★☆☆☆ |
| A-15 | Contract Testing | `inspect.getmembers` | ★★★★☆ |

### 📖 Book 2: Python Notes For Professionals
Đi sâu vào các khái niệm nâng cao, tối ưu hóa và concurrency.

| ID | Bài tập | Skill chính | Độ khó |
| :--- | :--- | :--- | :--- |
| B-01 | Network Packet Inspector | `Bitwise &`, `Masking` | ★★★☆☆ |
| B-02 | Memory-Efficient Stream | `Generators (yield)` | ★★★☆☆ |
| B-03 | Scope Isolation | `Globals`, `Locals` | ★★★☆☆ |
| B-04 | LRU Cache từ đầu | `OrderedDict`, `Linked List` | ★★★★☆ |
| B-05 | Priority Task Scheduler | `heapq`, `Priority Queue` | ★★★★☆ |
| B-06 | Inverted Index Builder | `Indexing`, `Full-text` | ★★★★☆ |
| B-07 | Async HTTP Crawler | `asyncio`, `aiohttp` | ★★★★☆ |
| B-08 | Image Processor (CPU) | `Multiprocessing` | ★★★★☆ |
| B-09 | Thread-Safe Pub/Sub | `Threading`, `Queue` | ★★★★☆ |
| B-10 | Raw HTTP Client | `Raw Sockets`, `HTTP Protocol` | ★★★★★ |
| B-11 | API Wrapper Generator | `Meta-programming` | ★★★★☆ |
| B-12 | Mini Flask Clone | `Routing`, `WSGI` | ★★★★☆ |
| B-13 | SQL Migration Runner | `sqlite3`, `Migrations` | ★★★★☆ |
| B-14 | ETL Data Pipeline | `Generators`, `ETL` | ★★★★☆ |
| B-15 | Password Hashing | `hashlib`, `Salt` | ★★★☆☆ |
| B-16 | JWT từ Scratch | `hmac`, `base64` | ★★★★☆ |
| B-17 | DI Container | `Dependency Injection` | ★★★★☆ |
| B-18 | Reactive Event System | `Observer Pattern` | ★★★★☆ |
| B-19 | Profiling & Optimization | `cProfile`, `Optimization` | ★★★★☆ |
| B-20 | Env Manager CLI | `Virtualenv`, `Subprocess` | ★★★★☆ |
| B-21 | Concurrency Shootout | `Benchmarking` | ★★★★☆ |
| B-22 | Modern Python 3.11+ | `Match-case`, `Task Groups` | ★★★☆☆ |

### 🚀 Career Tracks (Specialized)
Các bài tập mô phỏng công việc thực tế tại các doanh nghiệp lớn.

#### 🖥️ Backend & DevOps
| ID | Title | Main Skill | Difficulty |
| :--- | :--- | :--- | :--- |
| Backend-01 | FastAPI Boilerplate | `Pydantic-settings`, `Middleware` | ★★★★☆ |
| Backend-02 | DB Connection Pool | `Queue`, `Monitoring` | ★★★★☆ |
| Backend-03 | Async Task Queue | `asyncio.Queue` | ★★★★☆ |
| Backend-04 | DB Optimization | `Clustered Index`, `Queries` | ★★★★★ |
| DevOps-01 | Microservices | `Docker Compose` | ★★★★☆ |
| DevOps-02 | CI/CD Pipeline | `GitHub Actions` | ★★★★☆ |
| DevOps-03 | Observability | `Prometheus`, `Logging` | ★★★★☆ |

#### 📊 Data Analysis & Engineering
| ID | Title | Main Skill | Difficulty |
| :--- | :--- | :--- | :--- |
| Data-01 | DQ Framework | `Validation logic` | ★★★★☆ |
| Data-02 | Anomaly Detector | `Z-Score`, `Rolling Mean` | ★★★★☆ |
| Data-03 | SQL Performance | `EXPLAIN QUERY PLAN` | ★★★★☆ |
| Data-04 | Parquet Writer | `Binary struct`, `RLE` | ★★★★★ |
| Data-05 | CDC Engine | `SQLite WAL`, `Triggers` | ★★★★★ |
| Data-06 | Schema Registry | `Compatibility logic` | ★★★★★ |
| Data-07 | MapReduce Framework | `Multiprocessing`, `Shuffling` | ★★★★★ |
| Data-08 | TS Compression | `Gorilla`, `Delta encoding` | ★★★★★ |
| Data-09 | Data Lineage | `Adjacency List`, `BFS/DFS` | ★★★★★ |

#### 🔐 Cybersecurity
| ID | Title | Main Skill | Difficulty |
| :--- | :--- | :--- | :--- |
| Cyber-01 | Port Scanner | `socket`, `ThreadPool` | ★★★★☆ |
| Cyber-02 | Secure Transfer | `AES`, `Cryptography` | ★★★★☆ |
| Cyber-03 | Log Forensics | `RegEx`, `Anomly Detection` | ★★★★☆ |
| Cyber-04 | TLS Inspector | `ssl`, `X.509 Parsing` | ★★★★★ |
| Cyber-05 | PCAP Parser | `Binary parsing`, `struct` | ★★★★★ |
| Cyber-06 | JWT Auditor | `Attacker Simulation` | ★★★★★ |
| Cyber-07 | Compliance Scan | `AST Analysis`, `Decree 13` | ★★★★★ |

#### 🤖 AI, Vision & QA
| ID | Title | Main Skill | Difficulty |
| :--- | :--- | :--- | :--- |
| Agent-01 | Tool-Use Foundation | `Function Calling` | ★★★★★ |
| Agent-02 | Reasoning Agent | `ReAct Pattern` | ★★★★★ |
| Agent-03 | 🏆 MAIN Project | `Final Integration` | ★★★★★ |
| Vision-01 | Steganography | `LSB Manipulation` | ★★★★☆ |
| Vision-02 | Doc Scanner | `Perspective Transform` | ★★★★☆ |
| Vision-03 | CAPTCHA Gen | `Image Noise`, `PIL` | ★★★★☆ |
| Test-01 | Advanced Mocks | `unittest.mock` | ★★★★☆ |
| Test-02 | Property Testing | `Hypothesis` | ★★★★☆ |
| Test-03 | Integration Tests | `Fixtures`, `FastAPI test` | ★★★★☆ |
| Test-04 | Mutation Testing | `Fault Injection` | ★★★★☆ |

---

## 🛠️ Work In Progress (Đang cập nhật)
Dự án vẫn đang tích cực bổ sung nội dung mới cho Career Tracks:
- [ ] **Data Engineering**: Data-10 (Real-time Stream Processor with Flink-like logic)
- [ ] **Cybersecurity**: Cyber-08 (Mini Malware Sandbox with Restricted Execution)
- [ ] **SRE**: Platform-01 (Auto-scaling Simulation)

---

## 🤝 Contributing
Issues và Pull Requests luôn được chào đón. Hãy giúp chúng tôi hoàn thiện lộ trình này bằng cách đóng góp các bài tập mới hoặc sửa lỗi.

## 📄 License
MIT License — Copyright (c) 2026 Trần Tuấn Anh
