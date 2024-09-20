---
layout: container
name:  "ghcr.io/autamus/htslib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/htslib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/htslib/container.yaml"
updated_at: "2024-09-20 03:34:29.852851"
latest: "1.15.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/htslib"
aliases:
 - "htsfile"
versions:
 - "1.12"
 - "1.13"
 - "1.14"
 - "latest"
 - "1.15.1"
description: "A C library for reading/writing high-throughput sequencing data."
config: {"docker": "ghcr.io/autamus/htslib", "url": "https://github.com/orgs/autamus/packages/container/package/htslib", "maintainer": "@vsoch", "description": "A C library for reading/writing high-throughput sequencing data.", "latest": {"1.15.1": "sha256:be82ce023b25dbe27b1f2dcb4824a0b31e32f98aa9c00c6d1a475b7bb7b3be9e"}, "tags": {"1.12": "sha256:20fe48b8413f5039e6c7b8749702e931b187f3d24078f67fcaaebcba5b482318", "1.13": "sha256:712ad250d973b7cd460d93ece88038502ca8a8a70310a09f029da0f71f08865d", "1.14": "sha256:c328cb17c9942642975eafb75ac063b9249da5c5a3a49711ad338e191256eb8f", "latest": "sha256:be82ce023b25dbe27b1f2dcb4824a0b31e32f98aa9c00c6d1a475b7bb7b3be9e", "1.15.1": "sha256:be82ce023b25dbe27b1f2dcb4824a0b31e32f98aa9c00c6d1a475b7bb7b3be9e"}, "aliases": {"htsfile": "/opt/view/bin/htsfile"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/htslib.
A C library for reading/writing high-throughput sequencing data.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/htslib
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/htslib:1.15.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/htslib/1.15.1
$ module help ghcr.io/autamus/htslib/1.15.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### htslib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### htslib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### htslib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### htslib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### htslib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### htslib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### htsfile

```bash
$ singularity exec <container> /opt/view/bin/htsfile
$ podman run --it --rm --entrypoint /opt/view/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
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