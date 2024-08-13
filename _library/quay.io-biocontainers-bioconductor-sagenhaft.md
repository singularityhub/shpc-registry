---
layout: container
name:  "quay.io/biocontainers/bioconductor-sagenhaft"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sagenhaft/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sagenhaft/container.yaml"
updated_at: "2024-08-13 03:02:34.400711"
latest: "1.72.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-sagenhaft"

versions:
 - "1.64.0--r41hdfd78af_0"
 - "1.68.0--r42hdfd78af_0"
 - "1.70.0--r43hdfd78af_0"
 - "1.72.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-sagenhaft"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sagenhaft", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sagenhaft", "latest": {"1.72.0--r43hdfd78af_1": "sha256:9673a25c24ea006d14a39a2ed55aed9a78a973103514a5811f1406a7b011fbbe"}, "tags": {"1.64.0--r41hdfd78af_0": "sha256:d73a32bac8e7599e715ca3eb466756ceba874fc963c3fca4247048017e7cda0d", "1.68.0--r42hdfd78af_0": "sha256:44ee5013bf0e0d839cc816e38f04f4995a7929203d939af4d339149039ead521", "1.70.0--r43hdfd78af_0": "sha256:6a830adda0cbd15c399634a4382637ac2b217136425b731db0d381b40e3fee6b", "1.72.0--r43hdfd78af_1": "sha256:9673a25c24ea006d14a39a2ed55aed9a78a973103514a5811f1406a7b011fbbe"}, "docker": "quay.io/biocontainers/bioconductor-sagenhaft"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sagenhaft.
shpc-registry automated BioContainers addition for bioconductor-sagenhaft
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sagenhaft
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sagenhaft:1.72.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sagenhaft/1.72.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-sagenhaft/1.72.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sagenhaft-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sagenhaft-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sagenhaft-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sagenhaft-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sagenhaft-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sagenhaft-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sagenhaft

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