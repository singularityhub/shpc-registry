---
layout: container
name:  "quay.io/biocontainers/bioconductor-cepo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cepo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cepo/container.yaml"
updated_at: "2025-01-03 03:21:32.915487"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cepo"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cepo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cepo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cepo", "latest": {"1.6.0--r43hdfd78af_0": "sha256:891d28a6cdf6fd66e3b55a558810b2a6c0060c20c1a231b229eb0ef99f9cb047"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:7dd78404848a525171bf6096cba013414497708793b021ea7ffd15c8c3644ca4", "1.4.0--r42hdfd78af_0": "sha256:b654effdb1ac0793c0bbe5b0bf20e527f3c67a2a20adb8d38637e21479111532", "1.6.0--r43hdfd78af_0": "sha256:891d28a6cdf6fd66e3b55a558810b2a6c0060c20c1a231b229eb0ef99f9cb047"}, "docker": "quay.io/biocontainers/bioconductor-cepo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cepo.
shpc-registry automated BioContainers addition for bioconductor-cepo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cepo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cepo:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cepo/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cepo/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cepo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cepo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cepo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cepo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cepo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cepo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cepo

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