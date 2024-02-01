---
layout: container
name:  "quay.io/biocontainers/bioconductor-shinymethyl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-shinymethyl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-shinymethyl/container.yaml"
updated_at: "2024-02-01 03:42:17.664096"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-shinymethyl"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-shinymethyl"
config: {"url": "https://biocontainers.pro/tools/bioconductor-shinymethyl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-shinymethyl", "latest": {"1.38.0--r43hdfd78af_0": "sha256:7e55e6602805399f22e13518197068d9700ba594e105d74e33003f9693ec8f25"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:bb598efeb2150f87b9a7d4ba0b1f3833212455f7095cc152e1f87d70b9953c21", "1.34.0--r42hdfd78af_0": "sha256:22c80a621d7bcaf3fef8e88ac8479189a0ac865198c9af8663034215e022c974", "1.36.0--r43hdfd78af_0": "sha256:a0e5ae83cc54f5df6936005e5cce2eea3f394a9d0b92ed05ce720a5b36eab615", "1.38.0--r43hdfd78af_0": "sha256:7e55e6602805399f22e13518197068d9700ba594e105d74e33003f9693ec8f25"}, "docker": "quay.io/biocontainers/bioconductor-shinymethyl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-shinymethyl.
shpc-registry automated BioContainers addition for bioconductor-shinymethyl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-shinymethyl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-shinymethyl:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-shinymethyl/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-shinymethyl/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-shinymethyl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-shinymethyl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-shinymethyl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-shinymethyl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-shinymethyl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-shinymethyl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-shinymethyl

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