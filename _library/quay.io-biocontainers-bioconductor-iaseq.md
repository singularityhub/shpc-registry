---
layout: container
name:  "quay.io/biocontainers/bioconductor-iaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-iaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-iaseq/container.yaml"
updated_at: "2024-03-11 02:34:33.960734"
latest: "1.46.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-iaseq"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-iaseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-iaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-iaseq", "latest": {"1.46.0--r43hdfd78af_0": "sha256:1e3578bc44a0a8852041447e355cb88ac87f646850950ec99718b035b6fc6200"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:4e7e7d16ff9e33c5d596396dcacbeed82608cf3ba7d711678d74105ac749e2e6", "1.42.0--r42hdfd78af_0": "sha256:4f790d78d90f0ca85345ded26a7e6dd9f5477eee5ca5bc52ed2baa7f8309a705", "1.44.0--r43hdfd78af_0": "sha256:48c0c21b5c4af919e972442c6162d65f5d61bfec6f243ba29bfbf0e2ad6e802e", "1.46.0--r43hdfd78af_0": "sha256:1e3578bc44a0a8852041447e355cb88ac87f646850950ec99718b035b6fc6200"}, "docker": "quay.io/biocontainers/bioconductor-iaseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-iaseq.
shpc-registry automated BioContainers addition for bioconductor-iaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-iaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-iaseq:1.46.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-iaseq/1.46.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-iaseq/1.46.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-iaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-iaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-iaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-iaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-iaseq

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