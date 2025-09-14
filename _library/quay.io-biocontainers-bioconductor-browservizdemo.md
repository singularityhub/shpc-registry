---
layout: container
name:  "quay.io/biocontainers/bioconductor-browservizdemo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-browservizdemo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-browservizdemo/container.yaml"
updated_at: "2025-09-14 03:52:55.808348"
latest: "1.11.0--r351hfc679d8_0"
container_url: "https://biocontainers.pro/tools/bioconductor-browservizdemo"

versions:
 - "1.11.0--r351hfc679d8_0"
 - "1.11.0--r341hfc679d8_0"
description: "shpc-registry automated BioContainers addition for bioconductor-browservizdemo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-browservizdemo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-browservizdemo", "latest": {"1.11.0--r351hfc679d8_0": "sha256:5c2a75dee3a87a8a81df1965cb0f6019c81ac4a321d34dabe4b00c0aa1ac317f"}, "tags": {"1.11.0--r351hfc679d8_0": "sha256:5c2a75dee3a87a8a81df1965cb0f6019c81ac4a321d34dabe4b00c0aa1ac317f", "1.11.0--r341hfc679d8_0": "sha256:0b7d0e439c71b7dc36b5e7ffa704220fc7e2cce0d67b1d99776d66ea0332c6da"}, "docker": "quay.io/biocontainers/bioconductor-browservizdemo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-browservizdemo.
shpc-registry automated BioContainers addition for bioconductor-browservizdemo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-browservizdemo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-browservizdemo:1.11.0--r351hfc679d8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-browservizdemo/1.11.0--r351hfc679d8_0
$ module help quay.io/biocontainers/bioconductor-browservizdemo/1.11.0--r351hfc679d8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-browservizdemo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-browservizdemo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-browservizdemo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-browservizdemo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-browservizdemo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-browservizdemo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-browservizdemo

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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