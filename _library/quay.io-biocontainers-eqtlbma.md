---
layout: container
name:  "quay.io/biocontainers/eqtlbma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eqtlbma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eqtlbma/container.yaml"
updated_at: "2023-03-12 02:52:37.662976"
latest: "1.3.3--hcf8db43_3"
container_url: "https://biocontainers.pro/tools/eqtlbma"
aliases:
 - "eqtlbma_avg_bfs"
 - "eqtlbma_bf"
 - "eqtlbma_bf_parallel.bash"
 - "eqtlbma_hm"
 - "tutorial_eqtlbma.R"
 - "x86_64-conda-linux-gnu-gfortran.bin"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.3.3--hcf8db43_3"
description: "shpc-registry automated BioContainers addition for eqtlbma"
config: {"url": "https://biocontainers.pro/tools/eqtlbma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for eqtlbma", "latest": {"1.3.3--hcf8db43_3": "sha256:55a72cd5f2e4186941ad4337162a89ab2e21884b4480bee296ea3e2926cbec1a"}, "tags": {"1.3.3--hcf8db43_3": "sha256:55a72cd5f2e4186941ad4337162a89ab2e21884b4480bee296ea3e2926cbec1a"}, "docker": "quay.io/biocontainers/eqtlbma", "aliases": {"eqtlbma_avg_bfs": "/usr/local/bin/eqtlbma_avg_bfs", "eqtlbma_bf": "/usr/local/bin/eqtlbma_bf", "eqtlbma_bf_parallel.bash": "/usr/local/bin/eqtlbma_bf_parallel.bash", "eqtlbma_hm": "/usr/local/bin/eqtlbma_hm", "tutorial_eqtlbma.R": "/usr/local/bin/tutorial_eqtlbma.R", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eqtlbma.
shpc-registry automated BioContainers addition for eqtlbma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eqtlbma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eqtlbma:1.3.3--hcf8db43_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eqtlbma/1.3.3--hcf8db43_3
$ module help quay.io/biocontainers/eqtlbma/1.3.3--hcf8db43_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eqtlbma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eqtlbma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eqtlbma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eqtlbma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eqtlbma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eqtlbma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eqtlbma_avg_bfs

```bash
$ singularity exec <container> /usr/local/bin/eqtlbma_avg_bfs
$ podman run --it --rm --entrypoint /usr/local/bin/eqtlbma_avg_bfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eqtlbma_avg_bfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eqtlbma_bf

```bash
$ singularity exec <container> /usr/local/bin/eqtlbma_bf
$ podman run --it --rm --entrypoint /usr/local/bin/eqtlbma_bf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eqtlbma_bf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eqtlbma_bf_parallel.bash

```bash
$ singularity exec <container> /usr/local/bin/eqtlbma_bf_parallel.bash
$ podman run --it --rm --entrypoint /usr/local/bin/eqtlbma_bf_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eqtlbma_bf_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eqtlbma_hm

```bash
$ singularity exec <container> /usr/local/bin/eqtlbma_hm
$ podman run --it --rm --entrypoint /usr/local/bin/eqtlbma_hm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eqtlbma_hm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tutorial_eqtlbma.R

```bash
$ singularity exec <container> /usr/local/bin/tutorial_eqtlbma.R
$ podman run --it --rm --entrypoint /usr/local/bin/tutorial_eqtlbma.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tutorial_eqtlbma.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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