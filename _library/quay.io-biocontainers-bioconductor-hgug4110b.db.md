---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgug4110b.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgug4110b.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgug4110b.db/container.yaml"
updated_at: "2024-01-28 02:27:07.544994"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgug4110b.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgug4110b.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgug4110b.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgug4110b.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:c909e2ac9336a2cd1b6a792e7c5958cf95f80c2b3fdbf2b10cd292c899cb850a"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:48b9abbc99f22984247db39a217f2ba83617fa51a5b9ba445a0e097aa984add3", "3.2.3--r42hdfd78af_10": "sha256:ff0bb7de839f4d586dd8456d3f580e3fcf91eb4599a8e29186d5303746c8d229", "3.2.3--r43hdfd78af_11": "sha256:04585afd1555891b909fb0a0831992fe16520e2d1ea284435d21ba05f6a7d1f9", "3.2.3--r43hdfd78af_12": "sha256:c909e2ac9336a2cd1b6a792e7c5958cf95f80c2b3fdbf2b10cd292c899cb850a"}, "docker": "quay.io/biocontainers/bioconductor-hgug4110b.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgug4110b.db.
shpc-registry automated BioContainers addition for bioconductor-hgug4110b.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgug4110b.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgug4110b.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgug4110b.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgug4110b.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgug4110b.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgug4110b.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgug4110b.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgug4110b.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgug4110b.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgug4110b.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgug4110b.db

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