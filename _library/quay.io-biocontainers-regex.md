---
layout: container
name:  "quay.io/biocontainers/regex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/regex/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/regex/container.yaml"
updated_at: "2022-10-27 00:34:58.749082"
latest: "2016.06.24--py35_1"
container_url: "https://biocontainers.pro/tools/regex"

versions:
 - "2016.06.24--py35_1"
description: "shpc-registry automated BioContainers addition for regex"
config: {"url": "https://biocontainers.pro/tools/regex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for regex", "latest": {"2016.06.24--py35_1": "sha256:c5e4f4c85d2ea937db03838095672bcfe1fa453965e11cec53565f3a38763d1b"}, "tags": {"2016.06.24--py35_1": "sha256:c5e4f4c85d2ea937db03838095672bcfe1fa453965e11cec53565f3a38763d1b"}, "docker": "quay.io/biocontainers/regex"}
---

This module is a singularity container wrapper for quay.io/biocontainers/regex.
shpc-registry automated BioContainers addition for regex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/regex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/regex:2016.06.24--py35_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/regex/2016.06.24--py35_1
$ module help quay.io/biocontainers/regex/2016.06.24--py35_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### regex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### regex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### regex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### regex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### regex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### regex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### regex

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