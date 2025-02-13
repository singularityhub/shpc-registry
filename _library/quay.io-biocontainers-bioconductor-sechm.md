---
layout: container
name:  "quay.io/biocontainers/bioconductor-sechm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sechm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sechm/container.yaml"
updated_at: "2025-02-13 03:18:18.222305"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sechm"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sechm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sechm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sechm", "latest": {"1.14.0--r44hdfd78af_0": "sha256:934c57bff231373c6b3e54ea3a3b9fa4793c66868a5d3242a87f7a0394c8c566"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:119f6cfdc33f3d9326e4bfc7f72b19e07b329b218bcce80b844fd5cf93d961cb", "1.6.0--r42hdfd78af_0": "sha256:7b61350711283c5ddb5a8674e6ed92804b2c4b54e28a09539657886b3a004b96", "1.8.0--r43hdfd78af_0": "sha256:41e50f862cd361faf684d2fda1abe8ad6dc3476ab5317d595e3841ef5614d53f", "1.10.0--r43hdfd78af_0": "sha256:f4655007ffb2823c7ffa46f8c19d8d4934559bd1ffdb24083048214920512527", "1.14.0--r44hdfd78af_0": "sha256:934c57bff231373c6b3e54ea3a3b9fa4793c66868a5d3242a87f7a0394c8c566"}, "docker": "quay.io/biocontainers/bioconductor-sechm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sechm.
shpc-registry automated BioContainers addition for bioconductor-sechm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sechm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sechm:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sechm/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sechm/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sechm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sechm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sechm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sechm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sechm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sechm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sechm

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