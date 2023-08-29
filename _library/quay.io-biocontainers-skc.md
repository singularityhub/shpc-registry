---
layout: container
name:  "quay.io/biocontainers/skc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/skc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/skc/container.yaml"
updated_at: "2023-08-29 03:48:11.647573"
latest: "0.1.0--h031d066_0"
container_url: "https://biocontainers.pro/tools/skc"
aliases:
 - "skc"
versions:
 - "0.1.0--h031d066_0"
description: "singularity registry hpc automated addition for skc"
config: {"url": "https://biocontainers.pro/tools/skc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for skc", "latest": {"0.1.0--h031d066_0": "sha256:6e91d8f0561453cde407802b1b697e36ab41664309af6238db90f69d54d766e2"}, "tags": {"0.1.0--h031d066_0": "sha256:6e91d8f0561453cde407802b1b697e36ab41664309af6238db90f69d54d766e2"}, "docker": "quay.io/biocontainers/skc", "aliases": {"skc": "/usr/local/bin/skc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/skc.
singularity registry hpc automated addition for skc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/skc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/skc:0.1.0--h031d066_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/skc/0.1.0--h031d066_0
$ module help quay.io/biocontainers/skc/0.1.0--h031d066_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### skc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### skc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### skc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### skc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### skc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### skc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### skc

```bash
$ singularity exec <container> /usr/local/bin/skc
$ podman run --it --rm --entrypoint /usr/local/bin/skc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skc   -v ${PWD} -w ${PWD} <container> -c " $@"
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