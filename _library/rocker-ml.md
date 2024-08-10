---
layout: container
name:  "rocker/ml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocker/ml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocker/ml/container.yaml"
updated_at: "2024-08-10 02:37:51.498142"
latest: "4.4.1"
container_url: "https://hub.docker.com/r/rocker/ml"
aliases:
 - "R"
 - "Rscript"
 - "rocker-ml-run"
 - "rserver"
 - "rserver-pam"
 - "rsession"
 - "rstudio-server"
versions:
 - "4.2.2"
 - "4.2.3"
 - "4.3.0"
 - "4.3.1"
 - "4.3.2"
 - "4.4.0"
 - "4.4.1"
description: "Docker images with R + machine learning libraries (CPU versions)."
config: {"docker": "rocker/ml", "url": "https://hub.docker.com/r/rocker/ml", "maintainer": "@vsoch", "description": "Docker images with R + machine learning libraries (CPU versions).", "latest": {"4.4.1": "sha256:9a7ae69d0d4213a4ccabe93ccfcb6b611db5177e34590cf830b4ca8eae9c2f8c"}, "tags": {"4.2.2": "sha256:9c4ed7755fa4d692a7cc90a0266772f00b8e9fba50a819cfbf49a57de09207f6", "4.2.3": "sha256:92dc1cc1a917a76adbb7622e6573d633ad8aefbbb14fedfd1ac0b3ad8b8149c7", "4.3.0": "sha256:4b9bc8933882e52628f4b7336d0e1a10b8f204bcd6628fb3580a5731556574e5", "4.3.1": "sha256:931ff49b8aba52ebfca958337eee1f692dc6c8a8649dc68fb1c50b87510561f1", "4.3.2": "sha256:ada39a6d980edf54fc0756a36b99a09ef3c4a5ec7fd468890c42412311db21a4", "4.4.0": "sha256:b9c59ded7a16c589edc0ebcc5838fe92779a1d082ad5345762bce9f400433869", "4.4.1": "sha256:9a7ae69d0d4213a4ccabe93ccfcb6b611db5177e34590cf830b4ca8eae9c2f8c"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"R": "/usr/local/bin/R", "Rscript": "/usr/local/bin/Rscript", "rocker-ml-run": "/bin/bash", "rserver": "/usr/lib/rstudio-server/bin/rserver", "rserver-pam": "/usr/lib/rstudio-server/bin/rserver-pam", "rsession": "/usr/lib/rstudio-server/bin/rsession", "rstudio-server": "/usr/lib/rstudio-server/bin/rstudio-server"}}
---

This module is a singularity container wrapper for rocker/ml.
Docker images with R + machine learning libraries (CPU versions).
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocker/ml
```

Or a specific version:

```bash
$ shpc install rocker/ml:4.4.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/ml/4.4.1
$ module help rocker/ml/4.4.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### R

```bash
$ singularity exec <container> /usr/local/bin/R
$ podman run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rscript

```bash
$ singularity exec <container> /usr/local/bin/Rscript
$ podman run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rocker-ml-run

```bash
$ singularity exec <container> /bin/bash
$ podman run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rserver

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rserver
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rserver-pam

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rserver-pam
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver-pam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver-pam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsession

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rsession
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rsession   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rsession   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rstudio-server

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rstudio-server
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rstudio-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rstudio-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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