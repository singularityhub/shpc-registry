---
layout: container
name:  "ghcr.io/autamus/gnuplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/gnuplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/gnuplot/container.yaml"
updated_at: "2024-06-25 02:34:07.566355"
latest: "5.4.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/gnuplot"
aliases:
 - "gnuplot"
versions:
 - "5.2.8"
 - "5.4.2"
 - "latest"
description: "Gnuplot is a portable command-line driven graphing utility for Linux, OS/2, MS Windows, OSX, VMS, and many other platforms."
config: {"docker": "ghcr.io/autamus/gnuplot", "url": "https://github.com/orgs/autamus/packages/container/package/gnuplot", "maintainer": "@vsoch", "description": "Gnuplot is a portable command-line driven graphing utility for Linux, OS/2, MS Windows, OSX, VMS, and many other platforms.", "latest": {"5.4.2": "sha256:0f63f37292bc6bb27bac115e47c064c41da0ec40e71a20ccb4c8445db7d9b028"}, "tags": {"5.2.8": "sha256:9e18e91463b3db78df3505e43632ab5e9086ff72aa6a91d1d110efbfe0e51ca1", "5.4.2": "sha256:0f63f37292bc6bb27bac115e47c064c41da0ec40e71a20ccb4c8445db7d9b028", "latest": "sha256:0f63f37292bc6bb27bac115e47c064c41da0ec40e71a20ccb4c8445db7d9b028"}, "aliases": {"gnuplot": "/opt/view/bin/gnuplot"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/gnuplot.
Gnuplot is a portable command-line driven graphing utility for Linux, OS/2, MS Windows, OSX, VMS, and many other platforms.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/gnuplot
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gnuplot:5.4.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gnuplot/5.4.2
$ module help ghcr.io/autamus/gnuplot/5.4.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gnuplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gnuplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gnuplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gnuplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gnuplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gnuplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gnuplot

```bash
$ singularity exec <container> /opt/view/bin/gnuplot
$ podman run --it --rm --entrypoint /opt/view/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
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