---
layout: container
name:  "quay.io/biocontainers/export2graphlan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/export2graphlan/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/export2graphlan/container.yaml"
updated_at: "2022-10-27 00:51:10.532667"
latest: "0.22--py_0"
container_url: "https://biocontainers.pro/tools/export2graphlan"
aliases:
 - "export2graphlan.py"
 - "hclust2.py"
versions:
 - "0.22--py_0"
description: "shpc-registry automated BioContainers addition for export2graphlan"
config: {"url": "https://biocontainers.pro/tools/export2graphlan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for export2graphlan", "latest": {"0.22--py_0": "sha256:ff6e1a0ae7e114485b0c66aaa0f612b4b9c6677ce0465d37bc0ea7b8ed3cbc31"}, "tags": {"0.22--py_0": "sha256:ff6e1a0ae7e114485b0c66aaa0f612b4b9c6677ce0465d37bc0ea7b8ed3cbc31"}, "docker": "quay.io/biocontainers/export2graphlan", "aliases": {"export2graphlan.py": "/usr/local/bin/export2graphlan.py", "hclust2.py": "/usr/local/bin/hclust2.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/export2graphlan.
shpc-registry automated BioContainers addition for export2graphlan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/export2graphlan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/export2graphlan:0.22--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/export2graphlan/0.22--py_0
$ module help quay.io/biocontainers/export2graphlan/0.22--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### export2graphlan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### export2graphlan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### export2graphlan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### export2graphlan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### export2graphlan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### export2graphlan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### export2graphlan.py

```bash
$ singularity exec <container> /usr/local/bin/export2graphlan.py
$ podman run --it --rm --entrypoint /usr/local/bin/export2graphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2graphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hclust2.py

```bash
$ singularity exec <container> /usr/local/bin/hclust2.py
$ podman run --it --rm --entrypoint /usr/local/bin/hclust2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hclust2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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