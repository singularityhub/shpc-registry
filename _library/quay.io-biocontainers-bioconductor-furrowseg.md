---
layout: container
name:  "quay.io/biocontainers/bioconductor-furrowseg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-furrowseg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-furrowseg/container.yaml"
updated_at: "2024-03-12 02:51:12.827555"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-furrowseg"
aliases:
 - "fftw-wisdom"
 - "fftw-wisdom-to-conf"
 - "fftwf-wisdom"
 - "fftwl-wisdom"
versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.25.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-furrowseg"
config: {"url": "https://biocontainers.pro/tools/bioconductor-furrowseg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-furrowseg", "latest": {"1.30.0--r43hdfd78af_0": "sha256:1e0a44fc6b77d46e1d1abedc0e74d419457ac30d50ec43480a09ba3d1208afa7"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:6dd18e795393b431862b95edc187f771519cbdac976372a401c3d6997afe3744", "1.25.0--r42hdfd78af_0": "sha256:6ad77fb4a5979b8eb99f9e628e24c5a3e97beb271579ddffafa9e83a9e07fddd", "1.28.0--r43hdfd78af_0": "sha256:c5780e5f969d5d1d4d67b16dfd553f9727448240d26e038b89f3c28a5ab96b1c", "1.30.0--r43hdfd78af_0": "sha256:1e0a44fc6b77d46e1d1abedc0e74d419457ac30d50ec43480a09ba3d1208afa7"}, "docker": "quay.io/biocontainers/bioconductor-furrowseg", "aliases": {"fftw-wisdom": "/usr/local/bin/fftw-wisdom", "fftw-wisdom-to-conf": "/usr/local/bin/fftw-wisdom-to-conf", "fftwf-wisdom": "/usr/local/bin/fftwf-wisdom", "fftwl-wisdom": "/usr/local/bin/fftwl-wisdom"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-furrowseg.
shpc-registry automated BioContainers addition for bioconductor-furrowseg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-furrowseg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-furrowseg:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-furrowseg/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-furrowseg/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-furrowseg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-furrowseg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-furrowseg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-furrowseg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-furrowseg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-furrowseg-inspect-deffile:

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