---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgc/container.yaml"
updated_at: "2024-05-15 02:36:46.936958"
latest: "1.10.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hgc"

versions:
 - "1.2.0--r41hc247a5b_2"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_2"
 - "1.8.0--r43hf17093f_0"
 - "1.10.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hgc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgc", "latest": {"1.10.0--r43hf17093f_0": "sha256:14f832414d4972934a4cb0a26942455cada8405d7c3b990b47e04b3cf756c103"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:d90b193d5b533823481114e16ceffa1c43919e4cd0e7de55f1c5834002645cf9", "1.6.0--r42hc247a5b_0": "sha256:fe87b86a277cd17b546cfd657277f5a14d155cdbf8fbada4e7d14c496291ee1e", "1.6.0--r42hf17093f_2": "sha256:faf372d8c1570e424a5a1bfa45e0fab90819b1b06c37912994edc185c53210f1", "1.8.0--r43hf17093f_0": "sha256:4c9587a2b89b3b4ddf2eae92cf0de01bfbb15f0d28bae0aa58f972ff1c5eded1", "1.10.0--r43hf17093f_0": "sha256:14f832414d4972934a4cb0a26942455cada8405d7c3b990b47e04b3cf756c103"}, "docker": "quay.io/biocontainers/bioconductor-hgc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgc.
shpc-registry automated BioContainers addition for bioconductor-hgc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgc:1.10.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgc/1.10.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-hgc/1.10.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgc

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