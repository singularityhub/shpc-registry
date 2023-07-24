---
layout: container
name:  "quay.io/biocontainers/bioconductor-ritan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ritan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ritan/container.yaml"
updated_at: "2023-07-24 02:54:34.725073"
latest: "1.22.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ritan"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.17.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ritan"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ritan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ritan", "latest": {"1.22.0--r42hdfd78af_0": "sha256:4847a907fbcc9c8bc82a8605c8de6cb45ec20ec8e8bdb83237c2091ccb8f4c2e"}, "tags": {"1.8.0--r36_1": "sha256:cdbb92aa8369d23ed96e47fdca858a2e3eadc7f7ccec13dd90ab7eeedc4de399", "1.22.0--r42hdfd78af_0": "sha256:4847a907fbcc9c8bc82a8605c8de6cb45ec20ec8e8bdb83237c2091ccb8f4c2e", "1.17.0--r41hdfd78af_0": "sha256:8226cd0159029ee6f4cb33355494116fb4e65a64cf4a8228f4eea775eae18bc3", "1.16.0--r41hdfd78af_0": "sha256:1bf84f29a49ab2b9007cc5409ef1e7c9923cdaad85ea23b38487608fd708f4f1", "1.14.0--r40hdfd78af_1": "sha256:e2c3577e05b6cc2507ab0320b5d9811d790898e45297655c59098a08ae800ebd", "1.12.0--r40_0": "sha256:b70f6cf02a0481576fc918b15314b5424241b0e7b9a24938cb4866ce4113dd5c"}, "docker": "quay.io/biocontainers/bioconductor-ritan", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ritan.
shpc-registry automated BioContainers addition for bioconductor-ritan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ritan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ritan:1.22.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ritan/1.22.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ritan/1.22.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ritan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ritan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ritan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ritan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ritan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ritan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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