---
layout: container
name:  "quay.io/biocontainers/cooltools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cooltools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cooltools/container.yaml"
updated_at: "2022-10-27 00:21:57.176855"
latest: "0.5.1--py37h37892f8_1"
container_url: "https://biocontainers.pro/tools/cooltools"
aliases:
 - "cooltools"
 - "tiff2fsspec"
versions:
 - "0.5.1--py37h37892f8_1"
description: "shpc-registry automated BioContainers addition for cooltools"
config: {"url": "https://biocontainers.pro/tools/cooltools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cooltools", "latest": {"0.5.1--py37h37892f8_1": "sha256:84794ab72277c275326b75ca7a62a0bb7ed7d7dab600ed470df14bb9a9db45a0"}, "tags": {"0.5.1--py37h37892f8_1": "sha256:84794ab72277c275326b75ca7a62a0bb7ed7d7dab600ed470df14bb9a9db45a0"}, "docker": "quay.io/biocontainers/cooltools", "aliases": {"cooltools": "/usr/local/bin/cooltools", "tiff2fsspec": "/usr/local/bin/tiff2fsspec"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cooltools.
shpc-registry automated BioContainers addition for cooltools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cooltools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cooltools:0.5.1--py37h37892f8_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cooltools/0.5.1--py37h37892f8_1
$ module help quay.io/biocontainers/cooltools/0.5.1--py37h37892f8_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cooltools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cooltools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cooltools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cooltools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cooltools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cooltools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cooltools

```bash
$ singularity exec <container> /usr/local/bin/cooltools
$ podman run --it --rm --entrypoint /usr/local/bin/cooltools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooltools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2fsspec

```bash
$ singularity exec <container> /usr/local/bin/tiff2fsspec
$ podman run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
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