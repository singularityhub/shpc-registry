---
layout: container
name:  "quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp137"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp137/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp137/container.yaml"
updated_at: "2023-11-23 02:43:26.906418"
latest: "1.0.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-sift.hsapiens.dbsnp137"

versions:
 - "1.0.0--r41hdfd78af_9"
 - "1.0.0--r42hdfd78af_10"
 - "1.0.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-sift.hsapiens.dbsnp137"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sift.hsapiens.dbsnp137", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sift.hsapiens.dbsnp137", "latest": {"1.0.0--r43hdfd78af_11": "sha256:5ed937abfb783c4575a62010d516feb39d9797320e15e4d78ea39f350e4dbbd6"}, "tags": {"1.0.0--r41hdfd78af_9": "sha256:5aaa972e3d3dc84334bef8c49dbaeea44cc9988d7d5c7b42bfb7704dd256d17e", "1.0.0--r42hdfd78af_10": "sha256:72317e02b2499cf7e09315ef3dacc539c09a182cc833027ef1d37c9f887b8560", "1.0.0--r43hdfd78af_11": "sha256:5ed937abfb783c4575a62010d516feb39d9797320e15e4d78ea39f350e4dbbd6"}, "docker": "quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp137"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp137.
shpc-registry automated BioContainers addition for bioconductor-sift.hsapiens.dbsnp137
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp137
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp137:1.0.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp137/1.0.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp137/1.0.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sift.hsapiens.dbsnp137-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sift.hsapiens.dbsnp137-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sift.hsapiens.dbsnp137-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sift.hsapiens.dbsnp137-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sift.hsapiens.dbsnp137-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sift.hsapiens.dbsnp137-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sift.hsapiens.dbsnp137

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