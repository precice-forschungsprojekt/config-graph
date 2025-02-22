# This smoke test does not test generated graphs for correctness. Instead, it just tests if graph generation does not
# fail on the inputs.
# Provide files to test in the "./configs/"-folder. This script will test all files (including those in subfolders)
# whose names end in the ".xml"-extension.

import glob
import os

from precice_config_graph import graph
from precice_config_graph import xml_processing

search_pattern = os.getcwd() + "/tests/smoke-tests/configs/**/*.xml"
files = glob.glob(search_pattern, recursive=True)

print(f"Testing all {len(files)} files matching {search_pattern}")

errors = []
for file in glob.glob(search_pattern, recursive=True):
    try:
        xml = xml_processing.parse_file(file)
        G = graph.get_graph(xml)
    except Exception as e:
        errors.append((file, e))

if errors:
    for (file, error) in errors:
        print(f"Error in {file}:\n     {error}")
else:
    print("Graph generation did not fail on any files provided")

assert not errors, f"{len(errors)} files produced errors"
