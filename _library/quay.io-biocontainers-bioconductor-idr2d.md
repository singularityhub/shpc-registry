---
layout: container
name:  "quay.io/biocontainers/bioconductor-idr2d"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-idr2d/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-idr2d/container.yaml"
updated_at: "2025-09-22 03:56:31.273682"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-idr2d"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-idr2d"
config: {"url": "https://biocontainers.pro/tools/bioconductor-idr2d", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-idr2d", "latest": {"1.20.0--r44hdfd78af_0": "sha256:81ba04fc1a8bbf02b92d5db87f095e12ac9b7f46fc7046004ca358c027f958f1"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:0e5f9b289390e18e5276394d84bf30343e8ca4eaa93bcb3882acd09a5605cc66", "1.12.0--r42hdfd78af_0": "sha256:ed22bc1d31162e10db44fb23bf01331c575cab610352375ac3654946d09ba99d", "1.14.0--r43hdfd78af_0": "sha256:0aea1e0ebf34a4fb9d841b80c4b9b7464ed65ddaa3dfe6aea8f5cb16a42540ba", "1.16.0--r43hdfd78af_0": "sha256:ca3e1d8b596d8baf4304e040667ba48b260ea998680b4340ed9b4bce41ddcb90", "1.20.0--r44hdfd78af_0": "sha256:81ba04fc1a8bbf02b92d5db87f095e12ac9b7f46fc7046004ca358c027f958f1"}, "docker": "quay.io/biocontainers/bioconductor-idr2d"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-idr2d.
shpc-registry automated BioContainers addition for bioconductor-idr2d
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-idr2d
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-idr2d:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-idr2d/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-idr2d/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-idr2d-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-idr2d-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-idr2d-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-idr2d-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-idr2d-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-idr2d-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-idr2d

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