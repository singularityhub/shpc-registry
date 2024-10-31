---
layout: container
name:  "quay.io/biocontainers/circexplorer2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/circexplorer2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/circexplorer2/container.yaml"
updated_at: "2024-10-31 00:36:11.664355"
latest: "2.3.8--pyh5e36f6f_2"
container_url: "https://biocontainers.pro/tools/circexplorer2"
aliases:
 - "CIRCexplorer2"
 - "bam2fastx"
 - "bam_merge"
 - "bed_to_juncs"
 - "contig_to_chr_coords"
 - "cuffcompare"
 - "cuffdiff"
 - "cufflinks"
 - "cuffmerge"
 - "cuffnorm"
 - "cuffquant"
 - "fast_circ.py"
 - "fetch_ucsc.py"
 - "fix_map_ordering"
 - "genePredToGtf"
 - "gffread"
 - "gtfToGenePred"
 - "gtf_juncs"
 - "gtf_to_fasta"
 - "gtf_to_sam"
 - "juncs_db"
 - "long_spanning_reads"
 - "map2gtf"
 - "prep_reads"
 - "sam_juncs"
 - "samtools_0.1.18"
 - "segment_juncs"
 - "sra_to_solid"
 - "tophat"
 - "tophat-fusion-post"
 - "tophat2"
 - "tophat_reports"
 - "bedGraphToBigWig"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
versions:
 - "2.3.8--pyh5e36f6f_2"
description: "shpc-registry automated BioContainers addition for circexplorer2"
config: {"url": "https://biocontainers.pro/tools/circexplorer2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for circexplorer2", "latest": {"2.3.8--pyh5e36f6f_2": "sha256:813e2edc2f01a1afdae55985877d459fc2099123749434ce827727200b97ca0d"}, "tags": {"2.3.8--pyh5e36f6f_2": "sha256:813e2edc2f01a1afdae55985877d459fc2099123749434ce827727200b97ca0d"}, "docker": "quay.io/biocontainers/circexplorer2", "aliases": {"CIRCexplorer2": "/usr/local/bin/CIRCexplorer2", "bam2fastx": "/usr/local/bin/bam2fastx", "bam_merge": "/usr/local/bin/bam_merge", "bed_to_juncs": "/usr/local/bin/bed_to_juncs", "contig_to_chr_coords": "/usr/local/bin/contig_to_chr_coords", "cuffcompare": "/usr/local/bin/cuffcompare", "cuffdiff": "/usr/local/bin/cuffdiff", "cufflinks": "/usr/local/bin/cufflinks", "cuffmerge": "/usr/local/bin/cuffmerge", "cuffnorm": "/usr/local/bin/cuffnorm", "cuffquant": "/usr/local/bin/cuffquant", "fast_circ.py": "/usr/local/bin/fast_circ.py", "fetch_ucsc.py": "/usr/local/bin/fetch_ucsc.py", "fix_map_ordering": "/usr/local/bin/fix_map_ordering", "genePredToGtf": "/usr/local/bin/genePredToGtf", "gffread": "/usr/local/bin/gffread", "gtfToGenePred": "/usr/local/bin/gtfToGenePred", "gtf_juncs": "/usr/local/bin/gtf_juncs", "gtf_to_fasta": "/usr/local/bin/gtf_to_fasta", "gtf_to_sam": "/usr/local/bin/gtf_to_sam", "juncs_db": "/usr/local/bin/juncs_db", "long_spanning_reads": "/usr/local/bin/long_spanning_reads", "map2gtf": "/usr/local/bin/map2gtf", "prep_reads": "/usr/local/bin/prep_reads", "sam_juncs": "/usr/local/bin/sam_juncs", "samtools_0.1.18": "/usr/local/bin/samtools_0.1.18", "segment_juncs": "/usr/local/bin/segment_juncs", "sra_to_solid": "/usr/local/bin/sra_to_solid", "tophat": "/usr/local/bin/tophat", "tophat-fusion-post": "/usr/local/bin/tophat-fusion-post", "tophat2": "/usr/local/bin/tophat2", "tophat_reports": "/usr/local/bin/tophat_reports", "bedGraphToBigWig": "/usr/local/bin/bedGraphToBigWig", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/circexplorer2.
shpc-registry automated BioContainers addition for circexplorer2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/circexplorer2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/circexplorer2:2.3.8--pyh5e36f6f_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/circexplorer2/2.3.8--pyh5e36f6f_2
$ module help quay.io/biocontainers/circexplorer2/2.3.8--pyh5e36f6f_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### circexplorer2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### circexplorer2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### circexplorer2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### circexplorer2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### circexplorer2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### circexplorer2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CIRCexplorer2

```bash
$ singularity exec <container> /usr/local/bin/CIRCexplorer2
$ podman run --it --rm --entrypoint /usr/local/bin/CIRCexplorer2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CIRCexplorer2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cuffcompare

```bash
$ singularity exec <container> /usr/local/bin/cuffcompare
$ podman run --it --rm --entrypoint /usr/local/bin/cuffcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuffcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffdiff

```bash
$ singularity exec <container> /usr/local/bin/cuffdiff
$ podman run --it --rm --entrypoint /usr/local/bin/cuffdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuffdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cufflinks

```bash
$ singularity exec <container> /usr/local/bin/cufflinks
$ podman run --it --rm --entrypoint /usr/local/bin/cufflinks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cufflinks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffmerge

```bash
$ singularity exec <container> /usr/local/bin/cuffmerge
$ podman run --it --rm --entrypoint /usr/local/bin/cuffmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuffmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffnorm

```bash
$ singularity exec <container> /usr/local/bin/cuffnorm
$ podman run --it --rm --entrypoint /usr/local/bin/cuffnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuffnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffquant

```bash
$ singularity exec <container> /usr/local/bin/cuffquant
$ podman run --it --rm --entrypoint /usr/local/bin/cuffquant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuffquant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast_circ.py

```bash
$ singularity exec <container> /usr/local/bin/fast_circ.py
$ podman run --it --rm --entrypoint /usr/local/bin/fast_circ.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast_circ.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_ucsc.py

```bash
$ singularity exec <container> /usr/local/bin/fetch_ucsc.py
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_ucsc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_ucsc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_map_ordering

```bash
$ singularity exec <container> /usr/local/bin/fix_map_ordering
$ podman run --it --rm --entrypoint /usr/local/bin/fix_map_ordering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_map_ordering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genePredToGtf

```bash
$ singularity exec <container> /usr/local/bin/genePredToGtf
$ podman run --it --rm --entrypoint /usr/local/bin/genePredToGtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genePredToGtf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffread

```bash
$ singularity exec <container> /usr/local/bin/gffread
$ podman run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtfToGenePred

```bash
$ singularity exec <container> /usr/local/bin/gtfToGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/gtfToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtfToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gtf_to_sam

```bash
$ singularity exec <container> /usr/local/bin/gtf_to_sam
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_to_sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_to_sam   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bedGraphToBigWig

```bash
$ singularity exec <container> /usr/local/bin/bedGraphToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
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