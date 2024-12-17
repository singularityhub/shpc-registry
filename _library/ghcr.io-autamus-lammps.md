---
layout: container
name:  "ghcr.io/autamus/lammps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/lammps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/lammps/container.yaml"
updated_at: "2024-12-17 03:03:08.405420"
latest: "20220623"
container_url: "https://github.com/orgs/autamus/packages/container/package/lammps"

versions:
 - "latest"
 - "20210310"
 - "20220623"
description: "LAMMPS is a classical molecular dynamics code with a focus on materials modeling."
config: {"docker": "ghcr.io/autamus/lammps", "url": "https://github.com/orgs/autamus/packages/container/package/lammps", "maintainer": "@vsoch", "description": "LAMMPS is a classical molecular dynamics code with a focus on materials modeling.", "latest": {"20220623": "sha256:1dd156b2fee3842e30cd975d48cb4c36a45be6b6b549726ecfa7f6e7e3c35bdc"}, "tags": {"latest": "sha256:1dd156b2fee3842e30cd975d48cb4c36a45be6b6b549726ecfa7f6e7e3c35bdc", "20210310": "sha256:6b49f26c1d75e460ca1edae7ed7ad819204cff880c69acaeaa868c6e7eacc893", "20220623": "sha256:1dd156b2fee3842e30cd975d48cb4c36a45be6b6b549726ecfa7f6e7e3c35bdc"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/lammps.
LAMMPS is a classical molecular dynamics code with a focus on materials modeling.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/lammps
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/lammps:20220623
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/lammps/20220623
$ module help ghcr.io/autamus/lammps/20220623
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lammps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lammps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lammps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lammps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lammps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lammps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### lammps

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