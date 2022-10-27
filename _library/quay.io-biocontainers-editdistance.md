---
layout: container
name:  "quay.io/biocontainers/editdistance"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/editdistance/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/editdistance/container.yaml"
updated_at: "2022-10-27 00:25:51.258653"
latest: "0.4--py35_0"
container_url: "https://biocontainers.pro/tools/editdistance"

versions:
 - "0.4--py35_0"
description: "shpc-registry automated BioContainers addition for editdistance"
config: {"url": "https://biocontainers.pro/tools/editdistance", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for editdistance", "latest": {"0.4--py35_0": "sha256:e56b5eac4e31f43c6f9b7b5fa076a990258bde1657c2e49f43479ec4e122d69f"}, "tags": {"0.4--py35_0": "sha256:e56b5eac4e31f43c6f9b7b5fa076a990258bde1657c2e49f43479ec4e122d69f"}, "docker": "quay.io/biocontainers/editdistance"}
---

This module is a singularity container wrapper for quay.io/biocontainers/editdistance.
shpc-registry automated BioContainers addition for editdistance
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/editdistance
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/editdistance:0.4--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/editdistance/0.4--py35_0
$ module help quay.io/biocontainers/editdistance/0.4--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### editdistance-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### editdistance-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### editdistance-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### editdistance-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### editdistance-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### editdistance-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### editdistance

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