---
layout: container
name:  "quay.io/biocontainers/bioconductor-cytomapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cytomapper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cytomapper/container.yaml"
updated_at: "2023-11-19 03:01:31.715691"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cytomapper"
aliases:
 - "fftw-wisdom"
 - "fftw-wisdom-to-conf"
 - "fftwf-wisdom"
 - "fftwl-wisdom"
versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cytomapper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cytomapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cytomapper", "latest": {"1.12.0--r43hdfd78af_0": "sha256:20c9c1f388851d1aa56864dfcfdea0ab354a4e8859867b409971dafaa9767ea1"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:4c52afa7052b9d79277e9e41c70f3c475aed2b721534f095b8c2d8e4fdb5cddc", "1.10.0--r42hdfd78af_0": "sha256:d16906ddfad730ca8599a2090a3aa8ed0fa521da5dfb33bbeef1406e420aad37", "1.12.0--r43hdfd78af_0": "sha256:20c9c1f388851d1aa56864dfcfdea0ab354a4e8859867b409971dafaa9767ea1"}, "docker": "quay.io/biocontainers/bioconductor-cytomapper", "aliases": {"fftw-wisdom": "/usr/local/bin/fftw-wisdom", "fftw-wisdom-to-conf": "/usr/local/bin/fftw-wisdom-to-conf", "fftwf-wisdom": "/usr/local/bin/fftwf-wisdom", "fftwl-wisdom": "/usr/local/bin/fftwl-wisdom"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cytomapper.
shpc-registry automated BioContainers addition for bioconductor-cytomapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cytomapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cytomapper:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cytomapper/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cytomapper/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cytomapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytomapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytomapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cytomapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cytomapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cytomapper-inspect-deffile:

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