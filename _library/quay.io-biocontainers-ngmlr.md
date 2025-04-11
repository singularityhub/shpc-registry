---
layout: container
name:  "quay.io/biocontainers/ngmlr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngmlr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ngmlr/container.yaml"
updated_at: "2025-04-11 03:30:14.952371"
latest: "0.2.7--h077b44d_9"
container_url: "https://biocontainers.pro/tools/ngmlr"
aliases:
 - "ngmlr"
versions:
 - "0.2.7--hd03093a_4"
 - "0.2.7--hdcf5f25_6"
 - "0.2.7--hdcf5f25_7"
 - "0.2.7--h077b44d_8"
 - "0.2.7--h077b44d_9"
description: "shpc-registry automated BioContainers addition for ngmlr"
config: {"url": "https://biocontainers.pro/tools/ngmlr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngmlr", "latest": {"0.2.7--h077b44d_9": "sha256:67d21a2b355fe836e0d39a05901d9898cd355fdc9433bbeaf3aacd3deeb90b11"}, "tags": {"0.2.7--hd03093a_4": "sha256:2ddaed41716f36fa1aefeec4273ef37faaa6160242a21c0fa1df3497bc72c078", "0.2.7--hdcf5f25_6": "sha256:219b57f901904e3a719747b1c8c280e8142db25288285ba45f8ae67204225469", "0.2.7--hdcf5f25_7": "sha256:e1ed93dc57397451a100117b209b0df3d9f5335c7c8bf81cadcda38873bbe112", "0.2.7--h077b44d_8": "sha256:7e829ced4551d094118b64366a730f0f6116afb1550f976ebd65d9cc376c0974", "0.2.7--h077b44d_9": "sha256:67d21a2b355fe836e0d39a05901d9898cd355fdc9433bbeaf3aacd3deeb90b11"}, "docker": "quay.io/biocontainers/ngmlr", "aliases": {"ngmlr": "/usr/local/bin/ngmlr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngmlr.
shpc-registry automated BioContainers addition for ngmlr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngmlr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngmlr:0.2.7--h077b44d_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngmlr/0.2.7--h077b44d_9
$ module help quay.io/biocontainers/ngmlr/0.2.7--h077b44d_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngmlr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngmlr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngmlr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngmlr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngmlr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngmlr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ngmlr

```bash
$ singularity exec <container> /usr/local/bin/ngmlr
$ podman run --it --rm --entrypoint /usr/local/bin/ngmlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngmlr   -v ${PWD} -w ${PWD} <container> -c " $@"
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