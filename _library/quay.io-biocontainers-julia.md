---
layout: container
name:  "quay.io/biocontainers/julia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/julia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/julia/container.yaml"
updated_at: "2025-04-26 03:16:37.860884"
latest: "1.10"
container_url: "https://biocontainers.pro/tools/julia"
aliases:
 - "julia"
 - "cmpfillin"
 - "gpmetis"
 - "graphchk"
 - "m2gmetis"
 - "mpmetis"
 - "ndmetis"
 - "fftw-wisdom"
 - "fftw-wisdom-to-conf"
 - "fftwf-wisdom"
 - "fftwl-wisdom"
versions:
 - "1.0.3"
 - "1.10"
description: "shpc-registry automated BioContainers addition for julia"
config: {"url": "https://biocontainers.pro/tools/julia", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for julia", "latest": {"1.10": "sha256:bb1d64134510081502ce8492ad0c41d6899be876eb4107a2b6be0cae939d38a3"}, "tags": {"1.0.3": "sha256:237b63daad4b41130409419b785e8867f5434a649bfa15bbf860aff3080bc2c4", "1.10": "sha256:bb1d64134510081502ce8492ad0c41d6899be876eb4107a2b6be0cae939d38a3"}, "docker": "quay.io/biocontainers/julia", "aliases": {"julia": "/usr/local/bin/julia", "cmpfillin": "/usr/local/bin/cmpfillin", "gpmetis": "/usr/local/bin/gpmetis", "graphchk": "/usr/local/bin/graphchk", "m2gmetis": "/usr/local/bin/m2gmetis", "mpmetis": "/usr/local/bin/mpmetis", "ndmetis": "/usr/local/bin/ndmetis", "fftw-wisdom": "/usr/local/bin/fftw-wisdom", "fftw-wisdom-to-conf": "/usr/local/bin/fftw-wisdom-to-conf", "fftwf-wisdom": "/usr/local/bin/fftwf-wisdom", "fftwl-wisdom": "/usr/local/bin/fftwl-wisdom"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/julia.
shpc-registry automated BioContainers addition for julia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/julia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/julia:1.10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/julia/1.10
$ module help quay.io/biocontainers/julia/1.10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### julia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### julia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### julia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### julia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### julia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### julia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### julia

```bash
$ singularity exec <container> /usr/local/bin/julia
$ podman run --it --rm --entrypoint /usr/local/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpfillin

```bash
$ singularity exec <container> /usr/local/bin/cmpfillin
$ podman run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpmetis

```bash
$ singularity exec <container> /usr/local/bin/gpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphchk

```bash
$ singularity exec <container> /usr/local/bin/graphchk
$ podman run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m2gmetis

```bash
$ singularity exec <container> /usr/local/bin/m2gmetis
$ podman run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpmetis

```bash
$ singularity exec <container> /usr/local/bin/mpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ndmetis

```bash
$ singularity exec <container> /usr/local/bin/ndmetis
$ podman run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
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