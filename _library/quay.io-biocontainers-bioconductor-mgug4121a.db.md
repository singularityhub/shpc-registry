---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgug4121a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgug4121a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgug4121a.db/container.yaml"
updated_at: "2024-05-28 02:32:58.636557"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mgug4121a.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mgug4121a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgug4121a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgug4121a.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:e982f83b62807afadf9e50a2c8d94cfc4e4e3808f47f947912efffa8ad92d768"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:48fac3d97af616cdbf2a2a7ed8d641c277e4ca7e163eba747eb708829897eaa4", "3.2.3--r42hdfd78af_10": "sha256:c52032cdf2c6994dfbca9e0537bbbbe708f71e315be35dd6641ba4b3f6667c91", "3.2.3--r43hdfd78af_11": "sha256:61b99413be5041e78a06f7cc19d7413c5752442a917fbddf49931e547232a3f9", "3.2.3--r43hdfd78af_12": "sha256:e982f83b62807afadf9e50a2c8d94cfc4e4e3808f47f947912efffa8ad92d768"}, "docker": "quay.io/biocontainers/bioconductor-mgug4121a.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgug4121a.db.
shpc-registry automated BioContainers addition for bioconductor-mgug4121a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgug4121a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgug4121a.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgug4121a.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mgug4121a.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgug4121a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgug4121a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgug4121a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgug4121a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgug4121a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgug4121a.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgug4121a.db

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