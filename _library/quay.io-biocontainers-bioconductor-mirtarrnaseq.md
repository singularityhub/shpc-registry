---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirtarrnaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirtarrnaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirtarrnaseq/container.yaml"
updated_at: "2025-07-26 03:53:42.357202"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirtarrnaseq"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirtarrnaseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirtarrnaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirtarrnaseq", "latest": {"1.14.0--r44hdfd78af_0": "sha256:ac7a2d8de6c4bf2c44969dce478aae31afd16178a80a25c785a1df3ba356936e"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:f151033b7a5c465d3cebe78fa38dde21f77f0f7a2d54e222849ff3bd70db0408", "1.6.0--r42hdfd78af_0": "sha256:da6e8fa1977e9b6a3173b678367a2d08a81565ba3363d60860d6578f8856cebf", "1.8.0--r43hdfd78af_0": "sha256:8bccf7c8c7b71d418bb78af473d39496f85017c508e0e7190f20d5009cb347bf", "1.10.0--r43hdfd78af_0": "sha256:3fd8e99987485ec299988debadc574119b8262709a1eac0e5a6dd7194c0d21f4", "1.14.0--r44hdfd78af_0": "sha256:ac7a2d8de6c4bf2c44969dce478aae31afd16178a80a25c785a1df3ba356936e"}, "docker": "quay.io/biocontainers/bioconductor-mirtarrnaseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirtarrnaseq.
shpc-registry automated BioContainers addition for bioconductor-mirtarrnaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirtarrnaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirtarrnaseq:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirtarrnaseq/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mirtarrnaseq/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirtarrnaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirtarrnaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirtarrnaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirtarrnaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirtarrnaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirtarrnaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirtarrnaseq

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