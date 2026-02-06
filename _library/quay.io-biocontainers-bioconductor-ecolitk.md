---
layout: container
name:  "quay.io/biocontainers/bioconductor-ecolitk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ecolitk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ecolitk/container.yaml"
updated_at: "2026-02-06 04:30:15.038874"
latest: "1.78.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ecolitk"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.78.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ecolitk"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ecolitk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ecolitk", "latest": {"1.78.0--r44hdfd78af_0": "sha256:cdad29ea973a4bb42df32b18b951f60c2efb7da813d6816079c0b5287261c17c"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:09070fd67b133009372797f5246fcfa11c2e00b0baff508e42b0f1dc6e71de0b", "1.70.0--r42hdfd78af_0": "sha256:7cc33f65feda44634013070417e5049b6ae7e3c55369ac09ea274316ae986acd", "1.72.0--r43hdfd78af_0": "sha256:3069bdd34a01aaaaa37b2926a4f1c71e028cf9938478043ed6ade3942e149b19", "1.74.0--r43hdfd78af_0": "sha256:34b92e4af1bcaa3938f01f686f0d07166245dae1665a6916864c619139ed7808", "1.78.0--r44hdfd78af_0": "sha256:cdad29ea973a4bb42df32b18b951f60c2efb7da813d6816079c0b5287261c17c"}, "docker": "quay.io/biocontainers/bioconductor-ecolitk"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ecolitk.
shpc-registry automated BioContainers addition for bioconductor-ecolitk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ecolitk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ecolitk:1.78.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ecolitk/1.78.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ecolitk/1.78.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ecolitk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecolitk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecolitk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ecolitk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ecolitk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ecolitk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ecolitk

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