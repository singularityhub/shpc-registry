---
layout: container
name:  "quay.io/biocontainers/bioconductor-fantom3and4cage"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fantom3and4cage/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fantom3and4cage/container.yaml"
updated_at: "2024-03-08 02:42:27.673742"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fantom3and4cage"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fantom3and4cage"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fantom3and4cage", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fantom3and4cage", "latest": {"1.38.0--r43hdfd78af_0": "sha256:b3bcb17e4aff97368d197a892347dc37a9ea27ea101d857f11f05f047e0fdc9d"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:d3bda7169fd4282497bca0f181633f04aa950b6c26501b955f690fa899517581", "1.33.0--r42hdfd78af_0": "sha256:4b3ae605c2b8e7e9cc60ff966212a4cc8bdd3e37821c93e2c8666f0c99830dcd", "1.36.0--r43hdfd78af_0": "sha256:62747563b09d402553f5eb77c0927a7833e58310106d5a0187a6fc330778fb26", "1.38.0--r43hdfd78af_0": "sha256:b3bcb17e4aff97368d197a892347dc37a9ea27ea101d857f11f05f047e0fdc9d"}, "docker": "quay.io/biocontainers/bioconductor-fantom3and4cage"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fantom3and4cage.
shpc-registry automated BioContainers addition for bioconductor-fantom3and4cage
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fantom3and4cage
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fantom3and4cage:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fantom3and4cage/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-fantom3and4cage/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fantom3and4cage-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fantom3and4cage-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fantom3and4cage-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fantom3and4cage-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fantom3and4cage-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fantom3and4cage-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fantom3and4cage

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