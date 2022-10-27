---
layout: container
name:  "quay.io/biocontainers/bioconductor-pbase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pbase/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pbase/container.yaml"
updated_at: "2022-10-27 00:19:55.359535"
latest: "0.26.0--r36he1b5a44_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pbase"

versions:
 - "0.26.0--r36he1b5a44_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pbase"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pbase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pbase", "latest": {"0.26.0--r36he1b5a44_0": "sha256:1f7d12aea9287f438b9d2250517712aadc4c8394465f89913faa434a862a3854"}, "tags": {"0.26.0--r36he1b5a44_0": "sha256:1f7d12aea9287f438b9d2250517712aadc4c8394465f89913faa434a862a3854"}, "docker": "quay.io/biocontainers/bioconductor-pbase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pbase.
shpc-registry automated BioContainers addition for bioconductor-pbase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pbase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pbase:0.26.0--r36he1b5a44_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pbase/0.26.0--r36he1b5a44_0
$ module help quay.io/biocontainers/bioconductor-pbase/0.26.0--r36he1b5a44_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pbase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pbase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pbase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pbase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pbase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pbase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pbase

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