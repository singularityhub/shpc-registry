---
layout: container
name:  "quay.io/biocontainers/bioconductor-pmp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pmp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pmp/container.yaml"
updated_at: "2025-01-28 02:52:54.159991"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pmp"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pmp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pmp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pmp", "latest": {"1.18.0--r44hdfd78af_0": "sha256:7d41872d1f870b304e8d02255fb29e321b7e05ad857d14f2c91383c3f203016d"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:3822b7d67601931251672deb9320dfc4d6cec33fb0f657877c88a6520020c9c2", "1.10.0--r42hdfd78af_0": "sha256:7ef968af0c80e1f1163ab22d893c0bae9635a8f993d491800163377d28b0696d", "1.12.0--r43hdfd78af_0": "sha256:9ed3a95a72e47d6f520cf0497d39260d085df1e8b01e50c9756232041ebf087c", "1.14.0--r43hdfd78af_0": "sha256:8fc119a0320019072a2995b514fc09a016851fe586a58890c403856885bdc09e", "1.18.0--r44hdfd78af_0": "sha256:7d41872d1f870b304e8d02255fb29e321b7e05ad857d14f2c91383c3f203016d"}, "docker": "quay.io/biocontainers/bioconductor-pmp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pmp.
shpc-registry automated BioContainers addition for bioconductor-pmp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pmp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pmp:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pmp/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pmp/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pmp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pmp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pmp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pmp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pmp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pmp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pmp

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