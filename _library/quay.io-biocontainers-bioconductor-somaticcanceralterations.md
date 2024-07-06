---
layout: container
name:  "quay.io/biocontainers/bioconductor-somaticcanceralterations"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-somaticcanceralterations/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-somaticcanceralterations/container.yaml"
updated_at: "2024-07-06 02:45:59.381035"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-somaticcanceralterations"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-somaticcanceralterations"
config: {"url": "https://biocontainers.pro/tools/bioconductor-somaticcanceralterations", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-somaticcanceralterations", "latest": {"1.38.0--r43hdfd78af_0": "sha256:d65c6f1bc7d065f59bcf0558aba8f672d9d6cc4ef592ccd40048e97eda5ed815"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:962b529f5ebcfb7be6011345f2398e05ba1ea54ba12956b126128aed3388fd8a", "1.34.0--r42hdfd78af_0": "sha256:d0474102dc84e4342d3ce458b744dad3dd47982ea48863a3316b97f0d47cda6f", "1.36.0--r43hdfd78af_0": "sha256:e02afe248ff788accb82f50dce649906cbbd8e47f8d61e0b7b8c06bf1abbb444", "1.38.0--r43hdfd78af_0": "sha256:d65c6f1bc7d065f59bcf0558aba8f672d9d6cc4ef592ccd40048e97eda5ed815"}, "docker": "quay.io/biocontainers/bioconductor-somaticcanceralterations"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-somaticcanceralterations.
shpc-registry automated BioContainers addition for bioconductor-somaticcanceralterations
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-somaticcanceralterations
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-somaticcanceralterations:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-somaticcanceralterations/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-somaticcanceralterations/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-somaticcanceralterations-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-somaticcanceralterations-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-somaticcanceralterations-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-somaticcanceralterations-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-somaticcanceralterations-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-somaticcanceralterations-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-somaticcanceralterations

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