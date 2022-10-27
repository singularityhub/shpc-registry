---
layout: container
name:  "quay.io/biocontainers/google-api-python-client"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/google-api-python-client/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/google-api-python-client/container.yaml"
updated_at: "2022-10-27 00:29:23.332428"
latest: "1.4.2--py27_0"
container_url: "https://biocontainers.pro/tools/google-api-python-client"
aliases:
 - "smtpd.pyc"
versions:
 - "1.4.2--py27_0"
description: "shpc-registry automated BioContainers addition for google-api-python-client"
config: {"url": "https://biocontainers.pro/tools/google-api-python-client", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for google-api-python-client", "latest": {"1.4.2--py27_0": "sha256:52559bf6cae8d765456e58b95bbd7f6ab0af1c8659cf537a972a5901abc965b0"}, "tags": {"1.4.2--py27_0": "sha256:52559bf6cae8d765456e58b95bbd7f6ab0af1c8659cf537a972a5901abc965b0"}, "docker": "quay.io/biocontainers/google-api-python-client", "aliases": {"smtpd.pyc": "/usr/local/bin/smtpd.pyc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/google-api-python-client.
shpc-registry automated BioContainers addition for google-api-python-client
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/google-api-python-client
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/google-api-python-client:1.4.2--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/google-api-python-client/1.4.2--py27_0
$ module help quay.io/biocontainers/google-api-python-client/1.4.2--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### google-api-python-client-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### google-api-python-client-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### google-api-python-client-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### google-api-python-client-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### google-api-python-client-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### google-api-python-client-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### smtpd.pyc

```bash
$ singularity exec <container> /usr/local/bin/smtpd.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
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