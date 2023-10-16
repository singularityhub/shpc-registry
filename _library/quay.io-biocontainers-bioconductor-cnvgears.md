---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnvgears"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnvgears/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnvgears/container.yaml"
updated_at: "2023-10-16 02:45:27.320788"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cnvgears"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cnvgears"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnvgears", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnvgears", "latest": {"1.8.0--r43hdfd78af_0": "sha256:7d944fc8e22d975e9935fd28f0e0280052ef7e0f36efd7fcfc5eeadb715908df"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:7e4b667a3b0b324994ebeed87d95b6066a43a2e440644eedc59b3fba92c6da87", "1.6.0--r42hdfd78af_0": "sha256:551354539b3184e16d905d45b567e0cbc17d2678f27c7cc1e7210c0816bf9a4c", "1.8.0--r43hdfd78af_0": "sha256:7d944fc8e22d975e9935fd28f0e0280052ef7e0f36efd7fcfc5eeadb715908df"}, "docker": "quay.io/biocontainers/bioconductor-cnvgears"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnvgears.
shpc-registry automated BioContainers addition for bioconductor-cnvgears
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvgears
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvgears:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnvgears/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cnvgears/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cnvgears-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvgears-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvgears-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cnvgears-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cnvgears-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cnvgears-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cnvgears

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