---
layout: container
name:  "quay.io/biocontainers/bioconductor-mmuphin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mmuphin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mmuphin/container.yaml"
updated_at: "2024-07-08 02:41:17.423201"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mmuphin"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mmuphin"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mmuphin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mmuphin", "latest": {"1.16.0--r43hdfd78af_0": "sha256:fdd8ea30a8d2254e178ec52109a5ff5c168c0fba6a4015c4829305f0eb287f8c"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:4e2c9fc41452c42827611816fa66dd562397df402a6c8ee599b9aca976f928e2", "1.12.0--r42hdfd78af_0": "sha256:009027d90be7f8ed20300421e1c86b9029af84320ca84af8ab78a4c5b7d5fef5", "1.14.0--r43hdfd78af_0": "sha256:d929fcc92e66da0b1575ec17b5d4ca7b8c45fbc36d86576572754f805d206191", "1.16.0--r43hdfd78af_0": "sha256:fdd8ea30a8d2254e178ec52109a5ff5c168c0fba6a4015c4829305f0eb287f8c"}, "docker": "quay.io/biocontainers/bioconductor-mmuphin"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mmuphin.
shpc-registry automated BioContainers addition for bioconductor-mmuphin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mmuphin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mmuphin:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mmuphin/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mmuphin/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mmuphin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmuphin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmuphin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mmuphin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mmuphin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mmuphin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mmuphin

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