---
layout: container
name:  "quay.io/biocontainers/bioconductor-illumina450probevariants.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illumina450probevariants.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illumina450probevariants.db/container.yaml"
updated_at: "2025-04-02 03:35:12.080817"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-illumina450probevariants.db"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-illumina450probevariants.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illumina450probevariants.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illumina450probevariants.db", "latest": {"1.42.0--r44hdfd78af_0": "sha256:aa43509c14ec667612cfe113fc39a35eb46a300b30e75bb30971618b97c27df3"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:9e46aea5ff59ce784072d181b0c2d5192689ab39808dceecc76d1cab7c1e9a41", "1.33.0--r42hdfd78af_0": "sha256:a370ea6e619ccdea4b3a70d6d6715ee0c301b0421012db0848f593e1e345340e", "1.34.0--r42hdfd78af_0": "sha256:f4087905ec585aaa99891ce16957e5294d5832c767367a9816daf0e7aff369d8", "1.36.0--r43hdfd78af_0": "sha256:aa3c57a2d80f356ff70e5706311b9eadc10dbfac6f42ca42431f4c19fa1ef037", "1.38.0--r43hdfd78af_0": "sha256:2c11932001daedfc1991373c5ddf07fb1d9e3fc85b0ac6b25987d391214ad9bc", "1.42.0--r44hdfd78af_0": "sha256:aa43509c14ec667612cfe113fc39a35eb46a300b30e75bb30971618b97c27df3"}, "docker": "quay.io/biocontainers/bioconductor-illumina450probevariants.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illumina450probevariants.db.
shpc-registry automated BioContainers addition for bioconductor-illumina450probevariants.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illumina450probevariants.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illumina450probevariants.db:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illumina450probevariants.db/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-illumina450probevariants.db/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illumina450probevariants.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illumina450probevariants.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illumina450probevariants.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illumina450probevariants.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illumina450probevariants.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illumina450probevariants.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illumina450probevariants.db

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