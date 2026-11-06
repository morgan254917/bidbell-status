"""Present actual Upptime results without links to an unhosted status website."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
results = json.loads((root / "history/summary.json").read_text(encoding="utf-8"))
rows = ["| Service | Recorded status | History |", "| --- | --- | --- |"]
for result in results:
    status = {"up": "Up", "down": "Down", "degraded": "Degraded"}.get(result["status"], "Unknown")
    name = result["name"].replace("|", "/").replace("\n", " ")
    slug = result["slug"]
    if not slug or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in slug):
        raise ValueError("Unexpected history filename")
    if not (root / "history" / (slug + ".yml")).is_file():
        raise ValueError("Missing actual history record")
    rows.append("| " + name + " | " + status + " | [View record](history/" + slug + ".yml) |")
start = "<!--start: status pages-->"
end = "<!--end: status pages-->"
readme = root / "README.md"
text = readme.read_text(encoding="utf-8")
if text.count(start) != 1 or text.count(end) != 1:
    raise ValueError("Expected exactly one status summary")
before, rest = text.split(start)
_, after = rest.split(end)
readme.write_text(before + start + "\n" + "\n".join(rows) + "\n" + end + after, encoding="utf-8")
print("Rendered " + str(len(results)) + " actual Upptime results.")
