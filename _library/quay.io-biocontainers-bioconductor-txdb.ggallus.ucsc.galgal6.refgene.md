---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal6.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal6.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal6.refgene/container.yaml"
updated_at: "2025-07-31 11:33:22.480055"
latest: "3.10.0--r43hdfd78af_8"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.ggallus.ucsc.galgal6.refgene"

versions:
 - "3.10.0--r41hdfd78af_6"
 - "3.10.0--r42hdfd78af_7"
 - "3.10.0--r43hdfd78af_8"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.ggallus.ucsc.galgal6.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.ggallus.ucsc.galgal6.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.ggallus.ucsc.galgal6.refgene", "latest": {"3.10.0--r43hdfd78af_8": "sha256:3cd94149f3514ff92e7265040b07a5deb7ba41b690370a5a1495abe1a0307f50"}, "tags": {"3.10.0--r41hdfd78af_6": "sha256:757cc33d4282dd5b584d333a3a0176a41aafd02b0706b4b972e38214a88f1d98", "3.10.0--r42hdfd78af_7": "sha256:d0b0f94140c638abd5680fc048bf3b75e60ba9f27e0814531e26f1d4467e2f96", "3.10.0--r43hdfd78af_8": "sha256:3cd94149f3514ff92e7265040b07a5deb7ba41b690370a5a1495abe1a0307f50"}, "docker": "quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal6.refgene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal6.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.ggallus.ucsc.galgal6.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal6.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal6.refgene:3.10.0--r43hdfd78af_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal6.refgene/3.10.0--r43hdfd78af_8
$ module help quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal6.refgene/3.10.0--r43hdfd78af_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.ggallus.ucsc.galgal6.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal6.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal6.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.ggallus.ucsc.galgal6.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal6.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal6.refgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txdb.ggallus.ucsc.galgal6.refgene

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