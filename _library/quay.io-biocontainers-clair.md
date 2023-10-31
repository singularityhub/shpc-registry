---
layout: container
name:  "quay.io/biocontainers/clair"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clair/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clair/container.yaml"
updated_at: "2023-10-31 03:13:07.647300"
latest: "2.1.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/clair"

versions:
 - "2.1.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for clair"
config: {"url": "https://biocontainers.pro/tools/clair", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clair", "latest": {"2.1.1--hdfd78af_1": "sha256:810206e3580a4405bbcb975e930a5fd7afe76c4535730fff08a3051a121ad6ed"}, "tags": {"2.1.1--hdfd78af_1": "sha256:810206e3580a4405bbcb975e930a5fd7afe76c4535730fff08a3051a121ad6ed"}, "docker": "quay.io/biocontainers/clair"}
---

This module is a singularity container wrapper for quay.io/biocontainers/clair.
shpc-registry automated BioContainers addition for clair
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clair
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clair:2.1.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clair/2.1.1--hdfd78af_1
$ module help quay.io/biocontainers/clair/2.1.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clair-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clair-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clair-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clair-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clair-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clair-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### clair

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