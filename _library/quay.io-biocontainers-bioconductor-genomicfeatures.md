---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomicfeatures"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomicfeatures/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomicfeatures/container.yaml"
updated_at: "2025-05-03 03:25:09.148829"
latest: "1.58.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomicfeatures"

versions:
 - "1.46.1--r41hdfd78af_0"
 - "1.50.2--r42hdfd78af_0"
 - "1.52.1--r43hdfd78af_0"
 - "1.54.1--r43hdfd78af_0"
 - "1.58.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomicfeatures"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomicfeatures", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomicfeatures", "latest": {"1.58.0--r44hdfd78af_0": "sha256:6b339d4077a772ad146afe353f9c459bb3b4d75e2cfa77b760ad6310438a67c6"}, "tags": {"1.46.1--r41hdfd78af_0": "sha256:18cb4d8ca45714d0ce3f1b6ff1c570771fe85588e1e55f6aa913d7c098dbb56b", "1.50.2--r42hdfd78af_0": "sha256:1254064bd08761e07e10ff3e7eb36e8094b95e770819a489f719367b1fb1202a", "1.52.1--r43hdfd78af_0": "sha256:54ea43c8b5168d70816ba23e5dc621d8c4669125283bfce61fa03b9903f4cf7e", "1.54.1--r43hdfd78af_0": "sha256:99bc387a86a70afd73f8d80bc680986dd1a8ef9d25a08584d8014b4054fe9cfe", "1.58.0--r44hdfd78af_0": "sha256:6b339d4077a772ad146afe353f9c459bb3b4d75e2cfa77b760ad6310438a67c6"}, "docker": "quay.io/biocontainers/bioconductor-genomicfeatures"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomicfeatures.
shpc-registry automated BioContainers addition for bioconductor-genomicfeatures
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicfeatures
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicfeatures:1.58.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomicfeatures/1.58.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genomicfeatures/1.58.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomicfeatures-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicfeatures-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicfeatures-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomicfeatures-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomicfeatures-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomicfeatures-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genomicfeatures

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