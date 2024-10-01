---
layout: container
name:  "quay.io/biocontainers/pipmir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pipmir/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pipmir/container.yaml"
updated_at: "2024-10-01 03:06:18.166188"
latest: "1.1--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/pipmir"
aliases:
 - "PIPmiR"
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
 - "1.1--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for pipmir"
config: {"url": "https://biocontainers.pro/tools/pipmir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pipmir", "latest": {"1.1--hdfd78af_5": "sha256:2894a578a6f2811009b64f555d3c72fe46c5a75fc34c9bb416c559012802fdfe"}, "tags": {"1.1--hdfd78af_5": "sha256:2894a578a6f2811009b64f555d3c72fe46c5a75fc34c9bb416c559012802fdfe"}, "docker": "quay.io/biocontainers/pipmir", "aliases": {"PIPmiR": "/usr/local/bin/PIPmiR", "RNAfold": "/usr/local/bin/RNAfold", "Kinfold": "/usr/local/bin/Kinfold", "RNALfold": "/usr/local/bin/RNALfold", "RNAaliduplex": "/usr/local/bin/RNAaliduplex", "RNAalifold": "/usr/local/bin/RNAalifold", "RNAcofold": "/usr/local/bin/RNAcofold", "RNAdistance": "/usr/local/bin/RNAdistance", "RNAduplex": "/usr/local/bin/RNAduplex", "RNAeval": "/usr/local/bin/RNAeval", "RNAforester": "/usr/local/bin/RNAforester"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pipmir.
shpc-registry automated BioContainers addition for pipmir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pipmir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pipmir:1.1--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pipmir/1.1--hdfd78af_5
$ module help quay.io/biocontainers/pipmir/1.1--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pipmir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pipmir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pipmir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pipmir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pipmir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pipmir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PIPmiR

```bash
$ singularity exec <container> /usr/local/bin/PIPmiR
$ podman run --it --rm --entrypoint /usr/local/bin/PIPmiR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PIPmiR   -v ${PWD} -w ${PWD} <container> -c " $@"
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