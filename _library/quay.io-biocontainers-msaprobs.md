---
layout: container
name:  "quay.io/biocontainers/msaprobs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/msaprobs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/msaprobs/container.yaml"
updated_at: "2023-05-30 03:15:47.767532"
latest: "0.9.7--h43eeafb_3"
container_url: "https://biocontainers.pro/tools/msaprobs"
aliases:
 - "msaprobs"
versions:
 - "0.9.7--h5b5514e_1"
 - "0.9.7--h43eeafb_3"
description: "shpc-registry automated BioContainers addition for msaprobs"
config: {"url": "https://biocontainers.pro/tools/msaprobs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for msaprobs", "latest": {"0.9.7--h43eeafb_3": "sha256:755e7cf6a6f2216125c5a87c6c55ce36890e6daadc23b7af42361dffc90cd224"}, "tags": {"0.9.7--h5b5514e_1": "sha256:8ecc7d4da45d2cd04db6b5ec713f256d2f73634067ff50cd6cbe689117c6e707", "0.9.7--h43eeafb_3": "sha256:755e7cf6a6f2216125c5a87c6c55ce36890e6daadc23b7af42361dffc90cd224"}, "docker": "quay.io/biocontainers/msaprobs", "aliases": {"msaprobs": "/usr/local/bin/msaprobs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/msaprobs.
shpc-registry automated BioContainers addition for msaprobs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/msaprobs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/msaprobs:0.9.7--h43eeafb_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/msaprobs/0.9.7--h43eeafb_3
$ module help quay.io/biocontainers/msaprobs/0.9.7--h43eeafb_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### msaprobs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### msaprobs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### msaprobs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### msaprobs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### msaprobs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### msaprobs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### msaprobs

```bash
$ singularity exec <container> /usr/local/bin/msaprobs
$ podman run --it --rm --entrypoint /usr/local/bin/msaprobs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msaprobs   -v ${PWD} -w ${PWD} <container> -c " $@"
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