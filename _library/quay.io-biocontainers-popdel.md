---
layout: container
name:  "quay.io/biocontainers/popdel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/popdel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/popdel/container.yaml"
updated_at: "2025-01-06 03:02:22.592022"
latest: "1.5.0--h077b44d_8"
container_url: "https://biocontainers.pro/tools/popdel"
aliases:
 - "popdel"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.5.0--h867801b_4"
 - "1.5.0--hd36ca80_5"
 - "1.5.0--h146fbdb_6"
 - "1.5.0--hdcf5f25_7"
 - "1.5.0--h077b44d_8"
description: "shpc-registry automated BioContainers addition for popdel"
config: {"url": "https://biocontainers.pro/tools/popdel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for popdel", "latest": {"1.5.0--h077b44d_8": "sha256:aad96500cc4074f1c428069801d062ca62cea565e060065ac0b83c88cf3aeec7"}, "tags": {"1.5.0--h867801b_4": "sha256:cb479343ab3c3e10b3fac1ab81e6ee91226d417ff4a6c3a37d178d46c49ef8f4", "1.5.0--hd36ca80_5": "sha256:9ac70793d6a7909e242d0e5e155a474896841ea8ff286bec58ab1b3ef827bb18", "1.5.0--h146fbdb_6": "sha256:444ccb43c0491359bf597892de4129cf8664e8719679921f650caf74e79d7de6", "1.5.0--hdcf5f25_7": "sha256:321ba5de2d22de25e75e4f27d5444ac9e04726440e1849e3e675142d1f4301c2", "1.5.0--h077b44d_8": "sha256:aad96500cc4074f1c428069801d062ca62cea565e060065ac0b83c88cf3aeec7"}, "docker": "quay.io/biocontainers/popdel", "aliases": {"popdel": "/usr/local/bin/popdel", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/popdel.
shpc-registry automated BioContainers addition for popdel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/popdel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/popdel:1.5.0--h077b44d_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/popdel/1.5.0--h077b44d_8
$ module help quay.io/biocontainers/popdel/1.5.0--h077b44d_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### popdel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### popdel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### popdel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### popdel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### popdel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### popdel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### popdel

```bash
$ singularity exec <container> /usr/local/bin/popdel
$ podman run --it --rm --entrypoint /usr/local/bin/popdel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/popdel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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