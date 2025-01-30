---
layout: container
name:  "quay.io/biocontainers/r-dwls"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-dwls/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-dwls/container.yaml"
updated_at: "2025-01-30 03:33:29.867115"
latest: "1.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/r-dwls"
aliases:
 - "geosop"
 - "geos-config"
 - "glpsol"
versions:
 - "1.0--r41hdfd78af_2"
 - "1.0--r42hdfd78af_3"
 - "1.0--r43hdfd78af_4"
 - "1.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for r-dwls"
config: {"url": "https://biocontainers.pro/tools/r-dwls", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-dwls", "latest": {"1.0--r44hdfd78af_5": "sha256:4fcfaba4734a44ba888a09b9239761536c016925945f913e8c2907aaace3496a"}, "tags": {"1.0--r41hdfd78af_2": "sha256:b62baa2490dbdb8487f90c2e730aaea8252f76ad183e8e3379381a3c1b6d720c", "1.0--r42hdfd78af_3": "sha256:f752833545af82404231147f9719c2594954e0f2c607913cec711fdf9273dbbc", "1.0--r43hdfd78af_4": "sha256:0746b97426dbbbcb19bafe75ffddc748ee88e30dc3a4f364223e5325976ddef8", "1.0--r44hdfd78af_5": "sha256:4fcfaba4734a44ba888a09b9239761536c016925945f913e8c2907aaace3496a"}, "docker": "quay.io/biocontainers/r-dwls", "aliases": {"geosop": "/usr/local/bin/geosop", "geos-config": "/usr/local/bin/geos-config", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-dwls.
shpc-registry automated BioContainers addition for r-dwls
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-dwls
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-dwls:1.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-dwls/1.0--r44hdfd78af_5
$ module help quay.io/biocontainers/r-dwls/1.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-dwls-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-dwls-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-dwls-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-dwls-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-dwls-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-dwls-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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