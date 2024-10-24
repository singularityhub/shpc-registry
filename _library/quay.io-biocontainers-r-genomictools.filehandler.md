---
layout: container
name:  "quay.io/biocontainers/r-genomictools.filehandler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-genomictools.filehandler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-genomictools.filehandler/container.yaml"
updated_at: "2024-10-24 11:14:04.247168"
latest: "0.1.5.9--r43h3342da4_4"
container_url: "https://biocontainers.pro/tools/r-genomictools.filehandler"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.1.5.9--r41h3342da4_2"
 - "0.1.5.9--r42h3342da4_3"
 - "0.1.5.9--r43h3342da4_4"
description: "shpc-registry automated BioContainers addition for r-genomictools.filehandler"
config: {"url": "https://biocontainers.pro/tools/r-genomictools.filehandler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-genomictools.filehandler", "latest": {"0.1.5.9--r43h3342da4_4": "sha256:5896fb7580fa3a571ad706a8cde4143e80104c9d26073731faee77195b9593ae"}, "tags": {"0.1.5.9--r41h3342da4_2": "sha256:98795ab4220f4904cccafe80c51f15c52be8b5a035c8492685ab6a9150a0a246", "0.1.5.9--r42h3342da4_3": "sha256:76c86448bac8563e1293c74d8a357cf55e1fe40f1c1c98220669136e23dd8c18", "0.1.5.9--r43h3342da4_4": "sha256:5896fb7580fa3a571ad706a8cde4143e80104c9d26073731faee77195b9593ae"}, "docker": "quay.io/biocontainers/r-genomictools.filehandler", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-genomictools.filehandler.
shpc-registry automated BioContainers addition for r-genomictools.filehandler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-genomictools.filehandler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-genomictools.filehandler:0.1.5.9--r43h3342da4_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-genomictools.filehandler/0.1.5.9--r43h3342da4_4
$ module help quay.io/biocontainers/r-genomictools.filehandler/0.1.5.9--r43h3342da4_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-genomictools.filehandler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-genomictools.filehandler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-genomictools.filehandler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-genomictools.filehandler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-genomictools.filehandler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-genomictools.filehandler-inspect-deffile:

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