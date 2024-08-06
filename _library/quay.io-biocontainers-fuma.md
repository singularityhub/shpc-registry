---
layout: container
name:  "quay.io/biocontainers/fuma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fuma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fuma/container.yaml"
updated_at: "2024-08-06 03:24:54.950933"
latest: "4.0.0--pyhb7b1952_0"
container_url: "https://biocontainers.pro/tools/fuma"
aliases:
 - "chimerascan-exclude-transcriptome-events"
 - "chimerascan-relative-bedpe-to-CG"
 - "defuse-clusters-to-CG"
 - "fuma"
 - "fuma-gencode-gtf-to-bed"
 - "fuma-list-to-boolean-list"
 - "fusioncatcher-to-CG"
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
 - "4.0.0--pyhb7b1952_0"
description: "shpc-registry automated BioContainers addition for fuma"
config: {"url": "https://biocontainers.pro/tools/fuma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fuma", "latest": {"4.0.0--pyhb7b1952_0": "sha256:49e62ca133824cf53d1932746127b59c8c6ccdcc3717c84d0387c95cc4385b30"}, "tags": {"4.0.0--pyhb7b1952_0": "sha256:49e62ca133824cf53d1932746127b59c8c6ccdcc3717c84d0387c95cc4385b30"}, "docker": "quay.io/biocontainers/fuma", "aliases": {"chimerascan-exclude-transcriptome-events": "/usr/local/bin/chimerascan-exclude-transcriptome-events", "chimerascan-relative-bedpe-to-CG": "/usr/local/bin/chimerascan-relative-bedpe-to-CG", "defuse-clusters-to-CG": "/usr/local/bin/defuse-clusters-to-CG", "fuma": "/usr/local/bin/fuma", "fuma-gencode-gtf-to-bed": "/usr/local/bin/fuma-gencode-gtf-to-bed", "fuma-list-to-boolean-list": "/usr/local/bin/fuma-list-to-boolean-list", "fusioncatcher-to-CG": "/usr/local/bin/fusioncatcher-to-CG", "htseq-count-barcodes": "/usr/local/bin/htseq-count-barcodes", "htseq-count": "/usr/local/bin/htseq-count", "htseq-qa": "/usr/local/bin/htseq-qa", "f2py3.9": "/usr/local/bin/f2py3.9", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fuma.
shpc-registry automated BioContainers addition for fuma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fuma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fuma:4.0.0--pyhb7b1952_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fuma/4.0.0--pyhb7b1952_0
$ module help quay.io/biocontainers/fuma/4.0.0--pyhb7b1952_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fuma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fuma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fuma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fuma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fuma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fuma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chimerascan-exclude-transcriptome-events

```bash
$ singularity exec <container> /usr/local/bin/chimerascan-exclude-transcriptome-events
$ podman run --it --rm --entrypoint /usr/local/bin/chimerascan-exclude-transcriptome-events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chimerascan-exclude-transcriptome-events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chimerascan-relative-bedpe-to-CG

```bash
$ singularity exec <container> /usr/local/bin/chimerascan-relative-bedpe-to-CG
$ podman run --it --rm --entrypoint /usr/local/bin/chimerascan-relative-bedpe-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chimerascan-relative-bedpe-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### defuse-clusters-to-CG

```bash
$ singularity exec <container> /usr/local/bin/defuse-clusters-to-CG
$ podman run --it --rm --entrypoint /usr/local/bin/defuse-clusters-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/defuse-clusters-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuma

```bash
$ singularity exec <container> /usr/local/bin/fuma
$ podman run --it --rm --entrypoint /usr/local/bin/fuma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuma-gencode-gtf-to-bed

```bash
$ singularity exec <container> /usr/local/bin/fuma-gencode-gtf-to-bed
$ podman run --it --rm --entrypoint /usr/local/bin/fuma-gencode-gtf-to-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuma-gencode-gtf-to-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuma-list-to-boolean-list

```bash
$ singularity exec <container> /usr/local/bin/fuma-list-to-boolean-list
$ podman run --it --rm --entrypoint /usr/local/bin/fuma-list-to-boolean-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuma-list-to-boolean-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fusioncatcher-to-CG

```bash
$ singularity exec <container> /usr/local/bin/fusioncatcher-to-CG
$ podman run --it --rm --entrypoint /usr/local/bin/fusioncatcher-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fusioncatcher-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
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