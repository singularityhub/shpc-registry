---
layout: container
name:  "quay.io/biocontainers/stringmlst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stringmlst/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/stringmlst/container.yaml"
updated_at: "2022-10-27 01:10:11.146671"
latest: "0.6.3--py_0"
container_url: "https://biocontainers.pro/tools/stringmlst"
aliases:
 - "perl5.30.3"
 - "stringMLST.py"
versions:
 - "0.6.3--py_0"
description: "shpc-registry automated BioContainers addition for stringmlst"
config: {"url": "https://biocontainers.pro/tools/stringmlst", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stringmlst", "latest": {"0.6.3--py_0": "sha256:47e6a52580fa521f520d0cd9449a1af6fbc25b3df49b954a125f6dad3e0c2a4b"}, "tags": {"0.6.3--py_0": "sha256:47e6a52580fa521f520d0cd9449a1af6fbc25b3df49b954a125f6dad3e0c2a4b"}, "docker": "quay.io/biocontainers/stringmlst", "aliases": {"perl5.30.3": "/usr/local/bin/perl5.30.3", "stringMLST.py": "/usr/local/bin/stringMLST.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stringmlst.
shpc-registry automated BioContainers addition for stringmlst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stringmlst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stringmlst:0.6.3--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stringmlst/0.6.3--py_0
$ module help quay.io/biocontainers/stringmlst/0.6.3--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stringmlst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stringmlst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stringmlst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stringmlst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stringmlst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stringmlst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.30.3

```bash
$ singularity exec <container> /usr/local/bin/perl5.30.3
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.30.3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.30.3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stringMLST.py

```bash
$ singularity exec <container> /usr/local/bin/stringMLST.py
$ podman run --it --rm --entrypoint /usr/local/bin/stringMLST.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stringMLST.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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