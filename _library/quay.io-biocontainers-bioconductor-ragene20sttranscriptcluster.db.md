---
layout: container
name:  "quay.io/biocontainers/bioconductor-ragene20sttranscriptcluster.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ragene20sttranscriptcluster.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ragene20sttranscriptcluster.db/container.yaml"
updated_at: "2023-07-06 03:24:01.011039"
latest: "8.8.0--r42hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-ragene20sttranscriptcluster.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-ragene20sttranscriptcluster.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ragene20sttranscriptcluster.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ragene20sttranscriptcluster.db", "latest": {"8.8.0--r42hdfd78af_2": "sha256:26d519615720e34334f2ee7c35a249ecef3d1d464fe929f9120babe4f6cadd0b"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:6d2586ae5a85f6f3e739a5e89da1adf1a1e69926077b9d81fe45f2f739c3bc6f", "8.8.0--r42hdfd78af_2": "sha256:26d519615720e34334f2ee7c35a249ecef3d1d464fe929f9120babe4f6cadd0b"}, "docker": "quay.io/biocontainers/bioconductor-ragene20sttranscriptcluster.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ragene20sttranscriptcluster.db.
shpc-registry automated BioContainers addition for bioconductor-ragene20sttranscriptcluster.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ragene20sttranscriptcluster.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ragene20sttranscriptcluster.db:8.8.0--r42hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ragene20sttranscriptcluster.db/8.8.0--r42hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-ragene20sttranscriptcluster.db/8.8.0--r42hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ragene20sttranscriptcluster.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ragene20sttranscriptcluster.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ragene20sttranscriptcluster.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ragene20sttranscriptcluster.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ragene20sttranscriptcluster.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ragene20sttranscriptcluster.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ragene20sttranscriptcluster.db

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