---
layout: container
name:  "ghcr.io/autamus/lp-solve"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/lp-solve/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/lp-solve/container.yaml"
updated_at: "2024-07-08 03:07:35.734081"
latest: "5.5.2.11"
container_url: "https://github.com/orgs/autamus/packages/container/package/lp-solve"
aliases:
 - "lp_solve"
versions:
 - "5.5.2.11"
 - "latest"
description: "Lp_solve is freely available (under LGPL 2) software for solving linear, integer and mixed integer programs."
config: {"docker": "ghcr.io/autamus/lp-solve", "url": "https://github.com/orgs/autamus/packages/container/package/lp-solve", "maintainer": "@vsoch", "description": "Lp_solve is freely available (under LGPL 2) software for solving linear, integer and mixed integer programs.", "latest": {"5.5.2.11": "sha256:cb91d0b15c13c91ceec54655dbc799c94d1da20076b0b9dbff97a5e16ef39e1a"}, "tags": {"5.5.2.11": "sha256:cb91d0b15c13c91ceec54655dbc799c94d1da20076b0b9dbff97a5e16ef39e1a", "latest": "sha256:cb91d0b15c13c91ceec54655dbc799c94d1da20076b0b9dbff97a5e16ef39e1a"}, "aliases": {"lp_solve": "/opt/view/bin/lp_solve"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/lp-solve.
Lp_solve is freely available (under LGPL 2) software for solving linear, integer and mixed integer programs.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/lp-solve
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/lp-solve:5.5.2.11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/lp-solve/5.5.2.11
$ module help ghcr.io/autamus/lp-solve/5.5.2.11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lp-solve-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lp-solve-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lp-solve-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lp-solve-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lp-solve-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lp-solve-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lp_solve

```bash
$ singularity exec <container> /opt/view/bin/lp_solve
$ podman run --it --rm --entrypoint /opt/view/bin/lp_solve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/lp_solve   -v ${PWD} -w ${PWD} <container> -c " $@"
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