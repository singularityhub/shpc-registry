---
layout: container
name:  "quay.io/biocontainers/subset-bam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/subset-bam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/subset-bam/container.yaml"
updated_at: "2024-10-21 03:33:29.835596"
latest: "1.1.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/subset-bam"
aliases:
 - "subset-bam"
versions:
 - "1.1.0--h4349ce8_0"
description: "singularity registry hpc automated addition for subset-bam"
config: {"url": "https://biocontainers.pro/tools/subset-bam", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for subset-bam", "latest": {"1.1.0--h4349ce8_0": "sha256:c0ff4759fffa3af899c7c469631068ef501880478dd44c77797c8ca041cb9fb0"}, "tags": {"1.1.0--h4349ce8_0": "sha256:c0ff4759fffa3af899c7c469631068ef501880478dd44c77797c8ca041cb9fb0"}, "docker": "quay.io/biocontainers/subset-bam", "aliases": {"subset-bam": "/usr/local/bin/subset-bam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/subset-bam.
singularity registry hpc automated addition for subset-bam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/subset-bam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/subset-bam:1.1.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/subset-bam/1.1.0--h4349ce8_0
$ module help quay.io/biocontainers/subset-bam/1.1.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### subset-bam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### subset-bam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### subset-bam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### subset-bam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### subset-bam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### subset-bam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### subset-bam

```bash
$ singularity exec <container> /usr/local/bin/subset-bam
$ podman run --it --rm --entrypoint /usr/local/bin/subset-bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subset-bam   -v ${PWD} -w ${PWD} <container> -c " $@"
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