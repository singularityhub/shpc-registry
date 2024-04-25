---
layout: container
name:  "ghcr.io/autamus/angsd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/angsd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/angsd/container.yaml"
updated_at: "2024-04-25 03:10:57.453481"
latest: "0.935"
container_url: "https://github.com/orgs/autamus/packages/container/package/angsd"
aliases:
 - "angsd"
versions:
 - "0.935"
 - "latest"
description: "ANGSD is a software for analyzing next generation sequencing data."
config: {"docker": "ghcr.io/autamus/angsd", "url": "https://github.com/orgs/autamus/packages/container/package/angsd", "maintainer": "@vsoch", "description": "ANGSD is a software for analyzing next generation sequencing data.", "latest": {"0.935": "sha256:338f13839b99de50694e13e59f3b067e672ca559fff5832eb1f47f16e355ba34"}, "tags": {"0.935": "sha256:338f13839b99de50694e13e59f3b067e672ca559fff5832eb1f47f16e355ba34", "latest": "sha256:338f13839b99de50694e13e59f3b067e672ca559fff5832eb1f47f16e355ba34"}, "aliases": {"angsd": "/opt/view/bin/angsd"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/angsd.
ANGSD is a software for analyzing next generation sequencing data.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/angsd
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/angsd:0.935
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/angsd/0.935
$ module help ghcr.io/autamus/angsd/0.935
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### angsd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### angsd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### angsd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### angsd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### angsd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### angsd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### angsd

```bash
$ singularity exec <container> /opt/view/bin/angsd
$ podman run --it --rm --entrypoint /opt/view/bin/angsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/angsd   -v ${PWD} -w ${PWD} <container> -c " $@"
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