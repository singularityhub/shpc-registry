---
layout: container
name:  "quay.io/biocontainers/xmlstarlet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xmlstarlet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xmlstarlet/container.yaml"
updated_at: "2024-12-15 04:39:36.154465"
latest: "1.6.1"
container_url: "https://biocontainers.pro/tools/xmlstarlet"
aliases:
 - "xml"
 - "xslt-config"
 - "xsltproc"
versions:
 - "1.6.1"
description: "shpc-registry automated BioContainers addition for xmlstarlet"
config: {"url": "https://biocontainers.pro/tools/xmlstarlet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xmlstarlet", "latest": {"1.6.1": "sha256:c07c380a5b1a7a469186d8bc088e9520ab8e2af23531135ecf17d705d90fac9d"}, "tags": {"1.6.1": "sha256:c07c380a5b1a7a469186d8bc088e9520ab8e2af23531135ecf17d705d90fac9d"}, "docker": "quay.io/biocontainers/xmlstarlet", "aliases": {"xml": "/usr/local/bin/xml", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xmlstarlet.
shpc-registry automated BioContainers addition for xmlstarlet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xmlstarlet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xmlstarlet:1.6.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xmlstarlet/1.6.1
$ module help quay.io/biocontainers/xmlstarlet/1.6.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xmlstarlet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xmlstarlet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xmlstarlet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xmlstarlet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xmlstarlet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xmlstarlet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xml

```bash
$ singularity exec <container> /usr/local/bin/xml
$ podman run --it --rm --entrypoint /usr/local/bin/xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
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