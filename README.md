# preCICE Config Graph

A Library that builds a graph from a preCICE configuration file for validation and visualization purposes.

**How does this differ from [the preCICE Config-Visualizer](https://github.com/precice/config-visualizer)?** The graph built by this library is not (directly) meant to be displayed. The focus is on building a graph that represents the structure of a preCICE configuration in a way that is useful in checking for logical errors.

> [!NOTE]
> This library assumes the config file to follow some basic rules. For example, references by name are assumed to exist.
> If the config file passes the preCICE-built-in checks (`precice-tools check`) without errors, then it is also read correctly by this library. If `precice-tools check` does not succeed, the behavior of this library is undefined (it will probably crash).

## Requirements

- Python 3.12+
- Pip
- Git for cloning the repository
- PyQt6
- Pytest for testing (`pip install -U pytest`)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/precice-forschungsprojekt/config-graph
cd config-graph
```
2. Create a new Python Virtual Environment (optional, but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install required dependencies:
```bash
pip install .
```

## Project Structure

```
config-graph
├── .github, .idea, etc…
│
├── docs                       # Useful information for unterstanding how this library works
│   └── …
│
├── debugging                  # Utility for debugging graph generation. See section in this README on the topic.
│   └── cli.py                 # Call this script to visualize a provided config
│
├── precice_config_graph       # Main library files
│   ├── edges.py               # Definition of edge types
│   ├── graph.py               # Main logic for building the graph from parsed XML
│   ├── nodes.py               # Definition of node types
│   └── xml_processing.py      # preCICE-specific utilities for reading XML files correctly
│
├── test                       # All files for automated testing
│   └── example-configs        # Contains sample configurations that are then tested one by one
│       └── <case-name>
│           ├── precice-config.xml
│           └── test.py        # File that tests the graph that is produced from precice-config.xml for validity
│
├── .gitignore, LICENSE, README.md
│
├── pyproject.toml             # Project configuration (dependencies etc.)
└── shell.nix                  # Dependencies for anyone using NixOS / the nix-package manager. Should be replaced by a flake in the future.
```

## Using in your project

This library is not yet published to any package registry. Nonetheless, it can still be imported into your `pyproject.toml` like so:

```toml
# …
dependencies = [
    "precice_config_graph @ git+https://github.com/precice-forschungsprojekt/config-graph.git",
    # …
]
# …
```

Then, run `pip install .` in your project. To build a graph, use the following code snippet:

```python
from precice_config_graph import graph, xml_processing

path = "./some/path/to/your/precice-config.xml"
root = xml_processing.parse_file(path)
G = graph.get_graph(root)
# use, traverse inspect the graph

# to view the graph
graph.print_graph(G)
```

## Debugging graph generation

This module includes a small utility that helps with debugging the output graph. You can pass a custom `precice-config.xml` and it displays the graph it built in a pop-up window.

To get started, run

```bash
python debugging/cli.py "./path-to-your/precice-config.xml"
```

## Graph structure

The types of nodes and edges are documented under `docs/Nodes-and-Edges.md`.
