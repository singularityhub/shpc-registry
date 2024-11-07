---
layout: container
name:  "python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/python/container.yaml"
updated_at: "2024-11-07 07:58:53.205947"
latest: "3.13-rc"
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
 - "3.12"
 - "3.13-rc"
description: "An interpreted, high-level and general-purpose programming language."
config: {"docker": "python", "url": "https://hub.docker.com/_/python", "maintainer": "@vsoch", "description": "An interpreted, high-level and general-purpose programming language.", "latest": {"3.13-rc": "sha256:e4c047cd05d461d49a819d2e7b2f1dbe81e9db463d0fdfe55919ec8b5d61e009"}, "tags": {"3.9.2-alpine": "sha256:f046c06388c0721961fe5c9b6184d2f8aeb7eb01b39601babab06cfd975dae01", "3.9.2-slim": "sha256:ce367bb30b8928efb632c369e3bd4a8dbd7905417bd0a245087a82c250e54a24", "3.9.4-alpine": "sha256:419a7502c95b49946fbdd8228b32243597d9e9f191ddfe5468a3b9b3fe64051d", "3.9.5-alpine": "sha256:7dd8962ad2a63403428d652a64d814a5002f1386379355edf5970e40557fe4e6", "3.9.6-alpine": "sha256:954ea8d05e9041d1dd17b69eb13708a60ef8b8bcc76d928beb4d137e2a9ceb30", "3.9.7": "sha256:8771691756bbf5beff80d64fca8f5b12e018352ddd9e30d8cdfef8cc3717b0e6", "3.9.9": "sha256:dd8335df6162579adadd56ff2b9fbd61199da5405c8856c6e34356c13b48cce4", "3.9.10": "sha256:3aae21920963df3205fba69826cc07fcf2fad91f9e062add921766b36e89e6e8", "3.10.0a7-alpine": "sha256:9b7958e47cd5bd4d092c3b28802493ad1870bce988b2f6ff97f6c81d96fcda80", "3.9": "sha256:e730f8ac1ff165f22c88b5fc9d3e53668ee3e80ea1aefe06c7f06f69da14e83d", "3": "sha256:336461f63f4eb1100e178d5acbfea3d1a5b2a53dea88aa0f9b8482d4d02e981c", "3.11-rc": "sha256:871f5e5c05f66bfa5b22f506a60774dbd45fc65fd309d23e856ab124a7cbb17b", "3.10": "sha256:d5b1fbbc00fd3b55620a9314222498bebf09c4bf606425bf464709ed6a79f202", "3.12-rc": "sha256:5cd18b1cf43ccc797ec20fadc9f9307bc709b7edca41675ff0c6eafd94479d9d", "3.11": "sha256:47d0618fb878d93e1b8cacb184fd8f727ae95c1b85d5959723e1d3e1848e2aba", "3.12": "sha256:336461f63f4eb1100e178d5acbfea3d1a5b2a53dea88aa0f9b8482d4d02e981c", "3.13-rc": "sha256:e4c047cd05d461d49a819d2e7b2f1dbe81e9db463d0fdfe55919ec8b5d61e009"}, "filter": ["3[.]*", "^(?!.*alpine).*$", "^(?!.*windows).*$"], "aliases": {"python": "/usr/local/bin/python"}}
---

This module is a singularity container wrapper for python.
An interpreted, high-level and general-purpose programming language.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install python
```

Or a specific version:

```bash
$ shpc install python:3.13-rc
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load python/3.13-rc
$ module help python/3.13-rc
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