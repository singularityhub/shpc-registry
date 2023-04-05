---
layout: container
name:  "quay.io/biocontainers/bioconductor-beadarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-beadarray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-beadarray/container.yaml"
updated_at: "2023-04-05 02:56:45.820436"
latest: "2.48.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-beadarray"

versions:
 - "2.44.0--r41hc0cfd56_2"
 - "2.48.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-beadarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-beadarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-beadarray", "latest": {"2.48.0--r42hc0cfd56_0": "sha256:3c9e49987d631922e8a24c1b94498edb7a9b27e7c6cb15d772bc186e2687a219"}, "tags": {"2.44.0--r41hc0cfd56_2": "sha256:6700a422255ef1da9d9879c3f797363238d17a3ddaf4424ce8350ffacc50ebd9", "2.48.0--r42hc0cfd56_0": "sha256:3c9e49987d631922e8a24c1b94498edb7a9b27e7c6cb15d772bc186e2687a219"}, "docker": "quay.io/biocontainers/bioconductor-beadarray"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-beadarray.
shpc-registry automated BioContainers addition for bioconductor-beadarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-beadarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-beadarray:2.48.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-beadarray/2.48.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-beadarray/2.48.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-beadarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beadarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beadarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-beadarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-beadarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-beadarray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-beadarray

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