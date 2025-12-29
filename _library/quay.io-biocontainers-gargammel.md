---
layout: container
name:  "quay.io/biocontainers/gargammel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gargammel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gargammel/container.yaml"
updated_at: "2025-12-29 04:42:45.186715"
latest: "1.1.4--hb66fcc3_0"
container_url: "https://biocontainers.pro/tools/gargammel"

versions:
 - "1.1.2--h51667aa_5"
 - "1.1.2--he905c8f_6"
 - "1.1.4--hb66fcc3_0"
description: "shpc-registry automated BioContainers addition for gargammel"
config: {"url": "https://biocontainers.pro/tools/gargammel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gargammel", "latest": {"1.1.4--hb66fcc3_0": "sha256:b0975a41756dfb9700eb44629020524c606845dba5934551281f405d771b5049"}, "tags": {"1.1.2--h51667aa_5": "sha256:84dc92dc17243162063fc7b48d3ca13778c6b8a7b1670f6de824283baf646b4c", "1.1.2--he905c8f_6": "sha256:1c24122fa44fed0f0daaac738df1eff97386d64c0c26dd04bfcaf650aec93d49", "1.1.4--hb66fcc3_0": "sha256:b0975a41756dfb9700eb44629020524c606845dba5934551281f405d771b5049"}, "docker": "quay.io/biocontainers/gargammel"}
---

This module is a singularity container wrapper for quay.io/biocontainers/gargammel.
shpc-registry automated BioContainers addition for gargammel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gargammel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gargammel:1.1.4--hb66fcc3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gargammel/1.1.4--hb66fcc3_0
$ module help quay.io/biocontainers/gargammel/1.1.4--hb66fcc3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gargammel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gargammel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gargammel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gargammel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gargammel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gargammel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gargammel

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