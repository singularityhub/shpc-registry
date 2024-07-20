---
layout: container
name:  "quay.io/biocontainers/trimal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trimal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trimal/container.yaml"
updated_at: "2024-07-20 02:52:40.926567"
latest: "1.4.1--h4ac6f70_9"
container_url: "https://biocontainers.pro/tools/trimal"
aliases:
 - "trimal"
 - "readal"
 - "statal"
versions:
 - "1.4.1--h9f5acd7_6"
 - "1.4.1--h4ac6f70_8"
 - "1.4.1--h4ac6f70_9"
description: "shpc-registry automated BioContainers addition for trimal"
config: {"url": "https://biocontainers.pro/tools/trimal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trimal", "latest": {"1.4.1--h4ac6f70_9": "sha256:1813a50be8f0e73bcebcce987047b53a8ab2abad78dc33879cafdbd70fe20e46"}, "tags": {"1.4.1--h9f5acd7_6": "sha256:a0e5f37ed058270b0ff00d7f683df2fbc65423822267848b2bae1a9ffe197b0c", "1.4.1--h4ac6f70_8": "sha256:d9a48609a6b4e01218863c8176efb0d4c1cc325277da04907d197d3215c8a125", "1.4.1--h4ac6f70_9": "sha256:1813a50be8f0e73bcebcce987047b53a8ab2abad78dc33879cafdbd70fe20e46"}, "docker": "quay.io/biocontainers/trimal", "aliases": {"trimal": "/usr/local/bin/trimal", "readal": "/usr/local/bin/readal", "statal": "/usr/local/bin/statal"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trimal.
shpc-registry automated BioContainers addition for trimal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trimal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trimal:1.4.1--h4ac6f70_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trimal/1.4.1--h4ac6f70_9
$ module help quay.io/biocontainers/trimal/1.4.1--h4ac6f70_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trimal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trimal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trimal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trimal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trimal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trimal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trimal

```bash
$ singularity exec <container> /usr/local/bin/trimal
$ podman run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readal

```bash
$ singularity exec <container> /usr/local/bin/readal
$ podman run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statal

```bash
$ singularity exec <container> /usr/local/bin/statal
$ podman run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
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