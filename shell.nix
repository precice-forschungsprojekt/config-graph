let
  pkgs = import <nixpkgs> {};
  pythonEnv = pkgs.python312.withPackages(ps: with pkgs; [
    python312Packages.lxml
    python312Packages.elementpath
    python312Packages.networkx
    python312Packages.matplotlib
    python312Packages.pytest
  ]);
in pkgs.mkShell {
  packages = [
    pythonEnv
  ];
  shellHook = ''
    # Tells pip to put packages into $PIP_PREFIX instead of the usual locations.
    # See https://pip.pypa.io/en/stable/user_guide/#environment-variables.
    export PIP_PREFIX=$(pwd)/_build/pip_packages
    export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
    export PATH="$PIP_PREFIX/bin:$PATH"
    unset SOURCE_DATE_EPOCH
  '';
}
