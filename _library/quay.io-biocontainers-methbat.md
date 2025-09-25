---
layout: container
name:  "quay.io/biocontainers/methbat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/methbat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/methbat/container.yaml"
updated_at: "2025-09-25 07:34:09.836201"
latest: "0.16.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/methbat"
aliases:
 - "methbat"
versions:
 - "0.13.0--h9ee0642_0"
 - "0.13.1--h9ee0642_0"
 - "0.13.2--h9ee0642_0"
 - "0.13.3--h9ee0642_0"
 - "0.14.0--h9ee0642_0"
 - "0.14.1--h9ee0642_0"
 - "0.14.2--h9ee0642_0"
 - "0.16.0--h9ee0642_0"
 - "0.15.0--h9ee0642_0"
description: "singularity registry hpc automated addition for methbat"
config: {"url": "https://biocontainers.pro/tools/methbat", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for methbat", "latest": {"0.16.0--h9ee0642_0": "sha256:c2a1b058b6a334a6353139eac0e382637e0f9233fdee3fdd065f39fc950fc43d"}, "tags": {"0.13.0--h9ee0642_0": "sha256:e8407f90e58ccad8deffed54d164c696e058e84233a61ef5abde3d9ff654ebbf", "0.13.1--h9ee0642_0": "sha256:09a72f141f2858fc1a933ff72bb8105c86693edffa2596c99477cf80bc874068", "0.13.2--h9ee0642_0": "sha256:aa641e65ad03f9688ec36adcb69b2f36fbee84a1af3ddaa7a6ef49fe9bf67650", "0.13.3--h9ee0642_0": "sha256:4437ddbc1d625317b1312ccb93065ea9d70c8ae9ef699d112df5f36d2098604f", "0.14.0--h9ee0642_0": "sha256:4ebfc97b126909e2de114fb27d71a8efbdc306551297b52734e90a886910ec01", "0.14.1--h9ee0642_0": "sha256:570ed4854ccc725b1b073c3bb6342c2b80e0141b682dde1860cccae9b51edee1", "0.14.2--h9ee0642_0": "sha256:874faf82db74ed566b3e32d9da7222bc7cbb3162927601b5a60b860ef799e024", "0.16.0--h9ee0642_0": "sha256:c2a1b058b6a334a6353139eac0e382637e0f9233fdee3fdd065f39fc950fc43d", "0.15.0--h9ee0642_0": "sha256:9d5ea76f18545e927fa8a3031fb219ac0e6c1996f6dbc319d789a53e937d6d0c"}, "docker": "quay.io/biocontainers/methbat", "aliases": {"methbat": "/usr/local/bin/methbat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/methbat.
singularity registry hpc automated addition for methbat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/methbat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/methbat:0.16.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/methbat/0.16.0--h9ee0642_0
$ module help quay.io/biocontainers/methbat/0.16.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### methbat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### methbat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### methbat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### methbat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### methbat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### methbat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### methbat

```bash
$ singularity exec <container> /usr/local/bin/methbat
$ podman run --it --rm --entrypoint /usr/local/bin/methbat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/methbat   -v ${PWD} -w ${PWD} <container> -c " $@"
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