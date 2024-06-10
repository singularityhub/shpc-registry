---
layout: container
name:  "quay.io/biocontainers/bioconductor-fletcher2013a"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fletcher2013a/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fletcher2013a/container.yaml"
updated_at: "2024-06-10 02:48:58.318491"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fletcher2013a"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fletcher2013a"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fletcher2013a", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fletcher2013a", "latest": {"1.38.0--r43hdfd78af_0": "sha256:ecf9f04cb9587eba72fea14d3db4900982f610da17897e8f2ff43565c08c4c0e"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:58a2048effd700ce9c05c8b65465d88317ee43591dd434c345174048874e2805", "1.34.0--r42hdfd78af_0": "sha256:3fe7851b4326f3d599c70f7eda8e1ecee89dd474e006ea5ddba1f8f7a0b9c9f9", "1.36.0--r43hdfd78af_0": "sha256:69f26d9c0fe38b07c336867848c066ee99badbe1d45a928457f17b4b021132f0", "1.38.0--r43hdfd78af_0": "sha256:ecf9f04cb9587eba72fea14d3db4900982f610da17897e8f2ff43565c08c4c0e"}, "docker": "quay.io/biocontainers/bioconductor-fletcher2013a"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fletcher2013a.
shpc-registry automated BioContainers addition for bioconductor-fletcher2013a
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fletcher2013a
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fletcher2013a:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fletcher2013a/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-fletcher2013a/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fletcher2013a-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fletcher2013a-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fletcher2013a-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fletcher2013a-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fletcher2013a-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fletcher2013a-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fletcher2013a

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