---
layout: container
name:  "quay.io/biocontainers/epa-ng"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/epa-ng/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/epa-ng/container.yaml"
updated_at: "2025-04-25 03:09:21.175919"
latest: "0.3.8--h077b44d_5"
container_url: "https://biocontainers.pro/tools/epa-ng"
aliases:
 - "epa-ng"
versions:
 - "0.3.8--hd03093a_2"
 - "0.3.8--hdcf5f25_4"
 - "0.3.8--h077b44d_5"
description: "shpc-registry automated BioContainers addition for epa-ng"
config: {"url": "https://biocontainers.pro/tools/epa-ng", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for epa-ng", "latest": {"0.3.8--h077b44d_5": "sha256:3ae79e85641239a35d85b5e54ded4393f635b47e0b28873a4fc5369f7b217154"}, "tags": {"0.3.8--hd03093a_2": "sha256:9e7a04e04cde0a2ae52646be7bacfdb846cd025a52c9edae304acbf7ea8f8539", "0.3.8--hdcf5f25_4": "sha256:53a5bae5754c49e746717ce91924ac21ed9853fb6f823fc17efb96a0c71c3634", "0.3.8--h077b44d_5": "sha256:3ae79e85641239a35d85b5e54ded4393f635b47e0b28873a4fc5369f7b217154"}, "docker": "quay.io/biocontainers/epa-ng", "aliases": {"epa-ng": "/usr/local/bin/epa-ng"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/epa-ng.
shpc-registry automated BioContainers addition for epa-ng
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/epa-ng
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/epa-ng:0.3.8--h077b44d_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/epa-ng/0.3.8--h077b44d_5
$ module help quay.io/biocontainers/epa-ng/0.3.8--h077b44d_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### epa-ng-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### epa-ng-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### epa-ng-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### epa-ng-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### epa-ng-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### epa-ng-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### epa-ng

```bash
$ singularity exec <container> /usr/local/bin/epa-ng
$ podman run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
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