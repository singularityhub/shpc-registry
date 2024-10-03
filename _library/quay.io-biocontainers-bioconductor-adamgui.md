---
layout: container
name:  "quay.io/biocontainers/bioconductor-adamgui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-adamgui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-adamgui/container.yaml"
updated_at: "2024-10-03 03:03:56.342901"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-adamgui"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-adamgui"
config: {"url": "https://biocontainers.pro/tools/bioconductor-adamgui", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-adamgui", "latest": {"1.18.0--r43hdfd78af_0": "sha256:7cdaf7bf81c94ed13dbf9edd88a6467022db977b23bc3e535c8159f2ec8ce82a"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:4c472a14d2fc8ee2e39dcd1a1c9bc69284893d193c617798ca0a30dc31bba1c5", "1.10.0--r41hdfd78af_0": "sha256:cf94bced1841396083c7905d82099c4799801895992ff249bb4f198da88f6c9d", "1.14.0--r42hdfd78af_0": "sha256:ac65acbb093d0fc2c0d631539d3e5e0c0cdd846b626e1120afd499aba49a595d", "1.16.0--r43hdfd78af_0": "sha256:fc88d0945d8ad2859a85300fdbc8008a3304fcd7a0ede3447bac5b3f0bf4ab91", "1.18.0--r43hdfd78af_0": "sha256:7cdaf7bf81c94ed13dbf9edd88a6467022db977b23bc3e535c8159f2ec8ce82a"}, "docker": "quay.io/biocontainers/bioconductor-adamgui", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-adamgui.
shpc-registry automated BioContainers addition for bioconductor-adamgui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-adamgui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-adamgui:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-adamgui/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-adamgui/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-adamgui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adamgui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adamgui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-adamgui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-adamgui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-adamgui-inspect-deffile:

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