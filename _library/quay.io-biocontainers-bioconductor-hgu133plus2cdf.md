---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133plus2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133plus2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133plus2cdf/container.yaml"
updated_at: "2023-12-05 02:36:36.514062"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133plus2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r41hdfd78af_10"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133plus2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133plus2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133plus2cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:0a988ae7e62ea9a876c3a412d9356dd1e084dd2151dbd43bb6cb39655e391246"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:0831cb3fe1cb7ddf6eaf9b9c78d77e5ac17c4de10e8d458128a2a1b3d1714c79", "2.18.0--r41hdfd78af_10": "sha256:73684029399fbcfd4cd9f571745b1070135b1abc30c4f0246b12e9275ec75d31", "2.18.0--r42hdfd78af_11": "sha256:42af4404bd72f9a88152b152e3ae67cec0793da9b2b3e9fa096ad67252d0a4d6", "2.18.0--r43hdfd78af_12": "sha256:0a988ae7e62ea9a876c3a412d9356dd1e084dd2151dbd43bb6cb39655e391246"}, "docker": "quay.io/biocontainers/bioconductor-hgu133plus2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133plus2cdf.
shpc-registry automated BioContainers addition for bioconductor-hgu133plus2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133plus2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133plus2cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133plus2cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgu133plus2cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133plus2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133plus2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133plus2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133plus2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133plus2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133plus2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133plus2cdf

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