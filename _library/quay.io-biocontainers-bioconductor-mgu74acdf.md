---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74acdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74acdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74acdf/container.yaml"
updated_at: "2025-02-19 03:07:33.599880"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74acdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74acdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74acdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74acdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:bf71d35a1b7eb22e960ebd5a22562d1e252b2e9909272132273d3d8fa512d047"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:2139ae26f8dfe18760f262aee81da31f0dc6632cb7e24aae33bec84c4e0170cd", "2.18.0--r42hdfd78af_10": "sha256:a7327c9b4268a82626765e37b61c9030a81b4b3085d7c088626a54fcce1f0639", "2.18.0--r43hdfd78af_11": "sha256:7f0a3bfae5f983cc6876fd046063da0d774476213cf63e4e882a92cb12a6c78b", "2.18.0--r43hdfd78af_12": "sha256:2b82eb8db3001fe6f5041f945f2859b564caeb98174152046cf7e9fe2aadd3bd", "2.18.0--r44hdfd78af_13": "sha256:bf71d35a1b7eb22e960ebd5a22562d1e252b2e9909272132273d3d8fa512d047"}, "docker": "quay.io/biocontainers/bioconductor-mgu74acdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74acdf.
shpc-registry automated BioContainers addition for bioconductor-mgu74acdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74acdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74acdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74acdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mgu74acdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74acdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74acdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74acdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74acdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74acdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74acdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgu74acdf

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