---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95ccdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95ccdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95ccdf/container.yaml"
updated_at: "2023-03-11 03:21:54.928669"
latest: "2.18.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95ccdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95ccdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95ccdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95ccdf", "latest": {"2.18.0--r42hdfd78af_10": "sha256:694407e0efd20dfdece4ab24cbdae1d1f26848a8a91bfa4930dd8e181d4c1267"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:a1b7ac829be42a2982dd63b65754f10e7321b4a0dc11fb86063721469c340c91", "2.18.0--r42hdfd78af_10": "sha256:694407e0efd20dfdece4ab24cbdae1d1f26848a8a91bfa4930dd8e181d4c1267"}, "docker": "quay.io/biocontainers/bioconductor-hgu95ccdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95ccdf.
shpc-registry automated BioContainers addition for bioconductor-hgu95ccdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95ccdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95ccdf:2.18.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95ccdf/2.18.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-hgu95ccdf/2.18.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95ccdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95ccdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95ccdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95ccdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95ccdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95ccdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu95ccdf

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