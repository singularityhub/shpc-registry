---
layout: container
name:  "quay.io/biocontainers/preseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/preseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/preseq/container.yaml"
updated_at: "2024-05-30 03:11:19.550305"
latest: "3.2.0--hdcf5f25_6"
container_url: "https://biocontainers.pro/tools/preseq"
aliases:
 - "preseq"
 - "to-mr"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "3.2.0--h867801b_3"
 - "3.2.0--hd36ca80_4"
 - "3.2.0--h146fbdb_5"
 - "3.2.0--hdcf5f25_6"
description: "shpc-registry automated BioContainers addition for preseq"
config: {"url": "https://biocontainers.pro/tools/preseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for preseq", "latest": {"3.2.0--hdcf5f25_6": "sha256:1eb53f4bb69b092bbef9d199a4ff177954e36ba13cf84c263326d37a95044475"}, "tags": {"3.2.0--h867801b_3": "sha256:b1d04c933457ce67cbe6fbc8d0a1877e417272796beb11f2bb31bed3c7dceeaa", "3.2.0--hd36ca80_4": "sha256:6c643d7caaa41e3d0fcdacdd1c391181a2ef38520f6a2d6709eb83d0a46a5813", "3.2.0--h146fbdb_5": "sha256:3b88ab655ba62f426f97ab5004cc6c0f74d7c9f86bd17acff055c5150165ffbd", "3.2.0--hdcf5f25_6": "sha256:1eb53f4bb69b092bbef9d199a4ff177954e36ba13cf84c263326d37a95044475"}, "docker": "quay.io/biocontainers/preseq", "aliases": {"preseq": "/usr/local/bin/preseq", "to-mr": "/usr/local/bin/to-mr", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/preseq.
shpc-registry automated BioContainers addition for preseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/preseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/preseq:3.2.0--hdcf5f25_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/preseq/3.2.0--hdcf5f25_6
$ module help quay.io/biocontainers/preseq/3.2.0--hdcf5f25_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### preseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### preseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### preseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### preseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### preseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### preseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### preseq

```bash
$ singularity exec <container> /usr/local/bin/preseq
$ podman run --it --rm --entrypoint /usr/local/bin/preseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/preseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### to-mr

```bash
$ singularity exec <container> /usr/local/bin/to-mr
$ podman run --it --rm --entrypoint /usr/local/bin/to-mr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/to-mr   -v ${PWD} -w ${PWD} <container> -c " $@"
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