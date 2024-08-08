---
layout: container
name:  "quay.io/biocontainers/cellrank"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cellrank/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cellrank/container.yaml"
updated_at: "2024-08-08 03:16:39.784200"
latest: "1.5.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cellrank"

versions:
 - "1.5.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cellrank"
config: {"url": "https://biocontainers.pro/tools/cellrank", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cellrank", "latest": {"1.5.1--pyhdfd78af_0": "sha256:127cf5d386ed2ceb0284033d5d3e5ad108861c9d944e4352cb302e1ec00e628a"}, "tags": {"1.5.1--pyhdfd78af_0": "sha256:127cf5d386ed2ceb0284033d5d3e5ad108861c9d944e4352cb302e1ec00e628a"}, "docker": "quay.io/biocontainers/cellrank"}
---

This module is a singularity container wrapper for quay.io/biocontainers/cellrank.
shpc-registry automated BioContainers addition for cellrank
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cellrank
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cellrank:1.5.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cellrank/1.5.1--pyhdfd78af_0
$ module help quay.io/biocontainers/cellrank/1.5.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cellrank-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cellrank-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cellrank-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cellrank-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cellrank-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cellrank-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### cellrank

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