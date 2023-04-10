---
layout: container
name:  "quay.io/biocontainers/fsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fsa/container.yaml"
updated_at: "2023-04-10 03:13:51.921180"
latest: "1.15.9--h5b5514e_3"
container_url: "https://biocontainers.pro/tools/fsa"
aliases:
 - "fsa"
 - "gapcleaner"
 - "isect_mercator_alignment_gff"
 - "map_coords"
 - "map_gff_coords"
 - "percentid"
 - "prot2codon"
 - "slice_fasta"
 - "slice_fasta_gff"
 - "slice_mercator_alignment"
 - "translate"
versions:
 - "1.15.9--h5b5514e_3"
description: "shpc-registry automated BioContainers addition for fsa"
config: {"url": "https://biocontainers.pro/tools/fsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fsa", "latest": {"1.15.9--h5b5514e_3": "sha256:63a805cfa5a45173df51bfa614fd1fde0044f4e83027a8e526afe2efab0472aa"}, "tags": {"1.15.9--h5b5514e_3": "sha256:63a805cfa5a45173df51bfa614fd1fde0044f4e83027a8e526afe2efab0472aa"}, "docker": "quay.io/biocontainers/fsa", "aliases": {"fsa": "/usr/local/bin/fsa", "gapcleaner": "/usr/local/bin/gapcleaner", "isect_mercator_alignment_gff": "/usr/local/bin/isect_mercator_alignment_gff", "map_coords": "/usr/local/bin/map_coords", "map_gff_coords": "/usr/local/bin/map_gff_coords", "percentid": "/usr/local/bin/percentid", "prot2codon": "/usr/local/bin/prot2codon", "slice_fasta": "/usr/local/bin/slice_fasta", "slice_fasta_gff": "/usr/local/bin/slice_fasta_gff", "slice_mercator_alignment": "/usr/local/bin/slice_mercator_alignment", "translate": "/usr/local/bin/translate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fsa.
shpc-registry automated BioContainers addition for fsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fsa:1.15.9--h5b5514e_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fsa/1.15.9--h5b5514e_3
$ module help quay.io/biocontainers/fsa/1.15.9--h5b5514e_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fsa

```bash
$ singularity exec <container> /usr/local/bin/fsa
$ podman run --it --rm --entrypoint /usr/local/bin/fsa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fsa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gapcleaner

```bash
$ singularity exec <container> /usr/local/bin/gapcleaner
$ podman run --it --rm --entrypoint /usr/local/bin/gapcleaner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gapcleaner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isect_mercator_alignment_gff

```bash
$ singularity exec <container> /usr/local/bin/isect_mercator_alignment_gff
$ podman run --it --rm --entrypoint /usr/local/bin/isect_mercator_alignment_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isect_mercator_alignment_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_coords

```bash
$ singularity exec <container> /usr/local/bin/map_coords
$ podman run --it --rm --entrypoint /usr/local/bin/map_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_gff_coords

```bash
$ singularity exec <container> /usr/local/bin/map_gff_coords
$ podman run --it --rm --entrypoint /usr/local/bin/map_gff_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_gff_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### percentid

```bash
$ singularity exec <container> /usr/local/bin/percentid
$ podman run --it --rm --entrypoint /usr/local/bin/percentid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/percentid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prot2codon

```bash
$ singularity exec <container> /usr/local/bin/prot2codon
$ podman run --it --rm --entrypoint /usr/local/bin/prot2codon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prot2codon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slice_fasta

```bash
$ singularity exec <container> /usr/local/bin/slice_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/slice_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slice_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slice_fasta_gff

```bash
$ singularity exec <container> /usr/local/bin/slice_fasta_gff
$ podman run --it --rm --entrypoint /usr/local/bin/slice_fasta_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slice_fasta_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slice_mercator_alignment

```bash
$ singularity exec <container> /usr/local/bin/slice_mercator_alignment
$ podman run --it --rm --entrypoint /usr/local/bin/slice_mercator_alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slice_mercator_alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### translate

```bash
$ singularity exec <container> /usr/local/bin/translate
$ podman run --it --rm --entrypoint /usr/local/bin/translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/translate   -v ${PWD} -w ${PWD} <container> -c " $@"
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