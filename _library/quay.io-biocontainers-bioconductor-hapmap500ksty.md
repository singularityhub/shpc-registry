---
layout: container
name:  "quay.io/biocontainers/bioconductor-hapmap500ksty"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hapmap500ksty/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hapmap500ksty/container.yaml"
updated_at: "2023-09-25 04:11:00.720437"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hapmap500ksty"

versions:
 - "1.36.0--r41hdfd78af_1"
 - "1.39.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hapmap500ksty"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hapmap500ksty", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hapmap500ksty", "latest": {"1.42.0--r43hdfd78af_0": "sha256:d1e7e2b3280eb5e17bf738c952c4d8292f5d15b17778252875f75b39e5e0b0cf"}, "tags": {"1.36.0--r41hdfd78af_1": "sha256:3bbeed4d0fee56ceaf8573720b599a10f29aee461f6b47b9c489b74c9365a25d", "1.39.0--r42hdfd78af_0": "sha256:2fc4b4f162c511030163107fcc839b219d021819cba2ee3d3bf2e2447c0edd3c", "1.42.0--r43hdfd78af_0": "sha256:d1e7e2b3280eb5e17bf738c952c4d8292f5d15b17778252875f75b39e5e0b0cf"}, "docker": "quay.io/biocontainers/bioconductor-hapmap500ksty"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hapmap500ksty.
shpc-registry automated BioContainers addition for bioconductor-hapmap500ksty
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmap500ksty
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmap500ksty:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hapmap500ksty/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hapmap500ksty/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hapmap500ksty-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmap500ksty-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmap500ksty-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hapmap500ksty-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hapmap500ksty-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hapmap500ksty-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hapmap500ksty

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