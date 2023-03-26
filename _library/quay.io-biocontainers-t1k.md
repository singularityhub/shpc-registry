---
layout: container
name:  "quay.io/biocontainers/t1k"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/t1k/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/t1k/container.yaml"
updated_at: "2023-03-26 03:20:25.709786"
latest: "1.0.1--h5b5514e_0"
container_url: "https://biocontainers.pro/tools/t1k"
aliases:
 - "AddGeneCoord.pl"
 - "ParseDatFile.pl"
 - "analyzer"
 - "bam-extractor"
 - "fastq-extractor"
 - "genotyper"
 - "run-t1k"
 - "t1k-build.pl"
 - "t1k-merge.py"
 - "t1k-smartseq.pl"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0.1--h5b5514e_0"
description: "singularity registry hpc automated addition for t1k"
config: {"url": "https://biocontainers.pro/tools/t1k", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for t1k", "latest": {"1.0.1--h5b5514e_0": "sha256:f93393f7a52b5149490a870137e8b37c33a9b17bb825efc58ac7168b88abc1f9"}, "tags": {"1.0.1--h5b5514e_0": "sha256:f93393f7a52b5149490a870137e8b37c33a9b17bb825efc58ac7168b88abc1f9"}, "docker": "quay.io/biocontainers/t1k", "aliases": {"AddGeneCoord.pl": "/usr/local/bin/AddGeneCoord.pl", "ParseDatFile.pl": "/usr/local/bin/ParseDatFile.pl", "analyzer": "/usr/local/bin/analyzer", "bam-extractor": "/usr/local/bin/bam-extractor", "fastq-extractor": "/usr/local/bin/fastq-extractor", "genotyper": "/usr/local/bin/genotyper", "run-t1k": "/usr/local/bin/run-t1k", "t1k-build.pl": "/usr/local/bin/t1k-build.pl", "t1k-merge.py": "/usr/local/bin/t1k-merge.py", "t1k-smartseq.pl": "/usr/local/bin/t1k-smartseq.pl", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/t1k.
singularity registry hpc automated addition for t1k
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/t1k
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/t1k:1.0.1--h5b5514e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/t1k/1.0.1--h5b5514e_0
$ module help quay.io/biocontainers/t1k/1.0.1--h5b5514e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### t1k-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### t1k-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### t1k-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### t1k-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### t1k-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### t1k-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AddGeneCoord.pl

```bash
$ singularity exec <container> /usr/local/bin/AddGeneCoord.pl
$ podman run --it --rm --entrypoint /usr/local/bin/AddGeneCoord.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AddGeneCoord.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ParseDatFile.pl

```bash
$ singularity exec <container> /usr/local/bin/ParseDatFile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ParseDatFile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ParseDatFile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzer

```bash
$ singularity exec <container> /usr/local/bin/analyzer
$ podman run --it --rm --entrypoint /usr/local/bin/analyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam-extractor

```bash
$ singularity exec <container> /usr/local/bin/bam-extractor
$ podman run --it --rm --entrypoint /usr/local/bin/bam-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-extractor

```bash
$ singularity exec <container> /usr/local/bin/fastq-extractor
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotyper

```bash
$ singularity exec <container> /usr/local/bin/genotyper
$ podman run --it --rm --entrypoint /usr/local/bin/genotyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-t1k

```bash
$ singularity exec <container> /usr/local/bin/run-t1k
$ podman run --it --rm --entrypoint /usr/local/bin/run-t1k   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-t1k   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t1k-build.pl

```bash
$ singularity exec <container> /usr/local/bin/t1k-build.pl
$ podman run --it --rm --entrypoint /usr/local/bin/t1k-build.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t1k-build.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t1k-merge.py

```bash
$ singularity exec <container> /usr/local/bin/t1k-merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/t1k-merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t1k-merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t1k-smartseq.pl

```bash
$ singularity exec <container> /usr/local/bin/t1k-smartseq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/t1k-smartseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t1k-smartseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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