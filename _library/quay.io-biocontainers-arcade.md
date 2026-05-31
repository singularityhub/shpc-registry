---
layout: container
name:  "quay.io/biocontainers/arcade"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arcade/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arcade/container.yaml"
updated_at: "2026-05-31 06:36:06.646171"
latest: "1.0.17--hf426362_0"
container_url: "https://biocontainers.pro/tools/arcade"
aliases:
 - "arcade"
 - "call_chets"
 - "count_by_gene"
 - "encode_vcf"
 - "filter_pp"
 - "filter_vcf_by_pp"
 - "interpret_phase"
 - "make_pseudo_vcf"
 - "orthogonalize"
 - "recode"
 - "ref-cache"
 - "annot-tsv"
 - "transform"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0.17--hf426362_0"
description: "singularity registry hpc automated addition for arcade"
config: {"url": "https://biocontainers.pro/tools/arcade", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for arcade", "latest": {"1.0.17--hf426362_0": "sha256:3820553c26498b97a4c817a93a3374dcfc7147443ae230bbc3472e1ebcd03289"}, "tags": {"1.0.17--hf426362_0": "sha256:3820553c26498b97a4c817a93a3374dcfc7147443ae230bbc3472e1ebcd03289"}, "docker": "quay.io/biocontainers/arcade", "aliases": {"arcade": "/usr/local/bin/arcade", "call_chets": "/usr/local/bin/call_chets", "count_by_gene": "/usr/local/bin/count_by_gene", "encode_vcf": "/usr/local/bin/encode_vcf", "filter_pp": "/usr/local/bin/filter_pp", "filter_vcf_by_pp": "/usr/local/bin/filter_vcf_by_pp", "interpret_phase": "/usr/local/bin/interpret_phase", "make_pseudo_vcf": "/usr/local/bin/make_pseudo_vcf", "orthogonalize": "/usr/local/bin/orthogonalize", "recode": "/usr/local/bin/recode", "ref-cache": "/usr/local/bin/ref-cache", "annot-tsv": "/usr/local/bin/annot-tsv", "transform": "/usr/local/bin/transform", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arcade.
singularity registry hpc automated addition for arcade
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arcade
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arcade:1.0.17--hf426362_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arcade/1.0.17--hf426362_0
$ module help quay.io/biocontainers/arcade/1.0.17--hf426362_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arcade-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arcade-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arcade-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arcade-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arcade-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arcade-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arcade

```bash
$ singularity exec <container> /usr/local/bin/arcade
$ podman run --it --rm --entrypoint /usr/local/bin/arcade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arcade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### call_chets

```bash
$ singularity exec <container> /usr/local/bin/call_chets
$ podman run --it --rm --entrypoint /usr/local/bin/call_chets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/call_chets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count_by_gene

```bash
$ singularity exec <container> /usr/local/bin/count_by_gene
$ podman run --it --rm --entrypoint /usr/local/bin/count_by_gene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count_by_gene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### encode_vcf

```bash
$ singularity exec <container> /usr/local/bin/encode_vcf
$ podman run --it --rm --entrypoint /usr/local/bin/encode_vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/encode_vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_pp

```bash
$ singularity exec <container> /usr/local/bin/filter_pp
$ podman run --it --rm --entrypoint /usr/local/bin/filter_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_vcf_by_pp

```bash
$ singularity exec <container> /usr/local/bin/filter_vcf_by_pp
$ podman run --it --rm --entrypoint /usr/local/bin/filter_vcf_by_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_vcf_by_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpret_phase

```bash
$ singularity exec <container> /usr/local/bin/interpret_phase
$ podman run --it --rm --entrypoint /usr/local/bin/interpret_phase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpret_phase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_pseudo_vcf

```bash
$ singularity exec <container> /usr/local/bin/make_pseudo_vcf
$ podman run --it --rm --entrypoint /usr/local/bin/make_pseudo_vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_pseudo_vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthogonalize

```bash
$ singularity exec <container> /usr/local/bin/orthogonalize
$ podman run --it --rm --entrypoint /usr/local/bin/orthogonalize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthogonalize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### recode

```bash
$ singularity exec <container> /usr/local/bin/recode
$ podman run --it --rm --entrypoint /usr/local/bin/recode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transform

```bash
$ singularity exec <container> /usr/local/bin/transform
$ podman run --it --rm --entrypoint /usr/local/bin/transform   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transform   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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