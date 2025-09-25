---
layout: container
name:  "quay.io/biocontainers/bioconductor-adverscarial"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-adverscarial/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-adverscarial/container.yaml"
updated_at: "2025-09-25 07:37:55.394934"
latest: "1.4.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-adverscarial"
aliases:
 - "pcre2posix_test"
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.0--r43hdfd78af_0"
 - "1.4.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-adverscarial"
config: {"url": "https://biocontainers.pro/tools/bioconductor-adverscarial", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-adverscarial", "latest": {"1.4.0--r44hdfd78af_0": "sha256:5976bd494d368795b8d495527a4b1e1c84b5308e6479c02381b32afc9d3df186"}, "tags": {"1.0.0--r43hdfd78af_0": "sha256:490759fecb9b35f935657b4209de912fa527ebd1a5ea950c80dadc2d7eca4e05", "1.4.0--r44hdfd78af_0": "sha256:5976bd494d368795b8d495527a4b1e1c84b5308e6479c02381b32afc9d3df186"}, "docker": "quay.io/biocontainers/bioconductor-adverscarial", "aliases": {"pcre2posix_test": "/usr/local/bin/pcre2posix_test", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-adverscarial.
singularity registry hpc automated addition for bioconductor-adverscarial
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-adverscarial
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-adverscarial:1.4.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-adverscarial/1.4.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-adverscarial/1.4.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-adverscarial-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adverscarial-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adverscarial-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-adverscarial-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-adverscarial-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-adverscarial-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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