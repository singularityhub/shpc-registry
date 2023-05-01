---
layout: container
name:  "quay.io/biocontainers/bioconductor-vulcandata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vulcandata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vulcandata/container.yaml"
updated_at: "2023-05-01 03:34:42.392898"
latest: "1.19.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-vulcandata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.19.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_1"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.11.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-vulcandata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vulcandata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vulcandata", "latest": {"1.19.0--r42hdfd78af_0": "sha256:bb3b03d201fb36ccc893189e43e64cd279eae0ccdd8632aef829a90c13bcac1a"}, "tags": {"1.8.0--r36_0": "sha256:86fda5b2e7f68ee250399689919209c425e82cc2834f187904e317fc1519563a", "1.19.0--r42hdfd78af_0": "sha256:bb3b03d201fb36ccc893189e43e64cd279eae0ccdd8632aef829a90c13bcac1a", "1.16.0--r41hdfd78af_1": "sha256:3dcc38f0efbbbee30351d5e4ecc44b822bcfb0b9d75258bb22d4948233d7f331", "1.14.0--r41hdfd78af_0": "sha256:9887042189d3c43ef0427e64cc2c525f823bea8dbc26b2db4ed2f9b99e4bd0c5", "1.12.0--r40hdfd78af_1": "sha256:753c9547e985a5fdf9c75fdd95b4414a401fd6ccdd2e784ca0a4ae654e29b3bc", "1.11.0--r40_0": "sha256:d6e6832c230be861162ec322f57bfafdee05429293b400f05f7b7e917fe9bb9b"}, "docker": "quay.io/biocontainers/bioconductor-vulcandata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vulcandata.
shpc-registry automated BioContainers addition for bioconductor-vulcandata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vulcandata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vulcandata:1.19.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vulcandata/1.19.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-vulcandata/1.19.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vulcandata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vulcandata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vulcandata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vulcandata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vulcandata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vulcandata-inspect-deffile:

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