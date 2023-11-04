---
layout: container
name:  "quay.io/biocontainers/bioconductor-epivizrdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epivizrdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epivizrdata/container.yaml"
updated_at: "2023-11-04 02:25:36.947531"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-epivizrdata"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-epivizrdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epivizrdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epivizrdata", "latest": {"1.28.0--r43hdfd78af_0": "sha256:9d394e8b3ba1e777f33a066a97fe7d9f7bd66b6ef5c5415306c6e1a8253ee680"}, "tags": {"1.8.0--r351_0": "sha256:887c44c2b50a3f36b1c68ab1316a7771f5018c94a8806d90af392151bc52ab5b", "1.26.0--r42hdfd78af_0": "sha256:9fe805cd2c3042d1c08199b46e15f382937d68c968d44e15a63423ad9db3ba8b", "1.22.0--r41hdfd78af_0": "sha256:41a8d765acdac12a687d44b38a368f9b8d800db5cd09538a751839a413cb060c", "1.20.0--r41hdfd78af_0": "sha256:cb5b4b8571bb8af3c44fc006c92541cc8896e64f972162d250f90ed45cd989fc", "1.18.0--r40hdfd78af_1": "sha256:c9e2c461e9197c3921b300e35274873261a935a742f995ad7f1c4380c80686c0", "1.16.0--r40_0": "sha256:c55a1556c3cc0a9a53befecb50cca35a2613e81b338d7df7056747bebe526544", "1.28.0--r43hdfd78af_0": "sha256:9d394e8b3ba1e777f33a066a97fe7d9f7bd66b6ef5c5415306c6e1a8253ee680"}, "docker": "quay.io/biocontainers/bioconductor-epivizrdata", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epivizrdata.
shpc-registry automated BioContainers addition for bioconductor-epivizrdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizrdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizrdata:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epivizrdata/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-epivizrdata/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epivizrdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizrdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizrdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epivizrdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epivizrdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epivizrdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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