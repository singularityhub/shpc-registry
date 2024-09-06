---
layout: container
name:  "quay.io/biocontainers/bioconductor-cghnormaliter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cghnormaliter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cghnormaliter/container.yaml"
updated_at: "2024-09-06 03:19:45.813313"
latest: "1.56.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cghnormaliter"

versions:
 - "1.48.0--r41hdfd78af_0"
 - "1.52.0--r42hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.56.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cghnormaliter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cghnormaliter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cghnormaliter", "latest": {"1.56.0--r43hdfd78af_0": "sha256:07665d6742eb8fafa881e5b4a80db15cdf5a334b29ac179ab557708e48b29821"}, "tags": {"1.48.0--r41hdfd78af_0": "sha256:31bcd3bdb3eea315bd4bd189817092d3c9fb9e6e09bc35ce82a5fac3ef122c55", "1.52.0--r42hdfd78af_0": "sha256:08333b709dbd4cddb501aa5684269d29c29a66635402c7a017e06ea94599b8e6", "1.54.0--r43hdfd78af_0": "sha256:47b6308f56046815bf325e29645c97726ba9cc165f3da70a273ea6bc8a7acac7", "1.56.0--r43hdfd78af_0": "sha256:07665d6742eb8fafa881e5b4a80db15cdf5a334b29ac179ab557708e48b29821"}, "docker": "quay.io/biocontainers/bioconductor-cghnormaliter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cghnormaliter.
shpc-registry automated BioContainers addition for bioconductor-cghnormaliter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cghnormaliter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cghnormaliter:1.56.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cghnormaliter/1.56.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cghnormaliter/1.56.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cghnormaliter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cghnormaliter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cghnormaliter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cghnormaliter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cghnormaliter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cghnormaliter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cghnormaliter

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