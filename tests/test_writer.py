import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, "scripts")

SAMPLE_BRIEF = {
    "current_event": "OpenAI researchers leaving for xAI at 3x salary",
    "gem_name": "gollum-effect",
    "gem_summary": "Identity fusion with a capability until transfer feels like death",
    "historical_precedent": "William Shockley invented the transistor at Bell Labs, then watched his best researchers leave to found Fairchild Semiconductor because he couldn't let go of control.",
    "historical_outcome": "Shockley's hoarding produced nothing. The people he couldn't release built Silicon Valley.",
    "open_loop": "Altman built the most capable AI researchers in the world and is learning the same lesson Shockley learned. The ring always escapes.",
    "source_urls": []
}

WRITER_SCRIPT = Path("/Users/danaschreiber/Dev-Projects/pantheon/scripts/writer.py")

def run_writer(brief: dict) -> dict:
    result = subprocess.run(
        [sys.executable, str(WRITER_SCRIPT)],
        input=json.dumps(brief),
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"writer.py failed: {result.stderr}"
    return json.loads(result.stdout.strip())

@pytest.fixture(scope="module")
def writer_output():
    return run_writer(SAMPLE_BRIEF)

def test_writer_returns_required_fields(writer_output):
    assert "x_thread" in writer_output
    assert "threads_thread" in writer_output
    assert "subject_line" in writer_output

def test_x_thread_is_four_posts(writer_output):
    assert len(writer_output["x_thread"]) == 4, f"Expected 4 X posts, got {len(writer_output['x_thread'])}"

def test_threads_thread_is_four_posts(writer_output):
    assert len(writer_output["threads_thread"]) == 4, f"Expected 4 Threads posts, got {len(writer_output['threads_thread'])}"

def test_x_posts_within_char_limit(writer_output):
    for i, post in enumerate(writer_output["x_thread"]):
        assert len(post) <= 280, f"x_thread[{i}] too long: {len(post)} chars"

def test_threads_posts_within_char_limit(writer_output):
    for i, post in enumerate(writer_output["threads_thread"]):
        assert len(post) <= 500, f"threads_thread[{i}] too long: {len(post)} chars"

def test_no_em_dashes_in_output(writer_output):
    for i, post in enumerate(writer_output["x_thread"]):
        assert "\u2014" not in post, f"em-dash found in x_thread[{i}]"
    for i, post in enumerate(writer_output["threads_thread"]):
        assert "\u2014" not in post, f"em-dash found in threads_thread[{i}]"

def test_x_thread_has_cliffhanger_markers(writer_output):
    for i in range(3):
        post = writer_output["x_thread"][i]
        assert "↓" in post or "🧵" in post, f"x_thread[{i}] missing cliffhanger marker"
