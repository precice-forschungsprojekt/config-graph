"""
This graph is intended for the preCICE logical-checker https://github.com/precice-forschungsprojekt/config-checker.

You can find documentation under README.md, docs/Nodes.md and docs/Edges.md.

This graph was developed by Simon Wazynski, Alexander Hutter and Orlando Ackermann as part of https://github.com/precice-forschungsprojekt.
"""

import argparse
import sys

from precice_config_graph import graph as g
from precice_config_graph.xml_processing import parse_file

color_cyan:str = "\033[1;36m"
color_red:str = "\033[1;31m"
color_reset:str = "\033[0m"

def main():
    file_path:str = None
    parser = argparse.ArgumentParser(usage='%(prog)s', description='Creates a graph from a config.xml file for preCICE.')
    parser.add_argument('src', type=argparse.FileType('r'), help='Path of the config.xml source file.')
    args = parser.parse_args()

    if args.src.name.endswith('.xml'):
        file_path = args.src.name
        print(f"Creating graph from '{color_cyan}{file_path}{color_reset}'")
    else:
        sys.exit(f"[{color_red}ERROR{color_reset}]: '{color_cyan}{args.src.name}{color_reset}' is not an xml file")

    root = parse_file(file_path)
    graph = g.get_graph(root)

    g.print_graph(graph)

if __name__ == "__main__":
    sys.exit(main())
