---
layout: container
name:  "ghcr.io/autamus/gawk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/gawk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/gawk/container.yaml"
updated_at: "2025-04-24 03:07:47.166162"
latest: "5.1.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/gawk"
aliases:
 - "gawk"
versions:
 - "5.1.0"
 - "5.1.1"
description: "gawk is the GNU implementation of awk. The awk utility interprets a special-purpose programming language that makes it possible to handle simple data-reformatting jobs with just a few lines of code. https://www.gnu.org/software/gawk/"
config: {"docker": "ghcr.io/autamus/gawk", "url": "https://github.com/orgs/autamus/packages/container/package/gawk", "maintainer": "@vsoch", "description": "gawk is the GNU implementation of awk. The awk utility interprets a special-purpose programming language that makes it possible to handle simple data-reformatting jobs with just a few lines of code. https://www.gnu.org/software/gawk/", "latest": {"5.1.1": "sha256:caae00cea035b1aba1a9a38e39cecf2ecc7f6ba443187204b405302645e7cac1"}, "tags": {"5.1.0": "sha256:b08a8df43c51257c5de2362eb68ee572494ce38609e689772faf41dd4cf0ffdb", "5.1.1": "sha256:caae00cea035b1aba1a9a38e39cecf2ecc7f6ba443187204b405302645e7cac1"}, "aliases": {"gawk": "/opt/view/bin/gawk"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/gawk.
gawk is the GNU implementation of awk. The awk utility interprets a special-purpose programming language that makes it possible to handle simple data-reformatting jobs with just a few lines of code. https://www.gnu.org/software/gawk/
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/gawk
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gawk:5.1.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gawk/5.1.1
$ module help ghcr.io/autamus/gawk/5.1.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gawk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gawk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gawk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gawk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gawk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gawk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gawk

```bash
$ singularity exec <container> /opt/view/bin/gawk
$ podman run --it --rm --entrypoint /opt/view/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
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