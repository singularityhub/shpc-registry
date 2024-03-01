---
layout: container
name:  "quay.io/biocontainers/pbsim3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbsim3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbsim3/container.yaml"
updated_at: "2024-03-01 03:02:09.148170"
latest: "3.0.1--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/pbsim3"
aliases:
 - "pbsim"
versions:
 - "3.0.0--h4ac6f70_0"
 - "3.0.1--h4ac6f70_0"
description: "singularity registry hpc automated addition for pbsim3"
config: {"url": "https://biocontainers.pro/tools/pbsim3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pbsim3", "latest": {"3.0.1--h4ac6f70_0": "sha256:e7251aaf28ec973c547cc0062c3a52c683e9340c600eb44e953907a053e5b2a4"}, "tags": {"3.0.0--h4ac6f70_0": "sha256:940e5060c68c8d6abe39efac4d0d1a7f31033b7058834b3be773372b5a39ddb5", "3.0.1--h4ac6f70_0": "sha256:e7251aaf28ec973c547cc0062c3a52c683e9340c600eb44e953907a053e5b2a4"}, "docker": "quay.io/biocontainers/pbsim3", "aliases": {"pbsim": "/usr/local/bin/pbsim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbsim3.
singularity registry hpc automated addition for pbsim3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbsim3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbsim3:3.0.1--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbsim3/3.0.1--h4ac6f70_0
$ module help quay.io/biocontainers/pbsim3/3.0.1--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbsim3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbsim3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbsim3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbsim3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbsim3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbsim3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pbsim

```bash
$ singularity exec <container> /usr/local/bin/pbsim
$ podman run --it --rm --entrypoint /usr/local/bin/pbsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbsim   -v ${PWD} -w ${PWD} <container> -c " $@"
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