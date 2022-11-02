---
layout: container
name:  "quay.io/biocontainers/bioconductor-drugvsdiseasedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-drugvsdiseasedata/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-drugvsdiseasedata/container.yaml"
updated_at: "2022-11-02 19:13:12.655124"
latest: "1.30.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-drugvsdiseasedata"
aliases:
 - ".bioconductor-drugvsdiseasedata-post-link.sh"
 - ".bioconductor-drugvsdiseasedata-pre-unlink.sh"
versions:
 - "1.30.0--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-drugvsdiseasedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-drugvsdiseasedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-drugvsdiseasedata", "latest": {"1.30.0--r41hdfd78af_1": "sha256:282ed4e9d6fb2345acfeee7141129a89e51387c7878cff74a51caa811bc4300d"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:282ed4e9d6fb2345acfeee7141129a89e51387c7878cff74a51caa811bc4300d"}, "docker": "quay.io/biocontainers/bioconductor-drugvsdiseasedata", "aliases": {".bioconductor-drugvsdiseasedata-post-link.sh": "/usr/local/bin/.bioconductor-drugvsdiseasedata-post-link.sh", ".bioconductor-drugvsdiseasedata-pre-unlink.sh": "/usr/local/bin/.bioconductor-drugvsdiseasedata-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-drugvsdiseasedata.
shpc-registry automated BioContainers addition for bioconductor-drugvsdiseasedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-drugvsdiseasedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-drugvsdiseasedata:1.30.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-drugvsdiseasedata/1.30.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-drugvsdiseasedata/1.30.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-drugvsdiseasedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drugvsdiseasedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drugvsdiseasedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-drugvsdiseasedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-drugvsdiseasedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-drugvsdiseasedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-drugvsdiseasedata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-drugvsdiseasedata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-drugvsdiseasedata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-drugvsdiseasedata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-drugvsdiseasedata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-drugvsdiseasedata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-drugvsdiseasedata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-drugvsdiseasedata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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