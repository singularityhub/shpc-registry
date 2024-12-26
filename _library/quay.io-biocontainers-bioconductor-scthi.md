---
layout: container
name:  "quay.io/biocontainers/bioconductor-scthi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scthi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scthi/container.yaml"
updated_at: "2024-12-26 03:27:34.793408"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scthi"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scthi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scthi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scthi", "latest": {"1.18.0--r44hdfd78af_0": "sha256:b2ea34b74d0f346b26b7b87b4af3ba423ddf66cee58152fd7c10057255704385"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:9d683643a76933928003214f26e96c8f15dad5ba4b937909ac2f4607524066dd", "1.10.0--r42hdfd78af_0": "sha256:8e6eccff630bd8422b7ca5a69fa8ac2adf31ea18def1c93b67224b1753ac78a4", "1.12.0--r43hdfd78af_0": "sha256:ac5769d82f653c3f0704287738cfe71db719093531c6b6904dbd5e5903fb414c", "1.14.0--r43hdfd78af_0": "sha256:c1f59b2b38b8c7a9c298e2bab4e6fc4fff1fbc77f160c229a80b7f4ee50f525c", "1.18.0--r44hdfd78af_0": "sha256:b2ea34b74d0f346b26b7b87b4af3ba423ddf66cee58152fd7c10057255704385"}, "docker": "quay.io/biocontainers/bioconductor-scthi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scthi.
shpc-registry automated BioContainers addition for bioconductor-scthi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scthi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scthi:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scthi/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scthi/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scthi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scthi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scthi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scthi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scthi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scthi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scthi

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