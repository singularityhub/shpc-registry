---
layout: container
name:  "quay.io/biocontainers/bioconductor-hs6ug171.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hs6ug171.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hs6ug171.db/container.yaml"
updated_at: "2025-01-26 02:49:59.828042"
latest: "3.2.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hs6ug171.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hs6ug171.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hs6ug171.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hs6ug171.db", "latest": {"3.2.3--r44hdfd78af_13": "sha256:de776870c69e571787cdd5c9bce522b0f5e525812ebaf5077bf99b6f4ffa8b32"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:8d7e514a5b0e102ccf51dd5f40799af3c879d5283d8d7a91966060cc8d60cac3", "3.2.3--r42hdfd78af_10": "sha256:f4737c87ffa25d8fde47ada0d7217068bca61f9b495498194389a3349f15746c", "3.2.3--r43hdfd78af_11": "sha256:dd958671739291b62b03c15006211a34b595daf59b67b8978ff1d9cbfdc02ba8", "3.2.3--r43hdfd78af_12": "sha256:6ad4d32a03e447d0fb63cb22d73b6bc6e90999f00d5e7fed26ef889ca730a41d", "3.2.3--r44hdfd78af_13": "sha256:de776870c69e571787cdd5c9bce522b0f5e525812ebaf5077bf99b6f4ffa8b32"}, "docker": "quay.io/biocontainers/bioconductor-hs6ug171.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hs6ug171.db.
shpc-registry automated BioContainers addition for bioconductor-hs6ug171.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hs6ug171.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hs6ug171.db:3.2.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hs6ug171.db/3.2.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hs6ug171.db/3.2.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hs6ug171.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hs6ug171.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hs6ug171.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hs6ug171.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hs6ug171.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hs6ug171.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hs6ug171.db

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