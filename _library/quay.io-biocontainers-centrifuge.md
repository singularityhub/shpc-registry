---
layout: container
name:  "quay.io/biocontainers/centrifuge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/centrifuge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/centrifuge/container.yaml"
updated_at: "2023-02-25 03:30:22.941108"
latest: "1.0.4_beta--h9a82719_6"
container_url: "https://biocontainers.pro/tools/centrifuge"

versions:
 - "1.0.4_beta--h9a82719_6"
description: "shpc-registry automated BioContainers addition for centrifuge"
config: {"url": "https://biocontainers.pro/tools/centrifuge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for centrifuge", "latest": {"1.0.4_beta--h9a82719_6": "sha256:e3ce6d3d83a1df5327ee27b66d4c9eedb05b7bcd2eae8f78a7f7b9c1e8672c1c"}, "tags": {"1.0.4_beta--h9a82719_6": "sha256:e3ce6d3d83a1df5327ee27b66d4c9eedb05b7bcd2eae8f78a7f7b9c1e8672c1c"}, "docker": "quay.io/biocontainers/centrifuge"}
---

This module is a singularity container wrapper for quay.io/biocontainers/centrifuge.
shpc-registry automated BioContainers addition for centrifuge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/centrifuge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/centrifuge:1.0.4_beta--h9a82719_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/centrifuge/1.0.4_beta--h9a82719_6
$ module help quay.io/biocontainers/centrifuge/1.0.4_beta--h9a82719_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### centrifuge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### centrifuge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### centrifuge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### centrifuge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### centrifuge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### centrifuge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### centrifuge

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