---
layout: container
name:  "quay.io/biocontainers/bioconductor-dexmadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dexmadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dexmadata/container.yaml"
updated_at: "2025-08-26 03:15:24.410062"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dexmadata"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dexmadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dexmadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dexmadata", "latest": {"1.14.0--r44hdfd78af_0": "sha256:bcdcbb7eafab43bce577a6636afcd00ee089b64ea257c8b6fcc1a3a5fa2161fd"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:0b44750cfadb17adec6a22adf72d816dfbcd56c9ac843c7928b11db610f0e2b7", "1.6.0--r42hdfd78af_0": "sha256:7f4478cdfe42e35b3e3e7cb4257b35fa648c82ad6ce1125c62912cd000bd43c0", "1.8.0--r43hdfd78af_0": "sha256:72bc4794a38bf1437c523bed9bbb9b5412ab8950beb11a680eb86f8116430a12", "1.10.0--r43hdfd78af_0": "sha256:fd9c0ddb9d50885b9c2f8f53bfbd6fe35936bedf2a38294691d52abaa7927d51", "1.14.0--r44hdfd78af_0": "sha256:bcdcbb7eafab43bce577a6636afcd00ee089b64ea257c8b6fcc1a3a5fa2161fd"}, "docker": "quay.io/biocontainers/bioconductor-dexmadata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dexmadata.
shpc-registry automated BioContainers addition for bioconductor-dexmadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dexmadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dexmadata:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dexmadata/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dexmadata/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dexmadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dexmadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dexmadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dexmadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dexmadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dexmadata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dexmadata

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