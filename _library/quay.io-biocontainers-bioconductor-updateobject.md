---
layout: container
name:  "quay.io/biocontainers/bioconductor-updateobject"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-updateobject/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-updateobject/container.yaml"
updated_at: "2024-01-17 02:58:48.708784"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-updateobject"

versions:
 - "1.2.0--r42hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-updateobject"
config: {"url": "https://biocontainers.pro/tools/bioconductor-updateobject", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-updateobject", "latest": {"1.6.0--r43hdfd78af_0": "sha256:9fc75e27678f02d32c7fd84baa3ed1270f35f45534eee074323e4064a3d6e6d7"}, "tags": {"1.2.0--r42hdfd78af_0": "sha256:3aede3ce544680c57ba16fc466419c8b1c2d76d15d4f03fb2f54f6141c9ea499", "1.4.0--r43hdfd78af_0": "sha256:b105792d2a7260ea18646c5f5367525c897a8264399041458df05a495f58215c", "1.6.0--r43hdfd78af_0": "sha256:9fc75e27678f02d32c7fd84baa3ed1270f35f45534eee074323e4064a3d6e6d7"}, "docker": "quay.io/biocontainers/bioconductor-updateobject"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-updateobject.
singularity registry hpc automated addition for bioconductor-updateobject
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-updateobject
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-updateobject:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-updateobject/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-updateobject/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-updateobject-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-updateobject-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-updateobject-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-updateobject-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-updateobject-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-updateobject-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-updateobject

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