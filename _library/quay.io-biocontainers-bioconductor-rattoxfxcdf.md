---
layout: container
name:  "quay.io/biocontainers/bioconductor-rattoxfxcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rattoxfxcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rattoxfxcdf/container.yaml"
updated_at: "2025-01-20 02:50:01.873472"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-rattoxfxcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-rattoxfxcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rattoxfxcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rattoxfxcdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:67ae1936ab9195bc12702c08bfbbd4e1841a2c5aae5d6afdf5d46722b6bcedb5"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:f9fe8458819c1b53c4ded21bec6d404ae815e88323194a587be937e4a8485ce9", "2.18.0--r42hdfd78af_10": "sha256:93f96f1539d206dae8ef317b1f696aeeddb341ce5dc20b78f440c09011ce5600", "2.18.0--r43hdfd78af_11": "sha256:7b5f9e77b2cf20718d8299d0f99e364f1eb2f39036c178db7594d4fceeae18a2", "2.18.0--r43hdfd78af_12": "sha256:4080b7b8a633fd3e76685668b41b6683a188dd181e3523264df7e74a8e98b7f6", "2.18.0--r44hdfd78af_13": "sha256:67ae1936ab9195bc12702c08bfbbd4e1841a2c5aae5d6afdf5d46722b6bcedb5"}, "docker": "quay.io/biocontainers/bioconductor-rattoxfxcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rattoxfxcdf.
shpc-registry automated BioContainers addition for bioconductor-rattoxfxcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rattoxfxcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rattoxfxcdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rattoxfxcdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-rattoxfxcdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rattoxfxcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rattoxfxcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rattoxfxcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rattoxfxcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rattoxfxcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rattoxfxcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rattoxfxcdf

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