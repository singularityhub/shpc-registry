---
layout: container
name:  "quay.io/biocontainers/bioconductor-microrna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-microrna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-microrna/container.yaml"
updated_at: "2024-06-21 03:08:57.551036"
latest: "1.60.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-microrna"

versions:
 - "1.52.0--r41hc247a5b_2"
 - "1.56.0--r42hc247a5b_0"
 - "1.56.0--r42hf17093f_1"
 - "1.58.0--r43hf17093f_0"
 - "1.60.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-microrna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-microrna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-microrna", "latest": {"1.60.0--r43hf17093f_0": "sha256:61361f73fcc319d094883d001eb1b17de6bf3d1b6250ce615d0e1fc70f4ca7c7"}, "tags": {"1.52.0--r41hc247a5b_2": "sha256:d196c507e23c7465156333dc220b9c4ce6fba3128c6b5b0f6e6ed291125c9bb8", "1.56.0--r42hc247a5b_0": "sha256:1d52828d1d7d0c572306a298b27f3ecadb6411c1940eef1d3cf8ac9de360dde1", "1.56.0--r42hf17093f_1": "sha256:63801afd1e74588bface28e99ee15008325e6376533f6b6036292b81ab68b682", "1.58.0--r43hf17093f_0": "sha256:39c01edc5ffb7a6ce9e5e5e8195f0300908e9e37844ec0bbeccecf4d3f65ff99", "1.60.0--r43hf17093f_0": "sha256:61361f73fcc319d094883d001eb1b17de6bf3d1b6250ce615d0e1fc70f4ca7c7"}, "docker": "quay.io/biocontainers/bioconductor-microrna"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-microrna.
shpc-registry automated BioContainers addition for bioconductor-microrna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-microrna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-microrna:1.60.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-microrna/1.60.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-microrna/1.60.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-microrna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-microrna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-microrna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-microrna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-microrna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-microrna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-microrna

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