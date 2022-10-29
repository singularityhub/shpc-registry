---
layout: container
name:  "quay.io/biocontainers/transposonpsi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transposonpsi/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/transposonpsi/container.yaml"
updated_at: "2022-10-29 05:30:33.811481"
latest: "1.0.0--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/transposonpsi"
aliases:
 - "BPbtab"
 - "TBLASTN_hit_chainer.pl"
 - "TBLASTN_hit_chainer_nonoverlapping_genome_DP_extraction.pl"
 - "TPSI_btab_to_gff3.pl"
 - "TPSI_chains_to_fasta.pl"
 - "TPSI_chains_to_gff3.pl"
 - "m2fmt_tier_hits.pl"
 - "transposonPSI.pl"
 - "transposon_db_m2fmt_to_gff3.pl"
 - "2to3-3.7"
 - "SOAPsh.pl"
 - "ace.pl"
 - "acyclic"
 - "annotate"
 - "bam2bedgraph"
 - "bamToGBrowse.pl"
 - "baseml"
 - "basemlg"
 - "bcomps"
versions:
 - "1.0.0--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for transposonpsi"
config: {"url": "https://biocontainers.pro/tools/transposonpsi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for transposonpsi", "latest": {"1.0.0--hdfd78af_2": "sha256:4d8f7db74586ba17230b160c77895aa1ab34cc87f1d44ce367bd0a5c6122dada"}, "tags": {"1.0.0--hdfd78af_2": "sha256:4d8f7db74586ba17230b160c77895aa1ab34cc87f1d44ce367bd0a5c6122dada"}, "docker": "quay.io/biocontainers/transposonpsi", "aliases": {"BPbtab": "/usr/local/bin/BPbtab", "TBLASTN_hit_chainer.pl": "/usr/local/bin/TBLASTN_hit_chainer.pl", "TBLASTN_hit_chainer_nonoverlapping_genome_DP_extraction.pl": "/usr/local/bin/TBLASTN_hit_chainer_nonoverlapping_genome_DP_extraction.pl", "TPSI_btab_to_gff3.pl": "/usr/local/bin/TPSI_btab_to_gff3.pl", "TPSI_chains_to_fasta.pl": "/usr/local/bin/TPSI_chains_to_fasta.pl", "TPSI_chains_to_gff3.pl": "/usr/local/bin/TPSI_chains_to_gff3.pl", "m2fmt_tier_hits.pl": "/usr/local/bin/m2fmt_tier_hits.pl", "transposonPSI.pl": "/usr/local/bin/transposonPSI.pl", "transposon_db_m2fmt_to_gff3.pl": "/usr/local/bin/transposon_db_m2fmt_to_gff3.pl", "2to3-3.7": "/usr/local/bin/2to3-3.7", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "ace.pl": "/usr/local/bin/ace.pl", "acyclic": "/usr/local/bin/acyclic", "annotate": "/usr/local/bin/annotate", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bamToGBrowse.pl": "/usr/local/bin/bamToGBrowse.pl", "baseml": "/usr/local/bin/baseml", "basemlg": "/usr/local/bin/basemlg", "bcomps": "/usr/local/bin/bcomps"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transposonpsi.
shpc-registry automated BioContainers addition for transposonpsi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transposonpsi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transposonpsi:1.0.0--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transposonpsi/1.0.0--hdfd78af_2
$ module help quay.io/biocontainers/transposonpsi/1.0.0--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transposonpsi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transposonpsi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transposonpsi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transposonpsi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transposonpsi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transposonpsi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BPbtab

```bash
$ singularity exec <container> /usr/local/bin/BPbtab
$ podman run --it --rm --entrypoint /usr/local/bin/BPbtab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BPbtab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TBLASTN_hit_chainer.pl

```bash
$ singularity exec <container> /usr/local/bin/TBLASTN_hit_chainer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/TBLASTN_hit_chainer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TBLASTN_hit_chainer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TBLASTN_hit_chainer_nonoverlapping_genome_DP_extraction.pl

```bash
$ singularity exec <container> /usr/local/bin/TBLASTN_hit_chainer_nonoverlapping_genome_DP_extraction.pl
$ podman run --it --rm --entrypoint /usr/local/bin/TBLASTN_hit_chainer_nonoverlapping_genome_DP_extraction.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TBLASTN_hit_chainer_nonoverlapping_genome_DP_extraction.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TPSI_btab_to_gff3.pl

```bash
$ singularity exec <container> /usr/local/bin/TPSI_btab_to_gff3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/TPSI_btab_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TPSI_btab_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TPSI_chains_to_fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/TPSI_chains_to_fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/TPSI_chains_to_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TPSI_chains_to_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TPSI_chains_to_gff3.pl

```bash
$ singularity exec <container> /usr/local/bin/TPSI_chains_to_gff3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/TPSI_chains_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TPSI_chains_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m2fmt_tier_hits.pl

```bash
$ singularity exec <container> /usr/local/bin/m2fmt_tier_hits.pl
$ podman run --it --rm --entrypoint /usr/local/bin/m2fmt_tier_hits.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m2fmt_tier_hits.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transposonPSI.pl

```bash
$ singularity exec <container> /usr/local/bin/transposonPSI.pl
$ podman run --it --rm --entrypoint /usr/local/bin/transposonPSI.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transposonPSI.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transposon_db_m2fmt_to_gff3.pl

```bash
$ singularity exec <container> /usr/local/bin/transposon_db_m2fmt_to_gff3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/transposon_db_m2fmt_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transposon_db_m2fmt_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToGBrowse.pl

```bash
$ singularity exec <container> /usr/local/bin/bamToGBrowse.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bamToGBrowse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToGBrowse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baseml

```bash
$ singularity exec <container> /usr/local/bin/baseml
$ podman run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basemlg

```bash
$ singularity exec <container> /usr/local/bin/basemlg
$ podman run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
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