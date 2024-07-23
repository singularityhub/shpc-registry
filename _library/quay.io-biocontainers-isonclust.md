---
layout: container
name:  "quay.io/biocontainers/isonclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/isonclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/isonclust/container.yaml"
updated_at: "2024-07-23 02:48:23.729395"
latest: "0.0.6.1--py_0"
container_url: "https://biocontainers.pro/tools/isonclust"

versions:
 - "0.0.6.1--py_0"
 - "0.0.6--py_1"
description: "shpc-registry automated BioContainers addition for isonclust"
config: {"url": "https://biocontainers.pro/tools/isonclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for isonclust", "latest": {"0.0.6.1--py_0": "sha256:f295ecaafb2fb55097b8a3f8196ea1db819476b870788b6a7c65beb597da70f7"}, "tags": {"0.0.6.1--py_0": "sha256:f295ecaafb2fb55097b8a3f8196ea1db819476b870788b6a7c65beb597da70f7", "0.0.6--py_1": "sha256:4c2cc9683c76181106361a7470b46b70e715fb50de6810e66adacc90a9691ad6"}, "docker": "quay.io/biocontainers/isonclust"}
---

This module is a singularity container wrapper for quay.io/biocontainers/isonclust.
shpc-registry automated BioContainers addition for isonclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/isonclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/isonclust:0.0.6.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/isonclust/0.0.6.1--py_0
$ module help quay.io/biocontainers/isonclust/0.0.6.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### isonclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### isonclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### isonclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### isonclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### isonclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### isonclust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### isonclust

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