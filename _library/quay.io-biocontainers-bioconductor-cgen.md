---
layout: container
name:  "quay.io/biocontainers/bioconductor-cgen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cgen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cgen/container.yaml"
updated_at: "2022-11-21 12:57:53.876794"
latest: "3.34.0--r42hefde4a7_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cgen"

versions:
 - "3.30.0--r41hefde4a7_2"
 - "3.34.0--r42hefde4a7_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cgen"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cgen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cgen", "latest": {"3.34.0--r42hefde4a7_0": "sha256:9aec86d82f54e7ac579e32458680906a498b5e8c5158fe16be73fe26bb01d7be"}, "tags": {"3.30.0--r41hefde4a7_2": "sha256:aae7b16f9b984647f1a1e4a21c52ba8650dbd1390ca7f35156045acdbde3a4be", "3.34.0--r42hefde4a7_0": "sha256:9aec86d82f54e7ac579e32458680906a498b5e8c5158fe16be73fe26bb01d7be"}, "docker": "quay.io/biocontainers/bioconductor-cgen"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cgen.
shpc-registry automated BioContainers addition for bioconductor-cgen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cgen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cgen:3.34.0--r42hefde4a7_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cgen/3.34.0--r42hefde4a7_0
$ module help quay.io/biocontainers/bioconductor-cgen/3.34.0--r42hefde4a7_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cgen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cgen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cgen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cgen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cgen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cgen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cgen

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