---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnaseqpower"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnaseqpower/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnaseqpower/container.yaml"
updated_at: "2024-11-12 03:42:45.226933"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnaseqpower"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnaseqpower"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnaseqpower", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnaseqpower", "latest": {"1.42.0--r43hdfd78af_0": "sha256:8bb482d145f109744487da3370da33e7cf0654152e76b73057cee6177832bffa"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:53d31eeb1ead8f6e3bdfb6e70d0918e570c76f04283a6b4681546eea72e0754e", "1.38.0--r42hdfd78af_0": "sha256:627af1c66e0630d2a9792304de8997c9abfa09d46ba09e89463dc097669cc10a", "1.40.0--r43hdfd78af_0": "sha256:59cceb261ea81dd103cc18e08bf091d772b4ce47c044d6419724d60bac640b67", "1.42.0--r43hdfd78af_0": "sha256:8bb482d145f109744487da3370da33e7cf0654152e76b73057cee6177832bffa"}, "docker": "quay.io/biocontainers/bioconductor-rnaseqpower"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnaseqpower.
shpc-registry automated BioContainers addition for bioconductor-rnaseqpower
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqpower
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqpower:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnaseqpower/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnaseqpower/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnaseqpower-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqpower-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqpower-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnaseqpower-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnaseqpower-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnaseqpower-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnaseqpower

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