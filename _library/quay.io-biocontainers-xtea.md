---
layout: container
name:  "quay.io/biocontainers/xtea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xtea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xtea/container.yaml"
updated_at: "2023-01-21 03:39:30.942396"
latest: "0.1.9--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/xtea"
aliases:
 - "wtdbg-cns"
 - "wtdbg2"
 - "wtpoa-cns"
 - "xtea"
 - "xtea_hg19"
 - "xtea_long"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "f2py3.7"
versions:
 - "0.1.9--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for xtea"
config: {"url": "https://biocontainers.pro/tools/xtea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xtea", "latest": {"0.1.9--hdfd78af_0": "sha256:0855c844a4e6298aacbbdef1d538507c33ab1683215b22b2b20aa0077af9bd42"}, "tags": {"0.1.9--hdfd78af_0": "sha256:0855c844a4e6298aacbbdef1d538507c33ab1683215b22b2b20aa0077af9bd42"}, "docker": "quay.io/biocontainers/xtea", "aliases": {"wtdbg-cns": "/usr/local/bin/wtdbg-cns", "wtdbg2": "/usr/local/bin/wtdbg2", "wtpoa-cns": "/usr/local/bin/wtpoa-cns", "xtea": "/usr/local/bin/xtea", "xtea_hg19": "/usr/local/bin/xtea_hg19", "xtea_long": "/usr/local/bin/xtea_long", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "f2py3.7": "/usr/local/bin/f2py3.7"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xtea.
shpc-registry automated BioContainers addition for xtea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xtea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xtea:0.1.9--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xtea/0.1.9--hdfd78af_0
$ module help quay.io/biocontainers/xtea/0.1.9--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xtea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xtea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xtea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xtea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xtea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xtea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wtdbg-cns

```bash
$ singularity exec <container> /usr/local/bin/wtdbg-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtdbg2

```bash
$ singularity exec <container> /usr/local/bin/wtdbg2
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtpoa-cns

```bash
$ singularity exec <container> /usr/local/bin/wtpoa-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtea

```bash
$ singularity exec <container> /usr/local/bin/xtea
$ podman run --it --rm --entrypoint /usr/local/bin/xtea   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtea   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtea_hg19

```bash
$ singularity exec <container> /usr/local/bin/xtea_hg19
$ podman run --it --rm --entrypoint /usr/local/bin/xtea_hg19   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtea_hg19   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtea_long

```bash
$ singularity exec <container> /usr/local/bin/xtea_long
$ podman run --it --rm --entrypoint /usr/local/bin/xtea_long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtea_long   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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