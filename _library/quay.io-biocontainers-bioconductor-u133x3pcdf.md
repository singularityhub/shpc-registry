---
layout: container
name:  "quay.io/biocontainers/bioconductor-u133x3pcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-u133x3pcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-u133x3pcdf/container.yaml"
updated_at: "2025-06-26 03:41:53.259540"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-u133x3pcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-u133x3pcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-u133x3pcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-u133x3pcdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:f0d5bbc8ca60d2c3ccc890cf02f6a18ea43b4e6d46b7270c0fba754092bf9807"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:34890681a29879b6115b6152f3c659fb59c5ec7ea8bfd119d2f1a2b7e92b3b71", "2.18.0--r42hdfd78af_10": "sha256:5cc1639db2c3a61fa53188d1e1a92e1b0a20c602ce5e3b763c0ab877e221b617", "2.18.0--r43hdfd78af_11": "sha256:eef9bfee77d7d17da3ca20ff3bf2c2337e6a79e2a3c6128bd21ace74f5984a2b", "2.18.0--r43hdfd78af_12": "sha256:a5ad36e392ed555aba4ef8ad8321e32a5b5cac2870195fd8c4974406caa04898", "2.18.0--r44hdfd78af_13": "sha256:f0d5bbc8ca60d2c3ccc890cf02f6a18ea43b4e6d46b7270c0fba754092bf9807"}, "docker": "quay.io/biocontainers/bioconductor-u133x3pcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-u133x3pcdf.
shpc-registry automated BioContainers addition for bioconductor-u133x3pcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-u133x3pcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-u133x3pcdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-u133x3pcdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-u133x3pcdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-u133x3pcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-u133x3pcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-u133x3pcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-u133x3pcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-u133x3pcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-u133x3pcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-u133x3pcdf

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