"""
=============================================================================
MRZROOT-OS-1: High-Performance Async Task Runner & Micro-Scheduler
=============================================================================
Pure Python asyncio implementation (Zero external dependencies)
=============================================================================
"""

import asyncio
import sys
import time


def banner():
    print(r"""
\033[1;34m  __  __ _____ ______ _____   ____   ____ _______        ____   _____        __ 
 |  \/  |  __ \___  /  __ \ / __ \ / __ \__   __|      / __ \ / ____|      /_ |
 | \  / | |__) | / /| |__) | |  | | |  | | | | ______ | |  | | (___   ______ | |
 | |\/| |  _  / / / |  _  /| |  | | |  | | | ||______| | |  | |\___ \ |______|| |
 | |  | | | \ \/ /__| | \ \| |__| | |__| | | |        | |__| |____) |        | |
 |_|  |_|_|  \_\_____|_|  \_\\____/ \____/  |_|         \____/|_____/         |_|\033[0m
 \033[1;32m[+] Async Micro-Scheduler & High-Concurrency Task Engine [v2.4.0]\033[0m
""")


async def worker_job(job_id: int, duration: float):
    print(f"  ⚡ [\033[1;33mTask-{job_id}\033[0m] Scheduled -> Executing...")
    await asyncio.sleep(duration)
    print(f"  ✅ [\033[1;32mTask-{job_id}\033[0m] Completed in {duration * 1000:.1f}ms")
    return f"Job-{job_id}-OK"


async def main_async():
    banner()
    print("🚀 \033[1;36mDispatching concurrent async micro-tasks...\033[0m\n")
    t0 = time.perf_counter()
    jobs = [worker_job(i, 0.05 + (i * 0.01)) for i in range(1, 6)]
    results = await asyncio.gather(*jobs)
    total_time = (time.perf_counter() - t0) * 1000
    print(f"\n✨ \033[1;32mAll {len(results)} tasks completed concurrently in {total_time:.2f} ms!\033[0m")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
