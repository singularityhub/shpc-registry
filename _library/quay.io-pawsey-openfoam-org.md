---
layout: container
name:  "quay.io/pawsey/openfoam-org"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/openfoam-org/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/pawsey/openfoam-org/container.yaml"
updated_at: "2025-07-15 04:31:02.464726"
latest: "10"
container_url: "https://quay.io/repository/pawsey/openfoam-org"

versions:
 - "10"
 - "9"
 - "8"
 - "7"
description: "OpenFOAM (openfoam.org) images built on top of MPICH."
config: {"docker": "quay.io/pawsey/openfoam-org", "url": "https://quay.io/repository/pawsey/openfoam-org", "maintainer": "@alexisespinosa", "description": "OpenFOAM (openfoam.org) images built on top of MPICH.", "latest": {"10": "sha256:28fac3f4a4eb564df635dbae9d55eaf7940a466807a5e81ee412863c316a9137"}, "tags": {"10": "sha256:28fac3f4a4eb564df635dbae9d55eaf7940a466807a5e81ee412863c316a9137", "9": "sha256:4bf84cb30534e8ab12d79e2f29708a4c9492064b432c9b4274d143f3d28f829e", "8": "sha256:ddc8c9d502d77c1f6d3b46282a41eed19c622deedb40d511c4991abc9a25f2bb", "7": "sha256:370c77f1c3920a19c16eb53596441280e38bbfca344a36332efaa45e32ace369"}, "overrides": {"10": "aliases/10.yaml", "9": "aliases/9.yaml", "8": "aliases/8.yaml", "7": "aliases/7.yaml"}}
---

This module is a singularity container wrapper for quay.io/pawsey/openfoam-org.
OpenFOAM (openfoam.org) images built on top of MPICH.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/openfoam-org
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/openfoam-org:10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/openfoam-org/10
$ module help quay.io/pawsey/openfoam-org/10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openfoam-org-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openfoam-org-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openfoam-org-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openfoam-org-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openfoam-org-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openfoam-org-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### openfoam-org

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