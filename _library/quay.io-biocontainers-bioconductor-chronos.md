---
layout: container
name:  "quay.io/biocontainers/bioconductor-chronos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chronos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chronos/container.yaml"
updated_at: "2024-06-22 02:36:11.867983"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chronos"

versions:
 - "1.8.1--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chronos"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chronos", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chronos", "latest": {"1.30.0--r43hdfd78af_0": "sha256:6ef75c6a106d7ad6d9842eefa4dcc8afbefd682cdac396d0ddc424eec1acd7d9"}, "tags": {"1.8.1--r351_0": "sha256:68f55464e2b2be67c77c757e92578a1a778cb82b1f7a694ed0ea9be3ac7cc528", "1.26.0--r42hdfd78af_0": "sha256:23e573425b594e0cc289be2aa60021d99cdfdd29b58699ba32d25a6be3fc8c10", "1.22.0--r41hdfd78af_0": "sha256:19cee4438457b72368ada9d6652811c36363542314eca465ecfa7ddffe65be9b", "1.20.0--r41hdfd78af_0": "sha256:cd3e58cc79deeb43769edf61f8f921bf30cdaa0bca4c708630d7747d2ba00237", "1.18.0--r40hdfd78af_1": "sha256:d4f4d9e7b9777cbf99415b2c4fcd7ebfe012bfe1a9a2d447fe69b35d45b3b016", "1.16.0--r40_0": "sha256:c3c480ab1aa23599e8ebc1415bb2004028da452b4f2db58b94c89b17f9d60049", "1.28.0--r43hdfd78af_0": "sha256:ee174e6aa688a42b0a8efe6253d26b5c31759509f4d87f9a43e8fdc045e59f77", "1.30.0--r43hdfd78af_0": "sha256:6ef75c6a106d7ad6d9842eefa4dcc8afbefd682cdac396d0ddc424eec1acd7d9"}, "docker": "quay.io/biocontainers/bioconductor-chronos"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chronos.
shpc-registry automated BioContainers addition for bioconductor-chronos
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chronos
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chronos:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chronos/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chronos/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chronos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chronos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chronos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chronos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chronos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chronos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chronos

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