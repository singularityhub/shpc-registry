---
layout: container
name:  "quay.io/biocontainers/aplanat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aplanat/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/aplanat/container.yaml"
updated_at: "2022-10-27 00:20:10.834655"
latest: "0.5.6--pyhfa5458b_0"
container_url: "https://biocontainers.pro/tools/aplanat"
aliases:
 - "aplanat"
 - "font-awesome-to-png"
 - "icon-font-to-png"
versions:
 - "0.5.6--pyhfa5458b_0"
description: "shpc-registry automated BioContainers addition for aplanat"
config: {"url": "https://biocontainers.pro/tools/aplanat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aplanat", "latest": {"0.5.6--pyhfa5458b_0": "sha256:552b0c20fa2f4c421661559e79af69a3a23e79550a4f6f650b4dba01b9cacfa7"}, "tags": {"0.5.6--pyhfa5458b_0": "sha256:552b0c20fa2f4c421661559e79af69a3a23e79550a4f6f650b4dba01b9cacfa7"}, "docker": "quay.io/biocontainers/aplanat", "aliases": {"aplanat": "/usr/local/bin/aplanat", "font-awesome-to-png": "/usr/local/bin/font-awesome-to-png", "icon-font-to-png": "/usr/local/bin/icon-font-to-png"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aplanat.
shpc-registry automated BioContainers addition for aplanat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aplanat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aplanat:0.5.6--pyhfa5458b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aplanat/0.5.6--pyhfa5458b_0
$ module help quay.io/biocontainers/aplanat/0.5.6--pyhfa5458b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aplanat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aplanat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aplanat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aplanat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aplanat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aplanat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aplanat

```bash
$ singularity exec <container> /usr/local/bin/aplanat
$ podman run --it --rm --entrypoint /usr/local/bin/aplanat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aplanat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### font-awesome-to-png

```bash
$ singularity exec <container> /usr/local/bin/font-awesome-to-png
$ podman run --it --rm --entrypoint /usr/local/bin/font-awesome-to-png   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/font-awesome-to-png   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### icon-font-to-png

```bash
$ singularity exec <container> /usr/local/bin/icon-font-to-png
$ podman run --it --rm --entrypoint /usr/local/bin/icon-font-to-png   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/icon-font-to-png   -v ${PWD} -w ${PWD} <container> -c " $@"
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