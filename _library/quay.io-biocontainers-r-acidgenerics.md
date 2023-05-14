---
layout: container
name:  "quay.io/biocontainers/r-acidgenerics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidgenerics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidgenerics/container.yaml"
updated_at: "2023-05-14 02:51:41.781417"
latest: "0.6.7--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-acidgenerics"

versions:
 - "0.6.0--r41hdfd78af_0"
 - "0.6.5--r42hdfd78af_0"
 - "0.6.6--r42hdfd78af_0"
 - "0.6.6--r42hdfd78af_1"
 - "0.6.7--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-acidgenerics"
config: {"url": "https://biocontainers.pro/tools/r-acidgenerics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidgenerics", "latest": {"0.6.7--r42hdfd78af_0": "sha256:dbe8c7c1023f081e981128e60ce920417d7c004e046d6623cb5c8315eace4dcd"}, "tags": {"0.6.0--r41hdfd78af_0": "sha256:5aecd9de123be462df57a67f21f21e4120ae904213ec2257935a228f93cc982e", "0.6.5--r42hdfd78af_0": "sha256:eb404b2df7f957fe5ec4ae9b5a3a2c4df0fdd81e8688bac22425e62738a0b664", "0.6.6--r42hdfd78af_0": "sha256:ba82417bd0ce82db4c572afb7882c08552393edeeb7c005837909c86cf07ccdd", "0.6.6--r42hdfd78af_1": "sha256:1ff8f30101a5f8884c96b8dd29e304640fbaa764b2c25aea58e21933e51e0c3d", "0.6.7--r42hdfd78af_0": "sha256:dbe8c7c1023f081e981128e60ce920417d7c004e046d6623cb5c8315eace4dcd"}, "docker": "quay.io/biocontainers/r-acidgenerics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidgenerics.
shpc-registry automated BioContainers addition for r-acidgenerics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidgenerics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidgenerics:0.6.7--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidgenerics/0.6.7--r42hdfd78af_0
$ module help quay.io/biocontainers/r-acidgenerics/0.6.7--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidgenerics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidgenerics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidgenerics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidgenerics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidgenerics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidgenerics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidgenerics

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