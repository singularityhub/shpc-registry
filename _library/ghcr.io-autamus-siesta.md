---
layout: container
name:  "ghcr.io/autamus/siesta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/siesta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/siesta/container.yaml"
updated_at: "2024-09-21 03:30:15.111044"
latest: "4.0.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/siesta"
aliases:
 - "siesta"
versions:
 - "4.0.2"
 - "latest"
description: "SIESTA performs electronic structure calculations and ab initio molecular dynamics simulations of molecules and solids."
config: {"docker": "ghcr.io/autamus/siesta", "url": "https://github.com/orgs/autamus/packages/container/package/siesta", "maintainer": "@vsoch", "description": "SIESTA performs electronic structure calculations and ab initio molecular dynamics simulations of molecules and solids.", "latest": {"4.0.2": "sha256:abab7286e84010408829b2c98afb2a927107905164a619f1f06db6b870457463"}, "tags": {"4.0.2": "sha256:abab7286e84010408829b2c98afb2a927107905164a619f1f06db6b870457463", "latest": "sha256:abab7286e84010408829b2c98afb2a927107905164a619f1f06db6b870457463"}, "aliases": {"siesta": "/opt/view/bin/siesta"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/siesta.
SIESTA performs electronic structure calculations and ab initio molecular dynamics simulations of molecules and solids.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/siesta
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/siesta:4.0.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/siesta/4.0.2
$ module help ghcr.io/autamus/siesta/4.0.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### siesta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### siesta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### siesta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### siesta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### siesta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### siesta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### siesta

```bash
$ singularity exec <container> /opt/view/bin/siesta
$ podman run --it --rm --entrypoint /opt/view/bin/siesta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/siesta   -v ${PWD} -w ${PWD} <container> -c " $@"
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