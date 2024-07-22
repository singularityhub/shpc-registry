---
layout: container
name:  "quay.io/biocontainers/scallop-umi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scallop-umi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scallop-umi/container.yaml"
updated_at: "2024-07-22 02:39:41.766776"
latest: "1.1.0--hbce0939_0"
container_url: "https://biocontainers.pro/tools/scallop-umi"
aliases:
 - "scallop-umi"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.1.0--hbce0939_0"
description: "shpc-registry automated BioContainers addition for scallop-umi"
config: {"url": "https://biocontainers.pro/tools/scallop-umi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scallop-umi", "latest": {"1.1.0--hbce0939_0": "sha256:18c63a8e99bb356484a5b3b3718454fb4fc6bb4bc5981a71f64b411e6b19c29a"}, "tags": {"1.1.0--hbce0939_0": "sha256:18c63a8e99bb356484a5b3b3718454fb4fc6bb4bc5981a71f64b411e6b19c29a"}, "docker": "quay.io/biocontainers/scallop-umi", "aliases": {"scallop-umi": "/usr/local/bin/scallop-umi", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scallop-umi.
shpc-registry automated BioContainers addition for scallop-umi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scallop-umi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scallop-umi:1.1.0--hbce0939_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scallop-umi/1.1.0--hbce0939_0
$ module help quay.io/biocontainers/scallop-umi/1.1.0--hbce0939_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scallop-umi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scallop-umi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scallop-umi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scallop-umi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scallop-umi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scallop-umi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scallop-umi

```bash
$ singularity exec <container> /usr/local/bin/scallop-umi
$ podman run --it --rm --entrypoint /usr/local/bin/scallop-umi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scallop-umi   -v ${PWD} -w ${PWD} <container> -c " $@"
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