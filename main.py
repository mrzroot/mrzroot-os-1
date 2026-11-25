"""Small asyncio task-runner demo. Jobs simulate I/O with sleep."""
import argparse
import asyncio
import sys
import time


def bounded_int(low, high):
    def parse(value):
        number = int(value)
        if not low <= number <= high:
            raise argparse.ArgumentTypeError(f"expected {low}–{high}")
        return number
    return parse


async def run_jobs(count, parallel, delay_ms):
    semaphore = asyncio.Semaphore(parallel)

    async def job(number):
        async with semaphore:
            await asyncio.sleep(delay_ms / 1000)
            return number

    return await asyncio.gather(*(job(number) for number in range(1, count + 1)))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs", type=bounded_int(1, 200), default=5)
    parser.add_argument("--parallel", type=bounded_int(1, 50), default=5)
    parser.add_argument("--delay-ms", type=bounded_int(0, 1000), default=80)
    args = parser.parse_args(argv)
    started = time.perf_counter()
    jobs = asyncio.run(run_jobs(args.jobs, args.parallel, args.delay_ms))
    elapsed = (time.perf_counter() - started) * 1000
    print(f"Completed {len(jobs)} jobs in {elapsed:.1f} ms (limit: {args.parallel})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
