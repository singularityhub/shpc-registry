---
layout: container
name:  "quay.io/biocontainers/riker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/riker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/riker/container.yaml"
updated_at: "2026-06-11 16:05:18.591122"
latest: "0.2.0--hec9b1f2_0"
container_url: "https://biocontainers.pro/tools/riker"
aliases:
 - "riker"
versions:
 - "0.1.0--h4349ce8_0"
 - "0.2.0--hec9b1f2_0"
description: "singularity registry hpc automated addition for riker"
config: {"url": "https://biocontainers.pro/tools/riker", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for riker", "latest": {"0.2.0--hec9b1f2_0": "sha256:794ac0e85d2ee714a1d1f844577c81d027853460e818eb9b34dea53add206bec"}, "tags": {"0.1.0--h4349ce8_0": "sha256:1cad1e50aab83e434f894800d7f4d9a3a24a26e02f8e5e87a05872d0b5707d8c", "0.2.0--hec9b1f2_0": "sha256:794ac0e85d2ee714a1d1f844577c81d027853460e818eb9b34dea53add206bec"}, "docker": "quay.io/biocontainers/riker", "aliases": {"riker": "/usr/local/bin/riker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/riker.
singularity registry hpc automated addition for riker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/riker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/riker:0.2.0--hec9b1f2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/riker/0.2.0--hec9b1f2_0
$ module help quay.io/biocontainers/riker/0.2.0--hec9b1f2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### riker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### riker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### riker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### riker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### riker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### riker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### riker

```bash
$ singularity exec <container> /usr/local/bin/riker
$ podman run --it --rm --entrypoint /usr/local/bin/riker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/riker   -v ${PWD} -w ${PWD} <container> -c " $@"
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