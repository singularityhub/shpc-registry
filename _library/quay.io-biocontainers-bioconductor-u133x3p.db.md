---
layout: container
name:  "quay.io/biocontainers/bioconductor-u133x3p.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-u133x3p.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-u133x3p.db/container.yaml"
updated_at: "2025-05-26 12:13:29.510246"
latest: "3.2.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-u133x3p.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-u133x3p.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-u133x3p.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-u133x3p.db", "latest": {"3.2.3--r44hdfd78af_13": "sha256:a08a025768b4d779af48db6deca6ebe80e401ba01b5c415e7456101c98ebda34"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:156484a9eb3d6f6b072a82a7a30c80b43257a55c6f21a9d32e894e6a7ca7fb8b", "3.2.3--r42hdfd78af_10": "sha256:a367e9ccdd1e73d30707277fda3aa10cfbf553afa3a85a8f3203d7a3309c7f6c", "3.2.3--r43hdfd78af_11": "sha256:0419328a89925029d7b217476d47f2cbe51c0552a086ed0a7d71eee7d379c87b", "3.2.3--r43hdfd78af_12": "sha256:50ac584b66e4f072e27762e35f65b16e034437cac7a5932d8e20daa5b9d4a376", "3.2.3--r44hdfd78af_13": "sha256:a08a025768b4d779af48db6deca6ebe80e401ba01b5c415e7456101c98ebda34"}, "docker": "quay.io/biocontainers/bioconductor-u133x3p.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-u133x3p.db.
shpc-registry automated BioContainers addition for bioconductor-u133x3p.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-u133x3p.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-u133x3p.db:3.2.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-u133x3p.db/3.2.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-u133x3p.db/3.2.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-u133x3p.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-u133x3p.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-u133x3p.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-u133x3p.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-u133x3p.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-u133x3p.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-u133x3p.db

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