---
layout: container
name:  "quay.io/biocontainers/tesseract-assembler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tesseract-assembler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tesseract-assembler/container.yaml"
updated_at: "2026-08-27 12:44:14.187109"
latest: "1.2.2--h03affb9_0"
container_url: "https://biocontainers.pro/tools/tesseract-assembler"
aliases:
 - "tessera"
 - "tessera-model"
versions:
 - "1.2.2--h03affb9_0"
description: "singularity registry hpc automated addition for tesseract-assembler"
config: {"url": "https://biocontainers.pro/tools/tesseract-assembler", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tesseract-assembler", "latest": {"1.2.2--h03affb9_0": "sha256:00d4daee77d4a7e68c687adfc260afe91cbd251561d6526c035d0284ba85c730"}, "tags": {"1.2.2--h03affb9_0": "sha256:00d4daee77d4a7e68c687adfc260afe91cbd251561d6526c035d0284ba85c730"}, "docker": "quay.io/biocontainers/tesseract-assembler", "aliases": {"tessera": "/usr/local/bin/tessera", "tessera-model": "/usr/local/bin/tessera-model"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tesseract-assembler.
singularity registry hpc automated addition for tesseract-assembler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tesseract-assembler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tesseract-assembler:1.2.2--h03affb9_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tesseract-assembler/1.2.2--h03affb9_0
$ module help quay.io/biocontainers/tesseract-assembler/1.2.2--h03affb9_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tesseract-assembler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tesseract-assembler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tesseract-assembler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tesseract-assembler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tesseract-assembler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tesseract-assembler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tessera

```bash
$ singularity exec <container> /usr/local/bin/tessera
$ podman run --it --rm --entrypoint /usr/local/bin/tessera   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tessera   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tessera-model

```bash
$ singularity exec <container> /usr/local/bin/tessera-model
$ podman run --it --rm --entrypoint /usr/local/bin/tessera-model   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tessera-model   -v ${PWD} -w ${PWD} <container> -c " $@"
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