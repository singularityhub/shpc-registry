---
layout: container
name:  "quay.io/biocontainers/pirate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pirate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pirate/container.yaml"
updated_at: "2023-05-30 02:49:55.421155"
latest: "1.0.5--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pirate"
aliases:
 - "PIRATE"
 - "PIRATE_to_Rtab.pl"
 - "PIRATE_to_roary.pl"
 - "analyse_blast_outputs.pl"
 - "analyse_loci_list.pl"
 - "annotate_treeWAS_output.pl"
 - "convert_to_distmat.pl"
 - "convert_to_treeWAS.pl"
 - "create_pangenome_alignment_aa.pl"
 - "pangenome_variants_to_treeWAS.pl"
 - "paralogs_to_Rtab.pl"
 - "select_representative"
 - "subsample_outputs.pl"
 - "subset_alignments.pl"
 - "unique_sequences.pl"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "mcl"
 - "mclblastline"
 - "mclcm"
 - "mclpipeline"
 - "mcx"
 - "mcxarray"
 - "mcxassemble"
versions:
 - "1.0.5--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for pirate"
config: {"url": "https://biocontainers.pro/tools/pirate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pirate", "latest": {"1.0.5--hdfd78af_0": "sha256:2e365e2fa46c6185c30feba261d5a30fa991c937646e4b3506ad470994175ea0"}, "tags": {"1.0.5--hdfd78af_0": "sha256:2e365e2fa46c6185c30feba261d5a30fa991c937646e4b3506ad470994175ea0"}, "docker": "quay.io/biocontainers/pirate", "aliases": {"PIRATE": "/usr/local/bin/PIRATE", "PIRATE_to_Rtab.pl": "/usr/local/bin/PIRATE_to_Rtab.pl", "PIRATE_to_roary.pl": "/usr/local/bin/PIRATE_to_roary.pl", "analyse_blast_outputs.pl": "/usr/local/bin/analyse_blast_outputs.pl", "analyse_loci_list.pl": "/usr/local/bin/analyse_loci_list.pl", "annotate_treeWAS_output.pl": "/usr/local/bin/annotate_treeWAS_output.pl", "convert_to_distmat.pl": "/usr/local/bin/convert_to_distmat.pl", "convert_to_treeWAS.pl": "/usr/local/bin/convert_to_treeWAS.pl", "create_pangenome_alignment_aa.pl": "/usr/local/bin/create_pangenome_alignment_aa.pl", "pangenome_variants_to_treeWAS.pl": "/usr/local/bin/pangenome_variants_to_treeWAS.pl", "paralogs_to_Rtab.pl": "/usr/local/bin/paralogs_to_Rtab.pl", "select_representative": "/usr/local/bin/select_representative", "subsample_outputs.pl": "/usr/local/bin/subsample_outputs.pl", "subset_alignments.pl": "/usr/local/bin/subset_alignments.pl", "unique_sequences.pl": "/usr/local/bin/unique_sequences.pl", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray", "mcxassemble": "/usr/local/bin/mcxassemble"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pirate.
shpc-registry automated BioContainers addition for pirate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pirate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pirate:1.0.5--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pirate/1.0.5--hdfd78af_0
$ module help quay.io/biocontainers/pirate/1.0.5--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pirate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pirate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pirate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pirate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pirate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pirate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PIRATE

```bash
$ singularity exec <container> /usr/local/bin/PIRATE
$ podman run --it --rm --entrypoint /usr/local/bin/PIRATE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PIRATE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PIRATE_to_Rtab.pl

```bash
$ singularity exec <container> /usr/local/bin/PIRATE_to_Rtab.pl
$ podman run --it --rm --entrypoint /usr/local/bin/PIRATE_to_Rtab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PIRATE_to_Rtab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PIRATE_to_roary.pl

```bash
$ singularity exec <container> /usr/local/bin/PIRATE_to_roary.pl
$ podman run --it --rm --entrypoint /usr/local/bin/PIRATE_to_roary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PIRATE_to_roary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyse_blast_outputs.pl

```bash
$ singularity exec <container> /usr/local/bin/analyse_blast_outputs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/analyse_blast_outputs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyse_blast_outputs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyse_loci_list.pl

```bash
$ singularity exec <container> /usr/local/bin/analyse_loci_list.pl
$ podman run --it --rm --entrypoint /usr/local/bin/analyse_loci_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyse_loci_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate_treeWAS_output.pl

```bash
$ singularity exec <container> /usr/local/bin/annotate_treeWAS_output.pl
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_treeWAS_output.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_treeWAS_output.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_to_distmat.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_to_distmat.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_to_distmat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_to_distmat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_to_treeWAS.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_to_treeWAS.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_to_treeWAS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_to_treeWAS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_pangenome_alignment_aa.pl

```bash
$ singularity exec <container> /usr/local/bin/create_pangenome_alignment_aa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/create_pangenome_alignment_aa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_pangenome_alignment_aa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pangenome_variants_to_treeWAS.pl

```bash
$ singularity exec <container> /usr/local/bin/pangenome_variants_to_treeWAS.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pangenome_variants_to_treeWAS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pangenome_variants_to_treeWAS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paralogs_to_Rtab.pl

```bash
$ singularity exec <container> /usr/local/bin/paralogs_to_Rtab.pl
$ podman run --it --rm --entrypoint /usr/local/bin/paralogs_to_Rtab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paralogs_to_Rtab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_representative

```bash
$ singularity exec <container> /usr/local/bin/select_representative
$ podman run --it --rm --entrypoint /usr/local/bin/select_representative   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_representative   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subsample_outputs.pl

```bash
$ singularity exec <container> /usr/local/bin/subsample_outputs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/subsample_outputs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subsample_outputs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subset_alignments.pl

```bash
$ singularity exec <container> /usr/local/bin/subset_alignments.pl
$ podman run --it --rm --entrypoint /usr/local/bin/subset_alignments.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subset_alignments.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unique_sequences.pl

```bash
$ singularity exec <container> /usr/local/bin/unique_sequences.pl
$ podman run --it --rm --entrypoint /usr/local/bin/unique_sequences.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unique_sequences.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clmformat

```bash
$ singularity exec <container> /usr/local/bin/clmformat
$ podman run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclblastline

```bash
$ singularity exec <container> /usr/local/bin/mclblastline
$ podman run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclcm

```bash
$ singularity exec <container> /usr/local/bin/mclcm
$ podman run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclpipeline

```bash
$ singularity exec <container> /usr/local/bin/mclpipeline
$ podman run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcx

```bash
$ singularity exec <container> /usr/local/bin/mcx
$ podman run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxarray

```bash
$ singularity exec <container> /usr/local/bin/mcxarray
$ podman run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxassemble

```bash
$ singularity exec <container> /usr/local/bin/mcxassemble
$ podman run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
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