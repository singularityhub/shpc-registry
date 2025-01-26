---
layout: container
name:  "quay.io/biocontainers/pgx-variant-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pgx-variant-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pgx-variant-tools/container.yaml"
updated_at: "2025-01-26 03:33:19.306666"
latest: "0.0.5--py_0"
container_url: "https://biocontainers.pro/tools/pgx-variant-tools"

versions:
 - "0.0.5--py_0"
description: "shpc-registry automated BioContainers addition for pgx-variant-tools"
config: {"url": "https://biocontainers.pro/tools/pgx-variant-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pgx-variant-tools", "latest": {"0.0.5--py_0": "sha256:766784f9551afdc7a2414e273467a9e89d90d2e59a26c83c1cc56337ea45da70"}, "tags": {"0.0.5--py_0": "sha256:766784f9551afdc7a2414e273467a9e89d90d2e59a26c83c1cc56337ea45da70"}, "docker": "quay.io/biocontainers/pgx-variant-tools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pgx-variant-tools.
shpc-registry automated BioContainers addition for pgx-variant-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pgx-variant-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pgx-variant-tools:0.0.5--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pgx-variant-tools/0.0.5--py_0
$ module help quay.io/biocontainers/pgx-variant-tools/0.0.5--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pgx-variant-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pgx-variant-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pgx-variant-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pgx-variant-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pgx-variant-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pgx-variant-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pgx-variant-tools

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