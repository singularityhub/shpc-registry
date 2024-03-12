---
layout: container
name:  "quay.io/biocontainers/bioconductor-kboost"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-kboost/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-kboost/container.yaml"
updated_at: "2024-03-12 02:40:18.840218"
latest: "1.10.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-kboost"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-kboost"
config: {"url": "https://biocontainers.pro/tools/bioconductor-kboost", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-kboost", "latest": {"1.10.0--r43hdfd78af_1": "sha256:787fe532958a32290abfb370f1fb76f6dbbaf64d494db6f0ca162b55ac6c0d6a"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:02b99844bf80d95006c91bacbd7b2781e915d75a07f1822e7003c89f99cfbd80", "1.6.0--r42hdfd78af_0": "sha256:af827851f30b34fea0a6391b4ca677d7ff99d8c2f79ec19808388525883e82d0", "1.8.0--r43hdfd78af_0": "sha256:e561054531b9af2f648f3880ae97526aaffda266b562469fff0ff42d6be2ea1f", "1.10.0--r43hdfd78af_1": "sha256:787fe532958a32290abfb370f1fb76f6dbbaf64d494db6f0ca162b55ac6c0d6a"}, "docker": "quay.io/biocontainers/bioconductor-kboost"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-kboost.
shpc-registry automated BioContainers addition for bioconductor-kboost
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-kboost
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-kboost:1.10.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-kboost/1.10.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-kboost/1.10.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-kboost-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kboost-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kboost-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-kboost-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-kboost-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-kboost-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-kboost

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