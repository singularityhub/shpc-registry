---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene/container.yaml"
updated_at: "2025-09-18 05:37:56.253502"
latest: "3.15.0--r44hdfd78af_3"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene"

versions:
 - "3.14.0--r41hdfd78af_1"
 - "3.15.0--r42hdfd78af_0"
 - "3.15.0--r43hdfd78af_1"
 - "3.15.0--r43hdfd78af_2"
 - "3.15.0--r44hdfd78af_3"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene", "latest": {"3.15.0--r44hdfd78af_3": "sha256:43d2cd4840be080420b55dd6b1170ed6facf854e1594a4e731099653b99d5d62"}, "tags": {"3.14.0--r41hdfd78af_1": "sha256:8d90988103e34742340152e702ec987931788771f7a601e53d39a4c5a7986e7b", "3.15.0--r42hdfd78af_0": "sha256:e094e0f9b50f311e5781387baab333d6337eeaab46ef1d5c0d5567ab72e24320", "3.15.0--r43hdfd78af_1": "sha256:43e4483f61f37f65dca2b90befc464bc2b4d796d0124bfde4b2856b0889aa4c2", "3.15.0--r43hdfd78af_2": "sha256:4a0b3ef637835d127afdf5936cd5dbc23a41d796ba374d4b12e569454ae2e9d8", "3.15.0--r44hdfd78af_3": "sha256:43d2cd4840be080420b55dd6b1170ed6facf854e1594a4e731099653b99d5d62"}, "docker": "quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene:3.15.0--r44hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene/3.15.0--r44hdfd78af_3
$ module help quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene/3.15.0--r44hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txdb.rnorvegicus.ucsc.rn7.refgene

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