---
layout: container
name:  "quay.io/biocontainers/lambda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lambda/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lambda/container.yaml"
updated_at: "2024-04-23 02:35:43.622171"
latest: "3.0.0--h6dccd9a_0"
container_url: "https://biocontainers.pro/tools/lambda"
aliases:
 - "lambda2"
versions:
 - "2.0.0--h19e8d03_3"
 - "2.0.0--h19e8d03_4"
 - "2.0.0--h6dccd9a_6"
 - "3.0.0--h6dccd9a_0"
 - "2.0.1--h6dccd9a_0"
description: "shpc-registry automated BioContainers addition for lambda"
config: {"url": "https://biocontainers.pro/tools/lambda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lambda", "latest": {"3.0.0--h6dccd9a_0": "sha256:ed860c1b32a3490c279e4a8ddebfc650472a3e69ef92c431e3364231641f93e9"}, "tags": {"2.0.0--h19e8d03_3": "sha256:90ebe144c12654b26c8147440767775928eb1c05449baa25f65f0a80a4de6a72", "2.0.0--h19e8d03_4": "sha256:936e76e99203614c60c061d94c2435120393142e79901eb8641e3b89e3909cdc", "2.0.0--h6dccd9a_6": "sha256:ae5c723e9892047df0ceb4c30688c79a36bbaafb9672cbfd5920a9a62254d78d", "3.0.0--h6dccd9a_0": "sha256:ed860c1b32a3490c279e4a8ddebfc650472a3e69ef92c431e3364231641f93e9", "2.0.1--h6dccd9a_0": "sha256:3f4f8bc516cd34239810437347f572d58c5205b92a03603747775b201038cc24"}, "docker": "quay.io/biocontainers/lambda", "aliases": {"lambda2": "/usr/local/bin/lambda2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lambda.
shpc-registry automated BioContainers addition for lambda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lambda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lambda:3.0.0--h6dccd9a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lambda/3.0.0--h6dccd9a_0
$ module help quay.io/biocontainers/lambda/3.0.0--h6dccd9a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lambda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lambda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lambda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lambda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lambda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lambda-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lambda2

```bash
$ singularity exec <container> /usr/local/bin/lambda2
$ podman run --it --rm --entrypoint /usr/local/bin/lambda2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lambda2   -v ${PWD} -w ${PWD} <container> -c " $@"
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