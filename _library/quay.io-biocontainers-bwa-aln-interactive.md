---
layout: container
name:  "quay.io/biocontainers/bwa-aln-interactive"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bwa-aln-interactive/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bwa-aln-interactive/container.yaml"
updated_at: "2024-11-08 03:13:34.970431"
latest: "0.7.18--he4a0461_1"
container_url: "https://biocontainers.pro/tools/bwa-aln-interactive"
aliases:
 - "bwa-aln-interactive"
versions:
 - "0.7.18--he4a0461_0"
 - "0.7.18--he4a0461_1"
description: "singularity registry hpc automated addition for bwa-aln-interactive"
config: {"url": "https://biocontainers.pro/tools/bwa-aln-interactive", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bwa-aln-interactive", "latest": {"0.7.18--he4a0461_1": "sha256:4a00c21d1c6093a22f0597541f55bfb26fefa5ee3b90ea049a4babaeb542d4ed"}, "tags": {"0.7.18--he4a0461_0": "sha256:eccc46aae5ae9649ef24d0f8be20cddf1875635e7d81e67e3622257a8f2f1eb7", "0.7.18--he4a0461_1": "sha256:4a00c21d1c6093a22f0597541f55bfb26fefa5ee3b90ea049a4babaeb542d4ed"}, "docker": "quay.io/biocontainers/bwa-aln-interactive", "aliases": {"bwa-aln-interactive": "/usr/local/bin/bwa-aln-interactive"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bwa-aln-interactive.
singularity registry hpc automated addition for bwa-aln-interactive
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bwa-aln-interactive
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bwa-aln-interactive:0.7.18--he4a0461_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bwa-aln-interactive/0.7.18--he4a0461_1
$ module help quay.io/biocontainers/bwa-aln-interactive/0.7.18--he4a0461_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bwa-aln-interactive-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bwa-aln-interactive-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bwa-aln-interactive-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bwa-aln-interactive-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bwa-aln-interactive-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bwa-aln-interactive-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa-aln-interactive

```bash
$ singularity exec <container> /usr/local/bin/bwa-aln-interactive
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-aln-interactive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-aln-interactive   -v ${PWD} -w ${PWD} <container> -c " $@"
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