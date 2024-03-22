---
layout: container
name:  "amdih/lammps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/amdih/lammps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/amdih/lammps/container.yaml"
updated_at: "2024-03-22 03:08:13.767132"
latest: "2022.5.04_130"
container_url: "https://www.amd.com/en/technologies/infinity-hub/lammps"
aliases:
 - "lmp"
versions:
 - "2022.5.04_130"
 - "2021.5.14_121"
description: "LAMMPS is a classical molecular dynamics code with a focus on materials modeling. It's an acronym for Large-scale Atomic/Molecular Massively Parallel Simulator."
config: {"docker": "amdih/lammps", "url": "https://www.amd.com/en/technologies/infinity-hub/lammps", "description": "LAMMPS is a classical molecular dynamics code with a focus on materials modeling. It's an acronym for Large-scale Atomic/Molecular Massively Parallel Simulator.", "maintainer": "@cristiandipietrantonio", "latest": {"2022.5.04_130": "sha256:d885a385d8d8c54e1ed82a6ca601f3f5db0781aa2439c01879998984e9e85b69"}, "tags": {"2022.5.04_130": "sha256:d885a385d8d8c54e1ed82a6ca601f3f5db0781aa2439c01879998984e9e85b69", "2021.5.14_121": "sha256:9479772560d24d31ef8f006e558a8a57b67ee1034776b061be5200cf3d92d9d6"}, "aliases": [{"name": "lmp", "command": "/opt/lammps/bin/lmp"}]}
---

This module is a singularity container wrapper for amdih/lammps.
LAMMPS is a classical molecular dynamics code with a focus on materials modeling. It's an acronym for Large-scale Atomic/Molecular Massively Parallel Simulator.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install amdih/lammps
```

Or a specific version:

```bash
$ shpc install amdih/lammps:2022.5.04_130
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load amdih/lammps/2022.5.04_130
$ module help amdih/lammps/2022.5.04_130
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


#### lmp

```bash
$ singularity exec <container> /opt/lammps/bin/lmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
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