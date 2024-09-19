---
layout: container
name:  "quay.io/biocontainers/bioconductor-bugsigdbr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bugsigdbr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bugsigdbr/container.yaml"
updated_at: "2024-09-19 02:54:54.042126"
latest: "1.8.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bugsigdbr"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.2--r43hdfd78af_0"
 - "1.8.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bugsigdbr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bugsigdbr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bugsigdbr", "latest": {"1.8.1--r43hdfd78af_0": "sha256:80af0663a800a4aac9e73218bedaf5acc050bfa4c61e6a75aa5e01bccad5a115"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:0632fdc6278b6c74f057bc1ffb8075717e96ebfc4ebc8ba35fc8b128eebb4ecd", "1.4.0--r42hdfd78af_0": "sha256:68e400d0d10349eddc56afd95a28a3cba4aa09cadd6ede29b24d9a28fb2d3c71", "1.6.2--r43hdfd78af_0": "sha256:7c8310de9f4c0d5308e1cb590290f26931fde351f373e1c60ab3f88ac2e9207a", "1.8.1--r43hdfd78af_0": "sha256:80af0663a800a4aac9e73218bedaf5acc050bfa4c61e6a75aa5e01bccad5a115"}, "docker": "quay.io/biocontainers/bioconductor-bugsigdbr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bugsigdbr.
shpc-registry automated BioContainers addition for bioconductor-bugsigdbr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bugsigdbr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bugsigdbr:1.8.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bugsigdbr/1.8.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bugsigdbr/1.8.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bugsigdbr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bugsigdbr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bugsigdbr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bugsigdbr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bugsigdbr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bugsigdbr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bugsigdbr

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