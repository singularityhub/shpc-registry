---
layout: container
name:  "quay.io/biocontainers/rnftools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnftools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rnftools/container.yaml"
updated_at: "2022-11-11 00:57:32.832638"
latest: "0.3.1.3--py36_0"
container_url: "https://biocontainers.pro/tools/rnftools"
aliases:
 - "art_454"
 - "art_SOLiD"
 - "art_illumina"
 - "cairosvg"
 - "curesim"
 - "dwgsim"
 - "dwgsim_eval"
 - "mason_frag_sequencing"
 - "mason_genome"
 - "mason_materializer"
 - "mason_methylation"
 - "mason_simulator"
 - "mason_splicing"
 - "mason_variator"
 - "rnftools"
 - "svg42pdf"
 - "gnuplot"
 - "gifecho"
 - "gifinto"
 - "gdlib-config"
 - "snakemake"
 - "snakemake-bash-completion"
 - "b2sum"
 - "base32"
 - "base64"
 - "basename"
versions:
 - "0.3.1.3--py36_0"
description: "shpc-registry automated BioContainers addition for rnftools"
config: {"url": "https://biocontainers.pro/tools/rnftools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnftools", "latest": {"0.3.1.3--py36_0": "sha256:8b588055977bbf83116f394d755c088c885b37b2ccce0b81d50b2d87ba0d2f29"}, "tags": {"0.3.1.3--py36_0": "sha256:8b588055977bbf83116f394d755c088c885b37b2ccce0b81d50b2d87ba0d2f29"}, "docker": "quay.io/biocontainers/rnftools", "aliases": {"art_454": "/usr/local/bin/art_454", "art_SOLiD": "/usr/local/bin/art_SOLiD", "art_illumina": "/usr/local/bin/art_illumina", "cairosvg": "/usr/local/bin/cairosvg", "curesim": "/usr/local/bin/curesim", "dwgsim": "/usr/local/bin/dwgsim", "dwgsim_eval": "/usr/local/bin/dwgsim_eval", "mason_frag_sequencing": "/usr/local/bin/mason_frag_sequencing", "mason_genome": "/usr/local/bin/mason_genome", "mason_materializer": "/usr/local/bin/mason_materializer", "mason_methylation": "/usr/local/bin/mason_methylation", "mason_simulator": "/usr/local/bin/mason_simulator", "mason_splicing": "/usr/local/bin/mason_splicing", "mason_variator": "/usr/local/bin/mason_variator", "rnftools": "/usr/local/bin/rnftools", "svg42pdf": "/usr/local/bin/svg42pdf", "gnuplot": "/usr/local/bin/gnuplot", "gifecho": "/usr/local/bin/gifecho", "gifinto": "/usr/local/bin/gifinto", "gdlib-config": "/usr/local/bin/gdlib-config", "snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnftools.
shpc-registry automated BioContainers addition for rnftools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnftools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnftools:0.3.1.3--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnftools/0.3.1.3--py36_0
$ module help quay.io/biocontainers/rnftools/0.3.1.3--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnftools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnftools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnftools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnftools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnftools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnftools-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### cairosvg

```bash
$ singularity exec <container> /usr/local/bin/cairosvg
$ podman run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curesim

```bash
$ singularity exec <container> /usr/local/bin/curesim
$ podman run --it --rm --entrypoint /usr/local/bin/curesim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curesim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwgsim

```bash
$ singularity exec <container> /usr/local/bin/dwgsim
$ podman run --it --rm --entrypoint /usr/local/bin/dwgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwgsim_eval

```bash
$ singularity exec <container> /usr/local/bin/dwgsim_eval
$ podman run --it --rm --entrypoint /usr/local/bin/dwgsim_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwgsim_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_frag_sequencing

```bash
$ singularity exec <container> /usr/local/bin/mason_frag_sequencing
$ podman run --it --rm --entrypoint /usr/local/bin/mason_frag_sequencing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_frag_sequencing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_genome

```bash
$ singularity exec <container> /usr/local/bin/mason_genome
$ podman run --it --rm --entrypoint /usr/local/bin/mason_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_materializer

```bash
$ singularity exec <container> /usr/local/bin/mason_materializer
$ podman run --it --rm --entrypoint /usr/local/bin/mason_materializer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_materializer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_methylation

```bash
$ singularity exec <container> /usr/local/bin/mason_methylation
$ podman run --it --rm --entrypoint /usr/local/bin/mason_methylation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_methylation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_simulator

```bash
$ singularity exec <container> /usr/local/bin/mason_simulator
$ podman run --it --rm --entrypoint /usr/local/bin/mason_simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_splicing

```bash
$ singularity exec <container> /usr/local/bin/mason_splicing
$ podman run --it --rm --entrypoint /usr/local/bin/mason_splicing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_splicing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_variator

```bash
$ singularity exec <container> /usr/local/bin/mason_variator
$ podman run --it --rm --entrypoint /usr/local/bin/mason_variator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_variator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnftools

```bash
$ singularity exec <container> /usr/local/bin/rnftools
$ podman run --it --rm --entrypoint /usr/local/bin/rnftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svg42pdf

```bash
$ singularity exec <container> /usr/local/bin/svg42pdf
$ podman run --it --rm --entrypoint /usr/local/bin/svg42pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svg42pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnuplot

```bash
$ singularity exec <container> /usr/local/bin/gnuplot
$ podman run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifecho

```bash
$ singularity exec <container> /usr/local/bin/gifecho
$ podman run --it --rm --entrypoint /usr/local/bin/gifecho   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifecho   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifinto

```bash
$ singularity exec <container> /usr/local/bin/gifinto
$ podman run --it --rm --entrypoint /usr/local/bin/gifinto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifinto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake-bash-completion

```bash
$ singularity exec <container> /usr/local/bin/snakemake-bash-completion
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base64

```bash
$ singularity exec <container> /usr/local/bin/base64
$ podman run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basename

```bash
$ singularity exec <container> /usr/local/bin/basename
$ podman run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
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