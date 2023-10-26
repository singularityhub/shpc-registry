---
layout: container
name:  "quay.io/biocontainers/kmcp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmcp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmcp/container.yaml"
updated_at: "2023-10-26 03:55:08.220523"
latest: "0.9.4--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/kmcp"
aliases:
 - "kmcp"
versions:
 - "0.9.1--h9ee0642_0"
 - "0.9.2--h9ee0642_0"
 - "0.9.3--h9ee0642_0"
 - "0.9.4--h9ee0642_0"
description: "singularity registry hpc automated addition for kmcp"
config: {"url": "https://biocontainers.pro/tools/kmcp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kmcp", "latest": {"0.9.4--h9ee0642_0": "sha256:d9ae110961755e9936aa8dece51096463d0e9dc5704f8e2c0431006bf6da279f"}, "tags": {"0.9.1--h9ee0642_0": "sha256:55dcafd3e81d5509044fc86c1b8f1a6f456ce512ec8debf2d39f5cd43abb2721", "0.9.2--h9ee0642_0": "sha256:c754575619c0a93e1ccdce239ca3f494ea0842ac39d46bf08874345fb0aa231c", "0.9.3--h9ee0642_0": "sha256:89eab7013dee076e2b9724aa7a7e27ad43f5f27da3d44b70d844e3bfcfe157a3", "0.9.4--h9ee0642_0": "sha256:d9ae110961755e9936aa8dece51096463d0e9dc5704f8e2c0431006bf6da279f"}, "docker": "quay.io/biocontainers/kmcp", "aliases": {"kmcp": "/usr/local/bin/kmcp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmcp.
singularity registry hpc automated addition for kmcp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmcp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmcp:0.9.4--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmcp/0.9.4--h9ee0642_0
$ module help quay.io/biocontainers/kmcp/0.9.4--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmcp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmcp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmcp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmcp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmcp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmcp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kmcp

```bash
$ singularity exec <container> /usr/local/bin/kmcp
$ podman run --it --rm --entrypoint /usr/local/bin/kmcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmcp   -v ${PWD} -w ${PWD} <container> -c " $@"
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