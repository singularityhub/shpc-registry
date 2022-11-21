---
layout: container
name:  "quay.io/biocontainers/bioconductor-chimphumanbraindata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chimphumanbraindata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chimphumanbraindata/container.yaml"
updated_at: "2022-11-21 00:41:30.633453"
latest: "1.36.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chimphumanbraindata"
aliases:
 - ".bioconductor-chimphumanbraindata-post-link.sh"
 - ".bioconductor-chimphumanbraindata-pre-unlink.sh"
versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chimphumanbraindata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chimphumanbraindata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chimphumanbraindata", "latest": {"1.36.0--r42hdfd78af_0": "sha256:a9b7e8a0b19f5da04d987c5fb198d501567381c236c266b586f5b28752804da3"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:dc94d743d7dc00051d265e8a854e96b49ca494af216c3213408017ecce1e283e", "1.36.0--r42hdfd78af_0": "sha256:a9b7e8a0b19f5da04d987c5fb198d501567381c236c266b586f5b28752804da3"}, "docker": "quay.io/biocontainers/bioconductor-chimphumanbraindata", "aliases": {".bioconductor-chimphumanbraindata-post-link.sh": "/usr/local/bin/.bioconductor-chimphumanbraindata-post-link.sh", ".bioconductor-chimphumanbraindata-pre-unlink.sh": "/usr/local/bin/.bioconductor-chimphumanbraindata-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chimphumanbraindata.
shpc-registry automated BioContainers addition for bioconductor-chimphumanbraindata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chimphumanbraindata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chimphumanbraindata:1.36.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chimphumanbraindata/1.36.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chimphumanbraindata/1.36.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chimphumanbraindata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chimphumanbraindata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chimphumanbraindata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chimphumanbraindata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chimphumanbraindata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chimphumanbraindata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-chimphumanbraindata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-chimphumanbraindata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-chimphumanbraindata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-chimphumanbraindata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-chimphumanbraindata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-chimphumanbraindata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-chimphumanbraindata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-chimphumanbraindata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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