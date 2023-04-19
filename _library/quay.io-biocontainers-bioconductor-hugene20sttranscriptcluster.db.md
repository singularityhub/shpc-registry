---
layout: container
name:  "quay.io/biocontainers/bioconductor-hugene20sttranscriptcluster.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hugene20sttranscriptcluster.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hugene20sttranscriptcluster.db/container.yaml"
updated_at: "2023-04-19 03:15:22.498068"
latest: "8.8.0--r42hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-hugene20sttranscriptcluster.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-hugene20sttranscriptcluster.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hugene20sttranscriptcluster.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hugene20sttranscriptcluster.db", "latest": {"8.8.0--r42hdfd78af_2": "sha256:13550dd59dd05eaa94e2b7a6102274fbc25a6a22f521d56dec90191022bf79e1"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:19e20415369eeb1f747085572ab6ac634ee94e92401cf0fece2c2f0713bb865c", "8.8.0--r42hdfd78af_2": "sha256:13550dd59dd05eaa94e2b7a6102274fbc25a6a22f521d56dec90191022bf79e1"}, "docker": "quay.io/biocontainers/bioconductor-hugene20sttranscriptcluster.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hugene20sttranscriptcluster.db.
shpc-registry automated BioContainers addition for bioconductor-hugene20sttranscriptcluster.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hugene20sttranscriptcluster.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hugene20sttranscriptcluster.db:8.8.0--r42hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hugene20sttranscriptcluster.db/8.8.0--r42hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-hugene20sttranscriptcluster.db/8.8.0--r42hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hugene20sttranscriptcluster.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hugene20sttranscriptcluster.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hugene20sttranscriptcluster.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hugene20sttranscriptcluster.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hugene20sttranscriptcluster.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hugene20sttranscriptcluster.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hugene20sttranscriptcluster.db

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