---
layout: container
name:  "quay.io/biocontainers/bioconductor-canine2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-canine2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-canine2cdf/container.yaml"
updated_at: "2024-09-16 03:39:43.967495"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-canine2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-canine2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-canine2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-canine2cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:fae7e468e949bc3e22f23e572ede5c18560c064772523e8ba62c73bd21256ab6"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:f7fbc8b89b7245aa6cf9cefd84dd7fb5137a332b0af4c299d337518fec246c49", "2.18.0--r42hdfd78af_10": "sha256:f633cf311371ce69ceee5d2658939ec0544e2675b310fd9cf7bd07b948d7c5de", "2.18.0--r43hdfd78af_11": "sha256:5076413f91ce3bcbf8a38fb8b9c6331838571c8c583ead51943651a6f3543557", "2.18.0--r43hdfd78af_12": "sha256:fae7e468e949bc3e22f23e572ede5c18560c064772523e8ba62c73bd21256ab6"}, "docker": "quay.io/biocontainers/bioconductor-canine2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-canine2cdf.
shpc-registry automated BioContainers addition for bioconductor-canine2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-canine2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-canine2cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-canine2cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-canine2cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-canine2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-canine2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-canine2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-canine2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-canine2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-canine2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-canine2cdf

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