---
layout: container
name:  "quay.io/biocontainers/bioconductor-maizecdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maizecdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maizecdf/container.yaml"
updated_at: "2024-05-27 03:50:53.307281"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-maizecdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-maizecdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maizecdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maizecdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:7b409107cce613b22b271d2eaef06eaaaec0a72fc4a8c2e9c882491129d9ccce"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:6b590ad050bf4004a94a4807067dd96428e1dd82608c414d6a12b456cee1632d", "2.18.0--r42hdfd78af_10": "sha256:b42c96e6a7f2b7de3f269c42976abf421845b792ebb82a7993c72d935ccf8681", "2.18.0--r43hdfd78af_11": "sha256:e25da3b82310550b40c80f59033fc932b5b10c9fbc5d7614c0398a22207ceb25", "2.18.0--r43hdfd78af_12": "sha256:7b409107cce613b22b271d2eaef06eaaaec0a72fc4a8c2e9c882491129d9ccce"}, "docker": "quay.io/biocontainers/bioconductor-maizecdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maizecdf.
shpc-registry automated BioContainers addition for bioconductor-maizecdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maizecdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maizecdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maizecdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-maizecdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maizecdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maizecdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maizecdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maizecdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maizecdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maizecdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-maizecdf

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