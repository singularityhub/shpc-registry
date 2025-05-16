---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74cv2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74cv2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74cv2cdf/container.yaml"
updated_at: "2025-05-16 03:46:33.306919"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74cv2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74cv2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74cv2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74cv2cdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:b13e3c5529f7b6c254d0cba0caded92aae5a286588dc3e4f468347dc3ed1faf3"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:d045459adeea0647b4c62c1ca75859f31acfc96cda5ecbde2924c5bee60c495f", "2.18.0--r42hdfd78af_10": "sha256:095541c767912ac4ffff4284cec7f76c76a584ea420e0d14e3c3dc130a794951", "2.18.0--r43hdfd78af_11": "sha256:c65461ece530437c00359e6302ffd31e5024915c3368c5ca648e76bf3c4bd22a", "2.18.0--r43hdfd78af_12": "sha256:6d834a7ebdaefeb4bcb1127119ce40f0d051c8c85c07924382badbd006562220", "2.18.0--r44hdfd78af_13": "sha256:b13e3c5529f7b6c254d0cba0caded92aae5a286588dc3e4f468347dc3ed1faf3"}, "docker": "quay.io/biocontainers/bioconductor-mgu74cv2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74cv2cdf.
shpc-registry automated BioContainers addition for bioconductor-mgu74cv2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74cv2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74cv2cdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74cv2cdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mgu74cv2cdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74cv2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74cv2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74cv2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74cv2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74cv2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74cv2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgu74cv2cdf

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