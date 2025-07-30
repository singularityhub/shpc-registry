---
layout: container
name:  "quay.io/biocontainers/bioconductor-maqcsubset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maqcsubset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maqcsubset/container.yaml"
updated_at: "2025-07-30 04:17:36.959606"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-maqcsubset"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-maqcsubset"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maqcsubset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maqcsubset", "latest": {"1.44.0--r44hdfd78af_0": "sha256:a8f01a51b6c606e1d3596d72143c74c9f2be6e6c60e31da5f4ed5711093abf0d"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:d1528716f1a628440a6a8f96b224f145d0c42dafdeaa46f1580ebcb95013cda9", "1.36.0--r42hdfd78af_0": "sha256:19b8936734d2bbbc8ab8fdd027f99b2b04949075c2f4414600fad5b8e7e5edbf", "1.38.0--r43hdfd78af_0": "sha256:ce8be4bd88041b826389c351ff4d8e23dcec8c555fbe6678f431388c82492d96", "1.40.0--r43hdfd78af_0": "sha256:b3a80f00d0df73857207270e4b62fb5a3a400b2c904ffe5bcd2c888f567a82d5", "1.44.0--r44hdfd78af_0": "sha256:a8f01a51b6c606e1d3596d72143c74c9f2be6e6c60e31da5f4ed5711093abf0d"}, "docker": "quay.io/biocontainers/bioconductor-maqcsubset"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maqcsubset.
shpc-registry automated BioContainers addition for bioconductor-maqcsubset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maqcsubset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maqcsubset:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maqcsubset/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-maqcsubset/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maqcsubset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maqcsubset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maqcsubset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maqcsubset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maqcsubset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maqcsubset-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-maqcsubset

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