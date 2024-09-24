---
layout: container
name:  "quay.io/biocontainers/bioconductor-ttgsea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ttgsea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ttgsea/container.yaml"
updated_at: "2024-09-24 03:07:53.908932"
latest: "1.10.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-ttgsea"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-ttgsea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ttgsea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ttgsea", "latest": {"1.10.0--r43hdfd78af_1": "sha256:8aa08ef571ea303074ed12211fb8b0adca1ab9b4d7de07e0436e891a2e5a64dd"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:837b5f521ff1387391df7b08d09760d60ccd3ff2a8d83b8c2cde249eb93562b5", "1.6.0--r42hdfd78af_0": "sha256:a6a59145b63bf13fa6c0e725ee78590698a5f2aebfce2a1d75574049d389c947", "1.8.0--r43hdfd78af_0": "sha256:6a6975cd1427d8b832030e1af562bdeab0ca78d4943f52bf4493a32dbf93bb3e", "1.10.0--r43hdfd78af_1": "sha256:8aa08ef571ea303074ed12211fb8b0adca1ab9b4d7de07e0436e891a2e5a64dd"}, "docker": "quay.io/biocontainers/bioconductor-ttgsea"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ttgsea.
shpc-registry automated BioContainers addition for bioconductor-ttgsea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ttgsea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ttgsea:1.10.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ttgsea/1.10.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-ttgsea/1.10.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ttgsea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ttgsea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ttgsea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ttgsea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ttgsea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ttgsea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ttgsea

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