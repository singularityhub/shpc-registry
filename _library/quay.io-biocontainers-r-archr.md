---
layout: container
name:  "quay.io/biocontainers/r-archr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-archr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-archr/container.yaml"
updated_at: "2025-08-17 03:36:53.148162"
latest: "1.0.3--r43hdbdd923_0"
container_url: "https://biocontainers.pro/tools/r-archr"
aliases:
 - "pandoc"
versions:
 - "1.0.2--r41hdbdd923_0"
 - "1.0.3--r43hdbdd923_0"
description: "singularity registry hpc automated addition for r-archr"
config: {"url": "https://biocontainers.pro/tools/r-archr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-archr", "latest": {"1.0.3--r43hdbdd923_0": "sha256:bef958e2788e5d62170c05ef54c6a37209be20891b73b84e23f1aff7835a9ebc"}, "tags": {"1.0.2--r41hdbdd923_0": "sha256:c332222f5ccfca2753766aec679b0f9dd1c29bfa7fe66b0853e8b552aca63337", "1.0.3--r43hdbdd923_0": "sha256:bef958e2788e5d62170c05ef54c6a37209be20891b73b84e23f1aff7835a9ebc"}, "docker": "quay.io/biocontainers/r-archr", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-archr.
singularity registry hpc automated addition for r-archr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-archr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-archr:1.0.3--r43hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-archr/1.0.3--r43hdbdd923_0
$ module help quay.io/biocontainers/r-archr/1.0.3--r43hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-archr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-archr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-archr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-archr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-archr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-archr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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