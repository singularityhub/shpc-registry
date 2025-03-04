---
layout: container
name:  "quay.io/biocontainers/bioconductor-dmelsgi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dmelsgi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dmelsgi/container.yaml"
updated_at: "2025-03-04 03:16:25.003918"
latest: "1.37.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dmelsgi"
aliases:
 - "glpsol"
versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.29.1--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.37.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dmelsgi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dmelsgi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dmelsgi", "latest": {"1.37.0--r44hdfd78af_0": "sha256:13c9dc59fa78e71e3c032a61504a7fd5472fb98b1a0b0ecf839e151ecea909b1"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:09100acbc06a941981dbdfc404455e793398feb27a0c4b025fd72aae7049f044", "1.29.1--r42hdfd78af_0": "sha256:9df82b739d7a47582f2898c5f4a12e276b89d7b9c556761b9412f034b0fe6f40", "1.32.0--r43hdfd78af_0": "sha256:0ded75289837dc4f24b3e5a1544601e4fde4b7a965b914ae114d60333c96be6d", "1.34.0--r43hdfd78af_0": "sha256:7c877d0ccf508c0e219aaa20a9a7ca3cf33fb69f73455351dde5a49ef0ce8b1e", "1.37.0--r44hdfd78af_0": "sha256:13c9dc59fa78e71e3c032a61504a7fd5472fb98b1a0b0ecf839e151ecea909b1"}, "docker": "quay.io/biocontainers/bioconductor-dmelsgi", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dmelsgi.
shpc-registry automated BioContainers addition for bioconductor-dmelsgi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dmelsgi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dmelsgi:1.37.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dmelsgi/1.37.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dmelsgi/1.37.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dmelsgi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmelsgi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmelsgi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dmelsgi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dmelsgi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dmelsgi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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