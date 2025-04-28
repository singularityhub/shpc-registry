---
layout: container
name:  "quay.io/biocontainers/r-alakazam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-alakazam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-alakazam/container.yaml"
updated_at: "2025-04-28 03:49:04.344402"
latest: "1.2.1--r43h21a89ab_3"
container_url: "https://biocontainers.pro/tools/r-alakazam"
aliases:
 - "glpsol"
versions:
 - "1.2.1--r41hecf12ef_0"
 - "1.2.1--r42hecf12ef_1"
 - "1.2.1--r42h21a89ab_2"
 - "1.2.1--r43h21a89ab_3"
description: "shpc-registry automated BioContainers addition for r-alakazam"
config: {"url": "https://biocontainers.pro/tools/r-alakazam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-alakazam", "latest": {"1.2.1--r43h21a89ab_3": "sha256:246adbb67bc97ada04fab89f3361156b6c3d57e962c4549c83dca33269e68786"}, "tags": {"1.2.1--r41hecf12ef_0": "sha256:d8374b2f940f05bc0e9286df8ce7f7463f436c3dd029e681f9d69e7856fa8945", "1.2.1--r42hecf12ef_1": "sha256:3e270ec77589d73f58116d068f29ce733319cd591817b1e275691cb1cda1986b", "1.2.1--r42h21a89ab_2": "sha256:d1e45b350c32b9bdab3cc2aa6da85fbe15dc788fe57d8308020567d7d74f8870", "1.2.1--r43h21a89ab_3": "sha256:246adbb67bc97ada04fab89f3361156b6c3d57e962c4549c83dca33269e68786"}, "docker": "quay.io/biocontainers/r-alakazam", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-alakazam.
shpc-registry automated BioContainers addition for r-alakazam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-alakazam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-alakazam:1.2.1--r43h21a89ab_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-alakazam/1.2.1--r43h21a89ab_3
$ module help quay.io/biocontainers/r-alakazam/1.2.1--r43h21a89ab_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-alakazam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-alakazam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-alakazam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-alakazam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-alakazam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-alakazam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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