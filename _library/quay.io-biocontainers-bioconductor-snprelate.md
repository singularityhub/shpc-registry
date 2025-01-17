---
layout: container
name:  "quay.io/biocontainers/bioconductor-snprelate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-snprelate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-snprelate/container.yaml"
updated_at: "2025-01-17 03:14:58.795570"
latest: "1.40.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-snprelate"

versions:
 - "1.28.0--r41hc247a5b_2"
 - "1.32.0--r42hc247a5b_0"
 - "1.32.0--r42hf17093f_1"
 - "1.34.1--r43hf17093f_0"
 - "1.36.0--r43hf17093f_0"
 - "1.36.0--r43hf17093f_1"
 - "1.40.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-snprelate"
config: {"url": "https://biocontainers.pro/tools/bioconductor-snprelate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-snprelate", "latest": {"1.40.0--r44he5774e6_0": "sha256:7a3ace2612d7c889a128aa22e7bcb709d9a0541778c7aa7b494e0fee115afa1b"}, "tags": {"1.28.0--r41hc247a5b_2": "sha256:a0c466bb78c868af1fa6d89a4d565fc75f8796aeb93042504e76e052eabffc4d", "1.32.0--r42hc247a5b_0": "sha256:8aba675bf147fd27d5372ed9c4ad8acbd8068a6ef6631b3b39a5c18c6a941618", "1.32.0--r42hf17093f_1": "sha256:501b57a37529f089852dc59387c09235837a6474c1ed6996853243385c8f160f", "1.34.1--r43hf17093f_0": "sha256:e26bebb203bd0ec0dbea4d5ea1eff197a34ec0710f8c399fad535893ebbdf737", "1.36.0--r43hf17093f_0": "sha256:4c842765a72d09c9d2c4eb3f116bc3fe4b84713e006acc86be0ee8d2cb0a82d9", "1.36.0--r43hf17093f_1": "sha256:ec023a6adefe2f6aac3df0d212e4f5a500fe02c5ef5d105af50c3ec87bcd50c7", "1.40.0--r44he5774e6_0": "sha256:7a3ace2612d7c889a128aa22e7bcb709d9a0541778c7aa7b494e0fee115afa1b"}, "docker": "quay.io/biocontainers/bioconductor-snprelate"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-snprelate.
shpc-registry automated BioContainers addition for bioconductor-snprelate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-snprelate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-snprelate:1.40.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-snprelate/1.40.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-snprelate/1.40.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-snprelate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snprelate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snprelate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-snprelate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-snprelate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-snprelate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-snprelate

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