---
layout: container
name:  "quay.io/biocontainers/coolbox"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/coolbox/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/coolbox/container.yaml"
updated_at: "2022-10-27 00:28:02.400834"
latest: "0.3.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/coolbox"
aliases:
 - "coolbox"
 - "jupyter-server"
 - "voila"
versions:
 - "0.3.8--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for coolbox"
config: {"url": "https://biocontainers.pro/tools/coolbox", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for coolbox", "latest": {"0.3.8--pyhdfd78af_0": "sha256:b4e9e211fe25d123cded2aa88b0297565a2bda58dd2d974a6be5b3f4b60d0fde"}, "tags": {"0.3.8--pyhdfd78af_0": "sha256:b4e9e211fe25d123cded2aa88b0297565a2bda58dd2d974a6be5b3f4b60d0fde"}, "docker": "quay.io/biocontainers/coolbox", "aliases": {"coolbox": "/usr/local/bin/coolbox", "jupyter-server": "/usr/local/bin/jupyter-server", "voila": "/usr/local/bin/voila"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/coolbox.
shpc-registry automated BioContainers addition for coolbox
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/coolbox
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/coolbox:0.3.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/coolbox/0.3.8--pyhdfd78af_0
$ module help quay.io/biocontainers/coolbox/0.3.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### coolbox-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### coolbox-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### coolbox-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### coolbox-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### coolbox-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### coolbox-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### coolbox

```bash
$ singularity exec <container> /usr/local/bin/coolbox
$ podman run --it --rm --entrypoint /usr/local/bin/coolbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coolbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-server

```bash
$ singularity exec <container> /usr/local/bin/jupyter-server
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### voila

```bash
$ singularity exec <container> /usr/local/bin/voila
$ podman run --it --rm --entrypoint /usr/local/bin/voila   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/voila   -v ${PWD} -w ${PWD} <container> -c " $@"
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