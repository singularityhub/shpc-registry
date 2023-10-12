---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133acdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133acdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133acdf/container.yaml"
updated_at: "2023-10-12 03:13:15.659514"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133acdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133acdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133acdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133acdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:9a3d3da5af13285b3e7b8f412e53a4763490b53a20fa4ceaf4e79587a3132923"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:5fb5163f122284ad3c9430122e42bd63c29b43a08a336294b490f6b297f46f7b", "2.18.0--r42hdfd78af_10": "sha256:700f1fb1e80e8ea64ee61f6f4b9d41b010785a8d8ecd880e6aacaddba1c32bcb", "2.18.0--r43hdfd78af_11": "sha256:9a3d3da5af13285b3e7b8f412e53a4763490b53a20fa4ceaf4e79587a3132923"}, "docker": "quay.io/biocontainers/bioconductor-hgu133acdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133acdf.
shpc-registry automated BioContainers addition for bioconductor-hgu133acdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133acdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133acdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133acdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-hgu133acdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133acdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133acdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133acdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133acdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133acdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133acdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133acdf

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