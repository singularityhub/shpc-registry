---
layout: container
name:  "quay.io/biocontainers/r-exomedepth"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-exomedepth/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-exomedepth/container.yaml"
updated_at: "2023-08-24 02:52:53.508349"
latest: "1.1.16--r43hfb3cda0_3"
container_url: "https://biocontainers.pro/tools/r-exomedepth"

versions:
 - "1.1.15--r41h833e266_4"
 - "1.1.16--r41h833e266_0"
 - "1.1.16--r42hfb3cda0_2"
 - "1.1.16--r43hfb3cda0_3"
description: "shpc-registry automated BioContainers addition for r-exomedepth"
config: {"url": "https://biocontainers.pro/tools/r-exomedepth", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-exomedepth", "latest": {"1.1.16--r43hfb3cda0_3": "sha256:33a39c1cde9a14626a42738db867e5081b891c85571fc4b9d8e301dff828867f"}, "tags": {"1.1.15--r41h833e266_4": "sha256:f7334c772f7021dbb89c372c7ffaad7b942d9eb1c13dd845522f8811648ffaf9", "1.1.16--r41h833e266_0": "sha256:d54cb6d7fc94f45fd6c3ead257e51263f0f68a1997b67fd81338e97105fe82eb", "1.1.16--r42hfb3cda0_2": "sha256:1455140a848025c0a8ee77becdcd904fd8cce95b6656b0e138f079438f03acbb", "1.1.16--r43hfb3cda0_3": "sha256:33a39c1cde9a14626a42738db867e5081b891c85571fc4b9d8e301dff828867f"}, "docker": "quay.io/biocontainers/r-exomedepth"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-exomedepth.
shpc-registry automated BioContainers addition for r-exomedepth
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-exomedepth
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-exomedepth:1.1.16--r43hfb3cda0_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-exomedepth/1.1.16--r43hfb3cda0_3
$ module help quay.io/biocontainers/r-exomedepth/1.1.16--r43hfb3cda0_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-exomedepth-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-exomedepth-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-exomedepth-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-exomedepth-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-exomedepth-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-exomedepth-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-exomedepth

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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