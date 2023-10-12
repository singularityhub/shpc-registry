---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133a2probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133a2probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133a2probe/container.yaml"
updated_at: "2023-10-12 03:56:33.695367"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133a2probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133a2probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133a2probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133a2probe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:021aaa8c0ba2c700b8e4254b3e13f7c2ccd06383741e66173cac1969bbfdfd59"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:03a3e55cfd7268df7a162ecb73b3ff754100915a2c987ede5dc664b1558d61f7", "2.18.0--r42hdfd78af_11": "sha256:546681fc441f012684c58e631f23df4b275cbb171c4bdb2f3d63a65bf984356c", "2.18.0--r43hdfd78af_12": "sha256:021aaa8c0ba2c700b8e4254b3e13f7c2ccd06383741e66173cac1969bbfdfd59"}, "docker": "quay.io/biocontainers/bioconductor-hgu133a2probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133a2probe.
shpc-registry automated BioContainers addition for bioconductor-hgu133a2probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133a2probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133a2probe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133a2probe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgu133a2probe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133a2probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133a2probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133a2probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133a2probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133a2probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133a2probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133a2probe

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