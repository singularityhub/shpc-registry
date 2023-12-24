---
layout: container
name:  "quay.io/biocontainers/pb-falcon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pb-falcon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pb-falcon/container.yaml"
updated_at: "2023-12-24 02:37:43.354564"
latest: "2.2.4--py39hb7ef6d5_4"
container_url: "https://biocontainers.pro/tools/pb-falcon"

versions:
 - "2.2.4--py38ha1fcc84_2"
 - "2.2.4--py37h6a4bb35_3"
 - "2.2.4--py39hb7ef6d5_4"
description: "shpc-registry automated BioContainers addition for pb-falcon"
config: {"url": "https://biocontainers.pro/tools/pb-falcon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pb-falcon", "latest": {"2.2.4--py39hb7ef6d5_4": "sha256:41fec34240293ad57029600b8c7c2d311142d1c0bc087d729bdd6efc2bbeec4b"}, "tags": {"2.2.4--py38ha1fcc84_2": "sha256:8270d1a95e6fb20c991ad67947600a55db8a50650b94b0efa0a58d5b76f23487", "2.2.4--py37h6a4bb35_3": "sha256:98e6432e4642bd1cfaed26f08c7c1186e7cf59d890f3e26730d5fc90d92a8ee9", "2.2.4--py39hb7ef6d5_4": "sha256:41fec34240293ad57029600b8c7c2d311142d1c0bc087d729bdd6efc2bbeec4b"}, "docker": "quay.io/biocontainers/pb-falcon"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pb-falcon.
shpc-registry automated BioContainers addition for pb-falcon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pb-falcon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pb-falcon:2.2.4--py39hb7ef6d5_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pb-falcon/2.2.4--py39hb7ef6d5_4
$ module help quay.io/biocontainers/pb-falcon/2.2.4--py39hb7ef6d5_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pb-falcon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pb-falcon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pb-falcon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pb-falcon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pb-falcon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pb-falcon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pb-falcon

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