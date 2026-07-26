---
layout: container
name:  "quay.io/biocontainers/r-variantstring"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-variantstring/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-variantstring/container.yaml"
updated_at: "2026-07-26 05:42:52.188162"
latest: "1.8.7--r45hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-variantstring"
aliases:
 - "psl"
 - "psl-make-dafsa"
 - "fc-genconf"
 - "hb-raster"
 - "hb-vector"
 - "x86_64-conda-linux-gnu.cfg"
 - "hb-info"
versions:
 - "1.8.7--r45hdfd78af_0"
description: "singularity registry hpc automated addition for r-variantstring"
config: {"url": "https://biocontainers.pro/tools/r-variantstring", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-variantstring", "latest": {"1.8.7--r45hdfd78af_0": "sha256:0a8177187682c2954e1de014528ce3419b8cdb53e801fa84f85bae852b692869"}, "tags": {"1.8.7--r45hdfd78af_0": "sha256:0a8177187682c2954e1de014528ce3419b8cdb53e801fa84f85bae852b692869"}, "docker": "quay.io/biocontainers/r-variantstring", "aliases": {"psl": "/usr/local/bin/psl", "psl-make-dafsa": "/usr/local/bin/psl-make-dafsa", "fc-genconf": "/usr/local/bin/fc-genconf", "hb-raster": "/usr/local/bin/hb-raster", "hb-vector": "/usr/local/bin/hb-vector", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "hb-info": "/usr/local/bin/hb-info"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-variantstring.
singularity registry hpc automated addition for r-variantstring
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-variantstring
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-variantstring:1.8.7--r45hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-variantstring/1.8.7--r45hdfd78af_0
$ module help quay.io/biocontainers/r-variantstring/1.8.7--r45hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-variantstring-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-variantstring-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-variantstring-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-variantstring-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-variantstring-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-variantstring-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### psl

```bash
$ singularity exec <container> /usr/local/bin/psl
$ podman run --it --rm --entrypoint /usr/local/bin/psl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl-make-dafsa

```bash
$ singularity exec <container> /usr/local/bin/psl-make-dafsa
$ podman run --it --rm --entrypoint /usr/local/bin/psl-make-dafsa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl-make-dafsa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-raster

```bash
$ singularity exec <container> /usr/local/bin/hb-raster
$ podman run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-vector

```bash
$ singularity exec <container> /usr/local/bin/hb-vector
$ podman run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
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