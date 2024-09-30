---
layout: container
name:  "quay.io/biocontainers/rebar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rebar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rebar/container.yaml"
updated_at: "2024-09-30 04:22:24.057639"
latest: "0.2.1--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/rebar"
aliases:
 - "rebar"
versions:
 - "0.2.0--h9ee0642_0"
 - "0.2.1--h9ee0642_0"
description: "singularity registry hpc automated addition for rebar"
config: {"url": "https://biocontainers.pro/tools/rebar", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rebar", "latest": {"0.2.1--h9ee0642_0": "sha256:5d7e83be02edba3bc7e5aa4603da5452f6bfa4c6ad8eb38cd5ac06a7c2b7962d"}, "tags": {"0.2.0--h9ee0642_0": "sha256:974f18ad93b012ab4d71d9a2f5bb6f74eefb80372f8c4055bc6fade74c9f9da5", "0.2.1--h9ee0642_0": "sha256:5d7e83be02edba3bc7e5aa4603da5452f6bfa4c6ad8eb38cd5ac06a7c2b7962d"}, "docker": "quay.io/biocontainers/rebar", "aliases": {"rebar": "/usr/local/bin/rebar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rebar.
singularity registry hpc automated addition for rebar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rebar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rebar:0.2.1--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rebar/0.2.1--h9ee0642_0
$ module help quay.io/biocontainers/rebar/0.2.1--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rebar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rebar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rebar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rebar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rebar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rebar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rebar

```bash
$ singularity exec <container> /usr/local/bin/rebar
$ podman run --it --rm --entrypoint /usr/local/bin/rebar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rebar   -v ${PWD} -w ${PWD} <container> -c " $@"
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