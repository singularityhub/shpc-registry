---
layout: container
name:  "quay.io/biocontainers/parascopy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/parascopy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/parascopy/container.yaml"
updated_at: "2025-08-04 04:24:45.451218"
latest: "1.11.0--py38h0517ac9_1"
container_url: "https://biocontainers.pro/tools/parascopy"
aliases:
 - "_parascopy_freebayes"
 - "parascopy"
 - "tabix++"
 - "bc"
 - "dc"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "f2py3.9"
 - "ace2sam"
versions:
 - "1.9.1--py39heba0655_0"
 - "1.9.7--py39h6519bef_0"
 - "1.11.0--py37h7321523_0"
 - "1.10.6--py39h002a086_0"
 - "1.9.7--py39h002a086_1"
 - "1.11.0--py38h0517ac9_1"
description: "shpc-registry automated BioContainers addition for parascopy"
config: {"url": "https://biocontainers.pro/tools/parascopy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for parascopy", "latest": {"1.11.0--py38h0517ac9_1": "sha256:c62558ae16aa14e24722d75bde863cb915042412169dffd7c3535ac3be502ec3"}, "tags": {"1.9.1--py39heba0655_0": "sha256:510ea5bec833767af1c344ca772bae2d9bab06a4cf6c260cec1ebf528b5887c3", "1.9.7--py39h6519bef_0": "sha256:370fd811e849293ffb438c84d1fd0bc80acb926fdd1cd2bd0d6f7e089020a808", "1.11.0--py37h7321523_0": "sha256:777f728dae0454ad9d726060d1a280d9fdb38079196f017bf699c2ba1deb4f47", "1.10.6--py39h002a086_0": "sha256:a69109d64a78ecff71d45f6855b6135893c940e0590a0ff8e69c50123d1c199b", "1.9.7--py39h002a086_1": "sha256:b98cacd798cb996302663d5035a9eb1ac297d4a0a9a3f2f91991b6c1f2a93db5", "1.11.0--py38h0517ac9_1": "sha256:c62558ae16aa14e24722d75bde863cb915042412169dffd7c3535ac3be502ec3"}, "docker": "quay.io/biocontainers/parascopy", "aliases": {"_parascopy_freebayes": "/usr/local/bin/_parascopy_freebayes", "parascopy": "/usr/local/bin/parascopy", "tabix++": "/usr/local/bin/tabix++", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "f2py3.9": "/usr/local/bin/f2py3.9", "ace2sam": "/usr/local/bin/ace2sam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/parascopy.
shpc-registry automated BioContainers addition for parascopy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/parascopy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/parascopy:1.11.0--py38h0517ac9_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/parascopy/1.11.0--py38h0517ac9_1
$ module help quay.io/biocontainers/parascopy/1.11.0--py38h0517ac9_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### parascopy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### parascopy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### parascopy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### parascopy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### parascopy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### parascopy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _parascopy_freebayes

```bash
$ singularity exec <container> /usr/local/bin/_parascopy_freebayes
$ podman run --it --rm --entrypoint /usr/local/bin/_parascopy_freebayes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_parascopy_freebayes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parascopy

```bash
$ singularity exec <container> /usr/local/bin/parascopy
$ podman run --it --rm --entrypoint /usr/local/bin/parascopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parascopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix++

```bash
$ singularity exec <container> /usr/local/bin/tabix++
$ podman run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
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