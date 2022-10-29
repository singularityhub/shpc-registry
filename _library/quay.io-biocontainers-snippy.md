---
layout: container
name:  "quay.io/biocontainers/snippy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snippy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/snippy/container.yaml"
updated_at: "2022-10-29 05:39:34.191343"
latest: "4.6.0--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/snippy"
aliases:
 - "split_ref_by_bai_datasize.py"
 - "2to3-3.7"
 - "abba-baba"
 - "ace2sam"
 - "annotateBed"
 - "any2fasta"
 - "bFst"
 - "bamToBed"
 - "bamToFastq"
 - "bamToGBrowse.pl"
 - "bamleftalign"
versions:
 - "4.6.0--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for snippy"
config: {"url": "https://biocontainers.pro/tools/snippy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snippy", "latest": {"4.6.0--hdfd78af_2": "sha256:8d1589ab60af6a9dac53dd069b71fdffc2d6530047e4b9742b59a89fbe2a5b70"}, "tags": {"4.6.0--hdfd78af_2": "sha256:8d1589ab60af6a9dac53dd069b71fdffc2d6530047e4b9742b59a89fbe2a5b70"}, "docker": "quay.io/biocontainers/snippy", "aliases": {"split_ref_by_bai_datasize.py": "/usr/local/bin/split_ref_by_bai_datasize.py", "2to3-3.7": "/usr/local/bin/2to3-3.7", "abba-baba": "/usr/local/bin/abba-baba", "ace2sam": "/usr/local/bin/ace2sam", "annotateBed": "/usr/local/bin/annotateBed", "any2fasta": "/usr/local/bin/any2fasta", "bFst": "/usr/local/bin/bFst", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bamToGBrowse.pl": "/usr/local/bin/bamToGBrowse.pl", "bamleftalign": "/usr/local/bin/bamleftalign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snippy.
shpc-registry automated BioContainers addition for snippy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snippy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snippy:4.6.0--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snippy/4.6.0--hdfd78af_2
$ module help quay.io/biocontainers/snippy/4.6.0--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snippy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snippy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snippy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snippy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snippy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snippy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### split_ref_by_bai_datasize.py

```bash
$ singularity exec <container> /usr/local/bin/split_ref_by_bai_datasize.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abba-baba

```bash
$ singularity exec <container> /usr/local/bin/abba-baba
$ podman run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bFst

```bash
$ singularity exec <container> /usr/local/bin/bFst
$ podman run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToGBrowse.pl

```bash
$ singularity exec <container> /usr/local/bin/bamToGBrowse.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bamToGBrowse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToGBrowse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamleftalign

```bash
$ singularity exec <container> /usr/local/bin/bamleftalign
$ podman run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
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