---
layout: container
name:  "quay.io/biocontainers/cmip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cmip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cmip/container.yaml"
updated_at: "2024-04-04 03:48:32.598784"
latest: "2.7.0--h8c3ec31_0"
container_url: "https://biocontainers.pro/tools/cmip"
aliases:
 - "avgEpsGrid"
 - "canal"
 - "cmip"
 - "getPatch"
 - "grd2cube"
 - "surfnet2binaryGrid"
 - "titration"
 - "watden"
versions:
 - "2.7.0--h8c3ec31_0"
description: "shpc-registry automated BioContainers addition for cmip"
config: {"url": "https://biocontainers.pro/tools/cmip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cmip", "latest": {"2.7.0--h8c3ec31_0": "sha256:98d3114cae3818eb553c0452848661bc047b3864701a169418a3bc21dd475758"}, "tags": {"2.7.0--h8c3ec31_0": "sha256:98d3114cae3818eb553c0452848661bc047b3864701a169418a3bc21dd475758"}, "docker": "quay.io/biocontainers/cmip", "aliases": {"avgEpsGrid": "/usr/local/bin/avgEpsGrid", "canal": "/usr/local/bin/canal", "cmip": "/usr/local/bin/cmip", "getPatch": "/usr/local/bin/getPatch", "grd2cube": "/usr/local/bin/grd2cube", "surfnet2binaryGrid": "/usr/local/bin/surfnet2binaryGrid", "titration": "/usr/local/bin/titration", "watden": "/usr/local/bin/watden"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cmip.
shpc-registry automated BioContainers addition for cmip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cmip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cmip:2.7.0--h8c3ec31_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cmip/2.7.0--h8c3ec31_0
$ module help quay.io/biocontainers/cmip/2.7.0--h8c3ec31_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cmip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cmip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cmip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cmip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cmip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cmip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### avgEpsGrid

```bash
$ singularity exec <container> /usr/local/bin/avgEpsGrid
$ podman run --it --rm --entrypoint /usr/local/bin/avgEpsGrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/avgEpsGrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canal

```bash
$ singularity exec <container> /usr/local/bin/canal
$ podman run --it --rm --entrypoint /usr/local/bin/canal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmip

```bash
$ singularity exec <container> /usr/local/bin/cmip
$ podman run --it --rm --entrypoint /usr/local/bin/cmip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getPatch

```bash
$ singularity exec <container> /usr/local/bin/getPatch
$ podman run --it --rm --entrypoint /usr/local/bin/getPatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getPatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grd2cube

```bash
$ singularity exec <container> /usr/local/bin/grd2cube
$ podman run --it --rm --entrypoint /usr/local/bin/grd2cube   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grd2cube   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### surfnet2binaryGrid

```bash
$ singularity exec <container> /usr/local/bin/surfnet2binaryGrid
$ podman run --it --rm --entrypoint /usr/local/bin/surfnet2binaryGrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/surfnet2binaryGrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### titration

```bash
$ singularity exec <container> /usr/local/bin/titration
$ podman run --it --rm --entrypoint /usr/local/bin/titration   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/titration   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watden

```bash
$ singularity exec <container> /usr/local/bin/watden
$ podman run --it --rm --entrypoint /usr/local/bin/watden   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watden   -v ${PWD} -w ${PWD} <container> -c " $@"
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