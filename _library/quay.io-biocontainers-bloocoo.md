---
layout: container
name:  "quay.io/biocontainers/bloocoo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bloocoo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bloocoo/container.yaml"
updated_at: "2023-11-07 02:34:01.931322"
latest: "1.0.7--h43eeafb_6"
container_url: "https://biocontainers.pro/tools/bloocoo"
aliases:
 - "Bloocoo"
versions:
 - "1.0.7--h5b5514e_4"
 - "1.0.7--h43eeafb_6"
description: "shpc-registry automated BioContainers addition for bloocoo"
config: {"url": "https://biocontainers.pro/tools/bloocoo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bloocoo", "latest": {"1.0.7--h43eeafb_6": "sha256:8c58cc0eed5796be1b11dd5665db5f9834fd5ff15e22685cfc66c900c32600f8"}, "tags": {"1.0.7--h5b5514e_4": "sha256:fd7227f98530192666b8d92564d34893e6216fcc8fc532e24aba5596ce76a84b", "1.0.7--h43eeafb_6": "sha256:8c58cc0eed5796be1b11dd5665db5f9834fd5ff15e22685cfc66c900c32600f8"}, "docker": "quay.io/biocontainers/bloocoo", "aliases": {"Bloocoo": "/usr/local/bin/Bloocoo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bloocoo.
shpc-registry automated BioContainers addition for bloocoo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bloocoo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bloocoo:1.0.7--h43eeafb_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bloocoo/1.0.7--h43eeafb_6
$ module help quay.io/biocontainers/bloocoo/1.0.7--h43eeafb_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bloocoo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bloocoo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bloocoo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bloocoo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bloocoo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bloocoo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Bloocoo

```bash
$ singularity exec <container> /usr/local/bin/Bloocoo
$ podman run --it --rm --entrypoint /usr/local/bin/Bloocoo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Bloocoo   -v ${PWD} -w ${PWD} <container> -c " $@"
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