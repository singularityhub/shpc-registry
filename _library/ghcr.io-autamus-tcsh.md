---
layout: container
name:  "ghcr.io/autamus/tcsh"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/tcsh/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/tcsh/container.yaml"
updated_at: "2023-09-14 02:40:52.234214"
latest: "6.24.00"
container_url: "https://github.com/orgs/autamus/packages/container/package/tcsh"
aliases:
 - "tcsh"
versions:
 - "6.22.02"
 - "latest"
 - "6.24.00"

config: {"docker": "ghcr.io/autamus/tcsh", "url": "https://github.com/orgs/autamus/packages/container/package/tcsh", "maintainer": "@vsoch", "description": "", "latest": {"6.24.00": "sha256:831d9880c678e9c38e1ea777dcc4fa96b9618016a3b9dee53ba72df7d2901010"}, "tags": {"6.22.02": "sha256:4c38a838e2139498164279b214c80acc45637c24ecd098fc725b80bbf94094c8", "latest": "sha256:831d9880c678e9c38e1ea777dcc4fa96b9618016a3b9dee53ba72df7d2901010", "6.24.00": "sha256:831d9880c678e9c38e1ea777dcc4fa96b9618016a3b9dee53ba72df7d2901010"}, "aliases": {"tcsh": "/opt/view/bin/tcsh"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/tcsh.

After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/tcsh
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/tcsh:6.24.00
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/tcsh/6.24.00
$ module help ghcr.io/autamus/tcsh/6.24.00
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tcsh-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tcsh-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tcsh-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tcsh-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tcsh-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tcsh-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tcsh

```bash
$ singularity exec <container> /opt/view/bin/tcsh
$ podman run --it --rm --entrypoint /opt/view/bin/tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
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