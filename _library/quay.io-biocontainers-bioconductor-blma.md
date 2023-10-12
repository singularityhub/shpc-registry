---
layout: container
name:  "quay.io/biocontainers/bioconductor-blma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-blma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-blma/container.yaml"
updated_at: "2023-10-12 03:43:04.955574"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-blma"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-blma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-blma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-blma", "latest": {"1.24.0--r43hdfd78af_0": "sha256:e19dcc3a1dc1c1bf635d8c61afa3c25ef2ba289f5e955c68c433ac0484be94c5"}, "tags": {"1.8.0--r36_1": "sha256:7b91129b99513cce5e35e6e44e305bd4ad18777769692214694a72aa28ddf5a8", "1.22.0--r42hdfd78af_0": "sha256:cce8a8f887835984101d7f04beb7f750fa6501be1e3ac9e895d697e2847c98da", "1.18.0--r41hdfd78af_0": "sha256:e30e573271ec97ef3825e8b30f82838f89bb8002197ba0a6d1fa835e502f6123", "1.16.0--r41hdfd78af_0": "sha256:e79c16bcf536ed72e071806d7184c2173376ed7fc96839d8aff527b903a92715", "1.14.0--r40hdfd78af_1": "sha256:997c2a78698d4dd148c0b795c4445b52e5d24fb1e644c2ac00ddd812bbf6f700", "1.12.0--r40_0": "sha256:9b78b08e9669ab9c95b5453976a97f5df0cfacf00febfbcd091e892d1a46b451", "1.24.0--r43hdfd78af_0": "sha256:e19dcc3a1dc1c1bf635d8c61afa3c25ef2ba289f5e955c68c433ac0484be94c5"}, "docker": "quay.io/biocontainers/bioconductor-blma", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-blma.
shpc-registry automated BioContainers addition for bioconductor-blma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-blma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-blma:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-blma/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-blma/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-blma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-blma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-blma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-blma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-blma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-blma-inspect-deffile:

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