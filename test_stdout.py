import subprocess
import unittest
from pathlib import Path


class WelcomeToGit(unittest.TestCase):

    def test_output(self):
        repo_dir = [x.name for x in Path().glob("*.py")]
        repo_dir.remove(Path(__file__).name)
        self.assertLessEqual(len(repo_dir), 1, "More than 1 python file found in the directory")
        self.assertEqual(len(repo_dir), 1, "No python file found in the directory")
        p = subprocess.run(f'python "{Path(repo_dir[0]).absolute()}"', capture_output=True, shell=True)
        self.assertEqual("Hello, Python".lower(), p.stdout.decode("UTF-8").strip().lower(), "Wrong output, try again!")


if __name__ == '__main__':
    unittest.main()
