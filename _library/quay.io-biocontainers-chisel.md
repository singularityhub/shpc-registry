---
layout: container
name:  "quay.io/biocontainers/chisel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chisel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chisel/container.yaml"
updated_at: "2023-01-22 03:46:55.906726"
latest: "1.1.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/chisel"
aliases:
 - "aln2bed.pl"
 - "art_454"
 - "art_SOLiD"
 - "art_illumina"
 - "art_profiler_454"
 - "art_profiler_illumina"
 - "chisel"
 - "chisel_bedding"
 - "chisel_calling"
 - "chisel_cloning"
 - "chisel_nonormal"
 - "chisel_plotting"
 - "chisel_prep"
 - "chisel_pseudonormal"
 - "chisel_rdr"
 - "combinedAvg.pl"
 - "empDist.pl"
 - "fastqReadAvg.pl"
 - "map2bed.pl"
 - "summation.pl"
 - "gff2gff.py"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
versions:
 - "1.1.3--pyhdfd78af_0"
 - "1.1.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for chisel"
config: {"url": "https://biocontainers.pro/tools/chisel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chisel", "latest": {"1.1.4--pyhdfd78af_0": "sha256:42528fd2dccf70a5c37bac984eaf1b06997ffe1e37f877a10cc7b4237d84d03c"}, "tags": {"1.1.3--pyhdfd78af_0": "sha256:6c2c6da2c9563444f1373fe04fe0e85999a4be5c13b92dbfbe717738388f91d6", "1.1.4--pyhdfd78af_0": "sha256:42528fd2dccf70a5c37bac984eaf1b06997ffe1e37f877a10cc7b4237d84d03c"}, "docker": "quay.io/biocontainers/chisel", "aliases": {"aln2bed.pl": "/usr/local/bin/aln2bed.pl", "art_454": "/usr/local/bin/art_454", "art_SOLiD": "/usr/local/bin/art_SOLiD", "art_illumina": "/usr/local/bin/art_illumina", "art_profiler_454": "/usr/local/bin/art_profiler_454", "art_profiler_illumina": "/usr/local/bin/art_profiler_illumina", "chisel": "/usr/local/bin/chisel", "chisel_bedding": "/usr/local/bin/chisel_bedding", "chisel_calling": "/usr/local/bin/chisel_calling", "chisel_cloning": "/usr/local/bin/chisel_cloning", "chisel_nonormal": "/usr/local/bin/chisel_nonormal", "chisel_plotting": "/usr/local/bin/chisel_plotting", "chisel_prep": "/usr/local/bin/chisel_prep", "chisel_pseudonormal": "/usr/local/bin/chisel_pseudonormal", "chisel_rdr": "/usr/local/bin/chisel_rdr", "combinedAvg.pl": "/usr/local/bin/combinedAvg.pl", "empDist.pl": "/usr/local/bin/empDist.pl", "fastqReadAvg.pl": "/usr/local/bin/fastqReadAvg.pl", "map2bed.pl": "/usr/local/bin/map2bed.pl", "summation.pl": "/usr/local/bin/summation.pl", "gff2gff.py": "/usr/local/bin/gff2gff.py", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chisel.
shpc-registry automated BioContainers addition for chisel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chisel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chisel:1.1.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chisel/1.1.4--pyhdfd78af_0
$ module help quay.io/biocontainers/chisel/1.1.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chisel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chisel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chisel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chisel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chisel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chisel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aln2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/aln2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aln2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aln2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### art_454

```bash
$ singularity exec <container> /usr/local/bin/art_454
$ podman run --it --rm --entrypoint /usr/local/bin/art_454   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/art_454   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### art_SOLiD

```bash
$ singularity exec <container> /usr/local/bin/art_SOLiD
$ podman run --it --rm --entrypoint /usr/local/bin/art_SOLiD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/art_SOLiD   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### art_illumina

```bash
$ singularity exec <container> /usr/local/bin/art_illumina
$ podman run --it --rm --entrypoint /usr/local/bin/art_illumina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/art_illumina   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### art_profiler_454

```bash
$ singularity exec <container> /usr/local/bin/art_profiler_454
$ podman run --it --rm --entrypoint /usr/local/bin/art_profiler_454   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/art_profiler_454   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### art_profiler_illumina

```bash
$ singularity exec <container> /usr/local/bin/art_profiler_illumina
$ podman run --it --rm --entrypoint /usr/local/bin/art_profiler_illumina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/art_profiler_illumina   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chisel

```bash
$ singularity exec <container> /usr/local/bin/chisel
$ podman run --it --rm --entrypoint /usr/local/bin/chisel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chisel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chisel_bedding

```bash
$ singularity exec <container> /usr/local/bin/chisel_bedding
$ podman run --it --rm --entrypoint /usr/local/bin/chisel_bedding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chisel_bedding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chisel_calling

```bash
$ singularity exec <container> /usr/local/bin/chisel_calling
$ podman run --it --rm --entrypoint /usr/local/bin/chisel_calling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chisel_calling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chisel_cloning

```bash
$ singularity exec <container> /usr/local/bin/chisel_cloning
$ podman run --it --rm --entrypoint /usr/local/bin/chisel_cloning   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chisel_cloning   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chisel_nonormal

```bash
$ singularity exec <container> /usr/local/bin/chisel_nonormal
$ podman run --it --rm --entrypoint /usr/local/bin/chisel_nonormal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chisel_nonormal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chisel_plotting

```bash
$ singularity exec <container> /usr/local/bin/chisel_plotting
$ podman run --it --rm --entrypoint /usr/local/bin/chisel_plotting   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chisel_plotting   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chisel_prep

```bash
$ singularity exec <container> /usr/local/bin/chisel_prep
$ podman run --it --rm --entrypoint /usr/local/bin/chisel_prep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chisel_prep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chisel_pseudonormal

```bash
$ singularity exec <container> /usr/local/bin/chisel_pseudonormal
$ podman run --it --rm --entrypoint /usr/local/bin/chisel_pseudonormal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chisel_pseudonormal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chisel_rdr

```bash
$ singularity exec <container> /usr/local/bin/chisel_rdr
$ podman run --it --rm --entrypoint /usr/local/bin/chisel_rdr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chisel_rdr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combinedAvg.pl

```bash
$ singularity exec <container> /usr/local/bin/combinedAvg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/combinedAvg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combinedAvg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### empDist.pl

```bash
$ singularity exec <container> /usr/local/bin/empDist.pl
$ podman run --it --rm --entrypoint /usr/local/bin/empDist.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/empDist.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqReadAvg.pl

```bash
$ singularity exec <container> /usr/local/bin/fastqReadAvg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fastqReadAvg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqReadAvg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/map2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/map2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summation.pl

```bash
$ singularity exec <container> /usr/local/bin/summation.pl
$ podman run --it --rm --entrypoint /usr/local/bin/summation.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summation.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
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