---
layout: container
name:  "quay.io/biocontainers/bioconductor-struct"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-struct/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-struct/container.yaml"
updated_at: "2023-09-28 03:29:38.770977"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-struct"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-struct"
config: {"url": "https://biocontainers.pro/tools/bioconductor-struct", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-struct", "latest": {"1.12.0--r43hdfd78af_0": "sha256:a8a740c4021423408eb1900480e0346dbe2ad708a5d7bbb148d53eb3eeb15a96"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:de8e3aab31205981cd8c7850de019877b91c125d06df500526a245ec511ba868", "1.10.0--r42hdfd78af_0": "sha256:9421eedd8daa68f109bbc5a64f1f92da9753fa8823ba5d31ffacdfef4ff1825e", "1.12.0--r43hdfd78af_0": "sha256:a8a740c4021423408eb1900480e0346dbe2ad708a5d7bbb148d53eb3eeb15a96"}, "docker": "quay.io/biocontainers/bioconductor-struct"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-struct.
shpc-registry automated BioContainers addition for bioconductor-struct
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-struct
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-struct:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-struct/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-struct/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-struct-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-struct-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-struct-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-struct-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-struct-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-struct-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-struct

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