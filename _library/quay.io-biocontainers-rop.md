---
layout: container
name:  "quay.io/biocontainers/rop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rop/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rop/container.yaml"
updated_at: "2022-10-29 05:53:16.583280"
latest: "1.1.2--py27heb79e2c_3"
container_url: "https://biocontainers.pro/tools/rop"
aliases:
 - "bam2fastx"
 - "bam_merge"
 - "bed_to_juncs"
 - "contig_to_chr_coords"
 - "fix_map_ordering"
 - "gtf_juncs"
 - "gtf_to_fasta"
 - "juncs_db"
 - "long_spanning_reads"
 - "map2gtf"
 - "prep_reads"
 - "rop"
 - "sam_juncs"
 - "samtools_0.1.18"
 - "segment_juncs"
 - "sra_to_solid"
 - "tophat"
 - "tophat-fusion-post"
 - "tophat2"
 - "tophat_reports"
 - "CA.pm"
 - "accn-at-a-time"
 - "ace2sam"
 - "amino-acid-composition"
 - "archive-pubmed"
 - "asp-cp"
 - "asp-ls"
 - "between-two-genes"
 - "bgzip"
 - "blast2sam.pl"
versions:
 - "1.1.2--py27heb79e2c_3"
description: "shpc-registry automated BioContainers addition for rop"
config: {"url": "https://biocontainers.pro/tools/rop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rop", "latest": {"1.1.2--py27heb79e2c_3": "sha256:faf170b3f75a72462539626a48068207786057f0c00a5d9f23e47a6d94783754"}, "tags": {"1.1.2--py27heb79e2c_3": "sha256:faf170b3f75a72462539626a48068207786057f0c00a5d9f23e47a6d94783754"}, "docker": "quay.io/biocontainers/rop", "aliases": {"bam2fastx": "/usr/local/bin/bam2fastx", "bam_merge": "/usr/local/bin/bam_merge", "bed_to_juncs": "/usr/local/bin/bed_to_juncs", "contig_to_chr_coords": "/usr/local/bin/contig_to_chr_coords", "fix_map_ordering": "/usr/local/bin/fix_map_ordering", "gtf_juncs": "/usr/local/bin/gtf_juncs", "gtf_to_fasta": "/usr/local/bin/gtf_to_fasta", "juncs_db": "/usr/local/bin/juncs_db", "long_spanning_reads": "/usr/local/bin/long_spanning_reads", "map2gtf": "/usr/local/bin/map2gtf", "prep_reads": "/usr/local/bin/prep_reads", "rop": "/usr/local/bin/rop", "sam_juncs": "/usr/local/bin/sam_juncs", "samtools_0.1.18": "/usr/local/bin/samtools_0.1.18", "segment_juncs": "/usr/local/bin/segment_juncs", "sra_to_solid": "/usr/local/bin/sra_to_solid", "tophat": "/usr/local/bin/tophat", "tophat-fusion-post": "/usr/local/bin/tophat-fusion-post", "tophat2": "/usr/local/bin/tophat2", "tophat_reports": "/usr/local/bin/tophat_reports", "CA.pm": "/usr/local/bin/CA.pm", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "ace2sam": "/usr/local/bin/ace2sam", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "archive-pubmed": "/usr/local/bin/archive-pubmed", "asp-cp": "/usr/local/bin/asp-cp", "asp-ls": "/usr/local/bin/asp-ls", "between-two-genes": "/usr/local/bin/between-two-genes", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rop.
shpc-registry automated BioContainers addition for rop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rop:1.1.2--py27heb79e2c_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rop/1.1.2--py27heb79e2c_3
$ module help quay.io/biocontainers/rop/1.1.2--py27heb79e2c_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2fastx

```bash
$ singularity exec <container> /usr/local/bin/bam2fastx
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam_merge

```bash
$ singularity exec <container> /usr/local/bin/bam_merge
$ podman run --it --rm --entrypoint /usr/local/bin/bam_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_to_juncs

```bash
$ singularity exec <container> /usr/local/bin/bed_to_juncs
$ podman run --it --rm --entrypoint /usr/local/bin/bed_to_juncs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_to_juncs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contig_to_chr_coords

```bash
$ singularity exec <container> /usr/local/bin/contig_to_chr_coords
$ podman run --it --rm --entrypoint /usr/local/bin/contig_to_chr_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contig_to_chr_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_map_ordering

```bash
$ singularity exec <container> /usr/local/bin/fix_map_ordering
$ podman run --it --rm --entrypoint /usr/local/bin/fix_map_ordering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_map_ordering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_juncs

```bash
$ singularity exec <container> /usr/local/bin/gtf_juncs
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_juncs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_juncs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_to_fasta

```bash
$ singularity exec <container> /usr/local/bin/gtf_to_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juncs_db

```bash
$ singularity exec <container> /usr/local/bin/juncs_db
$ podman run --it --rm --entrypoint /usr/local/bin/juncs_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juncs_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### long_spanning_reads

```bash
$ singularity exec <container> /usr/local/bin/long_spanning_reads
$ podman run --it --rm --entrypoint /usr/local/bin/long_spanning_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/long_spanning_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map2gtf

```bash
$ singularity exec <container> /usr/local/bin/map2gtf
$ podman run --it --rm --entrypoint /usr/local/bin/map2gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map2gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prep_reads

```bash
$ singularity exec <container> /usr/local/bin/prep_reads
$ podman run --it --rm --entrypoint /usr/local/bin/prep_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prep_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rop

```bash
$ singularity exec <container> /usr/local/bin/rop
$ podman run --it --rm --entrypoint /usr/local/bin/rop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_juncs

```bash
$ singularity exec <container> /usr/local/bin/sam_juncs
$ podman run --it --rm --entrypoint /usr/local/bin/sam_juncs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_juncs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools_0.1.18

```bash
$ singularity exec <container> /usr/local/bin/samtools_0.1.18
$ podman run --it --rm --entrypoint /usr/local/bin/samtools_0.1.18   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools_0.1.18   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### segment_juncs

```bash
$ singularity exec <container> /usr/local/bin/segment_juncs
$ podman run --it --rm --entrypoint /usr/local/bin/segment_juncs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segment_juncs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sra_to_solid

```bash
$ singularity exec <container> /usr/local/bin/sra_to_solid
$ podman run --it --rm --entrypoint /usr/local/bin/sra_to_solid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sra_to_solid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tophat

```bash
$ singularity exec <container> /usr/local/bin/tophat
$ podman run --it --rm --entrypoint /usr/local/bin/tophat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tophat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tophat-fusion-post

```bash
$ singularity exec <container> /usr/local/bin/tophat-fusion-post
$ podman run --it --rm --entrypoint /usr/local/bin/tophat-fusion-post   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tophat-fusion-post   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tophat2

```bash
$ singularity exec <container> /usr/local/bin/tophat2
$ podman run --it --rm --entrypoint /usr/local/bin/tophat2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tophat2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tophat_reports

```bash
$ singularity exec <container> /usr/local/bin/tophat_reports
$ podman run --it --rm --entrypoint /usr/local/bin/tophat_reports   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tophat_reports   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-cp

```bash
$ singularity exec <container> /usr/local/bin/asp-cp
$ podman run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-ls

```bash
$ singularity exec <container> /usr/local/bin/asp-ls
$ podman run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### between-two-genes

```bash
$ singularity exec <container> /usr/local/bin/between-two-genes
$ podman run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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