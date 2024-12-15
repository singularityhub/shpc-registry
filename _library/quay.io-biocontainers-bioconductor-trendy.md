---
layout: container
name:  "quay.io/biocontainers/bioconductor-trendy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-trendy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-trendy/container.yaml"
updated_at: "2024-12-15 04:48:25.511840"
latest: "1.24.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-trendy"
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
 - "1.22.0--r43hdfd78af_0"
 - "1.24.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-trendy"
config: {"url": "https://biocontainers.pro/tools/bioconductor-trendy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-trendy", "latest": {"1.24.1--r43hdfd78af_0": "sha256:79a15585018e36b3e45fe9536c1c2555c3f3a52fd22860463524accdfec21625"}, "tags": {"1.8.0--r36_0": "sha256:9174307b6f00993cf0eb70c483f1f93c363a6a066a9bed57e30597b24f41867c", "1.16.0--r41hdfd78af_0": "sha256:d672a5bf58b460d75db111ee789e36d7421ab31a7025da88fda1e5c402dd54d3", "1.14.0--r41hdfd78af_0": "sha256:467a07f245001a51d8980d915d3a999a7714c44bd035c20e4dfa6589467e578e", "1.12.0--r40hdfd78af_1": "sha256:51ce4863c06411acdcd7fe3319f7bfcd9d64bc8948a45b8a88eae221bfdce5b4", "1.10.0--r40_0": "sha256:5c9dbcb4833994061564cc1dbac93fc8b35669fc36f92027d96b2b80bf29a679", "1.20.0--r42hdfd78af_0": "sha256:33ff81f27f354130efa8bcce26a43dcd94301bc7afede7c9d344ba354bdee726", "1.22.0--r43hdfd78af_0": "sha256:ac6d5512418eb9b118d41143090520570956e781df6e9a3afa3443f01325c673", "1.24.1--r43hdfd78af_0": "sha256:79a15585018e36b3e45fe9536c1c2555c3f3a52fd22860463524accdfec21625"}, "docker": "quay.io/biocontainers/bioconductor-trendy", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-trendy.
shpc-registry automated BioContainers addition for bioconductor-trendy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-trendy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-trendy:1.24.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-trendy/1.24.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-trendy/1.24.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-trendy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trendy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trendy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-trendy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-trendy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-trendy-inspect-deffile:

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