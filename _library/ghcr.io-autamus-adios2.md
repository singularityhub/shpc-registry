---
layout: container
name:  "ghcr.io/autamus/adios2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/adios2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/adios2/container.yaml"
updated_at: "2025-05-24 11:09:14.502790"
latest: "2.8.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/adios2"
aliases:
 - "adios2-config"
 - "adios2_deactivate_bp"
 - "adios2_iotest"
 - "adios2_reorganize"
 - "adios2_reorganize_mpi"
versions:
 - "2.7.1"
 - "latest"
 - "2.8.3"
description: "The Adaptable Input Output System version 2, developed in the Exascale Computing Program"
config: {"docker": "ghcr.io/autamus/adios2", "url": "https://github.com/orgs/autamus/packages/container/package/adios2", "maintainer": "@vsoch", "description": "The Adaptable Input Output System version 2, developed in the Exascale Computing Program", "latest": {"2.8.3": "sha256:9e80c7aeed6091aba262a761376a2504699f3b3cd404f524db4c527d4c102c72"}, "tags": {"2.7.1": "sha256:ad475f144747104b57674f84e72efa877e904645ce5edeb9d43a06e058764c72", "latest": "sha256:9e80c7aeed6091aba262a761376a2504699f3b3cd404f524db4c527d4c102c72", "2.8.3": "sha256:9e80c7aeed6091aba262a761376a2504699f3b3cd404f524db4c527d4c102c72"}, "aliases": {"adios2-config": "/opt/view/bin/adios2-config", "adios2_deactivate_bp": "/opt/view/bin/adios2_deactivate_bp", "adios2_iotest": "/opt/view/bin/adios2_iotest", "adios2_reorganize": "/opt/view/bin/adios2_reorganize", "adios2_reorganize_mpi": "/opt/view/bin/adios2_reorganize_mpi"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/adios2.
The Adaptable Input Output System version 2, developed in the Exascale Computing Program
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/adios2
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/adios2:2.8.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/adios2/2.8.3
$ module help ghcr.io/autamus/adios2/2.8.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### adios2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### adios2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### adios2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### adios2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### adios2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### adios2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adios2-config

```bash
$ singularity exec <container> /opt/view/bin/adios2-config
$ podman run --it --rm --entrypoint /opt/view/bin/adios2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adios2_deactivate_bp

```bash
$ singularity exec <container> /opt/view/bin/adios2_deactivate_bp
$ podman run --it --rm --entrypoint /opt/view/bin/adios2_deactivate_bp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios2_deactivate_bp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adios2_iotest

```bash
$ singularity exec <container> /opt/view/bin/adios2_iotest
$ podman run --it --rm --entrypoint /opt/view/bin/adios2_iotest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios2_iotest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adios2_reorganize

```bash
$ singularity exec <container> /opt/view/bin/adios2_reorganize
$ podman run --it --rm --entrypoint /opt/view/bin/adios2_reorganize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios2_reorganize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adios2_reorganize_mpi

```bash
$ singularity exec <container> /opt/view/bin/adios2_reorganize_mpi
$ podman run --it --rm --entrypoint /opt/view/bin/adios2_reorganize_mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios2_reorganize_mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
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