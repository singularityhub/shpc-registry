---
layout: container
name:  "quay.io/biocontainers/bioconductor-degnorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-degnorm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-degnorm/container.yaml"
updated_at: "2025-01-08 03:02:59.949213"
latest: "1.16.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-degnorm"

versions:
 - "1.4.0--r41hc247a5b_2"
 - "1.8.0--r42hc247a5b_0"
 - "1.8.0--r42hf17093f_1"
 - "1.10.1--r43hf17093f_0"
 - "1.12.0--r43hf17093f_0"
 - "1.16.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-degnorm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-degnorm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-degnorm", "latest": {"1.16.0--r44he5774e6_0": "sha256:b803ca0c30f8cfd19bd89480aedc89cf11abade1f4a2518be9f9934faa70013a"}, "tags": {"1.4.0--r41hc247a5b_2": "sha256:c396013e1cd70c17f08fb541037617ffe4f4c125f069d10a7d614abaa9b27c90", "1.8.0--r42hc247a5b_0": "sha256:1ebc800cc56ba6432a92eb696968d30b8478d31fb8ce003a488a738f23d60e21", "1.8.0--r42hf17093f_1": "sha256:e11b45c7dff804e20a7927320c50eb38d5ff90a4228624e59848ebddc1bc67ff", "1.10.1--r43hf17093f_0": "sha256:2940f618300d29f01ef15285dabd29026f7a2affd261d35e675d43bb4d930e20", "1.12.0--r43hf17093f_0": "sha256:bae59a3ff1552bce9c5131b2549521dc739d5377063c1aaed395a742053bb7e4", "1.16.0--r44he5774e6_0": "sha256:b803ca0c30f8cfd19bd89480aedc89cf11abade1f4a2518be9f9934faa70013a"}, "docker": "quay.io/biocontainers/bioconductor-degnorm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-degnorm.
shpc-registry automated BioContainers addition for bioconductor-degnorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-degnorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-degnorm:1.16.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-degnorm/1.16.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-degnorm/1.16.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-degnorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-degnorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-degnorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-degnorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-degnorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-degnorm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-degnorm

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