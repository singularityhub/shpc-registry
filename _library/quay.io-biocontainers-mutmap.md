---
layout: container
name:  "quay.io/biocontainers/mutmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mutmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mutmap/container.yaml"
updated_at: "2025-09-18 03:21:16.321550"
latest: "2.3.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mutmap"
aliases:
 - "mutmap"
 - "mutplot"
 - "snpEff"
 - "trimmomatic"
 - "gff2gff.py"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
versions:
 - "2.3.3--pyhdfd78af_0"
 - "2.3.4--pyhdfd78af_0"
 - "2.3.8--pyhdfd78af_0"
 - "2.3.9--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for mutmap"
config: {"url": "https://biocontainers.pro/tools/mutmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mutmap", "latest": {"2.3.9--pyhdfd78af_0": "sha256:d9b71ae08fe22690a1fa6ae2b8d8bd56488a6a52023bc2184dcda132d1593036"}, "tags": {"2.3.3--pyhdfd78af_0": "sha256:c69c1cf7d39e7ff78811ce40ddca79b21219641aada2627b916e9790bdf48158", "2.3.4--pyhdfd78af_0": "sha256:20977094657505a683cefc2203b9ac3a074e5e75fefeeea489b1c647236464a1", "2.3.8--pyhdfd78af_0": "sha256:3de055302066c7a1ed5de6bf97ac95e258163e4f1f73bf068e87ef6f5c51835b", "2.3.9--pyhdfd78af_0": "sha256:d9b71ae08fe22690a1fa6ae2b8d8bd56488a6a52023bc2184dcda132d1593036"}, "docker": "quay.io/biocontainers/mutmap", "aliases": {"mutmap": "/usr/local/bin/mutmap", "mutplot": "/usr/local/bin/mutplot", "snpEff": "/usr/local/bin/snpEff", "trimmomatic": "/usr/local/bin/trimmomatic", "gff2gff.py": "/usr/local/bin/gff2gff.py", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mutmap.
shpc-registry automated BioContainers addition for mutmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mutmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mutmap:2.3.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mutmap/2.3.9--pyhdfd78af_0
$ module help quay.io/biocontainers/mutmap/2.3.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mutmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mutmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mutmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mutmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mutmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mutmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mutmap

```bash
$ singularity exec <container> /usr/local/bin/mutmap
$ podman run --it --rm --entrypoint /usr/local/bin/mutmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutplot

```bash
$ singularity exec <container> /usr/local/bin/mutplot
$ podman run --it --rm --entrypoint /usr/local/bin/mutplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpEff

```bash
$ singularity exec <container> /usr/local/bin/snpEff
$ podman run --it --rm --entrypoint /usr/local/bin/snpEff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpEff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmomatic

```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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