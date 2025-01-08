---
layout: container
name:  "quay.io/biocontainers/schema"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/schema/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/schema/container.yaml"
updated_at: "2025-01-08 02:58:50.829289"
latest: "0.7.0--py_0"
container_url: "https://biocontainers.pro/tools/schema"

versions:
 - "0.7.0--py_0"
description: "shpc-registry automated BioContainers addition for schema"
config: {"url": "https://biocontainers.pro/tools/schema", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for schema", "latest": {"0.7.0--py_0": "sha256:095051d8f2a0ae118b10a20ee788f8ff93db6ac758ecafc800661aeb2ac2a41e"}, "tags": {"0.7.0--py_0": "sha256:095051d8f2a0ae118b10a20ee788f8ff93db6ac758ecafc800661aeb2ac2a41e"}, "docker": "quay.io/biocontainers/schema"}
---

This module is a singularity container wrapper for quay.io/biocontainers/schema.
shpc-registry automated BioContainers addition for schema
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/schema
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/schema:0.7.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/schema/0.7.0--py_0
$ module help quay.io/biocontainers/schema/0.7.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### schema-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### schema-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### schema-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### schema-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### schema-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### schema-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### schema

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