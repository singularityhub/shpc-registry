---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellbarcode"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellbarcode/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellbarcode/container.yaml"
updated_at: "2025-09-19 03:05:09.976070"
latest: "1.6.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellbarcode"

versions:
 - "1.0.0--r41hc247a5b_2"
 - "1.4.0--r42hc247a5b_0"
 - "1.4.0--r42hf17093f_1"
 - "1.6.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellbarcode"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellbarcode", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellbarcode", "latest": {"1.6.0--r43hf17093f_0": "sha256:31891051956df6431c003b3d6a6978e47e1696111ac028ba14c35b98521b6555"}, "tags": {"1.0.0--r41hc247a5b_2": "sha256:61c3b28700d470a10f65cbb21f5c35f16d154f86b9952979fe23503c293e9f5a", "1.4.0--r42hc247a5b_0": "sha256:98afea33ec5a3c85da0683b61391f504194df5fc584324af592fa38ba3911e95", "1.4.0--r42hf17093f_1": "sha256:605a6ca053fe40ad0272d1af074969d5e229c0fdcfb14beb002672b7a740200d", "1.6.0--r43hf17093f_0": "sha256:31891051956df6431c003b3d6a6978e47e1696111ac028ba14c35b98521b6555"}, "docker": "quay.io/biocontainers/bioconductor-cellbarcode"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellbarcode.
shpc-registry automated BioContainers addition for bioconductor-cellbarcode
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellbarcode
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellbarcode:1.6.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellbarcode/1.6.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-cellbarcode/1.6.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellbarcode-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellbarcode-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellbarcode-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellbarcode-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellbarcode-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellbarcode-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cellbarcode

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