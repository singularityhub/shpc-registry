---
layout: container
name:  "quay.io/biocontainers/bioconductor-humanchrloc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-humanchrloc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-humanchrloc/container.yaml"
updated_at: "2024-06-18 03:12:59.244026"
latest: "2.1.6--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-humanchrloc"

versions:
 - "2.1.6--r41hdfd78af_9"
 - "2.1.6--r42hdfd78af_10"
 - "2.1.6--r43hdfd78af_11"
 - "2.1.6--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-humanchrloc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-humanchrloc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-humanchrloc", "latest": {"2.1.6--r43hdfd78af_12": "sha256:4d143226a140d6ffc80e4c9a80c82806c690127ef7bc82f53798394a296d4682"}, "tags": {"2.1.6--r41hdfd78af_9": "sha256:befce3387fe5d5f7c041c1c39c51310c59c23bfc1023209257b3034ae1c84e4b", "2.1.6--r42hdfd78af_10": "sha256:49678e0249f3c21fdc8da16be16ebb2a6402fe0aa0b94b12700484bae564f137", "2.1.6--r43hdfd78af_11": "sha256:997309bbbe3184c9805c61b02fe27bd76bdfded132448e842a1dad8359043925", "2.1.6--r43hdfd78af_12": "sha256:4d143226a140d6ffc80e4c9a80c82806c690127ef7bc82f53798394a296d4682"}, "docker": "quay.io/biocontainers/bioconductor-humanchrloc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-humanchrloc.
shpc-registry automated BioContainers addition for bioconductor-humanchrloc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-humanchrloc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-humanchrloc:2.1.6--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-humanchrloc/2.1.6--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-humanchrloc/2.1.6--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-humanchrloc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humanchrloc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humanchrloc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-humanchrloc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-humanchrloc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-humanchrloc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-humanchrloc

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