---
layout: container
name:  "quay.io/biocontainers/kakscalculator2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kakscalculator2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kakscalculator2/container.yaml"
updated_at: "2025-04-07 03:20:43.470314"
latest: "2.0.1--h9948957_6"
container_url: "https://biocontainers.pro/tools/kakscalculator2"
aliases:
 - "AXTConvertor"
 - "ConPairs"
 - "KaKs_Calculator"
versions:
 - "2.0.1--h9f5acd7_2"
 - "2.0.1--h4ac6f70_4"
 - "2.0.1--h9948957_5"
 - "2.0.1--h9948957_6"
description: "shpc-registry automated BioContainers addition for kakscalculator2"
config: {"url": "https://biocontainers.pro/tools/kakscalculator2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kakscalculator2", "latest": {"2.0.1--h9948957_6": "sha256:ae157b0f27553d80557083c4472f085f06707361b21c492ccd1105e4a553136f"}, "tags": {"2.0.1--h9f5acd7_2": "sha256:172eea3e171ef608e73e2bbae63645d9dd4c82052f6bdf924d19326fcdba6d40", "2.0.1--h4ac6f70_4": "sha256:f8e8cf39e32e533e60344df1cc9385128402284f47f40b01bd834931d27f0048", "2.0.1--h9948957_5": "sha256:20390c67b4255ea1475f08bfafa950c616649b72b39f646de72e5c33455ed5b3", "2.0.1--h9948957_6": "sha256:ae157b0f27553d80557083c4472f085f06707361b21c492ccd1105e4a553136f"}, "docker": "quay.io/biocontainers/kakscalculator2", "aliases": {"AXTConvertor": "/usr/local/bin/AXTConvertor", "ConPairs": "/usr/local/bin/ConPairs", "KaKs_Calculator": "/usr/local/bin/KaKs_Calculator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kakscalculator2.
shpc-registry automated BioContainers addition for kakscalculator2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kakscalculator2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kakscalculator2:2.0.1--h9948957_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kakscalculator2/2.0.1--h9948957_6
$ module help quay.io/biocontainers/kakscalculator2/2.0.1--h9948957_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kakscalculator2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kakscalculator2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kakscalculator2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kakscalculator2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kakscalculator2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kakscalculator2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AXTConvertor

```bash
$ singularity exec <container> /usr/local/bin/AXTConvertor
$ podman run --it --rm --entrypoint /usr/local/bin/AXTConvertor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AXTConvertor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ConPairs

```bash
$ singularity exec <container> /usr/local/bin/ConPairs
$ podman run --it --rm --entrypoint /usr/local/bin/ConPairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ConPairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KaKs_Calculator

```bash
$ singularity exec <container> /usr/local/bin/KaKs_Calculator
$ podman run --it --rm --entrypoint /usr/local/bin/KaKs_Calculator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KaKs_Calculator   -v ${PWD} -w ${PWD} <container> -c " $@"
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