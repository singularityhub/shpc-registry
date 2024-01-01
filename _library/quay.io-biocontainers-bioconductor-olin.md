---
layout: container
name:  "quay.io/biocontainers/bioconductor-olin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-olin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-olin/container.yaml"
updated_at: "2024-01-01 03:23:02.406303"
latest: "1.80.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-olin"

versions:
 - "1.72.0--r41hdfd78af_0"
 - "1.76.0--r42hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
 - "1.80.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-olin"
config: {"url": "https://biocontainers.pro/tools/bioconductor-olin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-olin", "latest": {"1.80.0--r43hdfd78af_0": "sha256:b7f0c12a141c0ce79a38d1bf2980a9dc144480ff2c14b8ad3d118c4e088ea592"}, "tags": {"1.72.0--r41hdfd78af_0": "sha256:ce8dab1a2ef2b074415fdae13f592bd6c0f19a33e9bba989783303e69614921e", "1.76.0--r42hdfd78af_0": "sha256:0373aef740b57f3d001269fe29ecdad5ae27aa9464a5b83f8aea5edd529e6205", "1.78.0--r43hdfd78af_0": "sha256:48cbec87d514cff9eb2f3d5d9dc87885cca211a1e9d27d0a4bdba4886fe39fab", "1.80.0--r43hdfd78af_0": "sha256:b7f0c12a141c0ce79a38d1bf2980a9dc144480ff2c14b8ad3d118c4e088ea592"}, "docker": "quay.io/biocontainers/bioconductor-olin"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-olin.
shpc-registry automated BioContainers addition for bioconductor-olin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-olin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-olin:1.80.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-olin/1.80.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-olin/1.80.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-olin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-olin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-olin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-olin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-olin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-olin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-olin

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