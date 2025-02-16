---
layout: container
name:  "quay.io/biocontainers/bioconductor-topconfects"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-topconfects/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-topconfects/container.yaml"
updated_at: "2025-02-16 03:28:34.656471"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-topconfects"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-topconfects"
config: {"url": "https://biocontainers.pro/tools/bioconductor-topconfects", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-topconfects", "latest": {"1.22.0--r44hdfd78af_0": "sha256:8acb4575598f4bbf7d2d4cb861e804198c947d7b7ccee87ff4060e1f6e359ab1"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:b58f263fecfac8ee2f0345b2c5a739f445f330286fb718213b7818a19dfd251d", "1.14.0--r42hdfd78af_0": "sha256:33295ff46b7d8456c28ee5adf743341847c44b3d94addbb7983cbd708a416ce4", "1.10.0--r41hdfd78af_0": "sha256:2e08200c00c3b7698c24b43141e2e2b2f13a21935c009c95ffc6b27f3515ca7e", "1.16.0--r43hdfd78af_0": "sha256:325a10042f260ec6b3da23078daf891ffa87246a1d9f236ab863d3464cd723d2", "1.18.0--r43hdfd78af_0": "sha256:553d684e10637fbdf22f5e3c5132eeb8d6b4ca416ef93a3b5a461790636815ec", "1.22.0--r44hdfd78af_0": "sha256:8acb4575598f4bbf7d2d4cb861e804198c947d7b7ccee87ff4060e1f6e359ab1"}, "docker": "quay.io/biocontainers/bioconductor-topconfects", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-topconfects.
shpc-registry automated BioContainers addition for bioconductor-topconfects
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-topconfects
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-topconfects:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-topconfects/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-topconfects/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-topconfects-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-topconfects-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-topconfects-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-topconfects-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-topconfects-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-topconfects-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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