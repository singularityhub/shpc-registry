---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm39.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm39.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm39.refgene/container.yaml"
updated_at: "2025-02-03 03:31:03.212507"
latest: "3.19.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.mmusculus.ucsc.mm39.refgene"

versions:
 - "3.12.0--r41hdfd78af_4"
 - "3.12.0--r42hdfd78af_5"
 - "3.12.0--r43hdfd78af_6"
 - "3.18.0--r43hdfd78af_0"
 - "3.19.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm39.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.mmusculus.ucsc.mm39.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm39.refgene", "latest": {"3.19.0--r44hdfd78af_0": "sha256:258bcc8047670ecec0d85705d94dc918e209d62a90238777485176943eb1f37a"}, "tags": {"3.12.0--r41hdfd78af_4": "sha256:793eddf2edc01b3961b03ccb2c7f0576eb985e864e92f351767ef99efb83566a", "3.12.0--r42hdfd78af_5": "sha256:c99ff37ab5f91204342128055dc24629d46cef0243e9e0757f75cedf4ef1c447", "3.12.0--r43hdfd78af_6": "sha256:f898e4c5cba39e2fdb9ae403af351ec90be8dc4a9349637b7896242d48c0d7f1", "3.18.0--r43hdfd78af_0": "sha256:6dd6e020328f6003ebcb96cb3729c88108ab42e7c6bc36fa25e2ff4c7bdd7c1c", "3.19.0--r44hdfd78af_0": "sha256:258bcc8047670ecec0d85705d94dc918e209d62a90238777485176943eb1f37a"}, "docker": "quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm39.refgene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm39.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm39.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm39.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm39.refgene:3.19.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm39.refgene/3.19.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm39.refgene/3.19.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.mmusculus.ucsc.mm39.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm39.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm39.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.mmusculus.ucsc.mm39.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm39.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm39.refgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txdb.mmusculus.ucsc.mm39.refgene

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