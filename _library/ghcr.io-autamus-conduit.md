---
layout: container
name:  "ghcr.io/autamus/conduit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/conduit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/conduit/container.yaml"
updated_at: "2024-07-10 02:34:39.681041"
latest: "0.7.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/conduit"
aliases:
 - "conduit_blueprint_verify"
 - "conduit_relay_entangle.py"
 - "conduit_relay_io_convert"
 - "conduit_relay_io_ls"
 - "conduit_relay_node_viewer"
 - "conduit_staging"
 - "conduit_staging.sh"
versions:
 - "0.7.2"
 - "latest"
description: "Conduit is an open source project from Lawrence Livermore National Laboratory that provides an intuitive model for describing hierarchical scientific data in C++, C, Fortran, and Python."
config: {"docker": "ghcr.io/autamus/conduit", "url": "https://github.com/orgs/autamus/packages/container/package/conduit", "maintainer": "@vsoch", "description": "Conduit is an open source project from Lawrence Livermore National Laboratory that provides an intuitive model for describing hierarchical scientific data in C++, C, Fortran, and Python.", "latest": {"0.7.2": "sha256:229cddc031a67d7a75f7bf90b22ac82c88b5ae12c58663397fab18c7e5608b72"}, "tags": {"0.7.2": "sha256:229cddc031a67d7a75f7bf90b22ac82c88b5ae12c58663397fab18c7e5608b72", "latest": "sha256:229cddc031a67d7a75f7bf90b22ac82c88b5ae12c58663397fab18c7e5608b72"}, "aliases": {"conduit_blueprint_verify": "/opt/view/bin/conduit_blueprint_verify", "conduit_relay_entangle.py": "/opt/view/bin/conduit_relay_entangle.py", "conduit_relay_io_convert": "/opt/view/bin/conduit_relay_io_convert", "conduit_relay_io_ls": "/opt/view/bin/conduit_relay_io_ls", "conduit_relay_node_viewer": "/opt/view/bin/conduit_relay_node_viewer", "conduit_staging": "/opt/view/bin/conduit_staging", "conduit_staging.sh": "/opt/view/bin/conduit_staging.sh"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/conduit.
Conduit is an open source project from Lawrence Livermore National Laboratory that provides an intuitive model for describing hierarchical scientific data in C++, C, Fortran, and Python.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/conduit
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/conduit:0.7.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/conduit/0.7.2
$ module help ghcr.io/autamus/conduit/0.7.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### conduit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### conduit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### conduit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### conduit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### conduit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### conduit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### conduit_blueprint_verify

```bash
$ singularity exec <container> /opt/view/bin/conduit_blueprint_verify
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_blueprint_verify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_blueprint_verify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_relay_entangle.py

```bash
$ singularity exec <container> /opt/view/bin/conduit_relay_entangle.py
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_relay_entangle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_relay_entangle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_relay_io_convert

```bash
$ singularity exec <container> /opt/view/bin/conduit_relay_io_convert
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_relay_io_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_relay_io_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_relay_io_ls

```bash
$ singularity exec <container> /opt/view/bin/conduit_relay_io_ls
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_relay_io_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_relay_io_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_relay_node_viewer

```bash
$ singularity exec <container> /opt/view/bin/conduit_relay_node_viewer
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_relay_node_viewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_relay_node_viewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_staging

```bash
$ singularity exec <container> /opt/view/bin/conduit_staging
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_staging   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_staging   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_staging.sh

```bash
$ singularity exec <container> /opt/view/bin/conduit_staging.sh
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_staging.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_staging.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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