---
layout: container
name:  "ghcr.io/autamus/cowsay"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/cowsay/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/cowsay/container.yaml"
updated_at: "2024-05-06 19:12:11.925168"
latest: "3.04"
container_url: "https://github.com/orgs/autamus/packages/container/package/cowsay"
aliases:
 - "cowsay"
versions:
 - "3.04"
 - "latest"
description: "What does the cow say?"
config: {"docker": "ghcr.io/autamus/cowsay", "url": "https://github.com/orgs/autamus/packages/container/package/cowsay", "maintainer": "@vsoch", "description": "What does the cow say?", "latest": {"3.04": "sha256:d0af39feede76382aa73a3938133e2415204be999997be1b24166e189b2e807b"}, "tags": {"3.04": "sha256:d0af39feede76382aa73a3938133e2415204be999997be1b24166e189b2e807b", "latest": "sha256:d0af39feede76382aa73a3938133e2415204be999997be1b24166e189b2e807b"}, "aliases": {"cowsay": "/opt/view/bin/cowsay"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/cowsay.
What does the cow say?
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/cowsay
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/cowsay:3.04
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/cowsay/3.04
$ module help ghcr.io/autamus/cowsay/3.04
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cowsay-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cowsay-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cowsay-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cowsay-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cowsay-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cowsay-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cowsay

```bash
$ singularity exec <container> /opt/view/bin/cowsay
$ podman run --it --rm --entrypoint /opt/view/bin/cowsay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cowsay   -v ${PWD} -w ${PWD} <container> -c " $@"
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