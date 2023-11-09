---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirbaseconverter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirbaseconverter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirbaseconverter/container.yaml"
updated_at: "2023-11-09 02:56:31.771945"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirbaseconverter"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirbaseconverter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirbaseconverter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirbaseconverter", "latest": {"1.24.0--r43hdfd78af_0": "sha256:a6a1cb98f83be20b145dab71ca72ec2115510bb3055e5cb9534ecd33b49a1137"}, "tags": {"1.8.0--r36_1": "sha256:156a194e76cc38a258fe798040efa8898413a4ab3380951f26d0e3d40f376739", "1.22.0--r42hdfd78af_0": "sha256:2ba2f859835a3e73100308c62fb18e66b640efbea6a627c3f7a265a9467047f4", "1.18.0--r41hdfd78af_0": "sha256:9943f007ab43b3a4061f3a27500ed2417a78994b67043e6d2c94482bb274d01e", "1.16.0--r41hdfd78af_0": "sha256:5e549a90d89bba47e394d4404a1c70e8e93e9c9af2154a37bd5316270125726d", "1.14.0--r40hdfd78af_1": "sha256:12bdef3306b1a97208e50595e6a113371a5a75bc26f5415db8482c9e6d85e911", "1.12.0--r40_0": "sha256:647b49fc76d1b5c10cfe6cf336810a7bb95d94bc8751e9b1006689e52de63125", "1.24.0--r43hdfd78af_0": "sha256:a6a1cb98f83be20b145dab71ca72ec2115510bb3055e5cb9534ecd33b49a1137"}, "docker": "quay.io/biocontainers/bioconductor-mirbaseconverter", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirbaseconverter.
shpc-registry automated BioContainers addition for bioconductor-mirbaseconverter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirbaseconverter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirbaseconverter:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirbaseconverter/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mirbaseconverter/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirbaseconverter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirbaseconverter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirbaseconverter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirbaseconverter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirbaseconverter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirbaseconverter-inspect-deffile:

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