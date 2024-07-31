---
layout: container
name:  "ghcr.io/autamus/wget"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/wget/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/wget/container.yaml"
updated_at: "2024-07-31 03:05:35.375835"
latest: "1.21.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/wget"
aliases:
 - "wget"
versions:
 - "1.21.1"
 - "latest"
 - "1.21.3"
description: "GNU Wget is a free software package for retrieving files using HTTP, HTTPS, FTP and FTPS, the most widely used Internet protocols."
config: {"docker": "ghcr.io/autamus/wget", "url": "https://github.com/orgs/autamus/packages/container/package/wget", "maintainer": "@vsoch", "description": "GNU Wget is a free software package for retrieving files using HTTP, HTTPS, FTP and FTPS, the most widely used Internet protocols.", "latest": {"1.21.1": "sha256:778b79c5811f523a69def3bd433a7ee2a5b37102a174be5e323c9003a587121c"}, "tags": {"1.21.1": "sha256:778b79c5811f523a69def3bd433a7ee2a5b37102a174be5e323c9003a587121c", "latest": "sha256:74bf7874ac7cc2de5cc6485ff56e4d228a2591ce4ac15c7ef4d72fccee587534", "1.21.3": "sha256:74bf7874ac7cc2de5cc6485ff56e4d228a2591ce4ac15c7ef4d72fccee587534"}, "aliases": {"wget": "/opt/view/bin/wget"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/wget.
GNU Wget is a free software package for retrieving files using HTTP, HTTPS, FTP and FTPS, the most widely used Internet protocols.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/wget
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/wget:1.21.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/wget/1.21.1
$ module help ghcr.io/autamus/wget/1.21.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wget-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wget-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wget-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wget-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wget-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wget-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /opt/view/bin/wget
$ podman run --it --rm --entrypoint /opt/view/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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