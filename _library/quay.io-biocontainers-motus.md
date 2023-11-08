---
layout: container
name:  "quay.io/biocontainers/motus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/motus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/motus/container.yaml"
updated_at: "2023-11-08 03:10:39.314464"
latest: "3.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/motus"
aliases:
 - "metaSNV.py"
 - "metaSNV_post.py"
 - "motus"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "f2py3.9"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
versions:
 - "3.0.3--pyhdfd78af_0"
 - "3.1.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for motus"
config: {"url": "https://biocontainers.pro/tools/motus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for motus", "latest": {"3.1.0--pyhdfd78af_0": "sha256:59e04b6be75355e392c32556c36fa9056802de1b9dc75d4276b3fcca69a42e76"}, "tags": {"3.0.3--pyhdfd78af_0": "sha256:2ea5d3a9448305bf1b7805cb078bbbd968771ddc9ee6a0d5a48c5a8f17e12b1e", "3.1.0--pyhdfd78af_0": "sha256:59e04b6be75355e392c32556c36fa9056802de1b9dc75d4276b3fcca69a42e76"}, "docker": "quay.io/biocontainers/motus", "aliases": {"metaSNV.py": "/usr/local/bin/metaSNV.py", "metaSNV_post.py": "/usr/local/bin/metaSNV_post.py", "motus": "/usr/local/bin/motus", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "f2py3.9": "/usr/local/bin/f2py3.9", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/motus.
shpc-registry automated BioContainers addition for motus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/motus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/motus:3.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/motus/3.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/motus/3.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### motus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### motus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### motus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### motus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### motus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### motus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metaSNV.py

```bash
$ singularity exec <container> /usr/local/bin/metaSNV.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaSNV.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaSNV.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaSNV_post.py

```bash
$ singularity exec <container> /usr/local/bin/metaSNV_post.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaSNV_post.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaSNV_post.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### motus

```bash
$ singularity exec <container> /usr/local/bin/motus
$ podman run --it --rm --entrypoint /usr/local/bin/motus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/motus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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