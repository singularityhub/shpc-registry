---
layout: container
name:  "quay.io/biocontainers/fg-stitch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fg-stitch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fg-stitch/container.yaml"
updated_at: "2026-05-09 06:32:44.976654"
latest: "0.1.2--h54198d6_0"
container_url: "https://biocontainers.pro/tools/fg-stitch"
aliases:
 - "stitch"
versions:
 - "0.1.2--h54198d6_0"
description: "singularity registry hpc automated addition for fg-stitch"
config: {"url": "https://biocontainers.pro/tools/fg-stitch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fg-stitch", "latest": {"0.1.2--h54198d6_0": "sha256:a707e0e19a73a3da135c269f2bd4df3b77b6a4beaf19b3ce04ad5dc77d4387d0"}, "tags": {"0.1.2--h54198d6_0": "sha256:a707e0e19a73a3da135c269f2bd4df3b77b6a4beaf19b3ce04ad5dc77d4387d0"}, "docker": "quay.io/biocontainers/fg-stitch", "aliases": {"stitch": "/usr/local/bin/stitch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fg-stitch.
singularity registry hpc automated addition for fg-stitch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fg-stitch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fg-stitch:0.1.2--h54198d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fg-stitch/0.1.2--h54198d6_0
$ module help quay.io/biocontainers/fg-stitch/0.1.2--h54198d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fg-stitch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fg-stitch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fg-stitch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fg-stitch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fg-stitch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fg-stitch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stitch

```bash
$ singularity exec <container> /usr/local/bin/stitch
$ podman run --it --rm --entrypoint /usr/local/bin/stitch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stitch   -v ${PWD} -w ${PWD} <container> -c " $@"
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