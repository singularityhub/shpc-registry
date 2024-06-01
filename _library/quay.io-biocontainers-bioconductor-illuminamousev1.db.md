---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminamousev1.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminamousev1.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminamousev1.db/container.yaml"
updated_at: "2024-06-01 02:57:31.030599"
latest: "1.26.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminamousev1.db"

versions:
 - "1.26.0--r41hdfd78af_9"
 - "1.26.0--r42hdfd78af_10"
 - "1.26.0--r43hdfd78af_11"
 - "1.26.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminamousev1.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminamousev1.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminamousev1.db", "latest": {"1.26.0--r43hdfd78af_12": "sha256:22d868485c9d78101e779a877d2a881cb3f057b66108814735f45284f0c69a3e"}, "tags": {"1.26.0--r41hdfd78af_9": "sha256:5cedf7992a12bacdc76915d5743ff0634e448cfe2b1a695aca733f79a9167303", "1.26.0--r42hdfd78af_10": "sha256:3e165ee08ea602eb69fa48de41a806af1a47b23fb2341b7869afa9871706d1b2", "1.26.0--r43hdfd78af_11": "sha256:847bade0b59192f1b380635ca668f8253349ebda0983a196588f39dfac578b9c", "1.26.0--r43hdfd78af_12": "sha256:22d868485c9d78101e779a877d2a881cb3f057b66108814735f45284f0c69a3e"}, "docker": "quay.io/biocontainers/bioconductor-illuminamousev1.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminamousev1.db.
shpc-registry automated BioContainers addition for bioconductor-illuminamousev1.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminamousev1.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminamousev1.db:1.26.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminamousev1.db/1.26.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-illuminamousev1.db/1.26.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminamousev1.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminamousev1.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminamousev1.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminamousev1.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminamousev1.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminamousev1.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminamousev1.db

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