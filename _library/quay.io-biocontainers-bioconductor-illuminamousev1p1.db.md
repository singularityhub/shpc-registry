---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminamousev1p1.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminamousev1p1.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminamousev1p1.db/container.yaml"
updated_at: "2024-08-12 03:26:40.263672"
latest: "1.26.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminamousev1p1.db"

versions:
 - "1.26.0--r41hdfd78af_9"
 - "1.26.0--r42hdfd78af_10"
 - "1.26.0--r43hdfd78af_11"
 - "1.26.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminamousev1p1.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminamousev1p1.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminamousev1p1.db", "latest": {"1.26.0--r43hdfd78af_12": "sha256:db763baab1a4d1cae65fbefaefbee5e5bca5979d414de2153e842e827db3d8c5"}, "tags": {"1.26.0--r41hdfd78af_9": "sha256:78a035b8985bdbc363c9c0fae219c81c133f27e00bfa0aaff242eddca1d259c3", "1.26.0--r42hdfd78af_10": "sha256:9411545e84d9c8058fe95c96d84a9a210e3d7676158495745209f6a9a5cbde33", "1.26.0--r43hdfd78af_11": "sha256:0179104d8840748fbd563f7a2c781d2dca4c88686cb40a9147900f3094bec199", "1.26.0--r43hdfd78af_12": "sha256:db763baab1a4d1cae65fbefaefbee5e5bca5979d414de2153e842e827db3d8c5"}, "docker": "quay.io/biocontainers/bioconductor-illuminamousev1p1.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminamousev1p1.db.
shpc-registry automated BioContainers addition for bioconductor-illuminamousev1p1.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminamousev1p1.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminamousev1p1.db:1.26.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminamousev1p1.db/1.26.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-illuminamousev1p1.db/1.26.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminamousev1p1.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminamousev1p1.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminamousev1p1.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminamousev1p1.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminamousev1p1.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminamousev1p1.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminamousev1p1.db

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