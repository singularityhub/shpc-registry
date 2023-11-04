---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowmeans"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowmeans/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowmeans/container.yaml"
updated_at: "2023-11-04 02:44:06.975788"
latest: "1.60.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowmeans"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowmeans"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowmeans", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowmeans", "latest": {"1.60.0--r43hdfd78af_0": "sha256:c053b37fbd173ba5ef26d8f1ed1d115acf083b1f3a07357b666f42d7265fcffd"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:3b5542d4c9ee9e0b8b2740d8d8ecd3bfcc12c4947c6b7ebdacc91d628c6b9bcc", "1.58.0--r42hdfd78af_0": "sha256:38725fca7538ab32dbc44337acb487f86edb7b604b0bda009445ff151e89ab85", "1.60.0--r43hdfd78af_0": "sha256:c053b37fbd173ba5ef26d8f1ed1d115acf083b1f3a07357b666f42d7265fcffd"}, "docker": "quay.io/biocontainers/bioconductor-flowmeans"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowmeans.
shpc-registry automated BioContainers addition for bioconductor-flowmeans
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowmeans
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowmeans:1.60.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowmeans/1.60.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowmeans/1.60.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowmeans-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowmeans-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowmeans-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowmeans-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowmeans-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowmeans-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowmeans

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