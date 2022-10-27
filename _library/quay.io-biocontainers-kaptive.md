---
layout: container
name:  "quay.io/biocontainers/kaptive"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kaptive/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/kaptive/container.yaml"
updated_at: "2022-10-27 01:15:42.259903"
latest: "0.7.3--py_0"
container_url: "https://biocontainers.pro/tools/kaptive"
aliases:
 - ".kaptive-post-link.sh"
 - "kaptive.py"
versions:
 - "0.7.3--py_0"
description: "shpc-registry automated BioContainers addition for kaptive"
config: {"url": "https://biocontainers.pro/tools/kaptive", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kaptive", "latest": {"0.7.3--py_0": "sha256:0341c20825209a66d5897ab27378824d1ad11258e5a982a5216a120604746b62"}, "tags": {"0.7.3--py_0": "sha256:0341c20825209a66d5897ab27378824d1ad11258e5a982a5216a120604746b62"}, "docker": "quay.io/biocontainers/kaptive", "aliases": {".kaptive-post-link.sh": "/usr/local/bin/.kaptive-post-link.sh", "kaptive.py": "/usr/local/bin/kaptive.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kaptive.
shpc-registry automated BioContainers addition for kaptive
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kaptive
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kaptive:0.7.3--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kaptive/0.7.3--py_0
$ module help quay.io/biocontainers/kaptive/0.7.3--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kaptive-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kaptive-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kaptive-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kaptive-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kaptive-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kaptive-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .kaptive-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.kaptive-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.kaptive-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.kaptive-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaptive.py

```bash
$ singularity exec <container> /usr/local/bin/kaptive.py
$ podman run --it --rm --entrypoint /usr/local/bin/kaptive.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaptive.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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