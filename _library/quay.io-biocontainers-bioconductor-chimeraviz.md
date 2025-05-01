---
layout: container
name:  "quay.io/biocontainers/bioconductor-chimeraviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chimeraviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chimeraviz/container.yaml"
updated_at: "2025-05-01 07:25:42.693382"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chimeraviz"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.1--r40hdfd78af_0"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chimeraviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chimeraviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chimeraviz", "latest": {"1.32.0--r44hdfd78af_0": "sha256:540524ef6aec296b7162093ab4c959eb217ad3081e673b11083ff993a0948467"}, "tags": {"1.8.0--r351_0": "sha256:09ad0047befe251c71fbd6cfdf0514bf29e293ba870680348fa3861ec7c17bb1", "1.20.0--r41hdfd78af_0": "sha256:aaf3a820ed47195b8544df481e1391b3c7ccc82f14c81b72844ecab9d1fb2417", "1.18.0--r41hdfd78af_0": "sha256:b118277231fd1f7b18737ebc1dd5efa46459bb0c45f15dac0e5226da52fa5463", "1.16.1--r40hdfd78af_0": "sha256:c19120252c215fcf72f22997b3e36e8917a057292e42980ada7d854d4665a840", "1.14.0--r40_0": "sha256:3dbbf6e6b38b0424816b74e55bbda5578080d5a3ce936a89736df526185059c6", "1.12.0--r36_0": "sha256:850e5fd347c6316901949290623a411499c3aa741fe7696d6b99e4f8e137de31", "1.24.0--r42hdfd78af_0": "sha256:359e1840fe0668c948229cd8be41aa25cd1470a4bef787a30449beec98be33da", "1.26.0--r43hdfd78af_0": "sha256:504a0a3e0298a69ad2749d058cfa69b4e5a9787df889e8ac6834255702fdcb71", "1.28.0--r43hdfd78af_0": "sha256:e8494d66f65921493212e99c0f2cad55f76d1044048f549cba0d3fed8e0e58f9", "1.32.0--r44hdfd78af_0": "sha256:540524ef6aec296b7162093ab4c959eb217ad3081e673b11083ff993a0948467"}, "docker": "quay.io/biocontainers/bioconductor-chimeraviz", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chimeraviz.
shpc-registry automated BioContainers addition for bioconductor-chimeraviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chimeraviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chimeraviz:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chimeraviz/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chimeraviz/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chimeraviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chimeraviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chimeraviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chimeraviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chimeraviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chimeraviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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