---
layout: container
name:  "quay.io/biocontainers/contrafold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/contrafold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/contrafold/container.yaml"
updated_at: "2023-07-06 03:12:32.273525"
latest: "2.02--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/contrafold"
aliases:
 - "contrafold"
 - "score_prediction"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.02--h9f5acd7_1"
 - "2.02--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for contrafold"
config: {"url": "https://biocontainers.pro/tools/contrafold", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for contrafold", "latest": {"2.02--h4ac6f70_3": "sha256:ac7783d6f69169a24310b6b679d4a00d95148c1f3f8ec7589425c4a4c00b21e4"}, "tags": {"2.02--h9f5acd7_1": "sha256:5bcefef7adfe3c3517f092bfa9ca4fcab9e3fc099dba56e35bac24d1975c2eea", "2.02--h4ac6f70_3": "sha256:ac7783d6f69169a24310b6b679d4a00d95148c1f3f8ec7589425c4a4c00b21e4"}, "docker": "quay.io/biocontainers/contrafold", "aliases": {"contrafold": "/usr/local/bin/contrafold", "score_prediction": "/usr/local/bin/score_prediction", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/contrafold.
shpc-registry automated BioContainers addition for contrafold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/contrafold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/contrafold:2.02--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/contrafold/2.02--h4ac6f70_3
$ module help quay.io/biocontainers/contrafold/2.02--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### contrafold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### contrafold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### contrafold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### contrafold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### contrafold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### contrafold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### contrafold

```bash
$ singularity exec <container> /usr/local/bin/contrafold
$ podman run --it --rm --entrypoint /usr/local/bin/contrafold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contrafold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### score_prediction

```bash
$ singularity exec <container> /usr/local/bin/score_prediction
$ podman run --it --rm --entrypoint /usr/local/bin/score_prediction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/score_prediction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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