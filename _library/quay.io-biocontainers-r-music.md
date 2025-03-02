---
layout: container
name:  "quay.io/biocontainers/r-music"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-music/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-music/container.yaml"
updated_at: "2025-03-02 03:35:56.117670"
latest: "0.2.0--r44hdfd78af_3"
container_url: "https://biocontainers.pro/tools/r-music"

versions:
 - "0.2.0--r41hdfd78af_0"
 - "0.2.0--r42hdfd78af_1"
 - "0.2.0--r43hdfd78af_2"
 - "0.2.0--r44hdfd78af_3"
description: "shpc-registry automated BioContainers addition for r-music"
config: {"url": "https://biocontainers.pro/tools/r-music", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-music", "latest": {"0.2.0--r44hdfd78af_3": "sha256:6d9a3a42a7dc418e752c2402029f9dcf453a8288d5339db84a4f7fed583c2d35"}, "tags": {"0.2.0--r41hdfd78af_0": "sha256:07194fe1180b905e8898467c9019729fe77a40fd74a1d8929a97969311e24012", "0.2.0--r42hdfd78af_1": "sha256:e9ba205c13d3d2f357ae924a36c11037d4db82b1e85e0689e5242fe4308ba479", "0.2.0--r43hdfd78af_2": "sha256:c349870d050e6e55017493400416d1a1d119457009639cfb05953129ba095f5e", "0.2.0--r44hdfd78af_3": "sha256:6d9a3a42a7dc418e752c2402029f9dcf453a8288d5339db84a4f7fed583c2d35"}, "docker": "quay.io/biocontainers/r-music"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-music.
shpc-registry automated BioContainers addition for r-music
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-music
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-music:0.2.0--r44hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-music/0.2.0--r44hdfd78af_3
$ module help quay.io/biocontainers/r-music/0.2.0--r44hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-music-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-music-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-music-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-music-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-music-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-music-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-music

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