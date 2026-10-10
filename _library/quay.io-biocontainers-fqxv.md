---
layout: container
name:  "quay.io/biocontainers/fqxv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fqxv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fqxv/container.yaml"
updated_at: "2026-10-10 18:58:31.030379"
latest: "0.7.0--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/fqxv"
aliases:
 - "fqxv"
versions:
 - "0.7.0--hfa8f182_0"
description: "singularity registry hpc automated addition for fqxv"
config: {"url": "https://biocontainers.pro/tools/fqxv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fqxv", "latest": {"0.7.0--hfa8f182_0": "sha256:a3c357b3acddf3c6fe80327714ab379442ab470ed237ef44887d3388075d761e"}, "tags": {"0.7.0--hfa8f182_0": "sha256:a3c357b3acddf3c6fe80327714ab379442ab470ed237ef44887d3388075d761e"}, "docker": "quay.io/biocontainers/fqxv", "aliases": {"fqxv": "/usr/local/bin/fqxv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fqxv.
singularity registry hpc automated addition for fqxv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fqxv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fqxv:0.7.0--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fqxv/0.7.0--hfa8f182_0
$ module help quay.io/biocontainers/fqxv/0.7.0--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fqxv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fqxv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fqxv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fqxv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fqxv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fqxv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fqxv

```bash
$ singularity exec <container> /usr/local/bin/fqxv
$ podman run --it --rm --entrypoint /usr/local/bin/fqxv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqxv   -v ${PWD} -w ${PWD} <container> -c " $@"
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