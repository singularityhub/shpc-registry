---
layout: container
name:  "quay.io/biocontainers/rseg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rseg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rseg/container.yaml"
updated_at: "2025-12-17 03:32:49.729748"
latest: "0.4.9--he941832_1"
container_url: "https://biocontainers.pro/tools/rseg"
aliases:
 - "deadzones"
 - "rseg"
 - "rseg-diff"
versions:
 - "0.4.9--he941832_1"
description: "shpc-registry automated BioContainers addition for rseg"
config: {"url": "https://biocontainers.pro/tools/rseg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rseg", "latest": {"0.4.9--he941832_1": "sha256:54ce2be873594c2513e0d805fba6701992646506e3fec5fb1221a6e1a9fbd8f2"}, "tags": {"0.4.9--he941832_1": "sha256:54ce2be873594c2513e0d805fba6701992646506e3fec5fb1221a6e1a9fbd8f2"}, "docker": "quay.io/biocontainers/rseg", "aliases": {"deadzones": "/usr/local/bin/deadzones", "rseg": "/usr/local/bin/rseg", "rseg-diff": "/usr/local/bin/rseg-diff"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rseg.
shpc-registry automated BioContainers addition for rseg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rseg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rseg:0.4.9--he941832_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rseg/0.4.9--he941832_1
$ module help quay.io/biocontainers/rseg/0.4.9--he941832_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rseg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rseg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rseg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rseg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rseg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rseg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deadzones

```bash
$ singularity exec <container> /usr/local/bin/deadzones
$ podman run --it --rm --entrypoint /usr/local/bin/deadzones   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deadzones   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rseg

```bash
$ singularity exec <container> /usr/local/bin/rseg
$ podman run --it --rm --entrypoint /usr/local/bin/rseg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rseg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rseg-diff

```bash
$ singularity exec <container> /usr/local/bin/rseg-diff
$ podman run --it --rm --entrypoint /usr/local/bin/rseg-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rseg-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
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