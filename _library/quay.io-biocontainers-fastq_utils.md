---
layout: container
name:  "quay.io/biocontainers/fastq_utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq_utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastq_utils/container.yaml"
updated_at: "2022-11-06 00:37:20.834739"
latest: "0.25.1--h20b1175_1"
container_url: "https://biocontainers.pro/tools/fastq_utils"
aliases:
 - "bam2fastq"
 - "bam_add_tags"
 - "bam_annotate.sh"
 - "bam_umi_count"
 - "fastq2bam"
 - "fastq_filter_n"
 - "fastq_filterpair"
 - "fastq_info"
 - "fastq_not_empty"
 - "fastq_num_reads"
 - "fastq_pre_barcodes"
 - "fastq_split_interleaved"
 - "fastq_tests"
 - "fastq_trim_poly_at"
 - "fastq_truncate"
 - "fastq_validator.sh"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "interpolate_sam.pl"
 - "maq2sam-long"
 - "maq2sam-short"
 - "md5fa"
versions:
 - "0.25.1--h20b1175_1"
description: "shpc-registry automated BioContainers addition for fastq_utils"
config: {"url": "https://biocontainers.pro/tools/fastq_utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastq_utils", "latest": {"0.25.1--h20b1175_1": "sha256:e8ae637065c59bd201d0927942765153249cf2e286036aa7b18e7adebfc2fd33"}, "tags": {"0.25.1--h20b1175_1": "sha256:e8ae637065c59bd201d0927942765153249cf2e286036aa7b18e7adebfc2fd33"}, "docker": "quay.io/biocontainers/fastq_utils", "aliases": {"bam2fastq": "/usr/local/bin/bam2fastq", "bam_add_tags": "/usr/local/bin/bam_add_tags", "bam_annotate.sh": "/usr/local/bin/bam_annotate.sh", "bam_umi_count": "/usr/local/bin/bam_umi_count", "fastq2bam": "/usr/local/bin/fastq2bam", "fastq_filter_n": "/usr/local/bin/fastq_filter_n", "fastq_filterpair": "/usr/local/bin/fastq_filterpair", "fastq_info": "/usr/local/bin/fastq_info", "fastq_not_empty": "/usr/local/bin/fastq_not_empty", "fastq_num_reads": "/usr/local/bin/fastq_num_reads", "fastq_pre_barcodes": "/usr/local/bin/fastq_pre_barcodes", "fastq_split_interleaved": "/usr/local/bin/fastq_split_interleaved", "fastq_tests": "/usr/local/bin/fastq_tests", "fastq_trim_poly_at": "/usr/local/bin/fastq_trim_poly_at", "fastq_truncate": "/usr/local/bin/fastq_truncate", "fastq_validator.sh": "/usr/local/bin/fastq_validator.sh", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq_utils.
shpc-registry automated BioContainers addition for fastq_utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq_utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq_utils:0.25.1--h20b1175_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq_utils/0.25.1--h20b1175_1
$ module help quay.io/biocontainers/fastq_utils/0.25.1--h20b1175_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq_utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq_utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq_utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq_utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq_utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq_utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2fastq

```bash
$ singularity exec <container> /usr/local/bin/bam2fastq
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam_add_tags

```bash
$ singularity exec <container> /usr/local/bin/bam_add_tags
$ podman run --it --rm --entrypoint /usr/local/bin/bam_add_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_add_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam_annotate.sh

```bash
$ singularity exec <container> /usr/local/bin/bam_annotate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bam_annotate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_annotate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam_umi_count

```bash
$ singularity exec <container> /usr/local/bin/bam_umi_count
$ podman run --it --rm --entrypoint /usr/local/bin/bam_umi_count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_umi_count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq2bam

```bash
$ singularity exec <container> /usr/local/bin/fastq2bam
$ podman run --it --rm --entrypoint /usr/local/bin/fastq2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_filter_n

```bash
$ singularity exec <container> /usr/local/bin/fastq_filter_n
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_filter_n   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_filter_n   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_filterpair

```bash
$ singularity exec <container> /usr/local/bin/fastq_filterpair
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_filterpair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_filterpair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_info

```bash
$ singularity exec <container> /usr/local/bin/fastq_info
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_not_empty

```bash
$ singularity exec <container> /usr/local/bin/fastq_not_empty
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_not_empty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_not_empty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_num_reads

```bash
$ singularity exec <container> /usr/local/bin/fastq_num_reads
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_num_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_num_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_pre_barcodes

```bash
$ singularity exec <container> /usr/local/bin/fastq_pre_barcodes
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_pre_barcodes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_pre_barcodes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_split_interleaved

```bash
$ singularity exec <container> /usr/local/bin/fastq_split_interleaved
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_split_interleaved   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_split_interleaved   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_tests

```bash
$ singularity exec <container> /usr/local/bin/fastq_tests
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_tests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_tests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_trim_poly_at

```bash
$ singularity exec <container> /usr/local/bin/fastq_trim_poly_at
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_trim_poly_at   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_trim_poly_at   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_truncate

```bash
$ singularity exec <container> /usr/local/bin/fastq_truncate
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_truncate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_truncate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_validator.sh

```bash
$ singularity exec <container> /usr/local/bin/fastq_validator.sh
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_validator.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_validator.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-long

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-long
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-short

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-short
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5fa

```bash
$ singularity exec <container> /usr/local/bin/md5fa
$ podman run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
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