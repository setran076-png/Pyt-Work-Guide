import json
import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

# Path settings
HOME_DIR = Path.home()
DB_DIR = HOME_DIR / ".python-curriculum"
DB_FILE = DB_DIR / "progress.json"
CONFIG_FILE = Path(__file__).parent / "config.json"

console = Console()

# ─── Career Track Roadmaps ──────────────────────────────────────────────────

ROADMAPS = {
    "backend": {
        "title": "🖥️  Backend Engineer",
        "duration": "~8 tuần",
        "description": "REST APIs, async, DB pools, task queues, microservices",
        "phases": [
            {
                "name": "Phase 1 — Python Fundamentals (Tuần 1-2)",
                "exercises": ["A-01", "A-03", "A-05", "A-06", "A-07"],
                "goal": "Nắm vững CLI, validation, và retry patterns"
            },
            {
                "name": "Phase 2 — Systems & Protocols (Tuần 3-4)",
                "exercises": ["A-09", "A-12", "B-10", "B-11", "B-12"],
                "goal": "Raw HTTP, ORM patterns, WSGI framework internals"
            },
            {
                "name": "Phase 3 — Async & Concurrency (Tuần 5-6)",
                "exercises": ["B-07", "B-09", "B-17", "B-18", "B-21"],
                "goal": "asyncio, threading, DI container, event bus"
            },
            {
                "name": "Phase 4 — Production Backend (Tuần 7-8)",
                "exercises": ["B-13", "B-14", "Backend-01", "Backend-02", "Backend-03", "Backend-04"],
                "goal": "FastAPI boilerplate, DB migrations, ETL, N+1 optimization"
            }
        ]
    },
    "data": {
        "title": "📊 Data Engineer",
        "duration": "~9 tuần",
        "description": "ETL pipelines, streaming, schema management, compliance logging",
        "phases": [
            {
                "name": "Phase 1 — Data Fundamentals (Tuần 1-2)",
                "exercises": ["A-02", "A-08", "B-02", "B-19"],
                "goal": "Log parsing, chunked processing, streaming stats, profiling"
            },
            {
                "name": "Phase 2 — Storage & Indexing (Tuần 3-4)",
                "exercises": ["A-12", "B-06", "B-13", "Data-03"],
                "goal": "ORM patterns, inverted index, SQLite migrations, query analysis"
            },
            {
                "name": "Phase 3 — Pipeline Engineering (Tuần 5-6)",
                "exercises": ["B-14", "B-21", "Data-01", "Data-02", "Data-07"],
                "goal": "ETL generator chains, concurrency models, quality framework, anomaly detection, MapReduce"
            },
            {
                "name": "Phase 4 — Advanced Data Engineering (Tuần 7-9)",
                "exercises": ["Data-04", "Data-05", "Data-06", "Data-08", "Data-09"],
                "goal": "Parquet columnar storage, CDC engine, schema registry, time-series compression, lineage tracking"
            }
        ]
    },
    "security": {
        "title": "🔐 Security Engineer",
        "duration": "~8 tuần",
        "description": "Network protocols, cryptography, forensics, compliance (Decree 13/2023)",
        "phases": [
            {
                "name": "Phase 1 — Low-level Python (Tuần 1-2)",
                "exercises": ["A-04", "A-05", "B-01", "B-03"],
                "goal": "Binary inspection, validation, bitwise ops, crash forensics"
            },
            {
                "name": "Phase 2 — Network & Crypto Fundamentals (Tuần 3-4)",
                "exercises": ["B-10", "B-15", "B-16", "Cyber-01"],
                "goal": "Raw sockets, password hashing, JWT from scratch, port scanning"
            },
            {
                "name": "Phase 3 — Threat Detection (Tuần 5-6)",
                "exercises": ["Cyber-02", "Cyber-03", "Cyber-04", "Cyber-05"],
                "goal": "AES file transfer, log forensics, TLS inspection, PCAP analysis"
            },
            {
                "name": "Phase 4 — Security Engineering (Tuần 7-8)",
                "exercises": ["Cyber-06", "Cyber-07", "B-22"],
                "goal": "JWT auditor, Decree 13/2023 compliance scanner, modern Python security patterns"
            }
        ]
    },
    "ai": {
        "title": "🤖 AI/ML Engineer",
        "duration": "~7 tuần",
        "description": "LLM agents, RAG, tool orchestration, multi-step reasoning",
        "phases": [
            {
                "name": "Phase 1 — Algorithms & Data Structures (Tuần 1-2)",
                "exercises": ["A-10", "A-11", "B-04", "B-05", "B-06"],
                "goal": "Graph algorithms, plugin patterns, LRU cache, priority queues, inverted index"
            },
            {
                "name": "Phase 2 — Async & Performance (Tuần 3-4)",
                "exercises": ["B-07", "B-08", "B-17", "B-19", "B-21"],
                "goal": "Async crawling, multiprocessing, DI container, profiling, concurrency models"
            },
            {
                "name": "Phase 3 — AI Agent Foundations (Tuần 5-7)",
                "exercises": ["Agent-01", "Agent-02", "Agent-03"],
                "goal": "Tool-use, ReAct reasoning loop, memory management, CLI assistant"
            }
        ]
    },
    "qa": {
        "title": "🧪 QA / Test Engineer",
        "duration": "~5 tuần",
        "description": "Unit testing, mocking, property-based testing, integration tests",
        "phases": [
            {
                "name": "Phase 1 — Testing Mindset (Tuần 1-2)",
                "exercises": ["A-05", "A-07", "A-15", "B-03"],
                "goal": "Validation patterns, retry testing, mini-pytest, debugger hooks"
            },
            {
                "name": "Phase 2 — Advanced Testing (Tuần 3-4)",
                "exercises": ["B-19", "Test-01", "Test-02", "Test-03"],
                "goal": "Profiling, pytest mocks, property-based testing, integration fixtures"
            },
            {
                "name": "Phase 3 — Quality Engineering (Tuần 5)",
                "exercises": ["Test-04", "Backend-01", "Data-01"],
                "goal": "Snapshot/mutation testing, API testing, data quality validation"
            }
        ]
    },
    "devops": {
        "title": "🛠️ DevOps / Platform Engineer",
        "duration": "~6 tuần",
        "description": "Docker, CI/CD, observability, infrastructure automation",
        "phases": [
            {
                "name": "Phase 1 — Scripting & Automation (Tuần 1-2)",
                "exercises": ["A-01", "A-14", "B-13", "B-20"],
                "goal": "CLI tools, project scaffolding, DB migrations, venv management"
            },
            {
                "name": "Phase 2 — Concurrency & Services (Tuần 3-4)",
                "exercises": ["B-09", "B-21", "Backend-02", "Backend-03"],
                "goal": "Threading, concurrency models, connection pools, async task queues"
            },
            {
                "name": "Phase 3 — Production Infrastructure (Tuần 5-6)",
                "exercises": ["DevOps-01", "DevOps-02", "DevOps-03"],
                "goal": "Docker multi-stage builds, GitHub Actions CI/CD matrix, observability stack (logs/metrics/traces)"
            }
        ]
    },
    "vision": {
        "title": "👁️  Computer Vision Engineer",
        "duration": "~5 tuần",
        "description": "Image processing, OCR prep, security features (KYC, CAPTCHA)",
        "phases": [
            {
                "name": "Phase 1 — Python & Binary Data (Tuần 1-2)",
                "exercises": ["A-04", "B-01", "B-08"],
                "goal": "Binary inspection, bitwise ops, multiprocessing for CPU-intensive work"
            },
            {
                "name": "Phase 2 — Image Engineering (Tuần 3-5)",
                "exercises": ["Vision-01", "Vision-02", "Vision-03"],
                "goal": "LSB steganography, document scanner (perspective transform), CAPTCHA generation"
            }
        ]
    },
    "fullstack": {
        "title": "🌐 Full-Stack Engineer",
        "duration": "~12 tuần",
        "description": "Toàn bộ curriculum — backend, data, security, testing, DevOps",
        "phases": [
            {
                "name": "Foundation (Tuần 1-3)",
                "exercises": ["A-01", "A-02", "A-05", "A-07", "A-10", "A-12", "A-15"],
                "goal": "Core Python engineering patterns"
            },
            {
                "name": "Advanced Python (Tuần 4-6)",
                "exercises": ["B-02", "B-04", "B-07", "B-09", "B-15", "B-16", "B-21", "B-22"],
                "goal": "Concurrency, crypto, modern Python features"
            },
            {
                "name": "Backend & Data (Tuần 7-9)",
                "exercises": ["Backend-01", "Backend-02", "B-13", "B-14", "Data-01", "Data-03"],
                "goal": "Production API + ETL fundamentals"
            },
            {
                "name": "Specialization (Tuần 10-12)",
                "exercises": ["Cyber-01", "Cyber-07", "Agent-01", "Test-01", "Test-02", "DevOps-01", "DevOps-02"],
                "goal": "Security, AI agents, testing, deployment"
            }
        ]
    }
}


# ─── Core tracker functions ──────────────────────────────────────────────────

def load_config():
    if not CONFIG_FILE.exists():
        console.print(f"[red]Error: config.json not found at {CONFIG_FILE}[/red]")
        sys.exit(1)
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_db():
    if not DB_FILE.exists():
        return {"exercises": {}, "last_activity": None, "streak": 0}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db):
    os.makedirs(DB_DIR, exist_ok=True)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4)

def update_streak(db):
    today = datetime.now().date().isoformat()
    last = db.get("last_activity")
    if last == today:
        return
    if last:
        last_date = datetime.fromisoformat(last).date()
        delta = (datetime.now().date() - last_date).days
        if delta == 1:
            db["streak"] = db.get("streak", 0) + 1
        else:
            db["streak"] = 1
    else:
        db["streak"] = 1
    db["last_activity"] = today

def init_tracker():
    db = load_db()
    os.makedirs(DB_DIR, exist_ok=True)
    save_db(db)
    console.print(f"[green]✓ Tracker initialized at {DB_FILE}[/green]")
    console.print("\n[bold]Next steps:[/bold]")
    console.print("  python tracker.py roadmap backend   # Xem lộ trình Backend")
    console.print("  python tracker.py roadmap data      # Xem lộ trình Data Engineer")
    console.print("  python tracker.py roadmap security  # Xem lộ trình Security")
    console.print("  python tracker.py start A-01        # Bắt đầu bài đầu tiên")

def set_status(ex_id, status):
    status = status.upper()
    valid = ["TODO", "IN_PROGRESS", "DONE", "SKIPPED"]
    if status not in valid:
        console.print(f"[red]Invalid status. Must be one of: {', '.join(valid)}[/red]")
        return
    config = load_config()
    all_ex = {item["id"]: item for item in config.get("exercises", [])}
    if ex_id not in all_ex:
        console.print(f"[red]Exercise ID '{ex_id}' not found in config.[/red]")
        console.print("[dim]Run 'python tracker.py' to see all valid IDs.[/dim]")
        return
    db = load_db()
    if "exercises" not in db:
        db["exercises"] = {}
    if ex_id not in db["exercises"]:
        db["exercises"][ex_id] = {}
    db["exercises"][ex_id]["status"] = status
    db["exercises"][ex_id]["updated_at"] = datetime.now().isoformat()
    update_streak(db)
    save_db(db)
    icons = {"DONE": "✅", "IN_PROGRESS": "🏃", "SKIPPED": "⏭️", "TODO": "📝"}
    console.print(f"[green]{icons.get(status, '')} {ex_id} → {status}[/green]")

def show_roadmap(track_name: str):
    """Display career track roadmap with progress indicators."""
    track_key = track_name.lower().strip()
    
    # Aliases
    aliases = {
        "be": "backend", "backend-engineer": "backend",
        "de": "data", "data-engineer": "data", "dataeng": "data",
        "sec": "security", "cyber": "security", "cybersec": "security",
        "ml": "ai", "aiml": "ai", "agent": "ai",
        "test": "qa", "testing": "qa",
        "ops": "devops", "infra": "devops",
        "cv": "vision", "computer-vision": "vision",
        "all": "fullstack", "full": "fullstack",
    }
    track_key = aliases.get(track_key, track_key)
    
    if track_key not in ROADMAPS:
        console.print(f"[red]Track '{track_name}' not found.[/red]")
        console.print("\n[bold]Available tracks:[/bold]")
        for key, data in ROADMAPS.items():
            console.print(f"  [cyan]{key:<12}[/cyan] {data['title']} ({data['duration']})")
        return

    roadmap = ROADMAPS[track_key]
    db = load_db()
    config = load_config()
    all_ex = {item["id"]: item for item in config.get("exercises", [])}
    
    # Header
    console.print()
    console.print(Panel(
        f"[bold]{roadmap['title']}[/bold]\n"
        f"[dim]{roadmap['description']}[/dim]\n"
        f"⏱️  Thời gian ước tính: [yellow]{roadmap['duration']}[/yellow]",
        expand=False
    ))
    
    total_exercises = sum(len(p["exercises"]) for p in roadmap["phases"])
    done_count = sum(
        1 for p in roadmap["phases"]
        for ex_id in p["exercises"]
        if db.get("exercises", {}).get(ex_id, {}).get("status") == "DONE"
    )
    progress_pct = int(done_count / total_exercises * 100) if total_exercises > 0 else 0
    
    # Progress bar
    bar_filled = progress_pct // 5
    bar = "█" * bar_filled + "░" * (20 - bar_filled)
    console.print(f"\n  Progress: [{bar}] {progress_pct}% ({done_count}/{total_exercises} bài)\n")
    
    # Phases
    for phase in roadmap["phases"]:
        phase_done = sum(
            1 for ex_id in phase["exercises"]
            if db.get("exercises", {}).get(ex_id, {}).get("status") == "DONE"
        )
        phase_total = len(phase["exercises"])
        phase_pct = int(phase_done / phase_total * 100) if phase_total > 0 else 0
        
        phase_color = "green" if phase_pct == 100 else ("yellow" if phase_pct > 0 else "blue")
        console.print(f"  [bold {phase_color}]{phase['name']}[/bold {phase_color}]")
        console.print(f"  [dim]🎯 {phase['goal']}[/dim]")
        
        table = Table(show_header=False, box=None, padding=(0, 1))
        table.add_column("ID", style="dim", width=14)
        table.add_column("Title", min_width=30)
        table.add_column("Status", width=14)
        
        for ex_id in phase["exercises"]:
            ex_info = all_ex.get(ex_id, {})
            title = ex_info.get("title", ex_id)
            status = db.get("exercises", {}).get(ex_id, {}).get("status", "TODO")
            
            status_display = {
                "DONE":        "[green]✅ Done[/green]",
                "IN_PROGRESS": "[yellow]🏃 In Progress[/yellow]",
                "SKIPPED":     "[magenta]⏭️  Skipped[/magenta]",
                "TODO":        "[dim]⬜ Todo[/dim]",
            }.get(status, "[dim]⬜ Todo[/dim]")
            
            table.add_row(ex_id, title, status_display)
        
        console.print(table)
        console.print()
    
    # Next action suggestion
    next_todo = None
    for phase in roadmap["phases"]:
        for ex_id in phase["exercises"]:
            status = db.get("exercises", {}).get(ex_id, {}).get("status", "TODO")
            if status == "TODO":
                next_todo = ex_id
                break
        if next_todo:
            break
    
    if next_todo:
        console.print(f"  [bold green]→ Bài tiếp theo:[/bold green] python tracker.py start {next_todo}")
    else:
        console.print(f"  [bold green]🎉 Track hoàn thành! Xem track tiếp theo:[/bold green]")
    console.print()

def show_dashboard():
    config = load_config()
    db = load_db()
    exercises = config.get("exercises", [])
    
    total = len(exercises)
    done_count = sum(1 for e in exercises if db.get("exercises", {}).get(e["id"], {}).get("status") == "DONE")
    skipped_count = sum(1 for e in exercises if db.get("exercises", {}).get(e["id"], {}).get("status") == "SKIPPED")
    in_progress_count = sum(1 for e in exercises if db.get("exercises", {}).get(e["id"], {}).get("status") == "IN_PROGRESS")
    streak = db.get("streak", 0)
    
    console.print(Panel(
        f"[bold blue]🐍 PYTHON MASTERY CURRICULUM[/bold blue]\n"
        f"🔥 Streak: {streak} days  |  "
        f"📚 Total: {total}  |  "
        f"✅ Done: {done_count}  |  "
        f"🏃 In Progress: {in_progress_count}  |  "
        f"⏭️  Skipped: {skipped_count}\n"
        f"[dim]Tip: python tracker.py roadmap <track>  để xem lộ trình career[/dim]",
        expand=False
    ))
    
    modules = {}
    for ex in exercises:
        mod = ex.get("track", "General")
        if mod not in modules:
            modules[mod] = []
        modules[mod].append(ex)
        
    for mod, mod_exercises in modules.items():
        mod_total = len(mod_exercises)
        mod_done = sum(1 for e in mod_exercises if db.get("exercises", {}).get(e["id"], {}).get("status") == "DONE")
        
        bar_filled = int((mod_done / mod_total) * 10) if mod_total > 0 else 0
        bar = "█" * bar_filled + "░" * (10 - bar_filled)
        
        console.print(f"\n[bold]{mod}[/bold] [{bar}] {mod_done}/{mod_total}")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=14)
        table.add_column("Title", min_width=32)
        table.add_column("Status", justify="center", width=14)
        
        for ex in mod_exercises:
            st = db.get("exercises", {}).get(ex["id"], {}).get("status", "TODO")
            status_str = {
                "TODO":        "[dim]⬜ TODO[/dim]",
                "IN_PROGRESS": "[yellow]🏃 IN PROGRESS[/yellow]",
                "DONE":        "[green]✅ DONE[/green]",
                "SKIPPED":     "[magenta]⏭️  SKIPPED[/magenta]"
            }.get(st, st)
            table.add_row(ex["id"], ex["title"], status_str)
            
        console.print(table)

def export_report():
    config = load_config()
    db = load_db()
    exercises = config.get("exercises", [])
    report_path = DB_DIR / "progress_report.md"
    done = sum(1 for e in exercises if db.get("exercises", {}).get(e["id"], {}).get("status") == "DONE")
    
    lines = [
        "# Python Mastery Curriculum — Progress Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Streak:** {db.get('streak', 0)} days",
        f"**Progress:** {done}/{len(exercises)} ({int(done/len(exercises)*100)}%)",
        "",
        "## Exercise Details",
        "| ID | Title | Track | Status | Updated |",
        "|---|---|---|---|---|"
    ]
    for ex in exercises:
        ex_db = db.get("exercises", {}).get(ex["id"], {})
        st = ex_db.get("status", "TODO")
        updated = ex_db.get("updated_at", "-")[:10] if ex_db.get("updated_at") else "-"
        lines.append(f"| {ex['id']} | {ex['title']} | {ex.get('track', '')} | {st} | {updated} |")
        
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    console.print(f"[green]✓ Report exported to {report_path}[/green]")

# ─── Entry point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python Curriculum Progress Tracker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  (no args)              Show full dashboard
  start  <ID>            Mark exercise as IN_PROGRESS
  done   <ID>            Mark exercise as DONE
  skip   <ID>            Mark exercise as SKIPPED
  reset  <ID>            Reset exercise to TODO
  roadmap <track>        Show career track roadmap + progress
  --init                 Initialize tracker (run once)
  --export               Export markdown progress report

Career tracks for 'roadmap':
  backend   data   security   ai   qa   devops   vision   fullstack

Examples:
  python tracker.py roadmap data
  python tracker.py start Data-04
  python tracker.py done  Data-04
        """
    )
    parser.add_argument("--init",   action="store_true", help="Initialize tracker")
    parser.add_argument("--export", action="store_true", help="Export markdown report")
    parser.add_argument("action", nargs="?",
                        choices=["done", "skip", "start", "reset", "roadmap"],
                        help="Action to perform")
    parser.add_argument("exercise_id", nargs="?",
                        help="Exercise ID (e.g. A-01) or track name (for roadmap)")
    
    args = parser.parse_args()
    
    if args.init:
        init_tracker()
    elif args.export:
        export_report()
    elif args.action == "roadmap":
        if not args.exercise_id:
            console.print("[yellow]Usage: python tracker.py roadmap <track>[/yellow]")
            console.print("\nAvailable tracks:")
            for key, data in ROADMAPS.items():
                console.print(f"  [cyan]{key:<12}[/cyan] {data['title']} ({data['duration']})")
        else:
            show_roadmap(args.exercise_id)
    elif args.action and args.exercise_id:
        status_map = {
            "done":  "DONE",
            "skip":  "SKIPPED",
            "start": "IN_PROGRESS",
            "reset": "TODO"
        }
        set_status(args.exercise_id, status_map[args.action])
    else:
        show_dashboard()
