# MRZROOT OS 1: Async Task Runner

Run simulated I/O tasks with asyncio and a configurable concurrency limit.

<div dir="rtl" lang="fa">

**اجرای هم‌زمان کارها** · چند کار آزمایشی را هم‌زمان اجرا کنید و سقف تعداد کارهای هم‌زمان را تغییر دهید.

</div>

- [Project page source](docs/index.html) · open it locally in a browser.
- Python 3.9+; no third-party runtime dependencies.

## Quick start

```sh
git clone https://github.com/mrzroot/mrzroot-os-1.git
cd mrzroot-os-1
python main.py --jobs 12 --parallel 3 --delay-ms 100
python main.py --help
```

Jobs simulate I/O using a sleep. This is not a persistent scheduler, worker service, or CPU benchmark.

## Features

- Adjust job count, concurrency, and delay.
- Read total elapsed time and completed job count.
- No packages to install.

## Tests

```sh
python -m unittest discover -v
```

## MRZROOT OS series

- [OS 1: Async Task Runner](https://github.com/mrzroot/mrzroot-os-1)
- [OS 2: Terminal Microbenchmark](https://github.com/mrzroot/mrzroot-os-2)
- [OS 3: System Snapshot](https://github.com/mrzroot/mrzroot-os-3)
