---
layout: container
name:  "quay.io/biocontainers/multigps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/multigps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/multigps/container.yaml"
updated_at: "2025-10-09 04:26:54.670665"
latest: "0.74--h9ee0642_3"
container_url: "https://biocontainers.pro/tools/multigps"
aliases:
 - "multigps"
 - "xsltproc_lite"
 - "alphtype"
 - "ama"
 - "ama-qvalues"
 - "ame"
 - "beeml2meme"
 - "centrimo"
 - "ceqlogo"
 - "chen2meme"
 - "clustalw2fasta"
 - "clustalw2phylip"
versions:
 - "0.74--h9ee0642_3"
description: "shpc-registry automated BioContainers addition for multigps"
config: {"url": "https://biocontainers.pro/tools/multigps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for multigps", "latest": {"0.74--h9ee0642_3": "sha256:973b31e273187a6bcdbc5fdfc19b2a4a03e7864009aad29c8e5adc6b473ec4d0"}, "tags": {"0.74--h9ee0642_3": "sha256:973b31e273187a6bcdbc5fdfc19b2a4a03e7864009aad29c8e5adc6b473ec4d0"}, "docker": "quay.io/biocontainers/multigps", "aliases": {"multigps": "/usr/local/bin/multigps", "xsltproc_lite": "/usr/local/bin/xsltproc_lite", "alphtype": "/usr/local/bin/alphtype", "ama": "/usr/local/bin/ama", "ama-qvalues": "/usr/local/bin/ama-qvalues", "ame": "/usr/local/bin/ame", "beeml2meme": "/usr/local/bin/beeml2meme", "centrimo": "/usr/local/bin/centrimo", "ceqlogo": "/usr/local/bin/ceqlogo", "chen2meme": "/usr/local/bin/chen2meme", "clustalw2fasta": "/usr/local/bin/clustalw2fasta", "clustalw2phylip": "/usr/local/bin/clustalw2phylip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/multigps.
shpc-registry automated BioContainers addition for multigps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/multigps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/multigps:0.74--h9ee0642_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/multigps/0.74--h9ee0642_3
$ module help quay.io/biocontainers/multigps/0.74--h9ee0642_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### multigps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### multigps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### multigps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### multigps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### multigps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### multigps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### multigps

```bash
$ singularity exec <container> /usr/local/bin/multigps
$ podman run --it --rm --entrypoint /usr/local/bin/multigps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multigps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc_lite

```bash
$ singularity exec <container> /usr/local/bin/xsltproc_lite
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc_lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc_lite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alphtype

```bash
$ singularity exec <container> /usr/local/bin/alphtype
$ podman run --it --rm --entrypoint /usr/local/bin/alphtype   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alphtype   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ama

```bash
$ singularity exec <container> /usr/local/bin/ama
$ podman run --it --rm --entrypoint /usr/local/bin/ama   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ama   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ama-qvalues

```bash
$ singularity exec <container> /usr/local/bin/ama-qvalues
$ podman run --it --rm --entrypoint /usr/local/bin/ama-qvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ama-qvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ame

```bash
$ singularity exec <container> /usr/local/bin/ame
$ podman run --it --rm --entrypoint /usr/local/bin/ame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### beeml2meme

```bash
$ singularity exec <container> /usr/local/bin/beeml2meme
$ podman run --it --rm --entrypoint /usr/local/bin/beeml2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beeml2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrimo

```bash
$ singularity exec <container> /usr/local/bin/centrimo
$ podman run --it --rm --entrypoint /usr/local/bin/centrimo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrimo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ceqlogo

```bash
$ singularity exec <container> /usr/local/bin/ceqlogo
$ podman run --it --rm --entrypoint /usr/local/bin/ceqlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ceqlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chen2meme

```bash
$ singularity exec <container> /usr/local/bin/chen2meme
$ podman run --it --rm --entrypoint /usr/local/bin/chen2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chen2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalw2fasta

```bash
$ singularity exec <container> /usr/local/bin/clustalw2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/clustalw2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalw2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalw2phylip

```bash
$ singularity exec <container> /usr/local/bin/clustalw2phylip
$ podman run --it --rm --entrypoint /usr/local/bin/clustalw2phylip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalw2phylip   -v ${PWD} -w ${PWD} <container> -c " $@"
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