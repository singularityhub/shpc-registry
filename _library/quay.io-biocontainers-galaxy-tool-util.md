---
layout: container
name:  "quay.io/biocontainers/galaxy-tool-util"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/galaxy-tool-util/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/galaxy-tool-util/container.yaml"
updated_at: "2022-10-27 00:49:12.272153"
latest: "21.9.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/galaxy-tool-util"
aliases:
 - "cheetah"
 - "cheetah-analyze"
 - "cheetah-compile"
 - "mulled-list"
 - "mulled-update-singularity-containers"
versions:
 - "21.9.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for galaxy-tool-util"
config: {"url": "https://biocontainers.pro/tools/galaxy-tool-util", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for galaxy-tool-util", "latest": {"21.9.1--pyhdfd78af_0": "sha256:4e24f41bbc203613d67c8b938dfe447a84f18289ba0ddadfde82252bb5e529ad"}, "tags": {"21.9.1--pyhdfd78af_0": "sha256:4e24f41bbc203613d67c8b938dfe447a84f18289ba0ddadfde82252bb5e529ad"}, "docker": "quay.io/biocontainers/galaxy-tool-util", "aliases": {"cheetah": "/usr/local/bin/cheetah", "cheetah-analyze": "/usr/local/bin/cheetah-analyze", "cheetah-compile": "/usr/local/bin/cheetah-compile", "mulled-list": "/usr/local/bin/mulled-list", "mulled-update-singularity-containers": "/usr/local/bin/mulled-update-singularity-containers"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/galaxy-tool-util.
shpc-registry automated BioContainers addition for galaxy-tool-util
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/galaxy-tool-util
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/galaxy-tool-util:21.9.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/galaxy-tool-util/21.9.1--pyhdfd78af_0
$ module help quay.io/biocontainers/galaxy-tool-util/21.9.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### galaxy-tool-util-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### galaxy-tool-util-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### galaxy-tool-util-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### galaxy-tool-util-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### galaxy-tool-util-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### galaxy-tool-util-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cheetah

```bash
$ singularity exec <container> /usr/local/bin/cheetah
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-analyze

```bash
$ singularity exec <container> /usr/local/bin/cheetah-analyze
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-compile

```bash
$ singularity exec <container> /usr/local/bin/cheetah-compile
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-list

```bash
$ singularity exec <container> /usr/local/bin/mulled-list
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-update-singularity-containers

```bash
$ singularity exec <container> /usr/local/bin/mulled-update-singularity-containers
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-update-singularity-containers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-update-singularity-containers   -v ${PWD} -w ${PWD} <container> -c " $@"
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