---
layout: container
name:  "quay.io/biocontainers/teloclip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/teloclip/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/teloclip/container.yaml"
updated_at: "2022-10-27 00:21:13.240829"
latest: "0.0.3--py_1"
container_url: "https://biocontainers.pro/tools/teloclip"
aliases:
 - "teloclip"
 - "teloclip-extract"
versions:
 - "0.0.3--py_1"
description: "shpc-registry automated BioContainers addition for teloclip"
config: {"url": "https://biocontainers.pro/tools/teloclip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for teloclip", "latest": {"0.0.3--py_1": "sha256:b378ec42281cb2140c313b5e8e1c061d3caa7f99921fa0fc82edbb59141558df"}, "tags": {"0.0.3--py_1": "sha256:b378ec42281cb2140c313b5e8e1c061d3caa7f99921fa0fc82edbb59141558df"}, "docker": "quay.io/biocontainers/teloclip", "aliases": {"teloclip": "/usr/local/bin/teloclip", "teloclip-extract": "/usr/local/bin/teloclip-extract"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/teloclip.
shpc-registry automated BioContainers addition for teloclip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/teloclip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/teloclip:0.0.3--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/teloclip/0.0.3--py_1
$ module help quay.io/biocontainers/teloclip/0.0.3--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### teloclip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### teloclip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### teloclip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### teloclip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### teloclip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### teloclip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### teloclip

```bash
$ singularity exec <container> /usr/local/bin/teloclip
$ podman run --it --rm --entrypoint /usr/local/bin/teloclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/teloclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### teloclip-extract

```bash
$ singularity exec <container> /usr/local/bin/teloclip-extract
$ podman run --it --rm --entrypoint /usr/local/bin/teloclip-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/teloclip-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
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