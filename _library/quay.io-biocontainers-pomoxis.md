---
layout: container
name:  "quay.io/biocontainers/pomoxis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pomoxis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pomoxis/container.yaml"
updated_at: "2024-07-06 02:34:57.505694"
latest: "0.3.15--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pomoxis"
aliases:
 - "assess_assembly"
 - "assess_homopolymers"
 - "catalogue_errors"
 - "common_errors_from_bam"
 - "coverage_from_bam"
 - "coverage_from_fastx"
 - "fast_convert"
 - "find_indels"
 - "intersect_assembly_errors"
 - "long_fastx"
 - "mini_align"
 - "mini_assemble"
 - "miniasm"
 - "minidot"
 - "pomoxis_path"
 - "porechop"
 - "qscores_from_summary"
 - "ref_seqs_from_bam"
 - "reverse_bed"
 - "split_fastx"
 - "stats_from_bam"
 - "subsample_bam"
 - "summary_from_stats"
 - "tag_bam"
 - "trim_alignments"
 - "seqkit"
 - "racon"
 - "rampler"
 - "racon_wrapper"
 - "gff2gff.py"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "guess-ploidy.py"
versions:
 - "0.3.9--pyhdfd78af_0"
 - "0.3.10--pyhdfd78af_0"
 - "0.3.11--pyhdfd78af_0"
 - "0.3.12--pyhdfd78af_0"
 - "0.3.13--pyhdfd78af_0"
 - "0.3.15--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for pomoxis"
config: {"url": "https://biocontainers.pro/tools/pomoxis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pomoxis", "latest": {"0.3.15--pyhdfd78af_0": "sha256:e3cd4bf27f6569b8393abfca0500a984b469faffd5afe3aaf93b6811b9e137f7"}, "tags": {"0.3.9--pyhdfd78af_0": "sha256:3aa7f109f3857cdfc5b23d00cf24af7b93b8664c603afc7348ac747311b870fa", "0.3.10--pyhdfd78af_0": "sha256:b42d95b742be3dc8333f57892c4aa2cc5cd739e796b33c7f310696856dcdea4d", "0.3.11--pyhdfd78af_0": "sha256:d248f9fc957bf655308d7d95e5cebec81d560aea87880c556a4e503c8fedc096", "0.3.12--pyhdfd78af_0": "sha256:7cd162388795f3a938a6b53bdb1aaca39f4c610a529c3a56e1536b561f6a1cd1", "0.3.13--pyhdfd78af_0": "sha256:96e20f9eb9aa50a76c61b9218d6bc26719f98934537a0b71a7725a42ee003741", "0.3.15--pyhdfd78af_0": "sha256:e3cd4bf27f6569b8393abfca0500a984b469faffd5afe3aaf93b6811b9e137f7"}, "docker": "quay.io/biocontainers/pomoxis", "aliases": {"assess_assembly": "/usr/local/bin/assess_assembly", "assess_homopolymers": "/usr/local/bin/assess_homopolymers", "catalogue_errors": "/usr/local/bin/catalogue_errors", "common_errors_from_bam": "/usr/local/bin/common_errors_from_bam", "coverage_from_bam": "/usr/local/bin/coverage_from_bam", "coverage_from_fastx": "/usr/local/bin/coverage_from_fastx", "fast_convert": "/usr/local/bin/fast_convert", "find_indels": "/usr/local/bin/find_indels", "intersect_assembly_errors": "/usr/local/bin/intersect_assembly_errors", "long_fastx": "/usr/local/bin/long_fastx", "mini_align": "/usr/local/bin/mini_align", "mini_assemble": "/usr/local/bin/mini_assemble", "miniasm": "/usr/local/bin/miniasm", "minidot": "/usr/local/bin/minidot", "pomoxis_path": "/usr/local/bin/pomoxis_path", "porechop": "/usr/local/bin/porechop", "qscores_from_summary": "/usr/local/bin/qscores_from_summary", "ref_seqs_from_bam": "/usr/local/bin/ref_seqs_from_bam", "reverse_bed": "/usr/local/bin/reverse_bed", "split_fastx": "/usr/local/bin/split_fastx", "stats_from_bam": "/usr/local/bin/stats_from_bam", "subsample_bam": "/usr/local/bin/subsample_bam", "summary_from_stats": "/usr/local/bin/summary_from_stats", "tag_bam": "/usr/local/bin/tag_bam", "trim_alignments": "/usr/local/bin/trim_alignments", "seqkit": "/usr/local/bin/seqkit", "racon": "/usr/local/bin/racon", "rampler": "/usr/local/bin/rampler", "racon_wrapper": "/usr/local/bin/racon_wrapper", "gff2gff.py": "/usr/local/bin/gff2gff.py", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pomoxis.
shpc-registry automated BioContainers addition for pomoxis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pomoxis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pomoxis:0.3.15--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pomoxis/0.3.15--pyhdfd78af_0
$ module help quay.io/biocontainers/pomoxis/0.3.15--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pomoxis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pomoxis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pomoxis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pomoxis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pomoxis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pomoxis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### assess_assembly

```bash
$ singularity exec <container> /usr/local/bin/assess_assembly
$ podman run --it --rm --entrypoint /usr/local/bin/assess_assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assess_assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assess_homopolymers

```bash
$ singularity exec <container> /usr/local/bin/assess_homopolymers
$ podman run --it --rm --entrypoint /usr/local/bin/assess_homopolymers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assess_homopolymers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### catalogue_errors

```bash
$ singularity exec <container> /usr/local/bin/catalogue_errors
$ podman run --it --rm --entrypoint /usr/local/bin/catalogue_errors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catalogue_errors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### common_errors_from_bam

```bash
$ singularity exec <container> /usr/local/bin/common_errors_from_bam
$ podman run --it --rm --entrypoint /usr/local/bin/common_errors_from_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/common_errors_from_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_from_bam

```bash
$ singularity exec <container> /usr/local/bin/coverage_from_bam
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_from_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_from_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_from_fastx

```bash
$ singularity exec <container> /usr/local/bin/coverage_from_fastx
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_from_fastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_from_fastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast_convert

```bash
$ singularity exec <container> /usr/local/bin/fast_convert
$ podman run --it --rm --entrypoint /usr/local/bin/fast_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_indels

```bash
$ singularity exec <container> /usr/local/bin/find_indels
$ podman run --it --rm --entrypoint /usr/local/bin/find_indels   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_indels   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersect_assembly_errors

```bash
$ singularity exec <container> /usr/local/bin/intersect_assembly_errors
$ podman run --it --rm --entrypoint /usr/local/bin/intersect_assembly_errors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersect_assembly_errors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### long_fastx

```bash
$ singularity exec <container> /usr/local/bin/long_fastx
$ podman run --it --rm --entrypoint /usr/local/bin/long_fastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/long_fastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mini_align

```bash
$ singularity exec <container> /usr/local/bin/mini_align
$ podman run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mini_assemble

```bash
$ singularity exec <container> /usr/local/bin/mini_assemble
$ podman run --it --rm --entrypoint /usr/local/bin/mini_assemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mini_assemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniasm

```bash
$ singularity exec <container> /usr/local/bin/miniasm
$ podman run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minidot

```bash
$ singularity exec <container> /usr/local/bin/minidot
$ podman run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pomoxis_path

```bash
$ singularity exec <container> /usr/local/bin/pomoxis_path
$ podman run --it --rm --entrypoint /usr/local/bin/pomoxis_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pomoxis_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### porechop

```bash
$ singularity exec <container> /usr/local/bin/porechop
$ podman run --it --rm --entrypoint /usr/local/bin/porechop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/porechop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qscores_from_summary

```bash
$ singularity exec <container> /usr/local/bin/qscores_from_summary
$ podman run --it --rm --entrypoint /usr/local/bin/qscores_from_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qscores_from_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref_seqs_from_bam

```bash
$ singularity exec <container> /usr/local/bin/ref_seqs_from_bam
$ podman run --it --rm --entrypoint /usr/local/bin/ref_seqs_from_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref_seqs_from_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reverse_bed

```bash
$ singularity exec <container> /usr/local/bin/reverse_bed
$ podman run --it --rm --entrypoint /usr/local/bin/reverse_bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reverse_bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_fastx

```bash
$ singularity exec <container> /usr/local/bin/split_fastx
$ podman run --it --rm --entrypoint /usr/local/bin/split_fastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_fastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stats_from_bam

```bash
$ singularity exec <container> /usr/local/bin/stats_from_bam
$ podman run --it --rm --entrypoint /usr/local/bin/stats_from_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stats_from_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subsample_bam

```bash
$ singularity exec <container> /usr/local/bin/subsample_bam
$ podman run --it --rm --entrypoint /usr/local/bin/subsample_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subsample_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summary_from_stats

```bash
$ singularity exec <container> /usr/local/bin/summary_from_stats
$ podman run --it --rm --entrypoint /usr/local/bin/summary_from_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summary_from_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tag_bam

```bash
$ singularity exec <container> /usr/local/bin/tag_bam
$ podman run --it --rm --entrypoint /usr/local/bin/tag_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tag_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim_alignments

```bash
$ singularity exec <container> /usr/local/bin/trim_alignments
$ podman run --it --rm --entrypoint /usr/local/bin/trim_alignments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_alignments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon

```bash
$ singularity exec <container> /usr/local/bin/racon
$ podman run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rampler

```bash
$ singularity exec <container> /usr/local/bin/rampler
$ podman run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon_wrapper

```bash
$ singularity exec <container> /usr/local/bin/racon_wrapper
$ podman run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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