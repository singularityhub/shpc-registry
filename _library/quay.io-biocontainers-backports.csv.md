---
layout: container
name:  "quay.io/biocontainers/backports.csv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/backports.csv/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/backports.csv/container.yaml"
updated_at: "2022-10-27 01:00:20.896962"
latest: "1.0.1--py36_0"
container_url: "https://biocontainers.pro/tools/backports.csv"

versions:
 - "1.0.1--py36_0"
description: "shpc-registry automated BioContainers addition for backports.csv"
config: {"url": "https://biocontainers.pro/tools/backports.csv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for backports.csv", "latest": {"1.0.1--py36_0": "sha256:3b085730458522719476d6a132aaf14fd71fa52cc560630cb0bd350d1be2d7e6"}, "tags": {"1.0.1--py36_0": "sha256:3b085730458522719476d6a132aaf14fd71fa52cc560630cb0bd350d1be2d7e6"}, "docker": "quay.io/biocontainers/backports.csv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/backports.csv.
shpc-registry automated BioContainers addition for backports.csv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/backports.csv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/backports.csv:1.0.1--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/backports.csv/1.0.1--py36_0
$ module help quay.io/biocontainers/backports.csv/1.0.1--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### backports.csv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### backports.csv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### backports.csv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### backports.csv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### backports.csv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### backports.csv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### backports.csv

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