---
layout: container
name:  "quay.io/biocontainers/bioconductor-levi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-levi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-levi/container.yaml"
updated_at: "2025-09-24 03:16:21.494400"
latest: "1.24.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-levi"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40h399db7b_1"
 - "1.12.0--r41hc247a5b_2"
 - "1.10.0--r41h399db7b_0"
 - "1.16.0--r42hc247a5b_0"
 - "1.16.0--r42hf17093f_1"
 - "1.18.0--r43hf17093f_0"
 - "1.20.0--r43hf17093f_1"
 - "1.24.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-levi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-levi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-levi", "latest": {"1.24.0--r44he5774e6_0": "sha256:bf7db720086fef035b347b95e5c3bcefdf089423e8d8bfd941ce950d294a2575"}, "tags": {"1.8.0--r40h399db7b_1": "sha256:9091bb30d944faafa6efa40b297de725a578dfa8052712364e48184efaeee11e", "1.12.0--r41hc247a5b_2": "sha256:2d5718d9c3596f1e8020d5fc99d3c1877c77633051f28d4e012e08c9962c9b8b", "1.10.0--r41h399db7b_0": "sha256:c5e5c9085b74800d52e9995e9eaea00230e0b0e94b235dc3055c5af05f4bcafe", "1.16.0--r42hc247a5b_0": "sha256:4ccf1475833a3fddd01e5ade5cee590bb2b0b777f2aa7dc5358cc4a7db82cb44", "1.16.0--r42hf17093f_1": "sha256:fed75e9feadbeb00c9f3cc9d0dcb1657758678ba6d45d2882c00a7e9c9f39f4c", "1.18.0--r43hf17093f_0": "sha256:b8843b575199b8797d1aa615a6ea17240fb04bfde3aa4d1a9b380cf2e16e993d", "1.20.0--r43hf17093f_1": "sha256:26447bf51051ba0f574847d6002bc558ffb5e2dd3527cedb6f6a054cbb059e6b", "1.24.0--r44he5774e6_0": "sha256:bf7db720086fef035b347b95e5c3bcefdf089423e8d8bfd941ce950d294a2575"}, "docker": "quay.io/biocontainers/bioconductor-levi", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-levi.
shpc-registry automated BioContainers addition for bioconductor-levi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-levi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-levi:1.24.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-levi/1.24.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-levi/1.24.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-levi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-levi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-levi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-levi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-levi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-levi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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