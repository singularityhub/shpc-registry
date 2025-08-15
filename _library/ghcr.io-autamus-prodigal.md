---
layout: container
name:  "ghcr.io/autamus/prodigal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/prodigal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/prodigal/container.yaml"
updated_at: "2025-08-15 04:17:20.612963"
latest: "2.6.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/prodigal"
aliases:
 - "prodigal"
versions:
 - "2.6.3"
 - "latest"
description: "Prodigal Gene Prediction Software"
config: {"docker": "ghcr.io/autamus/prodigal", "url": "https://github.com/orgs/autamus/packages/container/package/prodigal", "maintainer": "@vsoch", "description": "Prodigal Gene Prediction Software", "latest": {"2.6.3": "sha256:2aee17229343a050dd57b80c7a478c3444091e7f3c6f36835b1249d4c8243a1e"}, "tags": {"2.6.3": "sha256:2aee17229343a050dd57b80c7a478c3444091e7f3c6f36835b1249d4c8243a1e", "latest": "sha256:2aee17229343a050dd57b80c7a478c3444091e7f3c6f36835b1249d4c8243a1e"}, "aliases": {"prodigal": "/opt/view/prodigal"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/prodigal.
Prodigal Gene Prediction Software
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/prodigal
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/prodigal:2.6.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/prodigal/2.6.3
$ module help ghcr.io/autamus/prodigal/2.6.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prodigal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prodigal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prodigal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prodigal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prodigal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prodigal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prodigal

```bash
$ singularity exec <container> /opt/view/prodigal
$ podman run --it --rm --entrypoint /opt/view/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
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