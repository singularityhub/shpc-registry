---
layout: container
name:  "quay.io/biocontainers/ribolands"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ribolands/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ribolands/container.yaml"
updated_at: "2026-01-26 04:36:40.849508"
latest: "0.6.1--py_0"
container_url: "https://biocontainers.pro/tools/ribolands"
aliases:
 - "BarMap.py"
 - "DrTransformer.py"
 - "barriers"
 - "crnsimulator"
 - "crossrates.pl"
 - "fix_bar.pl"
 - "genPoHoLandscape"
 - "qd-config"
 - "saddle.pl"
 - "saddle2dot.pl"
 - "saddle2gml.pl"
 - "treekin"
 - "treeplot.pl"
 - "isympy"
 - "RNAdos"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
 - "b2ct"
 - "ct2db"
 - "kinwalker"
 - "popt"
 - "RNA2Dfold"
 - "RNALalifold"
 - "RNAPKplex"
 - "RNAparconv"
 - "RNAplex"
 - "RNAsnoop"
 - "RNAfold"
 - "Kinfold"
 - "RNALfold"
 - "RNAaliduplex"
 - "RNAalifold"
 - "RNAcofold"
 - "RNAdistance"
 - "RNAduplex"
 - "RNAeval"
versions:
 - "0.6.1--py_0"
description: "singularity registry hpc automated addition for ribolands"
config: {"url": "https://biocontainers.pro/tools/ribolands", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ribolands", "latest": {"0.6.1--py_0": "sha256:75d2a6f7dfd6157c1a8b03ed416f7dcc30b223232f588b41f93cf33d10a3c4cc"}, "tags": {"0.6.1--py_0": "sha256:75d2a6f7dfd6157c1a8b03ed416f7dcc30b223232f588b41f93cf33d10a3c4cc"}, "docker": "quay.io/biocontainers/ribolands", "aliases": {"BarMap.py": "/usr/local/bin/BarMap.py", "DrTransformer.py": "/usr/local/bin/DrTransformer.py", "barriers": "/usr/local/bin/barriers", "crnsimulator": "/usr/local/bin/crnsimulator", "crossrates.pl": "/usr/local/bin/crossrates.pl", "fix_bar.pl": "/usr/local/bin/fix_bar.pl", "genPoHoLandscape": "/usr/local/bin/genPoHoLandscape", "qd-config": "/usr/local/bin/qd-config", "saddle.pl": "/usr/local/bin/saddle.pl", "saddle2dot.pl": "/usr/local/bin/saddle2dot.pl", "saddle2gml.pl": "/usr/local/bin/saddle2gml.pl", "treekin": "/usr/local/bin/treekin", "treeplot.pl": "/usr/local/bin/treeplot.pl", "isympy": "/usr/local/bin/isympy", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold", "RNALalifold": "/usr/local/bin/RNALalifold", "RNAPKplex": "/usr/local/bin/RNAPKplex", "RNAparconv": "/usr/local/bin/RNAparconv", "RNAplex": "/usr/local/bin/RNAplex", "RNAsnoop": "/usr/local/bin/RNAsnoop", "RNAfold": "/usr/local/bin/RNAfold", "Kinfold": "/usr/local/bin/Kinfold", "RNALfold": "/usr/local/bin/RNALfold", "RNAaliduplex": "/usr/local/bin/RNAaliduplex", "RNAalifold": "/usr/local/bin/RNAalifold", "RNAcofold": "/usr/local/bin/RNAcofold", "RNAdistance": "/usr/local/bin/RNAdistance", "RNAduplex": "/usr/local/bin/RNAduplex", "RNAeval": "/usr/local/bin/RNAeval"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ribolands.
singularity registry hpc automated addition for ribolands
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ribolands
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ribolands:0.6.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ribolands/0.6.1--py_0
$ module help quay.io/biocontainers/ribolands/0.6.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ribolands-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ribolands-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ribolands-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ribolands-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ribolands-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ribolands-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BarMap.py

```bash
$ singularity exec <container> /usr/local/bin/BarMap.py
$ podman run --it --rm --entrypoint /usr/local/bin/BarMap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BarMap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DrTransformer.py

```bash
$ singularity exec <container> /usr/local/bin/DrTransformer.py
$ podman run --it --rm --entrypoint /usr/local/bin/DrTransformer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DrTransformer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barriers

```bash
$ singularity exec <container> /usr/local/bin/barriers
$ podman run --it --rm --entrypoint /usr/local/bin/barriers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barriers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crnsimulator

```bash
$ singularity exec <container> /usr/local/bin/crnsimulator
$ podman run --it --rm --entrypoint /usr/local/bin/crnsimulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crnsimulator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crossrates.pl

```bash
$ singularity exec <container> /usr/local/bin/crossrates.pl
$ podman run --it --rm --entrypoint /usr/local/bin/crossrates.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crossrates.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_bar.pl

```bash
$ singularity exec <container> /usr/local/bin/fix_bar.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fix_bar.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_bar.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genPoHoLandscape

```bash
$ singularity exec <container> /usr/local/bin/genPoHoLandscape
$ podman run --it --rm --entrypoint /usr/local/bin/genPoHoLandscape   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genPoHoLandscape   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qd-config

```bash
$ singularity exec <container> /usr/local/bin/qd-config
$ podman run --it --rm --entrypoint /usr/local/bin/qd-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qd-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saddle.pl

```bash
$ singularity exec <container> /usr/local/bin/saddle.pl
$ podman run --it --rm --entrypoint /usr/local/bin/saddle.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saddle.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saddle2dot.pl

```bash
$ singularity exec <container> /usr/local/bin/saddle2dot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/saddle2dot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saddle2dot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saddle2gml.pl

```bash
$ singularity exec <container> /usr/local/bin/saddle2gml.pl
$ podman run --it --rm --entrypoint /usr/local/bin/saddle2gml.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saddle2gml.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treekin

```bash
$ singularity exec <container> /usr/local/bin/treekin
$ podman run --it --rm --entrypoint /usr/local/bin/treekin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treekin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treeplot.pl

```bash
$ singularity exec <container> /usr/local/bin/treeplot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/treeplot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treeplot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isympy

```bash
$ singularity exec <container> /usr/local/bin/isympy
$ podman run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdos

```bash
$ singularity exec <container> /usr/local/bin/RNAdos
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseDists

```bash
$ singularity exec <container> /usr/local/bin/AnalyseDists
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseSeqs

```bash
$ singularity exec <container> /usr/local/bin/AnalyseSeqs
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAlocmin

```bash
$ singularity exec <container> /usr/local/bin/RNAlocmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNApvmin

```bash
$ singularity exec <container> /usr/local/bin/RNApvmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2ct

```bash
$ singularity exec <container> /usr/local/bin/b2ct
$ podman run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2db

```bash
$ singularity exec <container> /usr/local/bin/ct2db
$ podman run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinwalker

```bash
$ singularity exec <container> /usr/local/bin/kinwalker
$ podman run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### popt

```bash
$ singularity exec <container> /usr/local/bin/popt
$ podman run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNA2Dfold

```bash
$ singularity exec <container> /usr/local/bin/RNA2Dfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNALalifold

```bash
$ singularity exec <container> /usr/local/bin/RNALalifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNALalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNALalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAPKplex

```bash
$ singularity exec <container> /usr/local/bin/RNAPKplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAPKplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAPKplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAparconv

```bash
$ singularity exec <container> /usr/local/bin/RNAparconv
$ podman run --it --rm --entrypoint /usr/local/bin/RNAparconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAparconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAplex

```bash
$ singularity exec <container> /usr/local/bin/RNAplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAsnoop

```bash
$ singularity exec <container> /usr/local/bin/RNAsnoop
$ podman run --it --rm --entrypoint /usr/local/bin/RNAsnoop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAsnoop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAfold

```bash
$ singularity exec <container> /usr/local/bin/RNAfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Kinfold

```bash
$ singularity exec <container> /usr/local/bin/Kinfold
$ podman run --it --rm --entrypoint /usr/local/bin/Kinfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Kinfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNALfold

```bash
$ singularity exec <container> /usr/local/bin/RNALfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNALfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNALfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAaliduplex

```bash
$ singularity exec <container> /usr/local/bin/RNAaliduplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAaliduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAaliduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAalifold

```bash
$ singularity exec <container> /usr/local/bin/RNAalifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAcofold

```bash
$ singularity exec <container> /usr/local/bin/RNAcofold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAcofold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAcofold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdistance

```bash
$ singularity exec <container> /usr/local/bin/RNAdistance
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdistance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdistance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAduplex

```bash
$ singularity exec <container> /usr/local/bin/RNAduplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAeval

```bash
$ singularity exec <container> /usr/local/bin/RNAeval
$ podman run --it --rm --entrypoint /usr/local/bin/RNAeval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAeval   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)