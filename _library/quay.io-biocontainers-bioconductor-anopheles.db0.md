---
layout: container
name:  "quay.io/biocontainers/bioconductor-anopheles.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-anopheles.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-anopheles.db0/container.yaml"
updated_at: "2025-10-30 03:30:20.885909"
latest: "3.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-anopheles.db0"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.2--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
 - "3.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-anopheles.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-anopheles.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-anopheles.db0", "latest": {"3.20.0--r44hdfd78af_0": "sha256:e7cfc8bcae7c5bfcd9e5ca7ed352371cfbe2bb6173401e34cbace700802f0120"}, "tags": {"3.8.2--r36_1": "sha256:5369b49c5564c74777ad616f7db8c953a10270d631b26cbea0b1b9feae858f63", "3.16.0--r42hdfd78af_0": "sha256:c545973d839814b0b9af09a1fcafbb1359bea0ba2155886290bf81da1f48f1fb", "3.14.0--r41hdfd78af_1": "sha256:b2a034ca5afdbc1d76d055ffbd24364b825c569431031eff3e428edac8304917", "3.13.0--r41hdfd78af_0": "sha256:c68df037f5151face9fce9c3f1464bdc97308aa7edfb2cfe95d3bffe74013344", "3.12.0--r40hdfd78af_1": "sha256:d384877709364d5625dc822cf5b8e9360a4f5471594ee938430a9594622e330c", "3.11.2--r40_0": "sha256:8bc79228e66960d951ce42c13daaecc86dfde57e31739f35c0e3ab917f0839d9", "3.17.0--r43hdfd78af_0": "sha256:c1c388baca3811d7d3c4e5dcb884c380c7470dc54925cfd0b1d58cc645902e09", "3.18.0--r43hdfd78af_0": "sha256:6ba52bac3ed242f2e304ccf774ca654cb9b04959ee9b7d3dc892b65d87ad3827", "3.20.0--r44hdfd78af_0": "sha256:e7cfc8bcae7c5bfcd9e5ca7ed352371cfbe2bb6173401e34cbace700802f0120"}, "docker": "quay.io/biocontainers/bioconductor-anopheles.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-anopheles.db0.
shpc-registry automated BioContainers addition for bioconductor-anopheles.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-anopheles.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-anopheles.db0:3.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-anopheles.db0/3.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-anopheles.db0/3.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-anopheles.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anopheles.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anopheles.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-anopheles.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-anopheles.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-anopheles.db0-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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