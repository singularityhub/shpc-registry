---
layout: container
name:  "quay.io/biocontainers/bioconductor-vanillaice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vanillaice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vanillaice/container.yaml"
updated_at: "2025-07-07 03:55:50.544830"
latest: "1.68.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-vanillaice"

versions:
 - "1.56.3--r41hc0cfd56_1"
 - "1.60.0--r42hc0cfd56_0"
 - "1.62.0--r43ha9d7317_0"
 - "1.64.0--r43ha9d7317_0"
 - "1.68.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-vanillaice"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vanillaice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vanillaice", "latest": {"1.68.0--r44h3df3fcb_0": "sha256:1963e4849f85a06f11e18758cd1711e555e487923b42fe55e7903b93526be3e6"}, "tags": {"1.56.3--r41hc0cfd56_1": "sha256:716427b3995a872dbde820fca58432860828fc22340cf310bf034909a2b0f9cf", "1.60.0--r42hc0cfd56_0": "sha256:b3e5f576a17cc5b67514e5ea6572bf49db7c4549321a87e7ae2379965a3e272b", "1.62.0--r43ha9d7317_0": "sha256:e08a354a02153da20c66233ead77c5947b61171ce9a144a2cce65b5e2209c398", "1.64.0--r43ha9d7317_0": "sha256:95c29dbd00355a71b23f002b26ce86c0deab68d776e99a1acd3e5716202de7a6", "1.68.0--r44h3df3fcb_0": "sha256:1963e4849f85a06f11e18758cd1711e555e487923b42fe55e7903b93526be3e6"}, "docker": "quay.io/biocontainers/bioconductor-vanillaice"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vanillaice.
shpc-registry automated BioContainers addition for bioconductor-vanillaice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vanillaice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vanillaice:1.68.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vanillaice/1.68.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-vanillaice/1.68.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vanillaice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vanillaice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vanillaice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vanillaice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vanillaice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vanillaice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-vanillaice

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