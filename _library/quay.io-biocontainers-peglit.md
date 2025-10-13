---
layout: container
name:  "quay.io/biocontainers/peglit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/peglit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/peglit/container.yaml"
updated_at: "2025-10-13 04:01:09.269337"
latest: "1.1.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/peglit"
aliases:
 - "RNAmultifold"
 - "peglit"
 - "peglit.inspect"
 - "peglit.score"
 - "tjbench"
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
 - "RNAforester"
versions:
 - "1.0.2--pyh7cba7a3_0"
 - "1.1.0--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for peglit"
config: {"url": "https://biocontainers.pro/tools/peglit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for peglit", "latest": {"1.1.0--pyh7cba7a3_0": "sha256:e1adcbce6b769874c68dacbbda139ffaff93823a9c6b2e61155e3ac53f6a021e"}, "tags": {"1.0.2--pyh7cba7a3_0": "sha256:b6aa924c325390ebc962fc877216dda61706359f47651460833ba8ab306098bf", "1.1.0--pyh7cba7a3_0": "sha256:e1adcbce6b769874c68dacbbda139ffaff93823a9c6b2e61155e3ac53f6a021e"}, "docker": "quay.io/biocontainers/peglit", "aliases": {"RNAmultifold": "/usr/local/bin/RNAmultifold", "peglit": "/usr/local/bin/peglit", "peglit.inspect": "/usr/local/bin/peglit.inspect", "peglit.score": "/usr/local/bin/peglit.score", "tjbench": "/usr/local/bin/tjbench", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold", "RNALalifold": "/usr/local/bin/RNALalifold", "RNAPKplex": "/usr/local/bin/RNAPKplex", "RNAparconv": "/usr/local/bin/RNAparconv", "RNAplex": "/usr/local/bin/RNAplex", "RNAsnoop": "/usr/local/bin/RNAsnoop", "RNAfold": "/usr/local/bin/RNAfold", "Kinfold": "/usr/local/bin/Kinfold", "RNALfold": "/usr/local/bin/RNALfold", "RNAaliduplex": "/usr/local/bin/RNAaliduplex", "RNAalifold": "/usr/local/bin/RNAalifold", "RNAcofold": "/usr/local/bin/RNAcofold", "RNAdistance": "/usr/local/bin/RNAdistance", "RNAduplex": "/usr/local/bin/RNAduplex", "RNAeval": "/usr/local/bin/RNAeval", "RNAforester": "/usr/local/bin/RNAforester"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/peglit.
singularity registry hpc automated addition for peglit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/peglit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/peglit:1.1.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/peglit/1.1.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/peglit/1.1.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### peglit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### peglit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### peglit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### peglit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### peglit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### peglit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAmultifold

```bash
$ singularity exec <container> /usr/local/bin/RNAmultifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peglit

```bash
$ singularity exec <container> /usr/local/bin/peglit
$ podman run --it --rm --entrypoint /usr/local/bin/peglit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peglit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peglit.inspect

```bash
$ singularity exec <container> /usr/local/bin/peglit.inspect
$ podman run --it --rm --entrypoint /usr/local/bin/peglit.inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peglit.inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peglit.score

```bash
$ singularity exec <container> /usr/local/bin/peglit.score
$ podman run --it --rm --entrypoint /usr/local/bin/peglit.score   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peglit.score   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### RNAforester

```bash
$ singularity exec <container> /usr/local/bin/RNAforester
$ podman run --it --rm --entrypoint /usr/local/bin/RNAforester   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAforester   -v ${PWD} -w ${PWD} <container> -c " $@"
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