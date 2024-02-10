---
layout: container
name:  "quay.io/biocontainers/bioconductor-iasva"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-iasva/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-iasva/container.yaml"
updated_at: "2024-02-10 02:21:56.792848"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-iasva"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-iasva"
config: {"url": "https://biocontainers.pro/tools/bioconductor-iasva", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-iasva", "latest": {"1.20.0--r43hdfd78af_0": "sha256:bd2b9675128d03aad8e8a487e87fe1816b84e1096252c95a2f7ea2e1e952191e"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:f7aaf404d78ff993a53528403617218ae1e252c08e9f0aff5f34b68fc576ba28", "1.12.0--r41hdfd78af_0": "sha256:6721cb2d90391960ac064dac6916c4b8d1f715820cd0cf64eaded1c55daa3e72", "1.10.0--r41hdfd78af_0": "sha256:7f46a9417c19cf94f18c3e879169f95370f9245cbaf926ef2ea18abad36e6d7e", "1.16.0--r42hdfd78af_0": "sha256:6cf1f57887fe288071fc8e55cdc728c140d9205fc8a29bf9b0aa0b713d6d9111", "1.18.0--r43hdfd78af_0": "sha256:f037c5224d8559e3d411199ac036f6b39ecf9c585dbe03eb939d03071b38c539", "1.20.0--r43hdfd78af_0": "sha256:bd2b9675128d03aad8e8a487e87fe1816b84e1096252c95a2f7ea2e1e952191e"}, "docker": "quay.io/biocontainers/bioconductor-iasva", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-iasva.
shpc-registry automated BioContainers addition for bioconductor-iasva
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-iasva
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-iasva:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-iasva/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-iasva/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-iasva-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iasva-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iasva-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-iasva-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-iasva-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-iasva-inspect-deffile:

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