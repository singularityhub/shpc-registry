---
layout: container
name:  "quay.io/biocontainers/phylorank"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylorank/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/phylorank/container.yaml"
updated_at: "2022-10-29 05:53:02.049931"
latest: "0.1.9--py_0"
container_url: "https://biocontainers.pro/tools/phylorank"
aliases:
 - "phylorank"
 - "2to3-3.9"
 - "dendropy-format"
 - "f2py3.9"
 - "futurize"
 - "idle3.9"
 - "jpgicc"
 - "linkicc"
 - "pasteurize"
 - "psicc"
 - "pydoc3.9"
versions:
 - "0.1.9--py_0"
description: "shpc-registry automated BioContainers addition for phylorank"
config: {"url": "https://biocontainers.pro/tools/phylorank", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylorank", "latest": {"0.1.9--py_0": "sha256:d3700b258a02cd4c7421e4cd0a8cf80b7ca71a4a81abfa6e210dfd6e3ccbba98"}, "tags": {"0.1.9--py_0": "sha256:d3700b258a02cd4c7421e4cd0a8cf80b7ca71a4a81abfa6e210dfd6e3ccbba98"}, "docker": "quay.io/biocontainers/phylorank", "aliases": {"phylorank": "/usr/local/bin/phylorank", "2to3-3.9": "/usr/local/bin/2to3-3.9", "dendropy-format": "/usr/local/bin/dendropy-format", "f2py3.9": "/usr/local/bin/f2py3.9", "futurize": "/usr/local/bin/futurize", "idle3.9": "/usr/local/bin/idle3.9", "jpgicc": "/usr/local/bin/jpgicc", "linkicc": "/usr/local/bin/linkicc", "pasteurize": "/usr/local/bin/pasteurize", "psicc": "/usr/local/bin/psicc", "pydoc3.9": "/usr/local/bin/pydoc3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylorank.
shpc-registry automated BioContainers addition for phylorank
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylorank
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylorank:0.1.9--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylorank/0.1.9--py_0
$ module help quay.io/biocontainers/phylorank/0.1.9--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylorank-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylorank-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylorank-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylorank-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylorank-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylorank-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### phylorank

```bash
$ singularity exec <container> /usr/local/bin/phylorank
$ podman run --it --rm --entrypoint /usr/local/bin/phylorank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylorank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpgicc

```bash
$ singularity exec <container> /usr/local/bin/jpgicc
$ podman run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linkicc

```bash
$ singularity exec <container> /usr/local/bin/linkicc
$ podman run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psicc

```bash
$ singularity exec <container> /usr/local/bin/psicc
$ podman run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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