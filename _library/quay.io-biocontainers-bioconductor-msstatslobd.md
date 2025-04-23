---
layout: container
name:  "quay.io/biocontainers/bioconductor-msstatslobd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msstatslobd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msstatslobd/container.yaml"
updated_at: "2025-04-23 03:31:15.833662"
latest: "1.14.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msstatslobd"

versions:
 - "1.2.0--r41hc247a5b_2"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_2"
 - "1.8.0--r43hf17093f_0"
 - "1.10.0--r43hf17093f_0"
 - "1.14.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msstatslobd"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msstatslobd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msstatslobd", "latest": {"1.14.0--r44he5774e6_0": "sha256:f2463290e42d1b72828214c7248c58a75edeb6d5e43cf5ec5100f80bdc77bf7f"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:67058b031825913c9f78b47fa6b67ba0d15c9c2a53c329a27daf10881e97bcaf", "1.6.0--r42hc247a5b_0": "sha256:641caa61d9e6b9d5264b0b37053fe204cff8d0234d991fa86d7b5414f8965a2d", "1.6.0--r42hf17093f_2": "sha256:fdf303faa253afbf7531c2bca3932d17a9816bb313d941189a8e67266da9cff1", "1.8.0--r43hf17093f_0": "sha256:1fb1b68d23f5e5b930c874b9498bb1fdc6f03ebb8af072597459ad7ecc78620a", "1.10.0--r43hf17093f_0": "sha256:5d7914bce2bdd726872ecf96f422c332485683c19874833efda34ee7f006a67a", "1.14.0--r44he5774e6_0": "sha256:f2463290e42d1b72828214c7248c58a75edeb6d5e43cf5ec5100f80bdc77bf7f"}, "docker": "quay.io/biocontainers/bioconductor-msstatslobd"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msstatslobd.
shpc-registry automated BioContainers addition for bioconductor-msstatslobd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msstatslobd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msstatslobd:1.14.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msstatslobd/1.14.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-msstatslobd/1.14.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msstatslobd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msstatslobd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msstatslobd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msstatslobd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msstatslobd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msstatslobd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msstatslobd

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