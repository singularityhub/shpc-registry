---
layout: container
name:  "quay.io/biocontainers/bioconductor-amountain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-amountain/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-amountain/container.yaml"
updated_at: "2023-07-03 03:52:57.150022"
latest: "1.24.0--r42hee7dd41_2"
container_url: "https://biocontainers.pro/tools/bioconductor-amountain"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351ha21c8aa_0"
 - "1.20.0--r41hda872b5_3"
 - "1.18.0--r41ha4a0bc2_0"
 - "1.16.0--r40ha4a0bc2_1"
 - "1.14.0--r40hb42d971_0"
 - "1.12.0--r36h88e4a8a_0"
 - "1.24.0--r42hda872b5_0"
 - "1.24.0--r42hee7dd41_2"
description: "shpc-registry automated BioContainers addition for bioconductor-amountain"
config: {"url": "https://biocontainers.pro/tools/bioconductor-amountain", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-amountain", "latest": {"1.24.0--r42hee7dd41_2": "sha256:84334459c575d966fd1b38836ccd0b155d974a289a2cd63bd1b9cba0808d445b"}, "tags": {"1.8.0--r351ha21c8aa_0": "sha256:e87eec6beaf053f9cf2203a2f62a97567d4d3922c7cebb749151c689813ee5ba", "1.20.0--r41hda872b5_3": "sha256:ae5203490e6c6f09fa33ce1bcb2072a6ede3d522f44f121962f0ca2681777056", "1.18.0--r41ha4a0bc2_0": "sha256:85b91e4984da1cb3f37e39ba36e5272c7991b57ef7ebe70eda21aa1594d4fad8", "1.16.0--r40ha4a0bc2_1": "sha256:eef6d9f46c78634bf6984e836401f546d4c045f62282e5357f51ba89a8d903ef", "1.14.0--r40hb42d971_0": "sha256:a201e1042a7228270adf8e5ca281d7f6cbf5b8cd3adcd19bb3a24b3d0deef0f4", "1.12.0--r36h88e4a8a_0": "sha256:ea528b588a6bf881e339c1d707a9627297175e32fd2af2d775e015c3ba487f89", "1.24.0--r42hda872b5_0": "sha256:caae8e633f7373171b12003c1142e9b5689239017c1613a401254762780ab5a7", "1.24.0--r42hee7dd41_2": "sha256:84334459c575d966fd1b38836ccd0b155d974a289a2cd63bd1b9cba0808d445b"}, "docker": "quay.io/biocontainers/bioconductor-amountain", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-amountain.
shpc-registry automated BioContainers addition for bioconductor-amountain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-amountain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-amountain:1.24.0--r42hee7dd41_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-amountain/1.24.0--r42hee7dd41_2
$ module help quay.io/biocontainers/bioconductor-amountain/1.24.0--r42hee7dd41_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-amountain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-amountain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-amountain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-amountain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-amountain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-amountain-inspect-deffile:

```bash
$ singularity inspect -d <container>
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