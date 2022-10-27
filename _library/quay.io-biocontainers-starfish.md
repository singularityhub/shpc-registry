---
layout: container
name:  "quay.io/biocontainers/starfish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/starfish/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/starfish/container.yaml"
updated_at: "2022-10-27 00:24:13.449618"
latest: "0.2.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/starfish"
aliases:
 - "slicedimage"
 - "starfish"
 - "tiff2fsspec"
versions:
 - "0.2.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for starfish"
config: {"url": "https://biocontainers.pro/tools/starfish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for starfish", "latest": {"0.2.2--pyhdfd78af_0": "sha256:541f4726ec9c5cf5238922ebca8f1f8bad741cc0ad3277d08fecdd0fdd67b3d3"}, "tags": {"0.2.2--pyhdfd78af_0": "sha256:541f4726ec9c5cf5238922ebca8f1f8bad741cc0ad3277d08fecdd0fdd67b3d3"}, "docker": "quay.io/biocontainers/starfish", "aliases": {"slicedimage": "/usr/local/bin/slicedimage", "starfish": "/usr/local/bin/starfish", "tiff2fsspec": "/usr/local/bin/tiff2fsspec"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/starfish.
shpc-registry automated BioContainers addition for starfish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/starfish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/starfish:0.2.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/starfish/0.2.2--pyhdfd78af_0
$ module help quay.io/biocontainers/starfish/0.2.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### starfish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### starfish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### starfish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### starfish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### starfish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### starfish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### slicedimage

```bash
$ singularity exec <container> /usr/local/bin/slicedimage
$ podman run --it --rm --entrypoint /usr/local/bin/slicedimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slicedimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starfish

```bash
$ singularity exec <container> /usr/local/bin/starfish
$ podman run --it --rm --entrypoint /usr/local/bin/starfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2fsspec

```bash
$ singularity exec <container> /usr/local/bin/tiff2fsspec
$ podman run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
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