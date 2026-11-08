---
layout: container
name:  "quay.io/biocontainers/spearfish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spearfish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spearfish/container.yaml"
updated_at: "2026-11-08 09:13:31.717940"
latest: "0.1.0--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/spearfish"
aliases:
 - "spearfish"
versions:
 - "0.1.0--hfa8f182_0"
description: "singularity registry hpc automated addition for spearfish"
config: {"url": "https://biocontainers.pro/tools/spearfish", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for spearfish", "latest": {"0.1.0--hfa8f182_0": "sha256:f691c1eb14630644b6dd3cc3de9f4d00adc897731a022251979e9f723db76a0a"}, "tags": {"0.1.0--hfa8f182_0": "sha256:f691c1eb14630644b6dd3cc3de9f4d00adc897731a022251979e9f723db76a0a"}, "docker": "quay.io/biocontainers/spearfish", "aliases": {"spearfish": "/usr/local/bin/spearfish"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spearfish.
singularity registry hpc automated addition for spearfish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spearfish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spearfish:0.1.0--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spearfish/0.1.0--hfa8f182_0
$ module help quay.io/biocontainers/spearfish/0.1.0--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spearfish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spearfish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spearfish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spearfish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spearfish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spearfish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spearfish

```bash
$ singularity exec <container> /usr/local/bin/spearfish
$ podman run --it --rm --entrypoint /usr/local/bin/spearfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spearfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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