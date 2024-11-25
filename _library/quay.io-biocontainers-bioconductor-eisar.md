---
layout: container
name:  "quay.io/biocontainers/bioconductor-eisar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-eisar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-eisar/container.yaml"
updated_at: "2024-11-25 03:15:57.589506"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-eisar"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-eisar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-eisar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-eisar", "latest": {"1.14.0--r43hdfd78af_0": "sha256:3075c0638db97de97d54bcf04c1926ad97b84c1f6e9febfb76440302c14dcdf6"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:cbb7a248c07968cd66daac9a8d4d4055ebfd88e0e8dd9fe1dd5ddd8061098e87", "1.10.0--r42hdfd78af_0": "sha256:a58ee16573ee091bd2f722a2af2ba7b2e9a049b3469b1c38f93cc012eeae7058", "1.12.0--r43hdfd78af_0": "sha256:d6915cee001a379493704ba8ee2f4c7b8df5853c9034b3d39fc0f7f925ce1126", "1.14.0--r43hdfd78af_0": "sha256:3075c0638db97de97d54bcf04c1926ad97b84c1f6e9febfb76440302c14dcdf6"}, "docker": "quay.io/biocontainers/bioconductor-eisar"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-eisar.
shpc-registry automated BioContainers addition for bioconductor-eisar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-eisar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-eisar:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-eisar/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-eisar/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-eisar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eisar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eisar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-eisar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-eisar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-eisar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-eisar

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