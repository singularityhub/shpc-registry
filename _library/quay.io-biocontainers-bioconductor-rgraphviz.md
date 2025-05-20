---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgraphviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgraphviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgraphviz/container.yaml"
updated_at: "2025-05-20 03:29:21.793515"
latest: "2.50.0--r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rgraphviz"

versions:
 - "2.38.0--r41hc247a5b_2"
 - "2.42.0--r42hc247a5b_0"
 - "2.42.0--r42hf17093f_1"
 - "2.44.0--r43hf17093f_0"
 - "2.46.0--r43hf17093f_0"
 - "2.46.0--r43hf17093f_1"
 - "2.50.0--r44he5774e6_0"
 - "2.50.0--r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rgraphviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgraphviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgraphviz", "latest": {"2.50.0--r44he5774e6_1": "sha256:6eb9a873633b8e124f6daa0709159ddb508df48bc7f8d856071beeabe4722893"}, "tags": {"2.38.0--r41hc247a5b_2": "sha256:2d2512cf75e01304b658f482c1c3841026a1bf9c9bc963e691e3feac7cb3b3ac", "2.42.0--r42hc247a5b_0": "sha256:792360962162c82790ee0c174648b3ae703b74bdbd54228413f5d9fdd53c725d", "2.42.0--r42hf17093f_1": "sha256:497ba00f705e93f8b8b507858099f9c14925a9811e89c6c0418c2e38562cab2e", "2.44.0--r43hf17093f_0": "sha256:af49a7cfc7a86130c7809ccd441c986390e5e9bf3a712b195b5bcf45fd9ee0c2", "2.46.0--r43hf17093f_0": "sha256:f251c0350127dcacd3f1a85868fb3828f6ab83c457e8008ca71df55a229113d8", "2.46.0--r43hf17093f_1": "sha256:8ee7e3e7ff3112405d169d6955ce926b2e01ada28408907e1ea2e05d7ff28142", "2.50.0--r44he5774e6_0": "sha256:080af9b6225479a50c01f1f68008a3a370a70780ecc2feff4a72738a50d4d633", "2.50.0--r44he5774e6_1": "sha256:6eb9a873633b8e124f6daa0709159ddb508df48bc7f8d856071beeabe4722893"}, "docker": "quay.io/biocontainers/bioconductor-rgraphviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgraphviz.
shpc-registry automated BioContainers addition for bioconductor-rgraphviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgraphviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgraphviz:2.50.0--r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgraphviz/2.50.0--r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-rgraphviz/2.50.0--r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgraphviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgraphviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgraphviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgraphviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgraphviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgraphviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rgraphviz

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