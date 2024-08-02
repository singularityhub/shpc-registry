---
layout: container
name:  "quay.io/biocontainers/dadaist2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dadaist2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dadaist2/container.yaml"
updated_at: "2024-08-02 02:50:33.294414"
latest: "1.3.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/dadaist2"

versions:
 - "1.2.5--hdfd78af_0"
 - "1.3.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for dadaist2"
config: {"url": "https://biocontainers.pro/tools/dadaist2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dadaist2", "latest": {"1.3.0--hdfd78af_0": "sha256:ac3a3bfc9d94da5eeb293fb4edae3d105e8bd66cb1a5b2c6afda62b032a49944"}, "tags": {"1.2.5--hdfd78af_0": "sha256:8b77ca72ed269a2b7db38b2d47ba1d76c4789a3a3952bd409af3554533a15c23", "1.3.0--hdfd78af_0": "sha256:ac3a3bfc9d94da5eeb293fb4edae3d105e8bd66cb1a5b2c6afda62b032a49944"}, "docker": "quay.io/biocontainers/dadaist2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/dadaist2.
shpc-registry automated BioContainers addition for dadaist2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dadaist2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dadaist2:1.3.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dadaist2/1.3.0--hdfd78af_0
$ module help quay.io/biocontainers/dadaist2/1.3.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dadaist2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dadaist2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dadaist2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dadaist2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dadaist2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dadaist2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### dadaist2

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