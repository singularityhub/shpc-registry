---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnits"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnits/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnits/container.yaml"
updated_at: "2024-03-18 23:26:29.045848"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnits"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnits"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnits", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnits", "latest": {"1.36.0--r43hdfd78af_0": "sha256:51ee5f1acb1afe8d3a8a2bc2587db68e03325d55586034ce51da64aab4502588"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:306b3e369b56a82b1af8e7a9bb873445ebbe3f8ea14ac4bac1369268f7887770", "1.34.0--r43hdfd78af_0": "sha256:b31cd4ae612074d51256f27dee6ecb5dd69c7847544df1cd0483cb4e91c97b19", "1.36.0--r43hdfd78af_0": "sha256:51ee5f1acb1afe8d3a8a2bc2587db68e03325d55586034ce51da64aab4502588"}, "docker": "quay.io/biocontainers/bioconductor-rnits"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnits.
shpc-registry automated BioContainers addition for bioconductor-rnits
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnits
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnits:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnits/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnits/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnits-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnits-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnits-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnits-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnits-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnits-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnits

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