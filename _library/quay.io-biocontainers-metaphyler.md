---
layout: container
name:  "quay.io/biocontainers/metaphyler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaphyler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metaphyler/container.yaml"
updated_at: "2023-12-15 02:42:00.451659"
latest: "1.25--h031d066_7"
container_url: "https://biocontainers.pro/tools/metaphyler"
aliases:
 - "buildMetaphyler.pl"
 - "combine"
 - "installMetaphyler.pl"
 - "metaphylerClassify"
 - "metaphylerTrain"
 - "report.pl"
 - "runClassifier.pl"
 - "runMetaphyler.pl"
 - "simuReads"
 - "taxprof"
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
 - "copymat"
 - "fastacmd"
 - "formatdb"
 - "formatrpsdb"
 - "impala"
 - "makemat"
versions:
 - "1.25--hec16e2b_6"
 - "1.25--h031d066_7"
description: "shpc-registry automated BioContainers addition for metaphyler"
config: {"url": "https://biocontainers.pro/tools/metaphyler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaphyler", "latest": {"1.25--h031d066_7": "sha256:38046cc041aa01de689f1fa1cb80bf85a56261f2b736e125018055204a38c44b"}, "tags": {"1.25--hec16e2b_6": "sha256:45fe1435b5b087ce26d44fa6ab07ae5f574f39c74b5678c3fdd8503ed375c0bd", "1.25--h031d066_7": "sha256:38046cc041aa01de689f1fa1cb80bf85a56261f2b736e125018055204a38c44b"}, "docker": "quay.io/biocontainers/metaphyler", "aliases": {"buildMetaphyler.pl": "/usr/local/bin/buildMetaphyler.pl", "combine": "/usr/local/bin/combine", "installMetaphyler.pl": "/usr/local/bin/installMetaphyler.pl", "metaphylerClassify": "/usr/local/bin/metaphylerClassify", "metaphylerTrain": "/usr/local/bin/metaphylerTrain", "report.pl": "/usr/local/bin/report.pl", "runClassifier.pl": "/usr/local/bin/runClassifier.pl", "runMetaphyler.pl": "/usr/local/bin/runMetaphyler.pl", "simuReads": "/usr/local/bin/simuReads", "taxprof": "/usr/local/bin/taxprof", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp", "copymat": "/usr/local/bin/copymat", "fastacmd": "/usr/local/bin/fastacmd", "formatdb": "/usr/local/bin/formatdb", "formatrpsdb": "/usr/local/bin/formatrpsdb", "impala": "/usr/local/bin/impala", "makemat": "/usr/local/bin/makemat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaphyler.
shpc-registry automated BioContainers addition for metaphyler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaphyler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaphyler:1.25--h031d066_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaphyler/1.25--h031d066_7
$ module help quay.io/biocontainers/metaphyler/1.25--h031d066_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaphyler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaphyler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaphyler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaphyler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaphyler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaphyler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### buildMetaphyler.pl

```bash
$ singularity exec <container> /usr/local/bin/buildMetaphyler.pl
$ podman run --it --rm --entrypoint /usr/local/bin/buildMetaphyler.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildMetaphyler.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine

```bash
$ singularity exec <container> /usr/local/bin/combine
$ podman run --it --rm --entrypoint /usr/local/bin/combine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### installMetaphyler.pl

```bash
$ singularity exec <container> /usr/local/bin/installMetaphyler.pl
$ podman run --it --rm --entrypoint /usr/local/bin/installMetaphyler.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/installMetaphyler.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaphylerClassify

```bash
$ singularity exec <container> /usr/local/bin/metaphylerClassify
$ podman run --it --rm --entrypoint /usr/local/bin/metaphylerClassify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaphylerClassify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaphylerTrain

```bash
$ singularity exec <container> /usr/local/bin/metaphylerTrain
$ podman run --it --rm --entrypoint /usr/local/bin/metaphylerTrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaphylerTrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### report.pl

```bash
$ singularity exec <container> /usr/local/bin/report.pl
$ podman run --it --rm --entrypoint /usr/local/bin/report.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/report.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runClassifier.pl

```bash
$ singularity exec <container> /usr/local/bin/runClassifier.pl
$ podman run --it --rm --entrypoint /usr/local/bin/runClassifier.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runClassifier.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runMetaphyler.pl

```bash
$ singularity exec <container> /usr/local/bin/runMetaphyler.pl
$ podman run --it --rm --entrypoint /usr/local/bin/runMetaphyler.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runMetaphyler.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simuReads

```bash
$ singularity exec <container> /usr/local/bin/simuReads
$ podman run --it --rm --entrypoint /usr/local/bin/simuReads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simuReads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxprof

```bash
$ singularity exec <container> /usr/local/bin/taxprof
$ podman run --it --rm --entrypoint /usr/local/bin/taxprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copymat

```bash
$ singularity exec <container> /usr/local/bin/copymat
$ podman run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacmd

```bash
$ singularity exec <container> /usr/local/bin/fastacmd
$ podman run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatdb

```bash
$ singularity exec <container> /usr/local/bin/formatdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatrpsdb

```bash
$ singularity exec <container> /usr/local/bin/formatrpsdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### impala

```bash
$ singularity exec <container> /usr/local/bin/impala
$ podman run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makemat

```bash
$ singularity exec <container> /usr/local/bin/makemat
$ podman run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
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