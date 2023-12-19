---
layout: container
name:  "quay.io/biocontainers/bioconductor-casper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-casper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-casper/container.yaml"
updated_at: "2023-12-19 02:53:56.875816"
latest: "2.34.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-casper"

versions:
 - "2.28.0--r41hc247a5b_2"
 - "2.32.0--r42hc247a5b_0"
 - "2.32.0--r42hf17093f_1"
 - "2.34.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-casper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-casper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-casper", "latest": {"2.34.0--r43hf17093f_0": "sha256:5a00144994147fa176b6db56e7eae3fcd92357ff77933d9240a86aabb35d83a8"}, "tags": {"2.28.0--r41hc247a5b_2": "sha256:b433e51930c4e03a8bec6fa044fe6a44067b4a990e21d53f1e89cd34f56f3229", "2.32.0--r42hc247a5b_0": "sha256:d58e70e0e1caa1edea0e8d886da1e62dad1b4da18f34a27091f0b9de957ae886", "2.32.0--r42hf17093f_1": "sha256:2ae3eb45abd82098899691b1070f30030e0d2f5b0aca6365202887c35df03941", "2.34.0--r43hf17093f_0": "sha256:5a00144994147fa176b6db56e7eae3fcd92357ff77933d9240a86aabb35d83a8"}, "docker": "quay.io/biocontainers/bioconductor-casper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-casper.
shpc-registry automated BioContainers addition for bioconductor-casper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-casper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-casper:2.34.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-casper/2.34.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-casper/2.34.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-casper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-casper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-casper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-casper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-casper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-casper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-casper

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