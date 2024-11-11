---
layout: container
name:  "quay.io/biocontainers/imfusion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/imfusion/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/imfusion/container.yaml"
updated_at: "2024-11-11 03:07:56.433139"
latest: "0.3.2--py27_0"
container_url: "https://biocontainers.pro/tools/imfusion"
aliases:
 - "bam2fastx"
 - "bam_merge"
 - "bed_to_juncs"
 - "contig_to_chr_coords"
 - "exactSNP"
 - "featureCounts"
 - "fix_map_ordering"
 - "gtf_juncs"
 - "gtf_to_fasta"
 - "imfusion"
 - "imfusion-build"
 - "imfusion-ctg"
 - "imfusion-expression"
 - "imfusion-insertions"
 - "imfusion-merge"
 - "juncs_db"
 - "long_spanning_reads"
 - "map2gtf"
 - "prepDE.py"
 - "prep_reads"
 - "sam_juncs"
 - "samtools_0.1.18"
 - "segment_juncs"
 - "sra_to_solid"
 - "stringtie"
 - "subindel"
 - "subjunc"
 - "subread-align"
 - "subread-buildindex"
 - "tophat"
 - "tophat-fusion-post"
 - "tophat2"
 - "tophat_reports"
 - "STAR"
 - "STARlong"
 - "htseq-count"
 - "htseq-qa"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
versions:
 - "0.3.2--py27_0"
description: "shpc-registry automated BioContainers addition for imfusion"
config: {"url": "https://biocontainers.pro/tools/imfusion", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for imfusion", "latest": {"0.3.2--py27_0": "sha256:fa3a3446aac27236a67d5841eaecd6109aa96bcdb67ded3029ebfbb8d8c0b500"}, "tags": {"0.3.2--py27_0": "sha256:fa3a3446aac27236a67d5841eaecd6109aa96bcdb67ded3029ebfbb8d8c0b500"}, "docker": "quay.io/biocontainers/imfusion", "aliases": {"bam2fastx": "/usr/local/bin/bam2fastx", "bam_merge": "/usr/local/bin/bam_merge", "bed_to_juncs": "/usr/local/bin/bed_to_juncs", "contig_to_chr_coords": "/usr/local/bin/contig_to_chr_coords", "exactSNP": "/usr/local/bin/exactSNP", "featureCounts": "/usr/local/bin/featureCounts", "fix_map_ordering": "/usr/local/bin/fix_map_ordering", "gtf_juncs": "/usr/local/bin/gtf_juncs", "gtf_to_fasta": "/usr/local/bin/gtf_to_fasta", "imfusion": "/usr/local/bin/imfusion", "imfusion-build": "/usr/local/bin/imfusion-build", "imfusion-ctg": "/usr/local/bin/imfusion-ctg", "imfusion-expression": "/usr/local/bin/imfusion-expression", "imfusion-insertions": "/usr/local/bin/imfusion-insertions", "imfusion-merge": "/usr/local/bin/imfusion-merge", "juncs_db": "/usr/local/bin/juncs_db", "long_spanning_reads": "/usr/local/bin/long_spanning_reads", "map2gtf": "/usr/local/bin/map2gtf", "prepDE.py": "/usr/local/bin/prepDE.py", "prep_reads": "/usr/local/bin/prep_reads", "sam_juncs": "/usr/local/bin/sam_juncs", "samtools_0.1.18": "/usr/local/bin/samtools_0.1.18", "segment_juncs": "/usr/local/bin/segment_juncs", "sra_to_solid": "/usr/local/bin/sra_to_solid", "stringtie": "/usr/local/bin/stringtie", "subindel": "/usr/local/bin/subindel", "subjunc": "/usr/local/bin/subjunc", "subread-align": "/usr/local/bin/subread-align", "subread-buildindex": "/usr/local/bin/subread-buildindex", "tophat": "/usr/local/bin/tophat", "tophat-fusion-post": "/usr/local/bin/tophat-fusion-post", "tophat2": "/usr/local/bin/tophat2", "tophat_reports": "/usr/local/bin/tophat_reports", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "htseq-count": "/usr/local/bin/htseq-count", "htseq-qa": "/usr/local/bin/htseq-qa", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/imfusion.
shpc-registry automated BioContainers addition for imfusion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/imfusion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/imfusion:0.3.2--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/imfusion/0.3.2--py27_0
$ module help quay.io/biocontainers/imfusion/0.3.2--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### imfusion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### imfusion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### imfusion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### imfusion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### imfusion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### imfusion-inspect-deffile:

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


#### exactSNP

```bash
$ singularity exec <container> /usr/local/bin/exactSNP
$ podman run --it --rm --entrypoint /usr/local/bin/exactSNP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exactSNP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### featureCounts

```bash
$ singularity exec <container> /usr/local/bin/featureCounts
$ podman run --it --rm --entrypoint /usr/local/bin/featureCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/featureCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### imfusion

```bash
$ singularity exec <container> /usr/local/bin/imfusion
$ podman run --it --rm --entrypoint /usr/local/bin/imfusion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imfusion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imfusion-build

```bash
$ singularity exec <container> /usr/local/bin/imfusion-build
$ podman run --it --rm --entrypoint /usr/local/bin/imfusion-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imfusion-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imfusion-ctg

```bash
$ singularity exec <container> /usr/local/bin/imfusion-ctg
$ podman run --it --rm --entrypoint /usr/local/bin/imfusion-ctg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imfusion-ctg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imfusion-expression

```bash
$ singularity exec <container> /usr/local/bin/imfusion-expression
$ podman run --it --rm --entrypoint /usr/local/bin/imfusion-expression   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imfusion-expression   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imfusion-insertions

```bash
$ singularity exec <container> /usr/local/bin/imfusion-insertions
$ podman run --it --rm --entrypoint /usr/local/bin/imfusion-insertions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imfusion-insertions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imfusion-merge

```bash
$ singularity exec <container> /usr/local/bin/imfusion-merge
$ podman run --it --rm --entrypoint /usr/local/bin/imfusion-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imfusion-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### prepDE.py

```bash
$ singularity exec <container> /usr/local/bin/prepDE.py
$ podman run --it --rm --entrypoint /usr/local/bin/prepDE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepDE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prep_reads

```bash
$ singularity exec <container> /usr/local/bin/prep_reads
$ podman run --it --rm --entrypoint /usr/local/bin/prep_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prep_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### stringtie

```bash
$ singularity exec <container> /usr/local/bin/stringtie
$ podman run --it --rm --entrypoint /usr/local/bin/stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subindel

```bash
$ singularity exec <container> /usr/local/bin/subindel
$ podman run --it --rm --entrypoint /usr/local/bin/subindel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subindel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subjunc

```bash
$ singularity exec <container> /usr/local/bin/subjunc
$ podman run --it --rm --entrypoint /usr/local/bin/subjunc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subjunc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-align

```bash
$ singularity exec <container> /usr/local/bin/subread-align
$ podman run --it --rm --entrypoint /usr/local/bin/subread-align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-buildindex

```bash
$ singularity exec <container> /usr/local/bin/subread-buildindex
$ podman run --it --rm --entrypoint /usr/local/bin/subread-buildindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-buildindex   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong

```bash
$ singularity exec <container> /usr/local/bin/STARlong
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-count

```bash
$ singularity exec <container> /usr/local/bin/htseq-count
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-qa

```bash
$ singularity exec <container> /usr/local/bin/htseq-qa
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
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