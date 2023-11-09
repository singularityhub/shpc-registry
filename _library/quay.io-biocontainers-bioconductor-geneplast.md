---
layout: container
name:  "quay.io/biocontainers/bioconductor-geneplast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geneplast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geneplast/container.yaml"
updated_at: "2023-11-09 02:24:38.355968"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geneplast"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geneplast"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geneplast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geneplast", "latest": {"1.26.0--r43hdfd78af_0": "sha256:35934e5e9cef85cc0dcd970c71fd07f10d100c749acbee95fc11da96b16dfc3c"}, "tags": {"1.8.0--r351_0": "sha256:c8ebd52e1b89a9e4b739eb5efd97dcd73426bd9924f8c056d19ca6661802a6b9", "1.24.0--r42hdfd78af_0": "sha256:fc0f197c6463bb32e1946ebc8fc091267f61814f3fc56424476dfc1c34f682f4", "1.20.0--r41hdfd78af_0": "sha256:26812ca942b8cbf5f7d29902e74afeaa54a7b8dd4b82592f615b27b679441d8e", "1.18.0--r41hdfd78af_0": "sha256:b364123bfb7946e29f866df6097c973b1cffacf83ad924f35190f8e8be323e55", "1.16.0--r40hdfd78af_1": "sha256:a8021f4178e34ffa0307b427077b314fae0164c6c537be3bdfb465ea6484bbfe", "1.14.0--r40_0": "sha256:d7272e1315ec220e44ff4265060fc04b41757223c89c0478077a02e115314f58", "1.26.0--r43hdfd78af_0": "sha256:35934e5e9cef85cc0dcd970c71fd07f10d100c749acbee95fc11da96b16dfc3c"}, "docker": "quay.io/biocontainers/bioconductor-geneplast", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geneplast.
shpc-registry automated BioContainers addition for bioconductor-geneplast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geneplast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geneplast:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geneplast/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geneplast/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geneplast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneplast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneplast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geneplast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geneplast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geneplast-inspect-deffile:

```bash
$ singularity inspect -d <container>
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