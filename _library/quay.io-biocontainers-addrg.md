---
layout: container
name:  "quay.io/biocontainers/addrg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/addrg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/addrg/container.yaml"
updated_at: "2024-02-17 02:55:36.946893"
latest: "0.2.1--hbbffb53_11"
container_url: "https://biocontainers.pro/tools/addrg"
aliases:
 - "addrg"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.2.1--h8a6b41c_9"
 - "0.2.1--h04c669c_10"
 - "0.2.1--hbbffb53_11"
description: "shpc-registry automated BioContainers addition for addrg"
config: {"url": "https://biocontainers.pro/tools/addrg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for addrg", "latest": {"0.2.1--hbbffb53_11": "sha256:f0b70b384a6f2461b071cab978d6b79dbe3fb0aeecf5d78540c136f3f6e13065"}, "tags": {"0.2.1--h8a6b41c_9": "sha256:1c3fce8b7e81082864ca592d53913dabc7339f99e8f727698aa656b0ce7a70c7", "0.2.1--h04c669c_10": "sha256:e607aa7d0b22ec60f133d5540be5a0342fe4eedc7fcccc799ed6cb5f7c6f45ab", "0.2.1--hbbffb53_11": "sha256:f0b70b384a6f2461b071cab978d6b79dbe3fb0aeecf5d78540c136f3f6e13065"}, "docker": "quay.io/biocontainers/addrg", "aliases": {"addrg": "/usr/local/bin/addrg", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/addrg.
shpc-registry automated BioContainers addition for addrg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/addrg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/addrg:0.2.1--hbbffb53_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/addrg/0.2.1--hbbffb53_11
$ module help quay.io/biocontainers/addrg/0.2.1--hbbffb53_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### addrg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### addrg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### addrg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### addrg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### addrg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### addrg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addrg

```bash
$ singularity exec <container> /usr/local/bin/addrg
$ podman run --it --rm --entrypoint /usr/local/bin/addrg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addrg   -v ${PWD} -w ${PWD} <container> -c " $@"
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