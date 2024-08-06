---
layout: container
name:  "quay.io/biocontainers/bioawk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioawk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioawk/container.yaml"
updated_at: "2024-08-06 02:58:07.115836"
latest: "1.0--he4a0461_12"
container_url: "https://biocontainers.pro/tools/bioawk"
aliases:
 - "bioawk"
versions:
 - "1.0--h7132678_7"
 - "1.0--h7132678_8"
 - "1.0--he4a0461_9"
 - "1.0--he4a0461_10"
 - "1.0--he4a0461_12"
description: "shpc-registry automated BioContainers addition for bioawk"
config: {"url": "https://biocontainers.pro/tools/bioawk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioawk", "latest": {"1.0--he4a0461_12": "sha256:08727a9af12d29bfca0b97ab4081133227a64de402c964cc83115d8daa6ef015"}, "tags": {"1.0--h7132678_7": "sha256:0eff4c13f667526eaad90302737c5b7c01d63b3b876e81b4cd7723af5c5a118b", "1.0--h7132678_8": "sha256:e845d58f2e19aacec8e5cc48764639296c0f13d34bf84190b309a7ee471bcef3", "1.0--he4a0461_9": "sha256:55a0b991fd0057f91ead905cc6eedbf107d352a45eec9d29177ea9b4e3bda557", "1.0--he4a0461_10": "sha256:97bb4704bb1b01c38ed9f468430a8bfe03fedafea417794e3b004954be79502c", "1.0--he4a0461_12": "sha256:08727a9af12d29bfca0b97ab4081133227a64de402c964cc83115d8daa6ef015"}, "docker": "quay.io/biocontainers/bioawk", "aliases": {"bioawk": "/usr/local/bin/bioawk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioawk.
shpc-registry automated BioContainers addition for bioawk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioawk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioawk:1.0--he4a0461_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioawk/1.0--he4a0461_12
$ module help quay.io/biocontainers/bioawk/1.0--he4a0461_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioawk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioawk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioawk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioawk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioawk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioawk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bioawk

```bash
$ singularity exec <container> /usr/local/bin/bioawk
$ podman run --it --rm --entrypoint /usr/local/bin/bioawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioawk   -v ${PWD} -w ${PWD} <container> -c " $@"
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