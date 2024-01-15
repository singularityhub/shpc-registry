---
layout: container
name:  "quay.io/biocontainers/graphprot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/graphprot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/graphprot/container.yaml"
updated_at: "2024-01-15 02:38:30.493523"
latest: "1.1.7--h3445559_4"
container_url: "https://biocontainers.pro/tools/graphprot"
aliases:
 - "GraphProt.pl"
 - "RNAshapes"
 - "gawk-4.2.1"
 - "svm-predict"
 - "svm-scale"
 - "svm-train"
 - "transformseq"
 - "weblogo"
 - "conv-template"
 - "from-template"
 - "b2sum"
 - "awk"
 - "base32"
versions:
 - "1.1.7--h3445559_4"
description: "shpc-registry automated BioContainers addition for graphprot"
config: {"url": "https://biocontainers.pro/tools/graphprot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for graphprot", "latest": {"1.1.7--h3445559_4": "sha256:a8b00657d5cab0048bc35897fc666c9130240be47aab5c8c5f6cdc5b59a36668"}, "tags": {"1.1.7--h3445559_4": "sha256:a8b00657d5cab0048bc35897fc666c9130240be47aab5c8c5f6cdc5b59a36668"}, "docker": "quay.io/biocontainers/graphprot", "aliases": {"GraphProt.pl": "/usr/local/bin/GraphProt.pl", "RNAshapes": "/usr/local/bin/RNAshapes", "gawk-4.2.1": "/usr/local/bin/gawk-4.2.1", "svm-predict": "/usr/local/bin/svm-predict", "svm-scale": "/usr/local/bin/svm-scale", "svm-train": "/usr/local/bin/svm-train", "transformseq": "/usr/local/bin/transformseq", "weblogo": "/usr/local/bin/weblogo", "conv-template": "/usr/local/bin/conv-template", "from-template": "/usr/local/bin/from-template", "b2sum": "/usr/local/bin/b2sum", "awk": "/usr/local/bin/awk", "base32": "/usr/local/bin/base32"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/graphprot.
shpc-registry automated BioContainers addition for graphprot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/graphprot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/graphprot:1.1.7--h3445559_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/graphprot/1.1.7--h3445559_4
$ module help quay.io/biocontainers/graphprot/1.1.7--h3445559_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graphprot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graphprot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graphprot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graphprot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graphprot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graphprot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GraphProt.pl

```bash
$ singularity exec <container> /usr/local/bin/GraphProt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/GraphProt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphProt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAshapes

```bash
$ singularity exec <container> /usr/local/bin/RNAshapes
$ podman run --it --rm --entrypoint /usr/local/bin/RNAshapes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAshapes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-4.2.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-4.2.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-4.2.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-4.2.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-predict

```bash
$ singularity exec <container> /usr/local/bin/svm-predict
$ podman run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-scale

```bash
$ singularity exec <container> /usr/local/bin/svm-scale
$ podman run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-train

```bash
$ singularity exec <container> /usr/local/bin/svm-train
$ podman run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transformseq

```bash
$ singularity exec <container> /usr/local/bin/transformseq
$ podman run --it --rm --entrypoint /usr/local/bin/transformseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weblogo

```bash
$ singularity exec <container> /usr/local/bin/weblogo
$ podman run --it --rm --entrypoint /usr/local/bin/weblogo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weblogo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conv-template

```bash
$ singularity exec <container> /usr/local/bin/conv-template
$ podman run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from-template

```bash
$ singularity exec <container> /usr/local/bin/from-template
$ podman run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
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