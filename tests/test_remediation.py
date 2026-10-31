
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RemediationTests(unittest.TestCase):

    def run_demo(self, filename):
        result = subprocess.run(
            [sys.executable, str(ROOT / "remediation" / filename)],
            capture_output=True,
            text=True,
            timeout=10,
            check=True
        )
        return result.stdout

    def test_sql_injection_prevention(self):
        output = self.run_demo("sql_remediation.py")

        self.assertIn("Vulnerable query result:", output)
        self.assertIn("Banana Juice", output)
        self.assertIn("Secure query result:\n[]", output)

    def test_idor_access_control(self):
        output = self.run_demo("idor_remediation.py")

        self.assertIn("403 Forbidden: Access denied", output)
        self.assertIn("Authorized access test:", output)
        self.assertIn("'owner': 25", output)


if __name__ == "__main__":
    unittest.main()
