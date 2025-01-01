---
layout: container
name:  "quay.io/biocontainers/splitubam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/splitubam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/splitubam/container.yaml"
updated_at: "2025-01-01 03:26:04.684718"
latest: "0.1.1--hc9368f3_0"
container_url: "https://biocontainers.pro/tools/splitubam"
aliases:
 - "splitubam"
versions:
 - "0.1.1--hc9368f3_0"
description: "singularity registry hpc automated addition for splitubam"
config: {"url": "https://biocontainers.pro/tools/splitubam", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for splitubam", "latest": {"0.1.1--hc9368f3_0": "sha256:c29614a57ef61f6ad75eb767da6c964a603d0eb60fa2439a5c13769af4e3a85c"}, "tags": {"0.1.1--hc9368f3_0": "sha256:c29614a57ef61f6ad75eb767da6c964a603d0eb60fa2439a5c13769af4e3a85c"}, "docker": "quay.io/biocontainers/splitubam", "aliases": {"splitubam": "/usr/local/bin/splitubam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/splitubam.
singularity registry hpc automated addition for splitubam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/splitubam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/splitubam:0.1.1--hc9368f3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/splitubam/0.1.1--hc9368f3_0
$ module help quay.io/biocontainers/splitubam/0.1.1--hc9368f3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### splitubam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### splitubam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### splitubam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### splitubam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### splitubam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### splitubam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### splitubam

```bash
$ singularity exec <container> /usr/local/bin/splitubam
$ podman run --it --rm --entrypoint /usr/local/bin/splitubam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitubam   -v ${PWD} -w ${PWD} <container> -c " $@"
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