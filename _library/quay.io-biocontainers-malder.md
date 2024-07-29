---
layout: container
name:  "quay.io/biocontainers/malder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/malder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/malder/container.yaml"
updated_at: "2024-07-29 02:39:14.396833"
latest: "1.0.1e83d4e--h66ff86e_7"
container_url: "https://biocontainers.pro/tools/malder"
aliases:
 - "malder"
 - "fftw-wisdom"
 - "fftw-wisdom-to-conf"
 - "fftwf-wisdom"
 - "fftwl-wisdom"
versions:
 - "1.0.1e83d4e--h56c1e55_5"
 - "1.0.1e83d4e--h66ff86e_7"
description: "shpc-registry automated BioContainers addition for malder"
config: {"url": "https://biocontainers.pro/tools/malder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for malder", "latest": {"1.0.1e83d4e--h66ff86e_7": "sha256:2746fe1d8fec4175438d1c24578dc90008b7f3a3879eeb7ed54a32512c940162"}, "tags": {"1.0.1e83d4e--h56c1e55_5": "sha256:79416269a3002d178e735a65d454a49539be5953b80e75b4398c4cf942442c85", "1.0.1e83d4e--h66ff86e_7": "sha256:2746fe1d8fec4175438d1c24578dc90008b7f3a3879eeb7ed54a32512c940162"}, "docker": "quay.io/biocontainers/malder", "aliases": {"malder": "/usr/local/bin/malder", "fftw-wisdom": "/usr/local/bin/fftw-wisdom", "fftw-wisdom-to-conf": "/usr/local/bin/fftw-wisdom-to-conf", "fftwf-wisdom": "/usr/local/bin/fftwf-wisdom", "fftwl-wisdom": "/usr/local/bin/fftwl-wisdom"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/malder.
shpc-registry automated BioContainers addition for malder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/malder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/malder:1.0.1e83d4e--h66ff86e_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/malder/1.0.1e83d4e--h66ff86e_7
$ module help quay.io/biocontainers/malder/1.0.1e83d4e--h66ff86e_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### malder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### malder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### malder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### malder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### malder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### malder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### malder

```bash
$ singularity exec <container> /usr/local/bin/malder
$ podman run --it --rm --entrypoint /usr/local/bin/malder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/malder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftw-wisdom

```bash
$ singularity exec <container> /usr/local/bin/fftw-wisdom
$ podman run --it --rm --entrypoint /usr/local/bin/fftw-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftw-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftw-wisdom-to-conf

```bash
$ singularity exec <container> /usr/local/bin/fftw-wisdom-to-conf
$ podman run --it --rm --entrypoint /usr/local/bin/fftw-wisdom-to-conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftw-wisdom-to-conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftwf-wisdom

```bash
$ singularity exec <container> /usr/local/bin/fftwf-wisdom
$ podman run --it --rm --entrypoint /usr/local/bin/fftwf-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftwf-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftwl-wisdom

```bash
$ singularity exec <container> /usr/local/bin/fftwl-wisdom
$ podman run --it --rm --entrypoint /usr/local/bin/fftwl-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftwl-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
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