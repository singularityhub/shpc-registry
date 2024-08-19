---
layout: container
name:  "quay.io/biocontainers/rabbitqcplus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rabbitqcplus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rabbitqcplus/container.yaml"
updated_at: "2024-08-19 03:13:29.998493"
latest: "2.2.9--h43eeafb_1"
container_url: "https://biocontainers.pro/tools/rabbitqcplus"
aliases:
 - "RabbitQCPlus"
 - "rabbitqcplus"
versions:
 - "2.2.9--h43eeafb_0"
 - "2.2.9--h43eeafb_1"
description: "singularity registry hpc automated addition for rabbitqcplus"
config: {"url": "https://biocontainers.pro/tools/rabbitqcplus", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rabbitqcplus", "latest": {"2.2.9--h43eeafb_1": "sha256:1c9b8c4b585ad58016b8ebcd2772fe016d090927d85ede84ec5fccc72e4d4c98"}, "tags": {"2.2.9--h43eeafb_0": "sha256:f51b039b364284aa991e2be51dc9478633cfe395a1fbc47b0abd5347cfde58f9", "2.2.9--h43eeafb_1": "sha256:1c9b8c4b585ad58016b8ebcd2772fe016d090927d85ede84ec5fccc72e4d4c98"}, "docker": "quay.io/biocontainers/rabbitqcplus", "aliases": {"RabbitQCPlus": "/usr/local/bin/RabbitQCPlus", "rabbitqcplus": "/usr/local/bin/rabbitqcplus"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rabbitqcplus.
singularity registry hpc automated addition for rabbitqcplus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rabbitqcplus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rabbitqcplus:2.2.9--h43eeafb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rabbitqcplus/2.2.9--h43eeafb_1
$ module help quay.io/biocontainers/rabbitqcplus/2.2.9--h43eeafb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rabbitqcplus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rabbitqcplus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rabbitqcplus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rabbitqcplus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rabbitqcplus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rabbitqcplus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RabbitQCPlus

```bash
$ singularity exec <container> /usr/local/bin/RabbitQCPlus
$ podman run --it --rm --entrypoint /usr/local/bin/RabbitQCPlus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RabbitQCPlus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitqcplus

```bash
$ singularity exec <container> /usr/local/bin/rabbitqcplus
$ podman run --it --rm --entrypoint /usr/local/bin/rabbitqcplus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rabbitqcplus   -v ${PWD} -w ${PWD} <container> -c " $@"
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