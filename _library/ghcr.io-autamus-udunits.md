---
layout: container
name:  "ghcr.io/autamus/udunits"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/udunits/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/udunits/container.yaml"
updated_at: "2025-04-13 05:00:08.276407"
latest: "2.2.28"
container_url: "https://github.com/orgs/autamus/packages/container/package/udunits"
aliases:
 - "udunits2"
versions:
 - "2.2.28"
 - "latest"
description: "The UDUNITS package supports units of physical quantities. Its C library provides for arithmetic manipulation of units and for conversion of numeric values between compatible units."
config: {"docker": "ghcr.io/autamus/udunits", "url": "https://github.com/orgs/autamus/packages/container/package/udunits", "maintainer": "@vsoch", "description": "The UDUNITS package supports units of physical quantities. Its C library provides for arithmetic manipulation of units and for conversion of numeric values between compatible units.", "latest": {"2.2.28": "sha256:3143623c65c37c22a4a301ba4eb82941af4f9f196f6d504eab9051d45e30b1ab"}, "tags": {"2.2.28": "sha256:3143623c65c37c22a4a301ba4eb82941af4f9f196f6d504eab9051d45e30b1ab", "latest": "sha256:3143623c65c37c22a4a301ba4eb82941af4f9f196f6d504eab9051d45e30b1ab"}, "aliases": {"udunits2": "/opt/view/bin/udunits2"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/udunits.
The UDUNITS package supports units of physical quantities. Its C library provides for arithmetic manipulation of units and for conversion of numeric values between compatible units.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/udunits
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/udunits:2.2.28
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/udunits/2.2.28
$ module help ghcr.io/autamus/udunits/2.2.28
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### udunits-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### udunits-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### udunits-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### udunits-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### udunits-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### udunits-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### udunits2

```bash
$ singularity exec <container> /opt/view/bin/udunits2
$ podman run --it --rm --entrypoint /opt/view/bin/udunits2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/udunits2   -v ${PWD} -w ${PWD} <container> -c " $@"
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