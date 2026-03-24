import subprocess, sys

def test_get_secret_missing_key_exits():
    result = subprocess.run(
        [sys.executable, "-c",
         "import sys; sys.path.insert(0, 'scripts'); from shared import get_secret; get_secret('NONEXISTENT_KEY_XYZ')"],
        capture_output=True, text=True, cwd="/Users/danaschreiber/Dev-Projects/pantheon"
    )
    assert result.returncode != 0
