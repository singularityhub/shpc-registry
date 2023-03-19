---
layout: container
name:  "quay.io/biocontainers/bioconductor-omicspca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-omicspca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-omicspca/container.yaml"
updated_at: "2023-03-19 03:09:09.366038"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-omicspca"
aliases:
 - "pdfattach"
 - "pdfdetach"
 - "pdffonts"
 - "pdfimages"
 - "pdfinfo"
 - "pdfseparate"
 - "pdftocairo"
 - "pdftohtml"
 - "pdftoppm"
 - "pdftops"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-omicspca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-omicspca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-omicspca", "latest": {"1.16.0--r42hdfd78af_0": "sha256:2a71093cfdaa710ac2fb0b4ecbd938039fd618bd01babfa285d10a59d0190e39"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:fc74489aad6dcadefad2a87e640404bd117f7198ba78eeff8cbc5ce705e77fa1", "1.16.0--r42hdfd78af_0": "sha256:2a71093cfdaa710ac2fb0b4ecbd938039fd618bd01babfa285d10a59d0190e39", "1.12.0--r41hdfd78af_0": "sha256:24e4e6a6fdf71dbae75f4fba5cab86234b5070f4a10e0f66c34aafb5125ec2a9", "1.10.0--r41hdfd78af_0": "sha256:54007588ff31d0acd12959ec6755493e7f142005dd6e8f677798f368ec8b6593"}, "docker": "quay.io/biocontainers/bioconductor-omicspca", "aliases": {"pdfattach": "/usr/local/bin/pdfattach", "pdfdetach": "/usr/local/bin/pdfdetach", "pdffonts": "/usr/local/bin/pdffonts", "pdfimages": "/usr/local/bin/pdfimages", "pdfinfo": "/usr/local/bin/pdfinfo", "pdfseparate": "/usr/local/bin/pdfseparate", "pdftocairo": "/usr/local/bin/pdftocairo", "pdftohtml": "/usr/local/bin/pdftohtml", "pdftoppm": "/usr/local/bin/pdftoppm", "pdftops": "/usr/local/bin/pdftops"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-omicspca.
shpc-registry automated BioContainers addition for bioconductor-omicspca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-omicspca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-omicspca:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-omicspca/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-omicspca/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-omicspca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omicspca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omicspca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-omicspca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-omicspca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-omicspca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pdfattach

```bash
$ singularity exec <container> /usr/local/bin/pdfattach
$ podman run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfdetach

```bash
$ singularity exec <container> /usr/local/bin/pdfdetach
$ podman run --it --rm --entrypoint /usr/local/bin/pdfdetach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfdetach   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdffonts

```bash
$ singularity exec <container> /usr/local/bin/pdffonts
$ podman run --it --rm --entrypoint /usr/local/bin/pdffonts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdffonts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfimages

```bash
$ singularity exec <container> /usr/local/bin/pdfimages
$ podman run --it --rm --entrypoint /usr/local/bin/pdfimages   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfimages   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfinfo

```bash
$ singularity exec <container> /usr/local/bin/pdfinfo
$ podman run --it --rm --entrypoint /usr/local/bin/pdfinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfseparate

```bash
$ singularity exec <container> /usr/local/bin/pdfseparate
$ podman run --it --rm --entrypoint /usr/local/bin/pdfseparate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfseparate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftocairo

```bash
$ singularity exec <container> /usr/local/bin/pdftocairo
$ podman run --it --rm --entrypoint /usr/local/bin/pdftocairo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftocairo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftohtml

```bash
$ singularity exec <container> /usr/local/bin/pdftohtml
$ podman run --it --rm --entrypoint /usr/local/bin/pdftohtml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftohtml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftoppm

```bash
$ singularity exec <container> /usr/local/bin/pdftoppm
$ podman run --it --rm --entrypoint /usr/local/bin/pdftoppm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftoppm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftops

```bash
$ singularity exec <container> /usr/local/bin/pdftops
$ podman run --it --rm --entrypoint /usr/local/bin/pdftops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftops   -v ${PWD} -w ${PWD} <container> -c " $@"
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