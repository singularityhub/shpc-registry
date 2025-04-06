---
layout: container
name:  "quay.io/biocontainers/bioconductor-porcinecdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-porcinecdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-porcinecdf/container.yaml"
updated_at: "2025-04-06 03:24:35.538524"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-porcinecdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-porcinecdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-porcinecdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-porcinecdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:00ea2141d0e3eda59f7f70f1ec91891beab2f1b8ac3c556ecc22b9b6bc34af5a"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:b43fa12e7f5dbcceadb16b0dc7e1fb9d4c532f268fec82569d22d0f7c944f808", "2.18.0--r42hdfd78af_10": "sha256:162bb68a48c6debdb87f2852dfd371415f3c319c53eb9ec5a0b319402d2b7fe0", "2.18.0--r43hdfd78af_11": "sha256:558926a5d3ee853c5a5bf5c29398ea6c18f4d9a8aa69a139e87ee1cbdb69a43f", "2.18.0--r43hdfd78af_12": "sha256:f542ab55aa09650ecb3b4e6f7d4aacd2ea5b3ce046ccef79b3b9a89fc7690f17", "2.18.0--r44hdfd78af_13": "sha256:00ea2141d0e3eda59f7f70f1ec91891beab2f1b8ac3c556ecc22b9b6bc34af5a"}, "docker": "quay.io/biocontainers/bioconductor-porcinecdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-porcinecdf.
shpc-registry automated BioContainers addition for bioconductor-porcinecdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-porcinecdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-porcinecdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-porcinecdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-porcinecdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-porcinecdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-porcinecdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-porcinecdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-porcinecdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-porcinecdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-porcinecdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-porcinecdf

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