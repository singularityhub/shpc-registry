---
layout: container
name:  "quay.io/biocontainers/quip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/quip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/quip/container.yaml"
updated_at: "2023-03-04 03:05:25.644915"
latest: "1.1.8--h5bf99c6_1"
container_url: "https://biocontainers.pro/tools/quip"
aliases:
 - "bammd5"
 - "fastqmd5"
 - "quip"
 - "quipcat"
 - "unquip"
versions:
 - "1.1.8--h5bf99c6_1"
description: "shpc-registry automated BioContainers addition for quip"
config: {"url": "https://biocontainers.pro/tools/quip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for quip", "latest": {"1.1.8--h5bf99c6_1": "sha256:436b89302f0fdf85caae06fd03a844b515022595155773e43aacaf7d85dcf14d"}, "tags": {"1.1.8--h5bf99c6_1": "sha256:436b89302f0fdf85caae06fd03a844b515022595155773e43aacaf7d85dcf14d"}, "docker": "quay.io/biocontainers/quip", "aliases": {"bammd5": "/usr/local/bin/bammd5", "fastqmd5": "/usr/local/bin/fastqmd5", "quip": "/usr/local/bin/quip", "quipcat": "/usr/local/bin/quipcat", "unquip": "/usr/local/bin/unquip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/quip.
shpc-registry automated BioContainers addition for quip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/quip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/quip:1.1.8--h5bf99c6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/quip/1.1.8--h5bf99c6_1
$ module help quay.io/biocontainers/quip/1.1.8--h5bf99c6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bammd5

```bash
$ singularity exec <container> /usr/local/bin/bammd5
$ podman run --it --rm --entrypoint /usr/local/bin/bammd5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bammd5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqmd5

```bash
$ singularity exec <container> /usr/local/bin/fastqmd5
$ podman run --it --rm --entrypoint /usr/local/bin/fastqmd5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqmd5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quip

```bash
$ singularity exec <container> /usr/local/bin/quip
$ podman run --it --rm --entrypoint /usr/local/bin/quip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quipcat

```bash
$ singularity exec <container> /usr/local/bin/quipcat
$ podman run --it --rm --entrypoint /usr/local/bin/quipcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quipcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unquip

```bash
$ singularity exec <container> /usr/local/bin/unquip
$ podman run --it --rm --entrypoint /usr/local/bin/unquip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unquip   -v ${PWD} -w ${PWD} <container> -c " $@"
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