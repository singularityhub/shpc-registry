---
layout: container
name:  "quay.io/biocontainers/zpca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/zpca/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/zpca/container.yaml"
updated_at: "2022-10-27 01:08:49.840159"
latest: "0.8.3.post1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/zpca"
aliases:
 - "zpca-counts"
 - "zpca-tpm"
versions:
 - "0.8.3.post1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for zpca"
config: {"url": "https://biocontainers.pro/tools/zpca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for zpca", "latest": {"0.8.3.post1--pyh5e36f6f_0": "sha256:15ec36ef4aa7fab944b5ef421782fb499d92fdf0e36f175a56828c4ed66d8cfd"}, "tags": {"0.8.3.post1--pyh5e36f6f_0": "sha256:15ec36ef4aa7fab944b5ef421782fb499d92fdf0e36f175a56828c4ed66d8cfd"}, "docker": "quay.io/biocontainers/zpca", "aliases": {"zpca-counts": "/usr/local/bin/zpca-counts", "zpca-tpm": "/usr/local/bin/zpca-tpm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/zpca.
shpc-registry automated BioContainers addition for zpca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/zpca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/zpca:0.8.3.post1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/zpca/0.8.3.post1--pyh5e36f6f_0
$ module help quay.io/biocontainers/zpca/0.8.3.post1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### zpca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### zpca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### zpca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### zpca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### zpca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### zpca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### zpca-counts

```bash
$ singularity exec <container> /usr/local/bin/zpca-counts
$ podman run --it --rm --entrypoint /usr/local/bin/zpca-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zpca-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zpca-tpm

```bash
$ singularity exec <container> /usr/local/bin/zpca-tpm
$ podman run --it --rm --entrypoint /usr/local/bin/zpca-tpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zpca-tpm   -v ${PWD} -w ${PWD} <container> -c " $@"
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