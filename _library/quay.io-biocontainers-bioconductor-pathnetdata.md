---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathnetdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathnetdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathnetdata/container.yaml"
updated_at: "2024-10-31 00:25:01.962217"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pathnetdata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pathnetdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathnetdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathnetdata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:ec617466fc5b5c137b9a61d313ff7dbcabf62615921d2825e5b9a0cb7182e8de"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:6a6fa6e4e73a3e6fd8a7b0b85f92d4ef3d3fc08d6b82caf4d17358f22d655698", "1.33.0--r42hdfd78af_0": "sha256:00a82b3f54568fe7f7245e15b6d78bbc0c4e78a71d140d55fb34b0321d686a84", "1.36.0--r43hdfd78af_0": "sha256:efe05a34d25c2d025fab6c2d0e07316019ea64c61b14f529b56f925a3ecb56b2", "1.38.0--r43hdfd78af_0": "sha256:ec617466fc5b5c137b9a61d313ff7dbcabf62615921d2825e5b9a0cb7182e8de"}, "docker": "quay.io/biocontainers/bioconductor-pathnetdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pathnetdata.
shpc-registry automated BioContainers addition for bioconductor-pathnetdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pathnetdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pathnetdata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pathnetdata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pathnetdata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pathnetdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathnetdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathnetdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pathnetdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pathnetdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pathnetdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pathnetdata

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