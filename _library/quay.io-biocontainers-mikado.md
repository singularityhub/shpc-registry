---
layout: container
name:  "quay.io/biocontainers/mikado"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mikado/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mikado/container.yaml"
updated_at: "2024-10-20 03:39:51.164772"
latest: "2.3.4--py310ha14a713_0"
container_url: "https://biocontainers.pro/tools/mikado"
aliases:
 - "add_transcript_feature_to_gtf.py"
 - "align_collect.py"
 - "asm_collect.py"
 - "bam2gtf.py"
 - "black"
 - "black-primer"
 - "blackd"
 - "calculate_distances.py"
 - "class_run.py"
 - "convert_cdna_match_gff3.py"
 - "daijin"
 - "extract_promoter_regions.py"
 - "getFastaFromIds.py"
 - "gffjunc_to_bed12.py"
 - "grep.py"
 - "hypothesis"
 - "merge_junction_bed12.py"
 - "mikado"
 - "remove_from_embl.py"
 - "remove_utrs.py"
 - "sanitize_blast_db.py"
 - "split_fasta.py"
 - "tease_maker_apart.py"
 - "trim_long_introns.py"
 - "stone"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "dynamodb_dump"
 - "dynamodb_load"
 - "elbadmin"
 - "fetch_file"
versions:
 - "2.2.4--py39h70b41aa_0"
 - "2.3.4--py310ha14a713_0"
 - "2.2.5--py39h70b41aa_0"
description: "shpc-registry automated BioContainers addition for mikado"
config: {"url": "https://biocontainers.pro/tools/mikado", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mikado", "latest": {"2.3.4--py310ha14a713_0": "sha256:eb6238107c78079f752d8fcf9c41472eef3953660caecb46d5dd601c80ef4213"}, "tags": {"2.2.4--py39h70b41aa_0": "sha256:0a1fa4a62ed41707c54c3c4a31b8a4bfc15f18f5d1f1b06b69f9bc7a07de38ea", "2.3.4--py310ha14a713_0": "sha256:eb6238107c78079f752d8fcf9c41472eef3953660caecb46d5dd601c80ef4213", "2.2.5--py39h70b41aa_0": "sha256:a495f251c4f068b2a6d91e8615e763e4443fe15447a0da25c442c05003d12f76"}, "docker": "quay.io/biocontainers/mikado", "aliases": {"add_transcript_feature_to_gtf.py": "/usr/local/bin/add_transcript_feature_to_gtf.py", "align_collect.py": "/usr/local/bin/align_collect.py", "asm_collect.py": "/usr/local/bin/asm_collect.py", "bam2gtf.py": "/usr/local/bin/bam2gtf.py", "black": "/usr/local/bin/black", "black-primer": "/usr/local/bin/black-primer", "blackd": "/usr/local/bin/blackd", "calculate_distances.py": "/usr/local/bin/calculate_distances.py", "class_run.py": "/usr/local/bin/class_run.py", "convert_cdna_match_gff3.py": "/usr/local/bin/convert_cdna_match_gff3.py", "daijin": "/usr/local/bin/daijin", "extract_promoter_regions.py": "/usr/local/bin/extract_promoter_regions.py", "getFastaFromIds.py": "/usr/local/bin/getFastaFromIds.py", "gffjunc_to_bed12.py": "/usr/local/bin/gffjunc_to_bed12.py", "grep.py": "/usr/local/bin/grep.py", "hypothesis": "/usr/local/bin/hypothesis", "merge_junction_bed12.py": "/usr/local/bin/merge_junction_bed12.py", "mikado": "/usr/local/bin/mikado", "remove_from_embl.py": "/usr/local/bin/remove_from_embl.py", "remove_utrs.py": "/usr/local/bin/remove_utrs.py", "sanitize_blast_db.py": "/usr/local/bin/sanitize_blast_db.py", "split_fasta.py": "/usr/local/bin/split_fasta.py", "tease_maker_apart.py": "/usr/local/bin/tease_maker_apart.py", "trim_long_introns.py": "/usr/local/bin/trim_long_introns.py", "stone": "/usr/local/bin/stone", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin", "fetch_file": "/usr/local/bin/fetch_file"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mikado.
shpc-registry automated BioContainers addition for mikado
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mikado
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mikado:2.3.4--py310ha14a713_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mikado/2.3.4--py310ha14a713_0
$ module help quay.io/biocontainers/mikado/2.3.4--py310ha14a713_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mikado-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mikado-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mikado-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mikado-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mikado-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mikado-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_transcript_feature_to_gtf.py

```bash
$ singularity exec <container> /usr/local/bin/add_transcript_feature_to_gtf.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_transcript_feature_to_gtf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_transcript_feature_to_gtf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align_collect.py

```bash
$ singularity exec <container> /usr/local/bin/align_collect.py
$ podman run --it --rm --entrypoint /usr/local/bin/align_collect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_collect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asm_collect.py

```bash
$ singularity exec <container> /usr/local/bin/asm_collect.py
$ podman run --it --rm --entrypoint /usr/local/bin/asm_collect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asm_collect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2gtf.py

```bash
$ singularity exec <container> /usr/local/bin/bam2gtf.py
$ podman run --it --rm --entrypoint /usr/local/bin/bam2gtf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2gtf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black

```bash
$ singularity exec <container> /usr/local/bin/black
$ podman run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black-primer

```bash
$ singularity exec <container> /usr/local/bin/black-primer
$ podman run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blackd

```bash
$ singularity exec <container> /usr/local/bin/blackd
$ podman run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calculate_distances.py

```bash
$ singularity exec <container> /usr/local/bin/calculate_distances.py
$ podman run --it --rm --entrypoint /usr/local/bin/calculate_distances.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculate_distances.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### class_run.py

```bash
$ singularity exec <container> /usr/local/bin/class_run.py
$ podman run --it --rm --entrypoint /usr/local/bin/class_run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/class_run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_cdna_match_gff3.py

```bash
$ singularity exec <container> /usr/local/bin/convert_cdna_match_gff3.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_cdna_match_gff3.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_cdna_match_gff3.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### daijin

```bash
$ singularity exec <container> /usr/local/bin/daijin
$ podman run --it --rm --entrypoint /usr/local/bin/daijin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/daijin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_promoter_regions.py

```bash
$ singularity exec <container> /usr/local/bin/extract_promoter_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_promoter_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_promoter_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getFastaFromIds.py

```bash
$ singularity exec <container> /usr/local/bin/getFastaFromIds.py
$ podman run --it --rm --entrypoint /usr/local/bin/getFastaFromIds.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getFastaFromIds.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffjunc_to_bed12.py

```bash
$ singularity exec <container> /usr/local/bin/gffjunc_to_bed12.py
$ podman run --it --rm --entrypoint /usr/local/bin/gffjunc_to_bed12.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffjunc_to_bed12.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grep.py

```bash
$ singularity exec <container> /usr/local/bin/grep.py
$ podman run --it --rm --entrypoint /usr/local/bin/grep.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grep.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hypothesis

```bash
$ singularity exec <container> /usr/local/bin/hypothesis
$ podman run --it --rm --entrypoint /usr/local/bin/hypothesis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hypothesis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_junction_bed12.py

```bash
$ singularity exec <container> /usr/local/bin/merge_junction_bed12.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_junction_bed12.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_junction_bed12.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mikado

```bash
$ singularity exec <container> /usr/local/bin/mikado
$ podman run --it --rm --entrypoint /usr/local/bin/mikado   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mikado   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_from_embl.py

```bash
$ singularity exec <container> /usr/local/bin/remove_from_embl.py
$ podman run --it --rm --entrypoint /usr/local/bin/remove_from_embl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_from_embl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_utrs.py

```bash
$ singularity exec <container> /usr/local/bin/remove_utrs.py
$ podman run --it --rm --entrypoint /usr/local/bin/remove_utrs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_utrs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sanitize_blast_db.py

```bash
$ singularity exec <container> /usr/local/bin/sanitize_blast_db.py
$ podman run --it --rm --entrypoint /usr/local/bin/sanitize_blast_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sanitize_blast_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/split_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tease_maker_apart.py

```bash
$ singularity exec <container> /usr/local/bin/tease_maker_apart.py
$ podman run --it --rm --entrypoint /usr/local/bin/tease_maker_apart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tease_maker_apart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim_long_introns.py

```bash
$ singularity exec <container> /usr/local/bin/trim_long_introns.py
$ podman run --it --rm --entrypoint /usr/local/bin/trim_long_introns.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_long_introns.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stone

```bash
$ singularity exec <container> /usr/local/bin/stone
$ podman run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asadmin

```bash
$ singularity exec <container> /usr/local/bin/asadmin
$ podman run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundle_image

```bash
$ singularity exec <container> /usr/local/bin/bundle_image
$ podman run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfadmin

```bash
$ singularity exec <container> /usr/local/bin/cfadmin
$ podman run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cq

```bash
$ singularity exec <container> /usr/local/bin/cq
$ podman run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwutil

```bash
$ singularity exec <container> /usr/local/bin/cwutil
$ podman run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_dump

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_dump
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_load

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_load
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elbadmin

```bash
$ singularity exec <container> /usr/local/bin/elbadmin
$ podman run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_file

```bash
$ singularity exec <container> /usr/local/bin/fetch_file
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
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