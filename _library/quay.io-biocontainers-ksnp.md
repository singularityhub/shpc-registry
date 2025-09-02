---
layout: container
name:  "quay.io/biocontainers/ksnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ksnp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ksnp/container.yaml"
updated_at: "2025-09-02 03:19:29.958518"
latest: "1.0.3--h077b44d_2"
container_url: "https://biocontainers.pro/tools/ksnp"
aliases:
 - "ksnp"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0.3--h146fbdb_0"
 - "1.0.3--hdcf5f25_1"
 - "1.0.3--h077b44d_2"
description: "singularity registry hpc automated addition for ksnp"
config: {"url": "https://biocontainers.pro/tools/ksnp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ksnp", "latest": {"1.0.3--h077b44d_2": "sha256:cf19b3368c9a5c2ac6038bc03bdb6e2ad46146149793b75f4a7b978731e206b9"}, "tags": {"1.0.3--h146fbdb_0": "sha256:8e4d1565d5769ae33cbdc8c4a7ef8eb02b5dffb5de406cce787840fd87173888", "1.0.3--hdcf5f25_1": "sha256:1b30d594b3768a1305b1c64dde8d3a3514434521482993123b010dfb56ce8523", "1.0.3--h077b44d_2": "sha256:cf19b3368c9a5c2ac6038bc03bdb6e2ad46146149793b75f4a7b978731e206b9"}, "docker": "quay.io/biocontainers/ksnp", "aliases": {"ksnp": "/usr/local/bin/ksnp", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ksnp.
singularity registry hpc automated addition for ksnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ksnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ksnp:1.0.3--h077b44d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ksnp/1.0.3--h077b44d_2
$ module help quay.io/biocontainers/ksnp/1.0.3--h077b44d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ksnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ksnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ksnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ksnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ksnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ksnp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ksnp

```bash
$ singularity exec <container> /usr/local/bin/ksnp
$ podman run --it --rm --entrypoint /usr/local/bin/ksnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ksnp   -v ${PWD} -w ${PWD} <container> -c " $@"
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