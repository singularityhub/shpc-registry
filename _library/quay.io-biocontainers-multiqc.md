---
layout: container
name:  "quay.io/biocontainers/multiqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/multiqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/multiqc/container.yaml"
updated_at: "2023-12-29 02:29:49.075815"
latest: "1.12--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/multiqc"
aliases:
 - "multiqc"
versions:
 - "1.9--py_1"
 - "1.10.1--pyhdfd78af_1"
 - "1.11--pyhdfd78af_0"
 - "1.12--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for multiqc"
config: {"url": "https://biocontainers.pro/tools/multiqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for multiqc", "latest": {"1.12--pyhdfd78af_0": "sha256:82dae6463e1b19fafb6022401186300b66decf5ce319a725271700fe4e32e12a"}, "tags": {"1.9--py_1": "sha256:67cc651cb350b1ee2fc0929bd6bcd5189ec8c17f09566a3cd54cde7479e48a09", "1.10.1--pyhdfd78af_1": "sha256:c64ea8fcaf49dfc4b0594bc7349e6d1a662eb4484f5aac3252f4eea86cad164c", "1.11--pyhdfd78af_0": "sha256:88df23fac5b9eecda9943d922f81b68e30188eb4dd7cbfe9554e952ff5a3b0ee", "1.12--pyhdfd78af_0": "sha256:82dae6463e1b19fafb6022401186300b66decf5ce319a725271700fe4e32e12a"}, "docker": "quay.io/biocontainers/multiqc", "aliases": {"multiqc": "/usr/local/bin/multiqc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/multiqc.
shpc-registry automated BioContainers addition for multiqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/multiqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/multiqc:1.12--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/multiqc/1.12--pyhdfd78af_0
$ module help quay.io/biocontainers/multiqc/1.12--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### multiqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### multiqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### multiqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### multiqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### multiqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### multiqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### multiqc

```bash
$ singularity exec <container> /usr/local/bin/multiqc
$ podman run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
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