---
layout: container
name:  "quay.io/biocontainers/wes-service-client"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wes-service-client/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/wes-service-client/container.yaml"
updated_at: "2022-10-27 01:06:47.259581"
latest: "2.7--py_1"
container_url: "https://biocontainers.pro/tools/wes-service-client"
aliases:
 - "wes-client"
 - "wes-server"
versions:
 - "2.7--py_1"
description: "shpc-registry automated BioContainers addition for wes-service-client"
config: {"url": "https://biocontainers.pro/tools/wes-service-client", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wes-service-client", "latest": {"2.7--py_1": "sha256:b351bbc8a29b7ce06cca86fdc7aa4c04a9e2b33efde3c8184746a038c6b0d928"}, "tags": {"2.7--py_1": "sha256:b351bbc8a29b7ce06cca86fdc7aa4c04a9e2b33efde3c8184746a038c6b0d928"}, "docker": "quay.io/biocontainers/wes-service-client", "aliases": {"wes-client": "/usr/local/bin/wes-client", "wes-server": "/usr/local/bin/wes-server"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wes-service-client.
shpc-registry automated BioContainers addition for wes-service-client
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wes-service-client
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wes-service-client:2.7--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wes-service-client/2.7--py_1
$ module help quay.io/biocontainers/wes-service-client/2.7--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wes-service-client-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wes-service-client-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wes-service-client-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wes-service-client-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wes-service-client-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wes-service-client-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wes-client

```bash
$ singularity exec <container> /usr/local/bin/wes-client
$ podman run --it --rm --entrypoint /usr/local/bin/wes-client   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wes-client   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wes-server

```bash
$ singularity exec <container> /usr/local/bin/wes-server
$ podman run --it --rm --entrypoint /usr/local/bin/wes-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wes-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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