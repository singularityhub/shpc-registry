---
layout: container
name:  "quay.io/biocontainers/longgf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/longgf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/longgf/container.yaml"
updated_at: "2025-07-27 04:34:47.287188"
latest: "0.1.2--h9948957_8"
container_url: "https://biocontainers.pro/tools/longgf"
aliases:
 - "LongGF"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.1.2--h28e74a2_4"
 - "0.1.2--hf77a93e_5"
 - "0.1.2--h84372a0_6"
 - "0.1.2--h4ac6f70_7"
 - "0.1.2--h9948957_8"
description: "shpc-registry automated BioContainers addition for longgf"
config: {"url": "https://biocontainers.pro/tools/longgf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for longgf", "latest": {"0.1.2--h9948957_8": "sha256:c79e28860c7097222ab4ccb170ef795da68babc3b7ba60e0be35d04ce363f9b8"}, "tags": {"0.1.2--h28e74a2_4": "sha256:60f7ff2f499d28f8a4ff17fce5691a582a3d362cc667abdda55e00d803bf32bd", "0.1.2--hf77a93e_5": "sha256:e6f5e764731c7638693b4cb01607d8e9ed43b019bb9df407a2150a8a9596e3d4", "0.1.2--h84372a0_6": "sha256:41c05b0e46b34d19dbfb6d604067c1e917085ada12184bae1a46115f84953036", "0.1.2--h4ac6f70_7": "sha256:f064ef758bef432a54a46e38c220a616d92f39ba8d01a2215091206a8a649b51", "0.1.2--h9948957_8": "sha256:c79e28860c7097222ab4ccb170ef795da68babc3b7ba60e0be35d04ce363f9b8"}, "docker": "quay.io/biocontainers/longgf", "aliases": {"LongGF": "/usr/local/bin/LongGF", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/longgf.
shpc-registry automated BioContainers addition for longgf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/longgf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/longgf:0.1.2--h9948957_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/longgf/0.1.2--h9948957_8
$ module help quay.io/biocontainers/longgf/0.1.2--h9948957_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### longgf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### longgf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### longgf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### longgf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### longgf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### longgf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LongGF

```bash
$ singularity exec <container> /usr/local/bin/LongGF
$ podman run --it --rm --entrypoint /usr/local/bin/LongGF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LongGF   -v ${PWD} -w ${PWD} <container> -c " $@"
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