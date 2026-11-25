import asyncio
import unittest
from unittest.mock import patch

from main import run_jobs


class RunnerTests(unittest.TestCase):
    def test_results_keep_input_order(self):
        self.assertEqual(asyncio.run(run_jobs(4, 2, 0)), [1, 2, 3, 4])

    def test_concurrency_limit(self):
        sleep = asyncio.sleep
        active = peak = 0

        async def fake_sleep(delay):
            nonlocal active, peak
            active += 1
            peak = max(peak, active)
            await sleep(0)
            active -= 1

        with patch("main.asyncio.sleep", fake_sleep):
            asyncio.run(run_jobs(5, 2, 0))
        self.assertEqual(peak, 2)
