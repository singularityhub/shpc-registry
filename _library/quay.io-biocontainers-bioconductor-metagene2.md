---
layout: container
name:  "quay.io/biocontainers/bioconductor-metagene2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metagene2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metagene2/container.yaml"
updated_at: "2025-08-07 04:37:39.609725"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metagene2"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metagene2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metagene2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metagene2", "latest": {"1.22.0--r44hdfd78af_0": "sha256:8aa9d62f917ec2f1f9a38c3415604a7d120f8adb3591078c4f574dd56391beda"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:b43c0809e0da7df9a0a36d593af52bee4425a2fe01fcf2cf6d005887e228eef9", "1.14.0--r42hdfd78af_0": "sha256:8e8cd5815e31fd64e748cb4278f53e58689065fef853bb6c3f49f44b77383123", "1.10.0--r41hdfd78af_0": "sha256:52153a9597458d61086d006fd4650edcd0dd298944970675da9750bc88dbdec5", "1.16.0--r43hdfd78af_0": "sha256:916924dfcb025578f5893ab6adbc350e677d7388b4f5a1acba64d09a66f83a67", "1.18.0--r43hdfd78af_0": "sha256:a113fd4d73c38e58541483988a55236fdba5bae1621daf657fbb492e7244dc22", "1.22.0--r44hdfd78af_0": "sha256:8aa9d62f917ec2f1f9a38c3415604a7d120f8adb3591078c4f574dd56391beda"}, "docker": "quay.io/biocontainers/bioconductor-metagene2", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metagene2.
shpc-registry automated BioContainers addition for bioconductor-metagene2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metagene2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metagene2:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metagene2/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metagene2/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metagene2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metagene2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metagene2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metagene2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metagene2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metagene2-inspect-deffile:

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