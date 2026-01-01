---
layout: container
name:  "quay.io/biocontainers/bioconductor-metavizr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metavizr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metavizr/container.yaml"
updated_at: "2026-01-01 07:15:50.258765"
latest: "1.21.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metavizr"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.15.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.21.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metavizr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metavizr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metavizr", "latest": {"1.21.0--r42hdfd78af_0": "sha256:58e42fdcb76ec12485856cd100f9d943dff9efbc005ed8220cc43fde58c24300"}, "tags": {"1.8.0--r36_1": "sha256:332aabc980ab586b5a4e070cca73eaabe94e89de80fbd7490f9a8a27d9d2eaf5", "1.18.0--r41hdfd78af_0": "sha256:af963eb77744f203d48cf257a506428c94b0e2efe00b1a69f852fe89568891ca", "1.15.0--r41hdfd78af_0": "sha256:ff5103d28c71af1d80898e4e3355871e7a5dbf7184536d080f51613546694a58", "1.14.0--r40hdfd78af_1": "sha256:c62a86e61bb9d328af7209ef0b5841ab2d792320cdbf4404f8f6b0f16621a50f", "1.12.0--r40_0": "sha256:62ad689b2d41d29e8645b99f3da6433a705ed6b1e352044a8c2bab750765ecea", "1.10.0--r36_0": "sha256:b2512104eee030678a586c6411c0b119b93ef6247ed25373d769e6711754b0b8", "1.21.0--r42hdfd78af_0": "sha256:58e42fdcb76ec12485856cd100f9d943dff9efbc005ed8220cc43fde58c24300"}, "docker": "quay.io/biocontainers/bioconductor-metavizr", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metavizr.
shpc-registry automated BioContainers addition for bioconductor-metavizr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metavizr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metavizr:1.21.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metavizr/1.21.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metavizr/1.21.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metavizr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metavizr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metavizr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metavizr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metavizr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metavizr-inspect-deffile:

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