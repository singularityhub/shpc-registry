---
layout: container
name:  "quay.io/biocontainers/vawk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vawk/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/vawk/container.yaml"
updated_at: "2022-10-17 09:57:29.808902"
latest: "0.0.2--py_4"
container_url: "https://singularity-hpc.readthedocs.io"
aliases:
 - "vawk"
versions:
 - "0.0.2--py_4"
description: "A custom container to do X."
config: {"url": "https://singularity-hpc.readthedocs.io", "maintainer": "Dinosaur", "description": "A custom container to do X.", "latest": {"0.0.2--py_4": "sha256:5246f4a117de0142bfe2d06c72b813cd8e54f078bccf68d6407b7fc2703a52e2"}, "tags": {"0.0.2--py_4": "sha256:5246f4a117de0142bfe2d06c72b813cd8e54f078bccf68d6407b7fc2703a52e2"}, "docker": "quay.io/biocontainers/vawk", "aliases": {"vawk": "/usr/local/bin/vawk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vawk.
A custom container to do X.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vawk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vawk:0.0.2--py_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vawk/0.0.2--py_4
$ module help quay.io/biocontainers/vawk/0.0.2--py_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vawk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vawk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vawk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vawk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vawk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vawk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vawk
       
```bash
$ singularity exec <container> /usr/local/bin/vawk
$ podman run --it --rm --entrypoint /usr/local/bin/vawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vawk   -v ${PWD} -w ${PWD} <container> -c " $@"
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