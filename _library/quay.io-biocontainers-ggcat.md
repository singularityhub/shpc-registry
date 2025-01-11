---
layout: container
name:  "quay.io/biocontainers/ggcat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ggcat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ggcat/container.yaml"
updated_at: "2025-01-11 03:20:21.273151"
latest: "1.1.0--hc9368f3_0"
container_url: "https://biocontainers.pro/tools/ggcat"
aliases:
 - "ggcat"
versions:
 - "1.1.0--hc9368f3_0"
description: "singularity registry hpc automated addition for ggcat"
config: {"url": "https://biocontainers.pro/tools/ggcat", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ggcat", "latest": {"1.1.0--hc9368f3_0": "sha256:f7e2035f5143323eda8d70be605b34c0c8ea2e55dfa56b1da71bbebc09af45a3"}, "tags": {"1.1.0--hc9368f3_0": "sha256:f7e2035f5143323eda8d70be605b34c0c8ea2e55dfa56b1da71bbebc09af45a3"}, "docker": "quay.io/biocontainers/ggcat", "aliases": {"ggcat": "/usr/local/bin/ggcat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ggcat.
singularity registry hpc automated addition for ggcat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ggcat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ggcat:1.1.0--hc9368f3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ggcat/1.1.0--hc9368f3_0
$ module help quay.io/biocontainers/ggcat/1.1.0--hc9368f3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ggcat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ggcat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ggcat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ggcat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ggcat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ggcat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ggcat

```bash
$ singularity exec <container> /usr/local/bin/ggcat
$ podman run --it --rm --entrypoint /usr/local/bin/ggcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ggcat   -v ${PWD} -w ${PWD} <container> -c " $@"
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