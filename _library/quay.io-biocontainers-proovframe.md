---
layout: container
name:  "quay.io/biocontainers/proovframe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proovframe/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/proovframe/container.yaml"
updated_at: "2022-10-27 01:11:57.500223"
latest: "0.9.7--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/proovframe"
aliases:
 - "proovframe"
 - "proovframe-fix"
 - "proovframe-map"
 - "proovframe-prf"
versions:
 - "0.9.7--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for proovframe"
config: {"url": "https://biocontainers.pro/tools/proovframe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proovframe", "latest": {"0.9.7--hdfd78af_0": "sha256:87b2dcafe6bd7be8780ed127afec1b4f2d4a9f929abc48d12136d1e23729dae6"}, "tags": {"0.9.7--hdfd78af_0": "sha256:87b2dcafe6bd7be8780ed127afec1b4f2d4a9f929abc48d12136d1e23729dae6"}, "docker": "quay.io/biocontainers/proovframe", "aliases": {"proovframe": "/usr/local/bin/proovframe", "proovframe-fix": "/usr/local/bin/proovframe-fix", "proovframe-map": "/usr/local/bin/proovframe-map", "proovframe-prf": "/usr/local/bin/proovframe-prf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proovframe.
shpc-registry automated BioContainers addition for proovframe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proovframe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proovframe:0.9.7--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proovframe/0.9.7--hdfd78af_0
$ module help quay.io/biocontainers/proovframe/0.9.7--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proovframe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proovframe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proovframe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proovframe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proovframe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proovframe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### proovframe

```bash
$ singularity exec <container> /usr/local/bin/proovframe
$ podman run --it --rm --entrypoint /usr/local/bin/proovframe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proovframe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proovframe-fix

```bash
$ singularity exec <container> /usr/local/bin/proovframe-fix
$ podman run --it --rm --entrypoint /usr/local/bin/proovframe-fix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proovframe-fix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proovframe-map

```bash
$ singularity exec <container> /usr/local/bin/proovframe-map
$ podman run --it --rm --entrypoint /usr/local/bin/proovframe-map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proovframe-map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proovframe-prf

```bash
$ singularity exec <container> /usr/local/bin/proovframe-prf
$ podman run --it --rm --entrypoint /usr/local/bin/proovframe-prf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proovframe-prf   -v ${PWD} -w ${PWD} <container> -c " $@"
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