---
layout: container
name:  "ghcr.io/autamus/mpc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/mpc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/mpc/container.yaml"
updated_at: "2025-01-24 02:46:46.113740"
latest: "1.2.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/mpc"

versions:
 - "1.1.0"
 - "1.2.1"
 - "latest"
description: "mithi/mpc: A software pipeline using the Model Predictive Control method to drive a car around a virtual track."
config: {"docker": "ghcr.io/autamus/mpc", "url": "https://github.com/orgs/autamus/packages/container/package/mpc", "maintainer": "@vsoch", "description": "mithi/mpc: A software pipeline using the Model Predictive Control method to drive a car around a virtual track.", "latest": {"1.2.1": "sha256:3e6988675f77d36e691c7d974bc4979ed2b3a045be284d94eaa572231b147f53"}, "tags": {"1.1.0": "sha256:c7628ce2156af17ad77505740c40c85063dde3c4b17a46c3f6594fd2883a674f", "1.2.1": "sha256:3e6988675f77d36e691c7d974bc4979ed2b3a045be284d94eaa572231b147f53", "latest": "sha256:3e6988675f77d36e691c7d974bc4979ed2b3a045be284d94eaa572231b147f53"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/mpc.
mithi/mpc: A software pipeline using the Model Predictive Control method to drive a car around a virtual track.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/mpc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/mpc:1.2.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/mpc/1.2.1
$ module help ghcr.io/autamus/mpc/1.2.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mpc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mpc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mpc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mpc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mpc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mpc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### mpc

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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