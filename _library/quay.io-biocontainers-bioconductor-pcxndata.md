---
layout: container
name:  "quay.io/biocontainers/bioconductor-pcxndata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pcxndata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pcxndata/container.yaml"
updated_at: "2024-03-06 02:43:51.579315"
latest: "2.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pcxndata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_0"
 - "2.19.0--r42hdfd78af_0"
 - "2.16.0--r41hdfd78af_1"
 - "2.14.0--r41hdfd78af_0"
 - "2.12.0--r40hdfd78af_2"
 - "2.11.0--r40_0"
 - "2.22.0--r43hdfd78af_0"
 - "2.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pcxndata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pcxndata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pcxndata", "latest": {"2.24.0--r43hdfd78af_0": "sha256:7aab07617bd628a2c4144f76a76a46f4bb817026c79b1309d1b6a73a96838914"}, "tags": {"2.8.0--r36_0": "sha256:816352145f8c11c37242a3194b77924c9668940be6f2737a9021cb5c0d83a004", "2.19.0--r42hdfd78af_0": "sha256:259dd5c2b3f14b92fd462f8360843ef259d9c9ca25ce3b14be7eca6989bcd1ee", "2.16.0--r41hdfd78af_1": "sha256:6e845237e620c93f2df6256411d0f7f5b18055a23d6df21c6035231fae8f4666", "2.14.0--r41hdfd78af_0": "sha256:f1676f907e049d6a250537700c4edfcf7baac2d910332a448b1391b59c8a5244", "2.12.0--r40hdfd78af_2": "sha256:cd75cf8fdc219afb14d9b440c2f1552236b952fb5155d09727791739ae5173cc", "2.11.0--r40_0": "sha256:efaab3cd0443f92e4978dd7d6e804bbba43309e36b682f1ceba156586846bdd5", "2.22.0--r43hdfd78af_0": "sha256:ceced6d9388ff2f48d6ab7f0c9738aaf4f6aa7f6037ae3c3209fb669530b4a7e", "2.24.0--r43hdfd78af_0": "sha256:7aab07617bd628a2c4144f76a76a46f4bb817026c79b1309d1b6a73a96838914"}, "docker": "quay.io/biocontainers/bioconductor-pcxndata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pcxndata.
shpc-registry automated BioContainers addition for bioconductor-pcxndata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pcxndata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pcxndata:2.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pcxndata/2.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pcxndata/2.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pcxndata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcxndata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcxndata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pcxndata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pcxndata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pcxndata-inspect-deffile:

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