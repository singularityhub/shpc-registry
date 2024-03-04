---
layout: container
name:  "quay.io/biocontainers/bioconductor-scaledmatrix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scaledmatrix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scaledmatrix/container.yaml"
updated_at: "2024-03-04 04:48:14.483817"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scaledmatrix"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.1--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scaledmatrix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scaledmatrix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scaledmatrix", "latest": {"1.10.0--r43hdfd78af_0": "sha256:eb22fefc662125ab8e194e0f5d8b54453585bc75ea352b3ac8994cc9a8f71991"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:29b0c7f54a0e6801d4174310c076d17f68a54bbf74811b0e6de77bccd4424192", "1.6.0--r42hdfd78af_0": "sha256:b6cd2b6a53706ac710b8449501c95bcbc293193e5e9dc93fd8227101a508246a", "1.8.1--r43hdfd78af_0": "sha256:68a519abb968b64e5454c625d36d2d11df12c7fdbeeaf1f897ce64a603cc7ade", "1.10.0--r43hdfd78af_0": "sha256:eb22fefc662125ab8e194e0f5d8b54453585bc75ea352b3ac8994cc9a8f71991"}, "docker": "quay.io/biocontainers/bioconductor-scaledmatrix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scaledmatrix.
shpc-registry automated BioContainers addition for bioconductor-scaledmatrix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scaledmatrix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scaledmatrix:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scaledmatrix/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scaledmatrix/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scaledmatrix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scaledmatrix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scaledmatrix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scaledmatrix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scaledmatrix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scaledmatrix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scaledmatrix

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