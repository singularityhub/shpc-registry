---
layout: container
name:  "python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/python/container.yaml"
updated_at: "2023-05-10 02:32:20.711536"
latest: "3.12-rc"
container_url: "https://hub.docker.com/_/python"
aliases:
 - "python"
versions:
 - "3.9.2-alpine"
 - "3.9.2-slim"
 - "3.9.4-alpine"
 - "3.9.5-alpine"
 - "3.9.6-alpine"
 - "3.9.7"
 - "3.9.9"
 - "3.9.10"
 - "3.10.0a7-alpine"
 - "3.9"
 - "3"
 - "3.11-rc"
 - "3.10"
 - "3.12-rc"
 - "3.11"
description: "An interpreted, high-level and general-purpose programming language."
config: {"docker": "python", "url": "https://hub.docker.com/_/python", "maintainer": "@vsoch", "description": "An interpreted, high-level and general-purpose programming language.", "latest": {"3.12-rc": "sha256:c20fd637fa5d1dce4a2858684c53bcacb6ff21f04ca4bd4a4f881bf64b572edd"}, "tags": {"3.9.2-alpine": "sha256:f046c06388c0721961fe5c9b6184d2f8aeb7eb01b39601babab06cfd975dae01", "3.9.2-slim": "sha256:ce367bb30b8928efb632c369e3bd4a8dbd7905417bd0a245087a82c250e54a24", "3.9.4-alpine": "sha256:419a7502c95b49946fbdd8228b32243597d9e9f191ddfe5468a3b9b3fe64051d", "3.9.5-alpine": "sha256:7dd8962ad2a63403428d652a64d814a5002f1386379355edf5970e40557fe4e6", "3.9.6-alpine": "sha256:954ea8d05e9041d1dd17b69eb13708a60ef8b8bcc76d928beb4d137e2a9ceb30", "3.9.7": "sha256:8771691756bbf5beff80d64fca8f5b12e018352ddd9e30d8cdfef8cc3717b0e6", "3.9.9": "sha256:dd8335df6162579adadd56ff2b9fbd61199da5405c8856c6e34356c13b48cce4", "3.9.10": "sha256:3aae21920963df3205fba69826cc07fcf2fad91f9e062add921766b36e89e6e8", "3.10.0a7-alpine": "sha256:9b7958e47cd5bd4d092c3b28802493ad1870bce988b2f6ff97f6c81d96fcda80", "3.9": "sha256:2d8875d28ca023a9056a828518adcdd634ba03740e1e3b197c06eb4527c6152c", "3": "sha256:f7382f4f9dbc51183c72d621b9c196c1565f713a1fe40c119d215c961fa22815", "3.11-rc": "sha256:871f5e5c05f66bfa5b22f506a60774dbd45fc65fd309d23e856ab124a7cbb17b", "3.10": "sha256:f12d5573aa14fafc4b86ac76726fabdd1216e03f2dbd82e10406f302677a3754", "3.12-rc": "sha256:c20fd637fa5d1dce4a2858684c53bcacb6ff21f04ca4bd4a4f881bf64b572edd", "3.11": "sha256:f7382f4f9dbc51183c72d621b9c196c1565f713a1fe40c119d215c961fa22815"}, "filter": ["3[.]*", "^(?!.*alpine).*$", "^(?!.*windows).*$"], "aliases": {"python": "/usr/local/bin/python"}}
---

This module is a singularity container wrapper for python.
An interpreted, high-level and general-purpose programming language.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install python
```

Or a specific version:

```bash
$ shpc install python:3.12-rc
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load python/3.12-rc
$ module help python/3.12-rc
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python

```bash
$ singularity exec <container> /usr/local/bin/python
$ podman run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
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