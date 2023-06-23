---
layout: container
name:  "quay.io/biocontainers/kfoots"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kfoots/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kfoots/container.yaml"
updated_at: "2023-06-23 03:08:16.474129"
latest: "1.0--r42h031d066_9"
container_url: "https://biocontainers.pro/tools/kfoots"

versions:
 - "1.0--r41hec16e2b_6"
 - "1.0--r42hec16e2b_7"
 - "1.0--r42h031d066_9"
description: "shpc-registry automated BioContainers addition for kfoots"
config: {"url": "https://biocontainers.pro/tools/kfoots", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kfoots", "latest": {"1.0--r42h031d066_9": "sha256:fedbd2a7929fecc1fbb1a2a5e9bfa786f5f008eac0d0b0ef1286b7aaae2652e0"}, "tags": {"1.0--r41hec16e2b_6": "sha256:54429ee26edcc2d3e3660c2b1b7782f114a08ee7130f10c301b4fd8f90fe3891", "1.0--r42hec16e2b_7": "sha256:b688634c21f205266e83d114018b6bbf0c63db9495db8abd4d13855bf666fbf6", "1.0--r42h031d066_9": "sha256:fedbd2a7929fecc1fbb1a2a5e9bfa786f5f008eac0d0b0ef1286b7aaae2652e0"}, "docker": "quay.io/biocontainers/kfoots"}
---

This module is a singularity container wrapper for quay.io/biocontainers/kfoots.
shpc-registry automated BioContainers addition for kfoots
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kfoots
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kfoots:1.0--r42h031d066_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kfoots/1.0--r42h031d066_9
$ module help quay.io/biocontainers/kfoots/1.0--r42h031d066_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kfoots-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kfoots-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kfoots-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kfoots-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kfoots-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kfoots-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### kfoots

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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