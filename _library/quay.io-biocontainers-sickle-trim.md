---
layout: container
name:  "quay.io/biocontainers/sickle-trim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sickle-trim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sickle-trim/container.yaml"
updated_at: "2024-04-04 02:27:00.415124"
latest: "1.33--he4a0461_9"
container_url: "https://biocontainers.pro/tools/sickle-trim"
aliases:
 - "sickle"
versions:
 - "1.33--h7132678_7"
 - "1.33--he4a0461_9"
description: "shpc-registry automated BioContainers addition for sickle-trim"
config: {"url": "https://biocontainers.pro/tools/sickle-trim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sickle-trim", "latest": {"1.33--he4a0461_9": "sha256:39d01a4bec4635471349b90a7488193504df5942ce576e1b5b64f270183ca640"}, "tags": {"1.33--h7132678_7": "sha256:5488d89b91129983d095ad4392557abdbc25285fe9110426db2105960453a75d", "1.33--he4a0461_9": "sha256:39d01a4bec4635471349b90a7488193504df5942ce576e1b5b64f270183ca640"}, "docker": "quay.io/biocontainers/sickle-trim", "aliases": {"sickle": "/usr/local/bin/sickle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sickle-trim.
shpc-registry automated BioContainers addition for sickle-trim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sickle-trim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sickle-trim:1.33--he4a0461_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sickle-trim/1.33--he4a0461_9
$ module help quay.io/biocontainers/sickle-trim/1.33--he4a0461_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sickle-trim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sickle-trim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sickle-trim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sickle-trim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sickle-trim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sickle-trim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sickle

```bash
$ singularity exec <container> /usr/local/bin/sickle
$ podman run --it --rm --entrypoint /usr/local/bin/sickle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sickle   -v ${PWD} -w ${PWD} <container> -c " $@"
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