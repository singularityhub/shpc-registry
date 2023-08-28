---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74cv2.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74cv2.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74cv2.db/container.yaml"
updated_at: "2023-08-28 09:08:10.146126"
latest: "3.13.0--r43hdfd78af_3"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74cv2.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_8"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74cv2.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74cv2.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74cv2.db", "latest": {"3.13.0--r43hdfd78af_3": "sha256:dde22a44633ffc51eea817be10013916c96160780fab70d01291d8cf4e52e0ed"}, "tags": {"3.2.3--r41hdfd78af_8": "sha256:c17b20e4bae1d5469787134230fc2a15a116a1c12e331ab172f6c146b70c5d6a", "3.13.0--r42hdfd78af_2": "sha256:5bc23f24d94a33bfc18d7f6ef4965ebbc2794ccb78f378bb35baf9f968a0a066", "3.13.0--r43hdfd78af_3": "sha256:dde22a44633ffc51eea817be10013916c96160780fab70d01291d8cf4e52e0ed"}, "docker": "quay.io/biocontainers/bioconductor-mgu74cv2.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74cv2.db.
shpc-registry automated BioContainers addition for bioconductor-mgu74cv2.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74cv2.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74cv2.db:3.13.0--r43hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74cv2.db/3.13.0--r43hdfd78af_3
$ module help quay.io/biocontainers/bioconductor-mgu74cv2.db/3.13.0--r43hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74cv2.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74cv2.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74cv2.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74cv2.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74cv2.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74cv2.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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