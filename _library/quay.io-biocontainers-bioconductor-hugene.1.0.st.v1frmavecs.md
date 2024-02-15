---
layout: container
name:  "quay.io/biocontainers/bioconductor-hugene.1.0.st.v1frmavecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hugene.1.0.st.v1frmavecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hugene.1.0.st.v1frmavecs/container.yaml"
updated_at: "2024-02-15 02:57:50.033074"
latest: "1.1.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hugene.1.0.st.v1frmavecs"

versions:
 - "1.1.0--r41hdfd78af_9"
 - "1.1.0--r42hdfd78af_10"
 - "1.1.0--r43hdfd78af_11"
 - "1.1.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hugene.1.0.st.v1frmavecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hugene.1.0.st.v1frmavecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hugene.1.0.st.v1frmavecs", "latest": {"1.1.0--r43hdfd78af_12": "sha256:1edf4e1263d5d1dbe66218b8e17a53a9bc41cab1af1b9f883b5563d79563dfd7"}, "tags": {"1.1.0--r41hdfd78af_9": "sha256:7249aab0b8d3c11c078dc6b04362fd5579376597fb50d7b92460c0dce24914ca", "1.1.0--r42hdfd78af_10": "sha256:3ecf2b5351070570bfde8437a42be0984b3f139ad9dbe107d295308ee29cb955", "1.1.0--r43hdfd78af_11": "sha256:1625d34647ad8976accf6a101a5665ad2164be625e25031ca99751ae57a699e7", "1.1.0--r43hdfd78af_12": "sha256:1edf4e1263d5d1dbe66218b8e17a53a9bc41cab1af1b9f883b5563d79563dfd7"}, "docker": "quay.io/biocontainers/bioconductor-hugene.1.0.st.v1frmavecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hugene.1.0.st.v1frmavecs.
shpc-registry automated BioContainers addition for bioconductor-hugene.1.0.st.v1frmavecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hugene.1.0.st.v1frmavecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hugene.1.0.st.v1frmavecs:1.1.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hugene.1.0.st.v1frmavecs/1.1.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hugene.1.0.st.v1frmavecs/1.1.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hugene.1.0.st.v1frmavecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hugene.1.0.st.v1frmavecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hugene.1.0.st.v1frmavecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hugene.1.0.st.v1frmavecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hugene.1.0.st.v1frmavecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hugene.1.0.st.v1frmavecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hugene.1.0.st.v1frmavecs

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