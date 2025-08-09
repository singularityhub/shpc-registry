---
layout: container
name:  "quay.io/biocontainers/muse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/muse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/muse/container.yaml"
updated_at: "2025-08-09 04:06:26.890015"
latest: "2.1.2--h3b3e331_3"
container_url: "https://biocontainers.pro/tools/muse"
aliases:
 - "MuSE"
versions:
 - "1.0.rc--h5b5514e_6"
 - "1.0.rc--h43eeafb_8"
 - "2.1.2--h8a3fdc4_0"
 - "2.1.2--h3b3e331_3"
description: "shpc-registry automated BioContainers addition for muse"
config: {"url": "https://biocontainers.pro/tools/muse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for muse", "latest": {"2.1.2--h3b3e331_3": "sha256:3d305567e3233b92b9dfc4ea1fdf107d86f047a51cb8e05f91c574de21342f5f"}, "tags": {"1.0.rc--h5b5514e_6": "sha256:c8ffa1f7b3576796d13380f942812076479f3cdd7a807ff6991877c90dd698ed", "1.0.rc--h43eeafb_8": "sha256:ceb69e23a5c14c8f82f123c2cce4e812b8e12c3bee3ebf91fbe659cefe90648c", "2.1.2--h8a3fdc4_0": "sha256:8e3a56f0b8d839f275abd6783ffc745924defa092b9cce82ba3308b4b7aee377", "2.1.2--h3b3e331_3": "sha256:3d305567e3233b92b9dfc4ea1fdf107d86f047a51cb8e05f91c574de21342f5f"}, "docker": "quay.io/biocontainers/muse", "aliases": {"MuSE": "/usr/local/bin/MuSE"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/muse.
shpc-registry automated BioContainers addition for muse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/muse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/muse:2.1.2--h3b3e331_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/muse/2.1.2--h3b3e331_3
$ module help quay.io/biocontainers/muse/2.1.2--h3b3e331_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### muse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### muse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### muse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### muse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### muse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### muse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MuSE

```bash
$ singularity exec <container> /usr/local/bin/MuSE
$ podman run --it --rm --entrypoint /usr/local/bin/MuSE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MuSE   -v ${PWD} -w ${PWD} <container> -c " $@"
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