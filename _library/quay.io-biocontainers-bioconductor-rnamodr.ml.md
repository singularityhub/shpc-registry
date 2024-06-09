---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnamodr.ml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnamodr.ml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnamodr.ml/container.yaml"
updated_at: "2024-06-09 02:36:47.493285"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnamodr.ml"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnamodr.ml"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnamodr.ml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnamodr.ml", "latest": {"1.16.0--r43hdfd78af_0": "sha256:c870967194a9c953ff065a53781110330f8e8facd9cda8ca3fd313af9003e511"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:78db489427ef7312a4f0aa84181ce884b4d19caff814d2e912999c9e6472b20a", "1.12.0--r42hdfd78af_0": "sha256:192bed31b91b1babd156fa376b76f72601a533d95b5793c7dc9d05d84b3f8403", "1.14.0--r43hdfd78af_0": "sha256:b81af9f5b4460659a105bdede998ddb532e7726bf339e07a04fc73b134d88015", "1.16.0--r43hdfd78af_0": "sha256:c870967194a9c953ff065a53781110330f8e8facd9cda8ca3fd313af9003e511"}, "docker": "quay.io/biocontainers/bioconductor-rnamodr.ml"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnamodr.ml.
shpc-registry automated BioContainers addition for bioconductor-rnamodr.ml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnamodr.ml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnamodr.ml:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnamodr.ml/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnamodr.ml/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnamodr.ml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnamodr.ml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnamodr.ml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnamodr.ml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnamodr.ml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnamodr.ml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnamodr.ml

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