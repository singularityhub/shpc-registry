---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathwaypca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathwaypca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathwaypca/container.yaml"
updated_at: "2025-09-22 03:30:47.034701"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pathwaypca"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.1--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pathwaypca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathwaypca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathwaypca", "latest": {"1.22.0--r44hdfd78af_0": "sha256:0589c615a8cb21290af84301e7990eb208ca04926abe8070176d0eeab1d87eb7"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:aa800f8a0aaa1f192fbf31e092c404ff26447e35add0638e4f9294c533c0a734", "1.14.0--r42hdfd78af_0": "sha256:565ecf63c62ae8c6deb83023e366666d23b745d6338156924015248ceffbcbf9", "1.10.0--r41hdfd78af_0": "sha256:294f7cd7338002cfa231487fd89a8f3ce2679a9dc8b3c9924248fdc0aa6e205f", "1.16.1--r43hdfd78af_0": "sha256:9fe07bbeb92aed0bd662fa0e91c821f9a91039b6e389ba60f4fab254ba1446c7", "1.18.0--r43hdfd78af_0": "sha256:6dbfb60c0f473590abdcd321903893832dc24926a129dd97b20652753741f91f", "1.22.0--r44hdfd78af_0": "sha256:0589c615a8cb21290af84301e7990eb208ca04926abe8070176d0eeab1d87eb7"}, "docker": "quay.io/biocontainers/bioconductor-pathwaypca", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pathwaypca.
shpc-registry automated BioContainers addition for bioconductor-pathwaypca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pathwaypca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pathwaypca:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pathwaypca/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pathwaypca/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pathwaypca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathwaypca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathwaypca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pathwaypca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pathwaypca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pathwaypca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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