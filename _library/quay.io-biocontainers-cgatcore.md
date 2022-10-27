---
layout: container
name:  "quay.io/biocontainers/cgatcore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cgatcore/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cgatcore/container.yaml"
updated_at: "2022-10-27 00:50:44.780775"
latest: "0.6.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cgatcore"
aliases:
 - "docker-credential-gcloud"
 - "time"
versions:
 - "0.6.9--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cgatcore"
config: {"url": "https://biocontainers.pro/tools/cgatcore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cgatcore", "latest": {"0.6.9--pyhdfd78af_0": "sha256:baa5e4618d6c36e5a7764593addd1c5fc1aca45e8537f4dae7b67430492aafb4"}, "tags": {"0.6.9--pyhdfd78af_0": "sha256:baa5e4618d6c36e5a7764593addd1c5fc1aca45e8537f4dae7b67430492aafb4"}, "docker": "quay.io/biocontainers/cgatcore", "aliases": {"docker-credential-gcloud": "/usr/local/bin/docker-credential-gcloud", "time": "/usr/local/bin/time"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cgatcore.
shpc-registry automated BioContainers addition for cgatcore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cgatcore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cgatcore:0.6.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cgatcore/0.6.9--pyhdfd78af_0
$ module help quay.io/biocontainers/cgatcore/0.6.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cgatcore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cgatcore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cgatcore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cgatcore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cgatcore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cgatcore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### docker-credential-gcloud

```bash
$ singularity exec <container> /usr/local/bin/docker-credential-gcloud
$ podman run --it --rm --entrypoint /usr/local/bin/docker-credential-gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docker-credential-gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time

```bash
$ singularity exec <container> /usr/local/bin/time
$ podman run --it --rm --entrypoint /usr/local/bin/time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time   -v ${PWD} -w ${PWD} <container> -c " $@"
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