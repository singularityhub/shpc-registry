---
layout: container
name:  "quay.io/biocontainers/meme"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/meme/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/meme/container.yaml"
updated_at: "2024-02-12 03:09:08.590758"
latest: "5.1.1--py36pl526ha39971a_2"
container_url: "https://biocontainers.pro/tools/meme"

versions:
 - "5.1.1--py36pl526ha39971a_2"
description: "shpc-registry automated BioContainers addition for meme"
config: {"url": "https://biocontainers.pro/tools/meme", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for meme", "latest": {"5.1.1--py36pl526ha39971a_2": "sha256:e3e0b38a966ff909ceb573fa9072399c27eed5266f2a02ca9875a6f04461b1a4"}, "tags": {"5.1.1--py36pl526ha39971a_2": "sha256:e3e0b38a966ff909ceb573fa9072399c27eed5266f2a02ca9875a6f04461b1a4"}, "docker": "quay.io/biocontainers/meme"}
---

This module is a singularity container wrapper for quay.io/biocontainers/meme.
shpc-registry automated BioContainers addition for meme
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/meme
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/meme:5.1.1--py36pl526ha39971a_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/meme/5.1.1--py36pl526ha39971a_2
$ module help quay.io/biocontainers/meme/5.1.1--py36pl526ha39971a_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### meme-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### meme-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### meme-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### meme-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### meme-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### meme-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### meme

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