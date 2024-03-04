---
layout: container
name:  "quay.io/biocontainers/takeabreak"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/takeabreak/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/takeabreak/container.yaml"
updated_at: "2024-03-04 03:21:35.421586"
latest: "1.1.2--h43eeafb_7"
container_url: "https://biocontainers.pro/tools/takeabreak"
aliases:
 - "TakeABreak"
versions:
 - "1.1.2--h5b5514e_5"
 - "1.1.2--h43eeafb_7"
description: "shpc-registry automated BioContainers addition for takeabreak"
config: {"url": "https://biocontainers.pro/tools/takeabreak", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for takeabreak", "latest": {"1.1.2--h43eeafb_7": "sha256:8f545eac7745e3b8e97e608b0f9595b6d265446fdd3add4d323a2787737ff334"}, "tags": {"1.1.2--h5b5514e_5": "sha256:0a73a3e9efabc85fda45e054b6c294cca979ef31311ed1d2b7cc5c8e1140e38e", "1.1.2--h43eeafb_7": "sha256:8f545eac7745e3b8e97e608b0f9595b6d265446fdd3add4d323a2787737ff334"}, "docker": "quay.io/biocontainers/takeabreak", "aliases": {"TakeABreak": "/usr/local/bin/TakeABreak"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/takeabreak.
shpc-registry automated BioContainers addition for takeabreak
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/takeabreak
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/takeabreak:1.1.2--h43eeafb_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/takeabreak/1.1.2--h43eeafb_7
$ module help quay.io/biocontainers/takeabreak/1.1.2--h43eeafb_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### takeabreak-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### takeabreak-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### takeabreak-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### takeabreak-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### takeabreak-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### takeabreak-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TakeABreak

```bash
$ singularity exec <container> /usr/local/bin/TakeABreak
$ podman run --it --rm --entrypoint /usr/local/bin/TakeABreak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TakeABreak   -v ${PWD} -w ${PWD} <container> -c " $@"
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