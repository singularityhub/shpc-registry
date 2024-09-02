---
layout: container
name:  "quay.io/biocontainers/bioconductor-mlinterfaces"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mlinterfaces/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mlinterfaces/container.yaml"
updated_at: "2024-09-02 03:27:25.400734"
latest: "1.80.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mlinterfaces"
aliases:
 - "glpsol"
versions:
 - "1.74.0--r41hc247a5b_2"
 - "1.78.0--r42hc247a5b_0"
 - "1.78.0--r42hf17093f_1"
 - "1.80.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mlinterfaces"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mlinterfaces", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mlinterfaces", "latest": {"1.80.0--r43hf17093f_0": "sha256:33afbf7ba2653931f2873a04fcbb72c84fc22cad4216a69bc444e0b937487381"}, "tags": {"1.74.0--r41hc247a5b_2": "sha256:5aac51be351ed3c511e40e1dae34256152d71d0a0cf534bfe5f83a12b0cc8290", "1.78.0--r42hc247a5b_0": "sha256:5dcf1162f68ae8b7eee92051d2a3cba4bacc04e9abd2c03d1016a15bca5228f4", "1.78.0--r42hf17093f_1": "sha256:84f7a8e566a378276ae5fda5ecd01e93928b2c8b31455c4730450ee33c6c2339", "1.80.0--r43hf17093f_0": "sha256:33afbf7ba2653931f2873a04fcbb72c84fc22cad4216a69bc444e0b937487381"}, "docker": "quay.io/biocontainers/bioconductor-mlinterfaces", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mlinterfaces.
shpc-registry automated BioContainers addition for bioconductor-mlinterfaces
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mlinterfaces
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mlinterfaces:1.80.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mlinterfaces/1.80.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-mlinterfaces/1.80.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mlinterfaces-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mlinterfaces-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mlinterfaces-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mlinterfaces-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mlinterfaces-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mlinterfaces-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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