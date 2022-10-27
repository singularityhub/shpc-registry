---
layout: container
name:  "quay.io/biocontainers/scrappie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scrappie/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scrappie/container.yaml"
updated_at: "2022-10-27 00:47:47.939931"
latest: "1.4.2--py37pl5321hcc03fe6_3"
container_url: "https://biocontainers.pro/tools/scrappie"
aliases:
 - "scrappie"
 - "scrappy"
versions:
 - "1.4.2--py37pl5321hcc03fe6_3"
description: "shpc-registry automated BioContainers addition for scrappie"
config: {"url": "https://biocontainers.pro/tools/scrappie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scrappie", "latest": {"1.4.2--py37pl5321hcc03fe6_3": "sha256:228129414a1be5137c2aaac313673b0a6102290f6873f7bb39669213598c90b3"}, "tags": {"1.4.2--py37pl5321hcc03fe6_3": "sha256:228129414a1be5137c2aaac313673b0a6102290f6873f7bb39669213598c90b3"}, "docker": "quay.io/biocontainers/scrappie", "aliases": {"scrappie": "/usr/local/bin/scrappie", "scrappy": "/usr/local/bin/scrappy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scrappie.
shpc-registry automated BioContainers addition for scrappie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scrappie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scrappie:1.4.2--py37pl5321hcc03fe6_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scrappie/1.4.2--py37pl5321hcc03fe6_3
$ module help quay.io/biocontainers/scrappie/1.4.2--py37pl5321hcc03fe6_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scrappie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scrappie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scrappie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scrappie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scrappie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scrappie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scrappie

```bash
$ singularity exec <container> /usr/local/bin/scrappie
$ podman run --it --rm --entrypoint /usr/local/bin/scrappie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scrappie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scrappy

```bash
$ singularity exec <container> /usr/local/bin/scrappy
$ podman run --it --rm --entrypoint /usr/local/bin/scrappy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scrappy   -v ${PWD} -w ${PWD} <container> -c " $@"
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