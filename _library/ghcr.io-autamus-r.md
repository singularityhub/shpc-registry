---
layout: container
name:  "ghcr.io/autamus/r"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/r/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/r/container.yaml"
updated_at: "2024-10-22 02:52:57.310347"
latest: "4.1.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/r"
aliases:
 - "R"
versions:
 - "4.0.4"
 - "4.1.0"
 - "latest"
description: "R is a language and environment for statistical computing and graphics."
config: {"docker": "ghcr.io/autamus/r", "url": "https://github.com/orgs/autamus/packages/container/package/r", "maintainer": "@vsoch", "description": "R is a language and environment for statistical computing and graphics.", "latest": {"4.1.0": "sha256:68d20470a1c451c2d3ff5d5f388024db6f1294e5dbeb9712dd5000de7a0f6390"}, "tags": {"4.0.4": "sha256:047ce431f400d13df423898e62d78fc72e32c58236772eeaaf69ad2511dd528d", "4.1.0": "sha256:68d20470a1c451c2d3ff5d5f388024db6f1294e5dbeb9712dd5000de7a0f6390", "latest": "sha256:6f76327dcfd44529e4066bbf10cee6d2f4aa320dc3b3c8821bcb00ac2f8c495a"}, "aliases": {"R": "/opt/view/bin/R"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/r.
R is a language and environment for statistical computing and graphics.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/r
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/r:4.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/r/4.1.0
$ module help ghcr.io/autamus/r/4.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### R

```bash
$ singularity exec <container> /opt/view/bin/R
$ podman run --it --rm --entrypoint /opt/view/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
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