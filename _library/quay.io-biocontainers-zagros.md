---
layout: container
name:  "quay.io/biocontainers/zagros"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/zagros/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/zagros/container.yaml"
updated_at: "2024-01-11 04:03:01.074585"
latest: "1.0.0--h733e4d7_9"
container_url: "https://biocontainers.pro/tools/zagros"
aliases:
 - "extractDEs"
 - "thermo"
 - "zagros"
versions:
 - "1.0.0--h7fd9d64_7"
 - "1.0.0--h733e4d7_9"
description: "shpc-registry automated BioContainers addition for zagros"
config: {"url": "https://biocontainers.pro/tools/zagros", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for zagros", "latest": {"1.0.0--h733e4d7_9": "sha256:a0944481536903408fe95a79d82b67f5fb2aa5a1221fd8de35d4e6719468542b"}, "tags": {"1.0.0--h7fd9d64_7": "sha256:fdb6b2e961a0efb21a41047c0c27d7dfeb49eeef3ef8cbb762e7dcd54848acc1", "1.0.0--h733e4d7_9": "sha256:a0944481536903408fe95a79d82b67f5fb2aa5a1221fd8de35d4e6719468542b"}, "docker": "quay.io/biocontainers/zagros", "aliases": {"extractDEs": "/usr/local/bin/extractDEs", "thermo": "/usr/local/bin/thermo", "zagros": "/usr/local/bin/zagros"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/zagros.
shpc-registry automated BioContainers addition for zagros
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/zagros
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/zagros:1.0.0--h733e4d7_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/zagros/1.0.0--h733e4d7_9
$ module help quay.io/biocontainers/zagros/1.0.0--h733e4d7_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### zagros-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### zagros-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### zagros-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### zagros-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### zagros-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### zagros-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### extractDEs

```bash
$ singularity exec <container> /usr/local/bin/extractDEs
$ podman run --it --rm --entrypoint /usr/local/bin/extractDEs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractDEs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thermo

```bash
$ singularity exec <container> /usr/local/bin/thermo
$ podman run --it --rm --entrypoint /usr/local/bin/thermo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thermo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zagros

```bash
$ singularity exec <container> /usr/local/bin/zagros
$ podman run --it --rm --entrypoint /usr/local/bin/zagros   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zagros   -v ${PWD} -w ${PWD} <container> -c " $@"
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