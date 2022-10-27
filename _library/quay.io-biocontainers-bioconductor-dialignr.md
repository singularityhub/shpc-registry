---
layout: container
name:  "quay.io/biocontainers/bioconductor-dialignr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dialignr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dialignr/container.yaml"
updated_at: "2022-10-27 00:45:08.064173"
latest: "2.2.0--r41hc247a5b_2"
container_url: "https://biocontainers.pro/tools/bioconductor-dialignr"

versions:
 - "2.2.0--r41hc247a5b_2"
description: "shpc-registry automated BioContainers addition for bioconductor-dialignr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dialignr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dialignr", "latest": {"2.2.0--r41hc247a5b_2": "sha256:5f19f2cf1f68175db7d5d1451df164f6f2e778d28c0239672cd5065e13f80e8d"}, "tags": {"2.2.0--r41hc247a5b_2": "sha256:5f19f2cf1f68175db7d5d1451df164f6f2e778d28c0239672cd5065e13f80e8d"}, "docker": "quay.io/biocontainers/bioconductor-dialignr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dialignr.
shpc-registry automated BioContainers addition for bioconductor-dialignr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dialignr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dialignr:2.2.0--r41hc247a5b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dialignr/2.2.0--r41hc247a5b_2
$ module help quay.io/biocontainers/bioconductor-dialignr/2.2.0--r41hc247a5b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dialignr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dialignr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dialignr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dialignr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dialignr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dialignr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dialignr

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