---
layout: container
name:  "quay.io/biocontainers/bioconductor-alternativesplicingevents.hg19"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-alternativesplicingevents.hg19/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-alternativesplicingevents.hg19/container.yaml"
updated_at: "2025-05-27 03:37:38.823354"
latest: "1.1.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-alternativesplicingevents.hg19"

versions:
 - "1.1.0--r41hdfd78af_1"
 - "1.1.0--r42hdfd78af_2"
 - "1.1.0--r43hdfd78af_3"
 - "1.1.0--r43hdfd78af_4"
 - "1.1.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-alternativesplicingevents.hg19"
config: {"url": "https://biocontainers.pro/tools/bioconductor-alternativesplicingevents.hg19", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-alternativesplicingevents.hg19", "latest": {"1.1.0--r44hdfd78af_5": "sha256:9887fc74df8a6a9e148905f306814a656fee5b698488bdde4be8891501f77d11"}, "tags": {"1.1.0--r41hdfd78af_1": "sha256:a431839c8ab42a0d0bd88bc98e2ff24c9af552d31def27a65c35bf65fda417cb", "1.1.0--r42hdfd78af_2": "sha256:347de6efb6f98568e66b59adc98d301089195d612bb42bc9752dcc02c1da7687", "1.1.0--r43hdfd78af_3": "sha256:a23b5b25ffefcddfd7e9887254ee9251ca408a60d776700bebe538bb068326d7", "1.1.0--r43hdfd78af_4": "sha256:3aa83ab1ded6ea2924f5ea05d01f8cb449fe24a27ff950d77643bfae68ea6de1", "1.1.0--r44hdfd78af_5": "sha256:9887fc74df8a6a9e148905f306814a656fee5b698488bdde4be8891501f77d11"}, "docker": "quay.io/biocontainers/bioconductor-alternativesplicingevents.hg19"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-alternativesplicingevents.hg19.
shpc-registry automated BioContainers addition for bioconductor-alternativesplicingevents.hg19
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-alternativesplicingevents.hg19
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-alternativesplicingevents.hg19:1.1.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-alternativesplicingevents.hg19/1.1.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-alternativesplicingevents.hg19/1.1.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-alternativesplicingevents.hg19-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alternativesplicingevents.hg19-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alternativesplicingevents.hg19-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-alternativesplicingevents.hg19-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-alternativesplicingevents.hg19-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-alternativesplicingevents.hg19-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-alternativesplicingevents.hg19

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