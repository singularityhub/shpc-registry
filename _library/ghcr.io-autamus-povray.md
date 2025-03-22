---
layout: container
name:  "ghcr.io/autamus/povray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/povray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/povray/container.yaml"
updated_at: "2025-03-22 03:46:41.311231"
latest: "3.7.0.10"
container_url: "https://github.com/orgs/autamus/packages/container/package/povray"
aliases:
 - "povray"
versions:
 - "3.7.0.8"
 - "3.7.0.9"
 - "3.7.0.10"
 - "latest"
description: "The Persistence of Vision Ray Tracer, most commonly acronymed as POV-Ray, is a cross-platform ray-tracing program that generates images from a text-based scene description."
config: {"docker": "ghcr.io/autamus/povray", "url": "https://github.com/orgs/autamus/packages/container/package/povray", "maintainer": "@vsoch", "description": "The Persistence of Vision Ray Tracer, most commonly acronymed as POV-Ray, is a cross-platform ray-tracing program that generates images from a text-based scene description.", "latest": {"3.7.0.10": "sha256:40fab1ae617f55fccd3f8f213161139413446519afe3c0243241ac20e316026d"}, "tags": {"3.7.0.8": "sha256:78e76a31bf7a620cb40e41857d6cc6e23e75fb5c780026fbf951d476ee218dc8", "3.7.0.9": "sha256:2b6b1aad9a6ddd5747c872171b26e65f5a2eea77bb59b8d5682e4b7b004c66bb", "3.7.0.10": "sha256:40fab1ae617f55fccd3f8f213161139413446519afe3c0243241ac20e316026d", "latest": "sha256:78e76a31bf7a620cb40e41857d6cc6e23e75fb5c780026fbf951d476ee218dc8"}, "aliases": {"povray": "/opt/view/bin/povray"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/povray.
The Persistence of Vision Ray Tracer, most commonly acronymed as POV-Ray, is a cross-platform ray-tracing program that generates images from a text-based scene description.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/povray
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/povray:3.7.0.10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/povray/3.7.0.10
$ module help ghcr.io/autamus/povray/3.7.0.10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### povray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### povray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### povray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### povray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### povray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### povray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### povray

```bash
$ singularity exec <container> /opt/view/bin/povray
$ podman run --it --rm --entrypoint /opt/view/bin/povray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/povray   -v ${PWD} -w ${PWD} <container> -c " $@"
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