---
layout: container
name:  "quay.io/biocontainers/bioconductor-shortread"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-shortread/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-shortread/container.yaml"
updated_at: "2025-02-22 03:28:00.090595"
latest: "1.64.0--r44h77050f0_0"
container_url: "https://biocontainers.pro/tools/bioconductor-shortread"

versions:
 - "1.52.0--r41hc247a5b_2"
 - "1.56.0--r42hc247a5b_0"
 - "1.56.0--r42hf17093f_1"
 - "1.58.0--r43hf17093f_0"
 - "1.60.0--r43hf17093f_0"
 - "1.60.0--r43hf17093f_1"
 - "1.64.0--r44h77050f0_0"
description: "shpc-registry automated BioContainers addition for bioconductor-shortread"
config: {"url": "https://biocontainers.pro/tools/bioconductor-shortread", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-shortread", "latest": {"1.64.0--r44h77050f0_0": "sha256:58844c53580b7ab7f7bd46f5208543b32dcac3da701b51d2e769613e770a89ce"}, "tags": {"1.52.0--r41hc247a5b_2": "sha256:77cb697d362696e9e66c70ed1131bf515a713d42d304038d788e73b1b1b1927a", "1.56.0--r42hc247a5b_0": "sha256:d5eafad82984223bd84e7af53b29a1adbf9591e7db27630875774fe3b97e77ac", "1.56.0--r42hf17093f_1": "sha256:3a56d14e6443f2de3cebfb63c790875f293735a68b81fdbe69d9a4b77b98728c", "1.58.0--r43hf17093f_0": "sha256:bc0eec4e3bccc18e0a1d5d9fe29b55e78a749fa44ab0a6bccdcc8d2d439ad6d7", "1.60.0--r43hf17093f_0": "sha256:b9ccdc86da92a7338b1c88836c1ef5510461e4851201362cddd8fd774e62fdf9", "1.60.0--r43hf17093f_1": "sha256:29b30e626b810ff6bb02deaf0d7fbb7c004d4e37399fc0551e0a9dda7eb78634", "1.64.0--r44h77050f0_0": "sha256:58844c53580b7ab7f7bd46f5208543b32dcac3da701b51d2e769613e770a89ce"}, "docker": "quay.io/biocontainers/bioconductor-shortread"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-shortread.
shpc-registry automated BioContainers addition for bioconductor-shortread
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-shortread
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-shortread:1.64.0--r44h77050f0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-shortread/1.64.0--r44h77050f0_0
$ module help quay.io/biocontainers/bioconductor-shortread/1.64.0--r44h77050f0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-shortread-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-shortread-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-shortread-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-shortread-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-shortread-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-shortread-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-shortread

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