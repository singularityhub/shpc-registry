---
layout: container
name:  "quay.io/biocontainers/bioconductor-repviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-repviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-repviz/container.yaml"
updated_at: "2025-07-28 09:25:03.358239"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-repviz"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-repviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-repviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-repviz", "latest": {"1.22.0--r44hdfd78af_0": "sha256:847c83eecfe473574ff455f3275bd6c17159c1c023433d1ce2de49424704bda5"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:efa1d56959e527df15354f9eac7f58588cd87b751ae88527eaafbe0f2b6d45cc", "1.10.0--r41hdfd78af_0": "sha256:9b33cc8f50d5d0e6847ee0f05f96e20f7b323996e5f75e726a006f1e71dc8fc2", "1.14.0--r42hdfd78af_0": "sha256:6836797459f627ae98edece49b1890cb185a0f8e1d0dbe2272ee49983ceb72b1", "1.16.0--r43hdfd78af_0": "sha256:988d076e8ce25a6409d1df2d5dae1c1086fc15bfc76dfc00bce6acef96092b4e", "1.18.0--r43hdfd78af_0": "sha256:d97d183ddb58803eb592103df7c0415e35db992f34c9db2fa0937dda9a229eb9", "1.22.0--r44hdfd78af_0": "sha256:847c83eecfe473574ff455f3275bd6c17159c1c023433d1ce2de49424704bda5"}, "docker": "quay.io/biocontainers/bioconductor-repviz", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-repviz.
shpc-registry automated BioContainers addition for bioconductor-repviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-repviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-repviz:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-repviz/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-repviz/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-repviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-repviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-repviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-repviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-repviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-repviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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