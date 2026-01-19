---
layout: container
name:  "quay.io/biocontainers/bioconductor-dewseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dewseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dewseq/container.yaml"
updated_at: "2026-01-19 03:59:58.364559"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dewseq"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.2--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dewseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dewseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dewseq", "latest": {"1.20.0--r44hdfd78af_0": "sha256:85fc657e1c43d7597cfd39c9cc135447d21b1c395c5b2711ad4739c82305a4d2"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:15ef3930143ffc5fb5d73a2d78dd47c96577ea7ae0e0edb5957050e7d442da38", "1.12.0--r42hdfd78af_0": "sha256:f012250e71887ac5f1b05bf70eef7477f16b974948f89c2bd96269097af219aa", "1.14.0--r43hdfd78af_0": "sha256:5f753f5445d048dce338d59ad4e403370d3c7798cf551f64e7c3982497f38565", "1.16.2--r43hdfd78af_0": "sha256:cf7dd9f649a203715bc0c2261cc634a6f743439070c0ce7fc111f520a6f6e5da", "1.20.0--r44hdfd78af_0": "sha256:85fc657e1c43d7597cfd39c9cc135447d21b1c395c5b2711ad4739c82305a4d2"}, "docker": "quay.io/biocontainers/bioconductor-dewseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dewseq.
shpc-registry automated BioContainers addition for bioconductor-dewseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dewseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dewseq:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dewseq/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dewseq/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dewseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dewseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dewseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dewseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dewseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dewseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dewseq

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