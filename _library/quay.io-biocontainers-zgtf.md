---
layout: container
name:  "quay.io/biocontainers/zgtf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/zgtf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/zgtf/container.yaml"
updated_at: "2024-09-05 04:23:02.453502"
latest: "0.1.2--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/zgtf"
aliases:
 - "gtf2bed12"
 - "htseq-count-barcodes"
 - "htseq-count"
 - "htseq-qa"
 - "f2py3.9"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
versions:
 - "0.1.2--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for zgtf"
config: {"url": "https://biocontainers.pro/tools/zgtf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for zgtf", "latest": {"0.1.2--pyh5e36f6f_0": "sha256:96713b2ac4888953120ed586612ca4cbd3b9dff632f92cac2d499dc4b8413f77"}, "tags": {"0.1.2--pyh5e36f6f_0": "sha256:96713b2ac4888953120ed586612ca4cbd3b9dff632f92cac2d499dc4b8413f77"}, "docker": "quay.io/biocontainers/zgtf", "aliases": {"gtf2bed12": "/usr/local/bin/gtf2bed12", "htseq-count-barcodes": "/usr/local/bin/htseq-count-barcodes", "htseq-count": "/usr/local/bin/htseq-count", "htseq-qa": "/usr/local/bin/htseq-qa", "f2py3.9": "/usr/local/bin/f2py3.9", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/zgtf.
shpc-registry automated BioContainers addition for zgtf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/zgtf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/zgtf:0.1.2--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/zgtf/0.1.2--pyh5e36f6f_0
$ module help quay.io/biocontainers/zgtf/0.1.2--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### zgtf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### zgtf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### zgtf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### zgtf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### zgtf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### zgtf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gtf2bed12

```bash
$ singularity exec <container> /usr/local/bin/gtf2bed12
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2bed12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2bed12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-count-barcodes

```bash
$ singularity exec <container> /usr/local/bin/htseq-count-barcodes
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count-barcodes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count-barcodes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-count

```bash
$ singularity exec <container> /usr/local/bin/htseq-count
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-qa

```bash
$ singularity exec <container> /usr/local/bin/htseq-qa
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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