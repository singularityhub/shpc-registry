---
layout: container
name:  "quay.io/biocontainers/bioconductor-tracktables"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tracktables/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tracktables/container.yaml"
updated_at: "2025-08-01 10:31:57.781135"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tracktables"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tracktables"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tracktables", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tracktables", "latest": {"1.40.0--r44hdfd78af_0": "sha256:33028a04a31917f5c778077e30f564cb2520cd20a1150218e9d0b7ed8a23b0a8"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:ed5025a301c6a026d2d9f90f516fe84680ee3620495a93b88a3aac7e9cda4b8f", "1.32.0--r42hdfd78af_0": "sha256:e67b53db4c7e4c9f253aae7f8f04a25c142aa46fe1e2746167776da05fca5f0d", "1.34.0--r43hdfd78af_0": "sha256:230b1bbf4e01f151b598be2733f61f70369fa35a44bcd9fb50ac93b7659c4d42", "1.36.0--r43hdfd78af_0": "sha256:880e07120f9276b522a828c06e79786a2372377987e5ea4c34f3fc3ef2bd012b", "1.40.0--r44hdfd78af_0": "sha256:33028a04a31917f5c778077e30f564cb2520cd20a1150218e9d0b7ed8a23b0a8"}, "docker": "quay.io/biocontainers/bioconductor-tracktables"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tracktables.
shpc-registry automated BioContainers addition for bioconductor-tracktables
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tracktables
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tracktables:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tracktables/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tracktables/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tracktables-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tracktables-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tracktables-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tracktables-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tracktables-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tracktables-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tracktables

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