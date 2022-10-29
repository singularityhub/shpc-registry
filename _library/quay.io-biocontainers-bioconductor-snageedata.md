---
layout: container
name:  "quay.io/biocontainers/bioconductor-snageedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-snageedata/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-snageedata/container.yaml"
updated_at: "2022-10-29 18:25:26.718944"
latest: "1.30.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-snageedata"
aliases:
 - ".bioconductor-snageedata-post-link.sh"
 - ".bioconductor-snageedata-pre-unlink.sh"
versions:
 - "1.30.0--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-snageedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-snageedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-snageedata", "latest": {"1.30.0--r41hdfd78af_1": "sha256:ab28c4063f36abe0c92b7e6f9f5bd48a908092bbd21453cc45b34de6af66b4d8"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:ab28c4063f36abe0c92b7e6f9f5bd48a908092bbd21453cc45b34de6af66b4d8"}, "docker": "quay.io/biocontainers/bioconductor-snageedata", "aliases": {".bioconductor-snageedata-post-link.sh": "/usr/local/bin/.bioconductor-snageedata-post-link.sh", ".bioconductor-snageedata-pre-unlink.sh": "/usr/local/bin/.bioconductor-snageedata-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-snageedata.
shpc-registry automated BioContainers addition for bioconductor-snageedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-snageedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-snageedata:1.30.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-snageedata/1.30.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-snageedata/1.30.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-snageedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snageedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snageedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-snageedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-snageedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-snageedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-snageedata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-snageedata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-snageedata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-snageedata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-snageedata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-snageedata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-snageedata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-snageedata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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