---
layout: container
name:  "quay.io/biocontainers/verse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/verse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/verse/container.yaml"
updated_at: "2023-08-07 03:19:34.023313"
latest: "0.1.5--he4a0461_8"
container_url: "https://biocontainers.pro/tools/verse"
aliases:
 - "verse"
versions:
 - "0.1.5--h7132678_6"
 - "0.1.5--he4a0461_8"
description: "shpc-registry automated BioContainers addition for verse"
config: {"url": "https://biocontainers.pro/tools/verse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for verse", "latest": {"0.1.5--he4a0461_8": "sha256:b8bfdf01b3d56a6350b123585184e86b7ad64d3b20b5b9c3ff9c78e8c5812c6f"}, "tags": {"0.1.5--h7132678_6": "sha256:66924b76b75aeab557905ffb3b0b6ba80a170b0338873df67c9bf8209b574170", "0.1.5--he4a0461_8": "sha256:b8bfdf01b3d56a6350b123585184e86b7ad64d3b20b5b9c3ff9c78e8c5812c6f"}, "docker": "quay.io/biocontainers/verse", "aliases": {"verse": "/usr/local/bin/verse"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/verse.
shpc-registry automated BioContainers addition for verse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/verse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/verse:0.1.5--he4a0461_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/verse/0.1.5--he4a0461_8
$ module help quay.io/biocontainers/verse/0.1.5--he4a0461_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### verse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### verse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### verse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### verse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### verse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### verse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### verse

```bash
$ singularity exec <container> /usr/local/bin/verse
$ podman run --it --rm --entrypoint /usr/local/bin/verse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/verse   -v ${PWD} -w ${PWD} <container> -c " $@"
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