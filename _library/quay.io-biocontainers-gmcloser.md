---
layout: container
name:  "quay.io/biocontainers/gmcloser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gmcloser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gmcloser/container.yaml"
updated_at: "2024-03-18 23:24:34.784581"
latest: "1.6.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/gmcloser"
aliases:
 - "Nucmer_contig_align.pl"
 - "Nucmer_contig_validate.pl"
 - "Nucmer_scaf_validate.pl"
 - "Nucmer_subcontig_validate.pl"
 - "connect_subcontigs_GMcloser2.pl"
 - "correct_contigs_coords.pl"
 - "correct_scafs_coords.pl"
 - "correct_subcontigs_coords.pl"
 - "coval-filter-short.pl"
 - "gmcloser"
 - "gmcloser-blast-LR-MT.pl"
 - "gmcloser-blast.pl"
 - "gmcloser-nucmer.pl"
 - "gmvalue"
 - "gmvalue.utl"
 - "split_scaffolds_to_subcontigs.pl"
 - "mapview"
 - "mgaps"
 - "run-mummer1"
 - "run-mummer3"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
 - "mummer"
 - "mummerplot"
versions:
 - "1.6.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for gmcloser"
config: {"url": "https://biocontainers.pro/tools/gmcloser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gmcloser", "latest": {"1.6.2--hdfd78af_1": "sha256:928ebaf71afe4fe0c1f6b36c0a2fd25f6c803f865fe0bb5e56703312fef9d7c1"}, "tags": {"1.6.2--hdfd78af_1": "sha256:928ebaf71afe4fe0c1f6b36c0a2fd25f6c803f865fe0bb5e56703312fef9d7c1"}, "docker": "quay.io/biocontainers/gmcloser", "aliases": {"Nucmer_contig_align.pl": "/usr/local/bin/Nucmer_contig_align.pl", "Nucmer_contig_validate.pl": "/usr/local/bin/Nucmer_contig_validate.pl", "Nucmer_scaf_validate.pl": "/usr/local/bin/Nucmer_scaf_validate.pl", "Nucmer_subcontig_validate.pl": "/usr/local/bin/Nucmer_subcontig_validate.pl", "connect_subcontigs_GMcloser2.pl": "/usr/local/bin/connect_subcontigs_GMcloser2.pl", "correct_contigs_coords.pl": "/usr/local/bin/correct_contigs_coords.pl", "correct_scafs_coords.pl": "/usr/local/bin/correct_scafs_coords.pl", "correct_subcontigs_coords.pl": "/usr/local/bin/correct_subcontigs_coords.pl", "coval-filter-short.pl": "/usr/local/bin/coval-filter-short.pl", "gmcloser": "/usr/local/bin/gmcloser", "gmcloser-blast-LR-MT.pl": "/usr/local/bin/gmcloser-blast-LR-MT.pl", "gmcloser-blast.pl": "/usr/local/bin/gmcloser-blast.pl", "gmcloser-nucmer.pl": "/usr/local/bin/gmcloser-nucmer.pl", "gmvalue": "/usr/local/bin/gmvalue", "gmvalue.utl": "/usr/local/bin/gmvalue.utl", "split_scaffolds_to_subcontigs.pl": "/usr/local/bin/split_scaffolds_to_subcontigs.pl", "mapview": "/usr/local/bin/mapview", "mgaps": "/usr/local/bin/mgaps", "run-mummer1": "/usr/local/bin/run-mummer1", "run-mummer3": "/usr/local/bin/run-mummer3", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems", "mummer": "/usr/local/bin/mummer", "mummerplot": "/usr/local/bin/mummerplot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gmcloser.
shpc-registry automated BioContainers addition for gmcloser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gmcloser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gmcloser:1.6.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gmcloser/1.6.2--hdfd78af_1
$ module help quay.io/biocontainers/gmcloser/1.6.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gmcloser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gmcloser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gmcloser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gmcloser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gmcloser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gmcloser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Nucmer_contig_align.pl

```bash
$ singularity exec <container> /usr/local/bin/Nucmer_contig_align.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Nucmer_contig_align.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Nucmer_contig_align.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Nucmer_contig_validate.pl

```bash
$ singularity exec <container> /usr/local/bin/Nucmer_contig_validate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Nucmer_contig_validate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Nucmer_contig_validate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Nucmer_scaf_validate.pl

```bash
$ singularity exec <container> /usr/local/bin/Nucmer_scaf_validate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Nucmer_scaf_validate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Nucmer_scaf_validate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Nucmer_subcontig_validate.pl

```bash
$ singularity exec <container> /usr/local/bin/Nucmer_subcontig_validate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Nucmer_subcontig_validate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Nucmer_subcontig_validate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### connect_subcontigs_GMcloser2.pl

```bash
$ singularity exec <container> /usr/local/bin/connect_subcontigs_GMcloser2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/connect_subcontigs_GMcloser2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/connect_subcontigs_GMcloser2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correct_contigs_coords.pl

```bash
$ singularity exec <container> /usr/local/bin/correct_contigs_coords.pl
$ podman run --it --rm --entrypoint /usr/local/bin/correct_contigs_coords.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correct_contigs_coords.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correct_scafs_coords.pl

```bash
$ singularity exec <container> /usr/local/bin/correct_scafs_coords.pl
$ podman run --it --rm --entrypoint /usr/local/bin/correct_scafs_coords.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correct_scafs_coords.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correct_subcontigs_coords.pl

```bash
$ singularity exec <container> /usr/local/bin/correct_subcontigs_coords.pl
$ podman run --it --rm --entrypoint /usr/local/bin/correct_subcontigs_coords.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correct_subcontigs_coords.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coval-filter-short.pl

```bash
$ singularity exec <container> /usr/local/bin/coval-filter-short.pl
$ podman run --it --rm --entrypoint /usr/local/bin/coval-filter-short.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coval-filter-short.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmcloser

```bash
$ singularity exec <container> /usr/local/bin/gmcloser
$ podman run --it --rm --entrypoint /usr/local/bin/gmcloser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmcloser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmcloser-blast-LR-MT.pl

```bash
$ singularity exec <container> /usr/local/bin/gmcloser-blast-LR-MT.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gmcloser-blast-LR-MT.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmcloser-blast-LR-MT.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmcloser-blast.pl

```bash
$ singularity exec <container> /usr/local/bin/gmcloser-blast.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gmcloser-blast.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmcloser-blast.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmcloser-nucmer.pl

```bash
$ singularity exec <container> /usr/local/bin/gmcloser-nucmer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gmcloser-nucmer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmcloser-nucmer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmvalue

```bash
$ singularity exec <container> /usr/local/bin/gmvalue
$ podman run --it --rm --entrypoint /usr/local/bin/gmvalue   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmvalue   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmvalue.utl

```bash
$ singularity exec <container> /usr/local/bin/gmvalue.utl
$ podman run --it --rm --entrypoint /usr/local/bin/gmvalue.utl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmvalue.utl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_scaffolds_to_subcontigs.pl

```bash
$ singularity exec <container> /usr/local/bin/split_scaffolds_to_subcontigs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/split_scaffolds_to_subcontigs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_scaffolds_to_subcontigs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapview

```bash
$ singularity exec <container> /usr/local/bin/mapview
$ podman run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgaps

```bash
$ singularity exec <container> /usr/local/bin/mgaps
$ podman run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer1

```bash
$ singularity exec <container> /usr/local/bin/run-mummer1
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer3

```bash
$ singularity exec <container> /usr/local/bin/run-mummer3
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummer

```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummerplot

```bash
$ singularity exec <container> /usr/local/bin/mummerplot
$ podman run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
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