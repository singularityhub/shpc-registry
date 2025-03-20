---
layout: container
name:  "quay.io/biocontainers/bioconductor-biodbmirbase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biodbmirbase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biodbmirbase/container.yaml"
updated_at: "2025-03-20 04:00:36.858844"
latest: "1.5.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biodbmirbase"

versions:
 - "1.2.0--r42hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.5.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-biodbmirbase"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biodbmirbase", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-biodbmirbase", "latest": {"1.5.0--r43hdfd78af_0": "sha256:1c483720ed07c5085ee5a1f1a1b1c17877e9c0cfbfeecb9ee27d22ba515111b9"}, "tags": {"1.2.0--r42hdfd78af_0": "sha256:20c41cabec89d218bdde6c100f6621a7b8482e6f25c49b874a8e7b74983a7121", "1.4.0--r43hdfd78af_0": "sha256:8110749069f2f82f5e146f28ddf81e1254825fd65c0b367ff2b9e4fdc02e69fe", "1.5.0--r43hdfd78af_0": "sha256:1c483720ed07c5085ee5a1f1a1b1c17877e9c0cfbfeecb9ee27d22ba515111b9"}, "docker": "quay.io/biocontainers/bioconductor-biodbmirbase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biodbmirbase.
singularity registry hpc automated addition for bioconductor-biodbmirbase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbmirbase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbmirbase:1.5.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biodbmirbase/1.5.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biodbmirbase/1.5.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biodbmirbase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbmirbase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbmirbase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biodbmirbase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biodbmirbase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biodbmirbase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biodbmirbase

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