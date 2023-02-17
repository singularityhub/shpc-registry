---
layout: container
name:  "quay.io/biocontainers/bioconductor-hiccompare"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hiccompare/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hiccompare/container.yaml"
updated_at: "2023-02-17 03:04:47.084610"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hiccompare"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.20.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hiccompare"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hiccompare", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hiccompare", "latest": {"1.20.0--r42hdfd78af_0": "sha256:808ceb517a2ee89749262e486ac99b967a74a04beb2e1417dbeea3e676ef33f2"}, "tags": {"1.8.0--r36_0": "sha256:6c993acbfa82672650843918e120e023a9f5ce2037dd58dd8ce09848da92541e", "1.16.0--r41hdfd78af_0": "sha256:24521c52588d7d49af326821df5931e22535e4710e95dceae9c9d621edfc4207", "1.14.0--r41hdfd78af_0": "sha256:3726e872f94cf5cb164ed2d3327bec00a6632afa308a65becf5cee8fc0d6836d", "1.12.0--r40hdfd78af_1": "sha256:6dfa720756eb163ddb8b6ad8d6667957edb2d8112ac51ff905298f1077f200ed", "1.10.0--r40_0": "sha256:92ca7dac8298b1beae8a601af081c6dc9ddd2c4f2b5e2c8caee8a3d3061605a4", "1.20.0--r42hdfd78af_0": "sha256:808ceb517a2ee89749262e486ac99b967a74a04beb2e1417dbeea3e676ef33f2"}, "docker": "quay.io/biocontainers/bioconductor-hiccompare", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hiccompare.
shpc-registry automated BioContainers addition for bioconductor-hiccompare
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hiccompare
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hiccompare:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hiccompare/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hiccompare/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hiccompare-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hiccompare-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hiccompare-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hiccompare-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hiccompare-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hiccompare-inspect-deffile:

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