---
layout: container
name:  "quay.io/biocontainers/bioconductor-confess"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-confess/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-confess/container.yaml"
updated_at: "2025-04-05 03:31:52.650172"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-confess"
aliases:
 - "fftw-wisdom"
 - "fftw-wisdom-to-conf"
 - "fftwf-wisdom"
 - "fftwl-wisdom"
versions:
 - "1.22.0--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-confess"
config: {"url": "https://biocontainers.pro/tools/bioconductor-confess", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-confess", "latest": {"1.34.0--r44hdfd78af_0": "sha256:002bdd8f7e4b42dba80f44b05a8efae8654ba4d6c044ca024b470d08414d9751"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:ab1b2bec1787b8abe3a1d62559050a7e470cee5dc017729bcb12aba50a48c560", "1.26.0--r42hdfd78af_0": "sha256:48d25c214cb41d73788e38a3d4babe12e07c0fe74f54a3c18c96d1395ac8fdda", "1.28.0--r43hdfd78af_0": "sha256:b0adb0ea7869f2789bdef24f6a249492c438e6b9daef08f60ceb5ddeae645d18", "1.30.0--r43hdfd78af_0": "sha256:ae7e4550ff5f13fa6d6f687edbadcad8448528b9b23fc81d2c6cbdfaacf877a5", "1.34.0--r44hdfd78af_0": "sha256:002bdd8f7e4b42dba80f44b05a8efae8654ba4d6c044ca024b470d08414d9751"}, "docker": "quay.io/biocontainers/bioconductor-confess", "aliases": {"fftw-wisdom": "/usr/local/bin/fftw-wisdom", "fftw-wisdom-to-conf": "/usr/local/bin/fftw-wisdom-to-conf", "fftwf-wisdom": "/usr/local/bin/fftwf-wisdom", "fftwl-wisdom": "/usr/local/bin/fftwl-wisdom"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-confess.
shpc-registry automated BioContainers addition for bioconductor-confess
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-confess
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-confess:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-confess/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-confess/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-confess-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-confess-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-confess-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-confess-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-confess-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-confess-inspect-deffile:

```bash
$ singularity inspect -d <container>
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