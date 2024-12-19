---
layout: container
name:  "amdih/gromacs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/amdih/gromacs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/amdih/gromacs/container.yaml"
updated_at: "2024-12-19 02:59:20.077511"
latest: "2022.3.amd1_174"
container_url: "https://www.amd.com/en/technologies/infinity-hub/gromacs"
aliases:
 - "gmx"
versions:
 - "2022.3.amd1_174"
 - "2022.3.amd1"
description: "GROMACS is a versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles."
config: {"docker": "amdih/gromacs", "url": "https://www.amd.com/en/technologies/infinity-hub/gromacs", "description": "GROMACS is a versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles.", "maintainer": "@cristiandipietrantonio", "latest": {"2022.3.amd1_174": "sha256:3def3e37a32b014a80620e588f16241e23d4043b6a0a022f09a3d856cda72ee3"}, "tags": {"2022.3.amd1_174": "sha256:3def3e37a32b014a80620e588f16241e23d4043b6a0a022f09a3d856cda72ee3", "2022.3.amd1": "sha256:3def3e37a32b014a80620e588f16241e23d4043b6a0a022f09a3d856cda72ee3"}, "aliases": [{"name": "gmx", "command": "/usr/local/gromacs/bin/gmx"}]}
---

This module is a singularity container wrapper for amdih/gromacs.
GROMACS is a versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install amdih/gromacs
```

Or a specific version:

```bash
$ shpc install amdih/gromacs:2022.3.amd1_174
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load amdih/gromacs/2022.3.amd1_174
$ module help amdih/gromacs/2022.3.amd1_174
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gromacs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gromacs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gromacs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gromacs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gromacs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gromacs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gmx

```bash
$ singularity exec <container> /usr/local/gromacs/bin/gmx
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