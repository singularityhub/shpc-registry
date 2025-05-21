---
layout: container
name:  "quay.io/biocontainers/transposonpsi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transposonpsi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/transposonpsi/container.yaml"
updated_at: "2025-05-21 03:45:26.307488"
latest: "1.0.0--hdfd78af_3"
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
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
 - "copymat"
 - "fastacmd"
 - "formatdb"
 - "formatrpsdb"
 - "impala"
 - "makemat"
versions:
 - "1.0.0--hdfd78af_2"
 - "1.0.0--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for transposonpsi"
config: {"url": "https://biocontainers.pro/tools/transposonpsi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for transposonpsi", "latest": {"1.0.0--hdfd78af_3": "sha256:c54fa49382dd74bfd2ef0bf927afd23c2b859f04cb3cf319a1bc86228bb4b6c3"}, "tags": {"1.0.0--hdfd78af_2": "sha256:4d8f7db74586ba17230b160c77895aa1ab34cc87f1d44ce367bd0a5c6122dada", "1.0.0--hdfd78af_3": "sha256:c54fa49382dd74bfd2ef0bf927afd23c2b859f04cb3cf319a1bc86228bb4b6c3"}, "docker": "quay.io/biocontainers/transposonpsi", "aliases": {"BPbtab": "/usr/local/bin/BPbtab", "TBLASTN_hit_chainer.pl": "/usr/local/bin/TBLASTN_hit_chainer.pl", "TBLASTN_hit_chainer_nonoverlapping_genome_DP_extraction.pl": "/usr/local/bin/TBLASTN_hit_chainer_nonoverlapping_genome_DP_extraction.pl", "TPSI_btab_to_gff3.pl": "/usr/local/bin/TPSI_btab_to_gff3.pl", "TPSI_chains_to_fasta.pl": "/usr/local/bin/TPSI_chains_to_fasta.pl", "TPSI_chains_to_gff3.pl": "/usr/local/bin/TPSI_chains_to_gff3.pl", "m2fmt_tier_hits.pl": "/usr/local/bin/m2fmt_tier_hits.pl", "transposonPSI.pl": "/usr/local/bin/transposonPSI.pl", "transposon_db_m2fmt_to_gff3.pl": "/usr/local/bin/transposon_db_m2fmt_to_gff3.pl", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp", "copymat": "/usr/local/bin/copymat", "fastacmd": "/usr/local/bin/fastacmd", "formatdb": "/usr/local/bin/formatdb", "formatrpsdb": "/usr/local/bin/formatrpsdb", "impala": "/usr/local/bin/impala", "makemat": "/usr/local/bin/makemat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transposonpsi.
shpc-registry automated BioContainers addition for transposonpsi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transposonpsi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transposonpsi:1.0.0--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transposonpsi/1.0.0--hdfd78af_3
$ module help quay.io/biocontainers/transposonpsi/1.0.0--hdfd78af_3
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


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copymat

```bash
$ singularity exec <container> /usr/local/bin/copymat
$ podman run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacmd

```bash
$ singularity exec <container> /usr/local/bin/fastacmd
$ podman run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatdb

```bash
$ singularity exec <container> /usr/local/bin/formatdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatrpsdb

```bash
$ singularity exec <container> /usr/local/bin/formatrpsdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### impala

```bash
$ singularity exec <container> /usr/local/bin/impala
$ podman run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makemat

```bash
$ singularity exec <container> /usr/local/bin/makemat
$ podman run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
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