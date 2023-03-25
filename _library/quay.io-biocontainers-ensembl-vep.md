---
layout: container
name:  "quay.io/biocontainers/ensembl-vep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ensembl-vep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ensembl-vep/container.yaml"
updated_at: "2023-03-25 03:12:45.489155"
latest: "98.1--pl526hecc5488_0"
container_url: "https://biocontainers.pro/tools/ensembl-vep"
aliases:
 - "filter_vep"
 - "haplo"
 - "variant_recoder"
 - "vep"
 - "vep_convert_cache"
 - "vep_install"
 - "giffilter"
 - "gifsponge"
 - "unzip"
 - "gifecho"
 - "gifinto"
 - "gdlib-config"
 - "bam2bedgraph"
 - "bp_pairwise_kaks"
 - "bp_find-blast-matches.pl"
 - "t_coffee"
versions:
 - "98.1--pl526hecc5488_0"
description: "shpc-registry automated BioContainers addition for ensembl-vep"
config: {"url": "https://biocontainers.pro/tools/ensembl-vep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ensembl-vep", "latest": {"98.1--pl526hecc5488_0": "sha256:d0c7e20d65a0c58d49589c4fccc6fed5f379001ad4e3f05fe85a727baf2713ad"}, "tags": {"98.1--pl526hecc5488_0": "sha256:d0c7e20d65a0c58d49589c4fccc6fed5f379001ad4e3f05fe85a727baf2713ad"}, "docker": "quay.io/biocontainers/ensembl-vep", "aliases": {"filter_vep": "/usr/local/bin/filter_vep", "haplo": "/usr/local/bin/haplo", "variant_recoder": "/usr/local/bin/variant_recoder", "vep": "/usr/local/bin/vep", "vep_convert_cache": "/usr/local/bin/vep_convert_cache", "vep_install": "/usr/local/bin/vep_install", "giffilter": "/usr/local/bin/giffilter", "gifsponge": "/usr/local/bin/gifsponge", "unzip": "/usr/local/bin/unzip", "gifecho": "/usr/local/bin/gifecho", "gifinto": "/usr/local/bin/gifinto", "gdlib-config": "/usr/local/bin/gdlib-config", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bp_pairwise_kaks": "/usr/local/bin/bp_pairwise_kaks", "bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "t_coffee": "/usr/local/bin/t_coffee"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ensembl-vep.
shpc-registry automated BioContainers addition for ensembl-vep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ensembl-vep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ensembl-vep:98.1--pl526hecc5488_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ensembl-vep/98.1--pl526hecc5488_0
$ module help quay.io/biocontainers/ensembl-vep/98.1--pl526hecc5488_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ensembl-vep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ensembl-vep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ensembl-vep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ensembl-vep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ensembl-vep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ensembl-vep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### filter_vep

```bash
$ singularity exec <container> /usr/local/bin/filter_vep
$ podman run --it --rm --entrypoint /usr/local/bin/filter_vep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_vep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haplo

```bash
$ singularity exec <container> /usr/local/bin/haplo
$ podman run --it --rm --entrypoint /usr/local/bin/haplo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haplo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### variant_recoder

```bash
$ singularity exec <container> /usr/local/bin/variant_recoder
$ podman run --it --rm --entrypoint /usr/local/bin/variant_recoder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variant_recoder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep

```bash
$ singularity exec <container> /usr/local/bin/vep
$ podman run --it --rm --entrypoint /usr/local/bin/vep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep_convert_cache

```bash
$ singularity exec <container> /usr/local/bin/vep_convert_cache
$ podman run --it --rm --entrypoint /usr/local/bin/vep_convert_cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep_convert_cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep_install

```bash
$ singularity exec <container> /usr/local/bin/vep_install
$ podman run --it --rm --entrypoint /usr/local/bin/vep_install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep_install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffilter

```bash
$ singularity exec <container> /usr/local/bin/giffilter
$ podman run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifsponge

```bash
$ singularity exec <container> /usr/local/bin/gifsponge
$ podman run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzip

```bash
$ singularity exec <container> /usr/local/bin/unzip
$ podman run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t_coffee

```bash
$ singularity exec <container> /usr/local/bin/t_coffee
$ podman run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
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