---
layout: container
name:  "quay.io/biocontainers/bioconductor-chromvar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chromvar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chromvar/container.yaml"
updated_at: "2024-08-11 02:57:21.305048"
latest: "1.24.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chromvar"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.16.0--r41hc247a5b_2"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
 - "1.20.0--r42hf17093f_1"
 - "1.22.1--r43hf17093f_0"
 - "1.24.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chromvar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chromvar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chromvar", "latest": {"1.24.0--r43hf17093f_0": "sha256:dca5723299579ee15f1a2a3d21ae8036beba478e7c5a69ef060afe2ca4c97f4e"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:501b23133a0e6284ffae4c11d4de4daf29226ddd532d5b242228f8d4721c4a0c", "1.20.0--r42hc247a5b_0": "sha256:7675ca05aee9e0b28fba6e36aea7d26a50002ec05daf239c05e89f41df7db0b4", "1.16.0--r41hc247a5b_2": "sha256:6e69e19984c751b4d60c663b4342a09ba65ce32193728a9bc424419fc7109240", "1.14.0--r41h399db7b_0": "sha256:8124a64b98261ea4160c715410e8f2f5135015f0b25c25867122a8186d735d45", "1.12.0--r40h399db7b_1": "sha256:89e7e99ee776309183d4b9dc0f514eba5b399c667b615864dcfc669c990c5095", "1.10.0--r40h5f743cb_0": "sha256:42e5dee8603f49efa74a0aea1174d56e405e2860aa77e47524e6bfdef102fddd", "1.20.0--r42hf17093f_1": "sha256:85cb751898e33d01c320aaf92c6c75b0b07232e37523ef0e4f23c4008e2ff693", "1.22.1--r43hf17093f_0": "sha256:24b44771f0003280f9a5d8208a4b94c3925bce8e297f2c2cf0e3321d320d9e17", "1.24.0--r43hf17093f_0": "sha256:dca5723299579ee15f1a2a3d21ae8036beba478e7c5a69ef060afe2ca4c97f4e"}, "docker": "quay.io/biocontainers/bioconductor-chromvar", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chromvar.
shpc-registry automated BioContainers addition for bioconductor-chromvar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chromvar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chromvar:1.24.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chromvar/1.24.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-chromvar/1.24.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chromvar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromvar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromvar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chromvar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chromvar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chromvar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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