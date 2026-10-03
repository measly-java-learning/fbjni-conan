"""Print the fbjni package folder from `conan create --format=json` output."""
import json
import sys

with open(sys.argv[1]) as f:
    nodes = json.load(f)["graph"]["nodes"].values()
print(next(n["package_folder"] for n in nodes if n["ref"].startswith("fbjni/")))
