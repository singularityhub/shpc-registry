---
layout: container
name:  "quay.io/biocontainers/mashmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mashmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mashmap/container.yaml"
updated_at: "2023-09-04 03:02:53.124046"
latest: "3.0.6--h07ea13f_0"
container_url: "https://biocontainers.pro/tools/mashmap"
aliases:
 - "mashmap"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.0--pl5321h8e5b204_8"
 - "3.0.1--h97b747e_1"
 - "3.0.4--h97b747e_0"
 - "3.0.6--h07ea13f_0"
description: "shpc-registry automated BioContainers addition for mashmap"
config: {"url": "https://biocontainers.pro/tools/mashmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mashmap", "latest": {"3.0.6--h07ea13f_0": "sha256:f159f3c225feaece5159b1b8171e7f08a1cba4303340057f792bc17008332d28"}, "tags": {"2.0--pl5321h8e5b204_8": "sha256:6b6c744b535f172a9f5f0b6ce936cb8a125c2c81eadfe306e499a5e16cc96122", "3.0.1--h97b747e_1": "sha256:7c73ae6da33523ccf8945c9544a57717496b7fffe284c1d81a36ca785357d811", "3.0.4--h97b747e_0": "sha256:c19f20459f605d302be35213ffca02dc21b16f6469698bcb7e87af995d089a79", "3.0.6--h07ea13f_0": "sha256:f159f3c225feaece5159b1b8171e7f08a1cba4303340057f792bc17008332d28"}, "docker": "quay.io/biocontainers/mashmap", "aliases": {"mashmap": "/usr/local/bin/mashmap", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mashmap.
shpc-registry automated BioContainers addition for mashmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mashmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mashmap:3.0.6--h07ea13f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mashmap/3.0.6--h07ea13f_0
$ module help quay.io/biocontainers/mashmap/3.0.6--h07ea13f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mashmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mashmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mashmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mashmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mashmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mashmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mashmap

```bash
$ singularity exec <container> /usr/local/bin/mashmap
$ podman run --it --rm --entrypoint /usr/local/bin/mashmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mashmap   -v ${PWD} -w ${PWD} <container> -c " $@"
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