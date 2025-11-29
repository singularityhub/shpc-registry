---
layout: container
name:  "quay.io/biocontainers/bioconductor-epivizrstandalone"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epivizrstandalone/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epivizrstandalone/container.yaml"
updated_at: "2025-11-29 03:05:39.135677"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-epivizrstandalone"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-epivizrstandalone"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epivizrstandalone", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epivizrstandalone", "latest": {"1.34.0--r44hdfd78af_0": "sha256:3fd3c013c42c6339bff67450d44c16111c046fd819d94e6f9f83759d72b906ec"}, "tags": {"1.8.0--r351_0": "sha256:b7f27106f8cbf8afaace0df1e939b7803ca857a235dab9a55f58b54fc4362a44", "1.26.0--r42hdfd78af_0": "sha256:ca5f5e0bf6642f7bdb1db3e92a4b65ba8d57e1ca99079ad40d546139cbf03b9a", "1.22.0--r41hdfd78af_0": "sha256:284677037a5b544cf599343406216512b89223b22ce1cfed691b21782dac5416", "1.20.0--r41hdfd78af_0": "sha256:c4dde09964229797bb064ca8b6f48a3b4c5e891caf8bc68e99b72eb4a86ef369", "1.18.0--r40hdfd78af_1": "sha256:07cfcd37ff72b77fa4744d241938fad73c808b3e7446ef9428b2aa0f1954d432", "1.16.0--r40_0": "sha256:a794bce8b7ff619446d27fa3eb745ce23ea04d7a6e3b94b9acf617bcc39f9729", "1.28.0--r43hdfd78af_0": "sha256:557ff0ad8e64528ed4284fbf4cee8aeb34f859aa49ddcad356e8113e553d61f7", "1.30.0--r43hdfd78af_0": "sha256:e9b17f48d45fd2cbbb59b863ad82fbaa11e95edd9c6c69ba70f0cffe3807fcf8", "1.34.0--r44hdfd78af_0": "sha256:3fd3c013c42c6339bff67450d44c16111c046fd819d94e6f9f83759d72b906ec"}, "docker": "quay.io/biocontainers/bioconductor-epivizrstandalone", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epivizrstandalone.
shpc-registry automated BioContainers addition for bioconductor-epivizrstandalone
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizrstandalone
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizrstandalone:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epivizrstandalone/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-epivizrstandalone/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epivizrstandalone-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizrstandalone-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizrstandalone-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epivizrstandalone-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epivizrstandalone-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epivizrstandalone-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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