---
layout: container
name:  "quay.io/biocontainers/bioconductor-deconrnaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-deconrnaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-deconrnaseq/container.yaml"
updated_at: "2023-03-10 03:16:53.274113"
latest: "1.40.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-deconrnaseq"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-deconrnaseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-deconrnaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-deconrnaseq", "latest": {"1.40.0--r42hdfd78af_0": "sha256:5184c2b66bd23baf47ecbe4cc75c26db1bb487952c30819d2a7e7f5a95af446f"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:8a8710c8fed9d641d28827ec8a6df61fc25c3a5f3f188c7dd18c799f5f013cf7", "1.40.0--r42hdfd78af_0": "sha256:5184c2b66bd23baf47ecbe4cc75c26db1bb487952c30819d2a7e7f5a95af446f"}, "docker": "quay.io/biocontainers/bioconductor-deconrnaseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-deconrnaseq.
shpc-registry automated BioContainers addition for bioconductor-deconrnaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-deconrnaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-deconrnaseq:1.40.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-deconrnaseq/1.40.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-deconrnaseq/1.40.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-deconrnaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deconrnaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deconrnaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-deconrnaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-deconrnaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-deconrnaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-deconrnaseq

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