---
layout: container
name:  "quay.io/biocontainers/r-tidyverse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-tidyverse/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-tidyverse/container.yaml"
updated_at: "2022-10-27 00:59:12.996897"
latest: "1.2.1"
container_url: "https://biocontainers.pro/tools/r-tidyverse"

versions:
 - "1.2.1"
description: "shpc-registry automated BioContainers addition for r-tidyverse"
config: {"url": "https://biocontainers.pro/tools/r-tidyverse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-tidyverse", "latest": {"1.2.1": "sha256:f4555efa35cb4b54fbfa59a15bb57ff758ba845577b7dcc107a47d1b6aa8807f"}, "tags": {"1.2.1": "sha256:f4555efa35cb4b54fbfa59a15bb57ff758ba845577b7dcc107a47d1b6aa8807f"}, "docker": "quay.io/biocontainers/r-tidyverse"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-tidyverse.
shpc-registry automated BioContainers addition for r-tidyverse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-tidyverse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-tidyverse:1.2.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-tidyverse/1.2.1
$ module help quay.io/biocontainers/r-tidyverse/1.2.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-tidyverse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-tidyverse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-tidyverse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-tidyverse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-tidyverse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-tidyverse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-tidyverse

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