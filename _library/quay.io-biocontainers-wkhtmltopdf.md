---
layout: container
name:  "quay.io/biocontainers/wkhtmltopdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wkhtmltopdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/wkhtmltopdf/container.yaml"
updated_at: "2023-01-15 03:01:18.102034"
latest: "0.12.3--0"
container_url: "https://biocontainers.pro/tools/wkhtmltopdf"
aliases:
 - "wkhtmltoimage"
 - "wkhtmltopdf"
versions:
 - "0.12.3--0"
description: "shpc-registry automated BioContainers addition for wkhtmltopdf"
config: {"url": "https://biocontainers.pro/tools/wkhtmltopdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wkhtmltopdf", "latest": {"0.12.3--0": "sha256:f61cd4881d7bead97fc674f7a11b653b7066add46598c8e7fc446f81d95daebd"}, "tags": {"0.12.3--0": "sha256:f61cd4881d7bead97fc674f7a11b653b7066add46598c8e7fc446f81d95daebd"}, "docker": "quay.io/biocontainers/wkhtmltopdf", "aliases": {"wkhtmltoimage": "/usr/local/bin/wkhtmltoimage", "wkhtmltopdf": "/usr/local/bin/wkhtmltopdf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wkhtmltopdf.
shpc-registry automated BioContainers addition for wkhtmltopdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wkhtmltopdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wkhtmltopdf:0.12.3--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wkhtmltopdf/0.12.3--0
$ module help quay.io/biocontainers/wkhtmltopdf/0.12.3--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wkhtmltopdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wkhtmltopdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wkhtmltopdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wkhtmltopdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wkhtmltopdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wkhtmltopdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wkhtmltoimage

```bash
$ singularity exec <container> /usr/local/bin/wkhtmltoimage
$ podman run --it --rm --entrypoint /usr/local/bin/wkhtmltoimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wkhtmltoimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wkhtmltopdf

```bash
$ singularity exec <container> /usr/local/bin/wkhtmltopdf
$ podman run --it --rm --entrypoint /usr/local/bin/wkhtmltopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wkhtmltopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
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