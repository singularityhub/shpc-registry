---
layout: container
name:  "quay.io/biocontainers/poseidon-trident"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/poseidon-trident/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/poseidon-trident/container.yaml"
updated_at: "2023-05-26 03:06:44.800658"
latest: "1.1.11.0--h9325052_0"
container_url: "https://biocontainers.pro/tools/poseidon-trident"
aliases:
 - "trident"
versions:
 - "0.28.0--h9325052_0"
 - "1.1.6.0--h9325052_0"
 - "1.1.11.0--h9325052_0"
description: "shpc-registry automated BioContainers addition for poseidon-trident"
config: {"url": "https://biocontainers.pro/tools/poseidon-trident", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for poseidon-trident", "latest": {"1.1.11.0--h9325052_0": "sha256:0b7450aeb4bfa7ff55621f6c5196cca92d5b527b7f70469291f9c2eb5ecf0ea0"}, "tags": {"0.28.0--h9325052_0": "sha256:3a6f2f51c9322434446b730231f9310ec146579f708287b1e88a97c53de1120f", "1.1.6.0--h9325052_0": "sha256:8286f010e2227d0bcd3440e173e34b07c0c841ebaab0f0fd5fbd0bb73266e62d", "1.1.11.0--h9325052_0": "sha256:0b7450aeb4bfa7ff55621f6c5196cca92d5b527b7f70469291f9c2eb5ecf0ea0"}, "docker": "quay.io/biocontainers/poseidon-trident", "aliases": {"trident": "/usr/local/bin/trident"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/poseidon-trident.
shpc-registry automated BioContainers addition for poseidon-trident
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/poseidon-trident
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/poseidon-trident:1.1.11.0--h9325052_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/poseidon-trident/1.1.11.0--h9325052_0
$ module help quay.io/biocontainers/poseidon-trident/1.1.11.0--h9325052_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### poseidon-trident-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### poseidon-trident-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### poseidon-trident-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### poseidon-trident-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### poseidon-trident-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### poseidon-trident-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trident

```bash
$ singularity exec <container> /usr/local/bin/trident
$ podman run --it --rm --entrypoint /usr/local/bin/trident   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trident   -v ${PWD} -w ${PWD} <container> -c " $@"
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