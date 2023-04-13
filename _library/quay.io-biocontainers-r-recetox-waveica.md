---
layout: container
name:  "quay.io/biocontainers/r-recetox-waveica"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-recetox-waveica/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-recetox-waveica/container.yaml"
updated_at: "2023-04-13 02:32:51.487477"
latest: "0.2.0--r42hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-recetox-waveica"

versions:
 - "0.2.0--r41hdfd78af_0"
 - "0.2.0--r42hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-recetox-waveica"
config: {"url": "https://biocontainers.pro/tools/r-recetox-waveica", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-recetox-waveica", "latest": {"0.2.0--r42hdfd78af_1": "sha256:da3a15f086c9149feca4ec65d74bebb5530df78605bd8f06a8535a36924c8487"}, "tags": {"0.2.0--r41hdfd78af_0": "sha256:da5346275d105b6983eee9d0e0bac791f9f051dfcda1061d246408c59d192b9e", "0.2.0--r42hdfd78af_1": "sha256:da3a15f086c9149feca4ec65d74bebb5530df78605bd8f06a8535a36924c8487"}, "docker": "quay.io/biocontainers/r-recetox-waveica"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-recetox-waveica.
shpc-registry automated BioContainers addition for r-recetox-waveica
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-recetox-waveica
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-recetox-waveica:0.2.0--r42hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-recetox-waveica/0.2.0--r42hdfd78af_1
$ module help quay.io/biocontainers/r-recetox-waveica/0.2.0--r42hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-recetox-waveica-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-recetox-waveica-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-recetox-waveica-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-recetox-waveica-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-recetox-waveica-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-recetox-waveica-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-recetox-waveica

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