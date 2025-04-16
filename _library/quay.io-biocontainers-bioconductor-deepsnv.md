---
layout: container
name:  "quay.io/biocontainers/bioconductor-deepsnv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-deepsnv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-deepsnv/container.yaml"
updated_at: "2025-04-16 03:49:06.132492"
latest: "1.52.0--r44h77050f0_1"
container_url: "https://biocontainers.pro/tools/bioconductor-deepsnv"

versions:
 - "1.40.0--r41hc247a5b_2"
 - "1.44.0--r42hc247a5b_0"
 - "1.44.0--r42hf17093f_1"
 - "1.46.0--r43hf17093f_0"
 - "1.48.0--r43hf17093f_0"
 - "1.52.0--r44h77050f0_0"
 - "1.52.0--r44h77050f0_1"
description: "shpc-registry automated BioContainers addition for bioconductor-deepsnv"
config: {"url": "https://biocontainers.pro/tools/bioconductor-deepsnv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-deepsnv", "latest": {"1.52.0--r44h77050f0_1": "sha256:ab5adbb9254212cccf6f77a6990db9fb99a7b27dbb2167cffc8f82bc61df58ed"}, "tags": {"1.40.0--r41hc247a5b_2": "sha256:bb10e0d7d40af1ea36021cdf900e2ca14a3caf5fa785957000ebb33fd5770722", "1.44.0--r42hc247a5b_0": "sha256:3e0f51ff9e3c9c11bbf9a2684efcee34365b53c99f1729b717712e2f115d8823", "1.44.0--r42hf17093f_1": "sha256:50b3932c0abb92ada5fe2abfa3867511d274514e9e23a5687195f9046a51ac74", "1.46.0--r43hf17093f_0": "sha256:3e2cff0a5fefe3df2104597761b4fa1ef41e6183617cc1e31d560784a8ce5fa0", "1.48.0--r43hf17093f_0": "sha256:a320c0fa910bb99d925ecb34ffcb39536bcbaaff31f617e51628bc55d2b39222", "1.52.0--r44h77050f0_0": "sha256:99065ee48c22b7290b5797ab12d450a362442deb6dd5c6bdd9f220265955e05f", "1.52.0--r44h77050f0_1": "sha256:ab5adbb9254212cccf6f77a6990db9fb99a7b27dbb2167cffc8f82bc61df58ed"}, "docker": "quay.io/biocontainers/bioconductor-deepsnv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-deepsnv.
shpc-registry automated BioContainers addition for bioconductor-deepsnv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-deepsnv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-deepsnv:1.52.0--r44h77050f0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-deepsnv/1.52.0--r44h77050f0_1
$ module help quay.io/biocontainers/bioconductor-deepsnv/1.52.0--r44h77050f0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-deepsnv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deepsnv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deepsnv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-deepsnv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-deepsnv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-deepsnv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-deepsnv

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