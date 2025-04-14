---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellbench"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellbench/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellbench/container.yaml"
updated_at: "2025-04-14 03:10:22.009933"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellbench"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellbench"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellbench", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellbench", "latest": {"1.22.0--r44hdfd78af_0": "sha256:af280057443b8eab8aa46891f6fe8db49ba8b86d67f558330563378069c7fb9f"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:811c0963c07be52ab3ca2a324dbe4e7591ad3b3ce0ce061d85d10c85b253bb3e", "1.14.0--r42hdfd78af_0": "sha256:e096606d6875a980b604bf735be6f9f7a0b4b9275f3b877d86bbb765ad65afcd", "1.10.0--r41hdfd78af_0": "sha256:bfaea4d2f0b8f7a6913275022e5ec18adad12bbc4b019492c687d69a9a5c282c", "1.16.0--r43hdfd78af_0": "sha256:c046fe9f67bee26d32b18b36fc5ab1f4dd419d2922e16c72285d1c9318f3fe9b", "1.18.0--r43hdfd78af_0": "sha256:912e62aa12080feff990914e453ca2411803ca7cd28a2594760e18510ce3353f", "1.22.0--r44hdfd78af_0": "sha256:af280057443b8eab8aa46891f6fe8db49ba8b86d67f558330563378069c7fb9f"}, "docker": "quay.io/biocontainers/bioconductor-cellbench", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellbench.
shpc-registry automated BioContainers addition for bioconductor-cellbench
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellbench
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellbench:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellbench/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cellbench/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellbench-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellbench-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellbench-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellbench-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellbench-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellbench-inspect-deffile:

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