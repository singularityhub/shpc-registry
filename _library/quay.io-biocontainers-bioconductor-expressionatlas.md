---
layout: container
name:  "quay.io/biocontainers/bioconductor-expressionatlas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-expressionatlas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-expressionatlas/container.yaml"
updated_at: "2023-09-05 02:23:36.992415"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-expressionatlas"

versions:
 - "1.22.0--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-expressionatlas"
config: {"url": "https://biocontainers.pro/tools/bioconductor-expressionatlas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-expressionatlas", "latest": {"1.28.0--r43hdfd78af_0": "sha256:f3b1b605b96f0b3e7c508f89eb6275ca644b6f6901a6d17e8bb3fcbf39be252c"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:caecbf4411994c57a17d80981911754694fab1898c02ab9ffdad457001f1841d", "1.26.0--r42hdfd78af_0": "sha256:1627091c59a803e4a93e76affd77518cbf09cea7875c3cb9adce63dc7e2aa194", "1.28.0--r43hdfd78af_0": "sha256:f3b1b605b96f0b3e7c508f89eb6275ca644b6f6901a6d17e8bb3fcbf39be252c"}, "docker": "quay.io/biocontainers/bioconductor-expressionatlas"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-expressionatlas.
shpc-registry automated BioContainers addition for bioconductor-expressionatlas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-expressionatlas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-expressionatlas:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-expressionatlas/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-expressionatlas/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-expressionatlas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-expressionatlas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-expressionatlas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-expressionatlas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-expressionatlas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-expressionatlas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-expressionatlas

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