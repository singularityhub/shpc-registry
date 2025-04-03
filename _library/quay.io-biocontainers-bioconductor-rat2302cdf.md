---
layout: container
name:  "quay.io/biocontainers/bioconductor-rat2302cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rat2302cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rat2302cdf/container.yaml"
updated_at: "2025-04-03 03:28:26.273903"
latest: "2.18.0--r44hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-rat2302cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
 - "2.18.0--r44hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-rat2302cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rat2302cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rat2302cdf", "latest": {"2.18.0--r44hdfd78af_14": "sha256:d9c84e8ddb22bb4b110a4a71be7873c9c7f55ec57a0b817f8ef2bc6aa9d90bad"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:f1d98fba5d2c067c08a4ed55fbb9c09ae810546ed429d7db4a7ba74034ccca8f", "2.18.0--r42hdfd78af_11": "sha256:5d759317ef7a48434353ced73ace92391d4c3b640104db4357aa65d9dd57e585", "2.18.0--r43hdfd78af_12": "sha256:7a3f671ad78c3872284edcde8704f9c8be6b6e0c580500cee041f33528a8121e", "2.18.0--r43hdfd78af_13": "sha256:8ffbd5821e1065b83a346eab18793940e9785acdc28f498df8c9a54d8d14290f", "2.18.0--r44hdfd78af_14": "sha256:d9c84e8ddb22bb4b110a4a71be7873c9c7f55ec57a0b817f8ef2bc6aa9d90bad"}, "docker": "quay.io/biocontainers/bioconductor-rat2302cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rat2302cdf.
shpc-registry automated BioContainers addition for bioconductor-rat2302cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rat2302cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rat2302cdf:2.18.0--r44hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rat2302cdf/2.18.0--r44hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-rat2302cdf/2.18.0--r44hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rat2302cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rat2302cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rat2302cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rat2302cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rat2302cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rat2302cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rat2302cdf

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