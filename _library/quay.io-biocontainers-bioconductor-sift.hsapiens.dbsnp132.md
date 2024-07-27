---
layout: container
name:  "quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp132"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp132/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp132/container.yaml"
updated_at: "2024-07-27 03:14:54.833918"
latest: "1.0.2--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-sift.hsapiens.dbsnp132"

versions:
 - "1.0.2--r41hdfd78af_9"
 - "1.0.2--r42hdfd78af_10"
 - "1.0.2--r43hdfd78af_11"
 - "1.0.2--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-sift.hsapiens.dbsnp132"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sift.hsapiens.dbsnp132", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sift.hsapiens.dbsnp132", "latest": {"1.0.2--r43hdfd78af_12": "sha256:1dad58980c4b948a9540277d69dd1e6fe24a73c30a5058f06def12807ea6c7a6"}, "tags": {"1.0.2--r41hdfd78af_9": "sha256:4f0c67351636180da5316b7f9d80af0f6722add9db890eb1af1e7d385457b876", "1.0.2--r42hdfd78af_10": "sha256:b332e26fa1d95c3a79bd839cc24bc339e98e12e7cb82b41e5bfbbd4badd37a91", "1.0.2--r43hdfd78af_11": "sha256:f72d76de807542a682375a0b689e8288bb5a60b747a71ce8f0e0c4fbc12338db", "1.0.2--r43hdfd78af_12": "sha256:1dad58980c4b948a9540277d69dd1e6fe24a73c30a5058f06def12807ea6c7a6"}, "docker": "quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp132"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp132.
shpc-registry automated BioContainers addition for bioconductor-sift.hsapiens.dbsnp132
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp132
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp132:1.0.2--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp132/1.0.2--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-sift.hsapiens.dbsnp132/1.0.2--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sift.hsapiens.dbsnp132-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sift.hsapiens.dbsnp132-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sift.hsapiens.dbsnp132-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sift.hsapiens.dbsnp132-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sift.hsapiens.dbsnp132-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sift.hsapiens.dbsnp132-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sift.hsapiens.dbsnp132

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