---
layout: container
name:  "ghcr.io/autamus/mercurial"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/mercurial/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/mercurial/container.yaml"
updated_at: "2025-01-18 02:41:14.392108"
latest: "5.8"
container_url: "https://github.com/orgs/autamus/packages/container/package/mercurial"
aliases:
 - "hg"
versions:
 - "5.7.1"
 - "5.8"
 - "latest"
description: "Mercurial is a distributed revision control tool for software developers."
config: {"docker": "ghcr.io/autamus/mercurial", "url": "https://github.com/orgs/autamus/packages/container/package/mercurial", "maintainer": "@vsoch", "description": "Mercurial is a distributed revision control tool for software developers.", "latest": {"5.8": "sha256:17a6a0f03fef5de91a1cffbfdf12a5fd6c285391a748f28dffb30c285551c152"}, "tags": {"5.7.1": "sha256:5671150262c821b0b66376c50f74a577a9f04d1668f25f0f4d2b414c4d14d94f", "5.8": "sha256:17a6a0f03fef5de91a1cffbfdf12a5fd6c285391a748f28dffb30c285551c152", "latest": "sha256:17a6a0f03fef5de91a1cffbfdf12a5fd6c285391a748f28dffb30c285551c152"}, "aliases": {"hg": "/opt/view/bin/hg"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/mercurial.
Mercurial is a distributed revision control tool for software developers.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/mercurial
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/mercurial:5.8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/mercurial/5.8
$ module help ghcr.io/autamus/mercurial/5.8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mercurial-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mercurial-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mercurial-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mercurial-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mercurial-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mercurial-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hg

```bash
$ singularity exec <container> /opt/view/bin/hg
$ podman run --it --rm --entrypoint /opt/view/bin/hg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hg   -v ${PWD} -w ${PWD} <container> -c " $@"
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