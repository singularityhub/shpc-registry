---
layout: container
name:  "quay.io/biocontainers/rilseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rilseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rilseq/container.yaml"
updated_at: "2023-12-20 03:51:39.117340"
latest: "0.82--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/rilseq"
aliases:
 - "RILseq_significant_regions.py"
 - "count_chimeric_reads_per_gene.py"
 - "generate_BED_file_of_endpoints.py"
 - "generate_genes_gff.py"
 - "generate_transcripts_gff.py"
 - "get_sequences_for_meme.py"
 - "map_chimeric_fragments.py"
 - "map_single_fragments.py"
 - "plot_circos_plot.py"
 - "plot_regions_interactions.py"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "f2py3.9"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
versions:
 - "0.82--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for rilseq"
config: {"url": "https://biocontainers.pro/tools/rilseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rilseq", "latest": {"0.82--pyhdfd78af_0": "sha256:4ea40a494d6b70358559d977fb17e836019dc41ab87693514d6ef804e640d18c"}, "tags": {"0.82--pyhdfd78af_0": "sha256:4ea40a494d6b70358559d977fb17e836019dc41ab87693514d6ef804e640d18c"}, "docker": "quay.io/biocontainers/rilseq", "aliases": {"RILseq_significant_regions.py": "/usr/local/bin/RILseq_significant_regions.py", "count_chimeric_reads_per_gene.py": "/usr/local/bin/count_chimeric_reads_per_gene.py", "generate_BED_file_of_endpoints.py": "/usr/local/bin/generate_BED_file_of_endpoints.py", "generate_genes_gff.py": "/usr/local/bin/generate_genes_gff.py", "generate_transcripts_gff.py": "/usr/local/bin/generate_transcripts_gff.py", "get_sequences_for_meme.py": "/usr/local/bin/get_sequences_for_meme.py", "map_chimeric_fragments.py": "/usr/local/bin/map_chimeric_fragments.py", "map_single_fragments.py": "/usr/local/bin/map_single_fragments.py", "plot_circos_plot.py": "/usr/local/bin/plot_circos_plot.py", "plot_regions_interactions.py": "/usr/local/bin/plot_regions_interactions.py", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "f2py3.9": "/usr/local/bin/f2py3.9", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rilseq.
shpc-registry automated BioContainers addition for rilseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rilseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rilseq:0.82--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rilseq/0.82--pyhdfd78af_0
$ module help quay.io/biocontainers/rilseq/0.82--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rilseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rilseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rilseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rilseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rilseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rilseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RILseq_significant_regions.py

```bash
$ singularity exec <container> /usr/local/bin/RILseq_significant_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/RILseq_significant_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RILseq_significant_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count_chimeric_reads_per_gene.py

```bash
$ singularity exec <container> /usr/local/bin/count_chimeric_reads_per_gene.py
$ podman run --it --rm --entrypoint /usr/local/bin/count_chimeric_reads_per_gene.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count_chimeric_reads_per_gene.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_BED_file_of_endpoints.py

```bash
$ singularity exec <container> /usr/local/bin/generate_BED_file_of_endpoints.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_BED_file_of_endpoints.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_BED_file_of_endpoints.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_genes_gff.py

```bash
$ singularity exec <container> /usr/local/bin/generate_genes_gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_genes_gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_genes_gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_transcripts_gff.py

```bash
$ singularity exec <container> /usr/local/bin/generate_transcripts_gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_transcripts_gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_transcripts_gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_sequences_for_meme.py

```bash
$ singularity exec <container> /usr/local/bin/get_sequences_for_meme.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_sequences_for_meme.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_sequences_for_meme.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_chimeric_fragments.py

```bash
$ singularity exec <container> /usr/local/bin/map_chimeric_fragments.py
$ podman run --it --rm --entrypoint /usr/local/bin/map_chimeric_fragments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_chimeric_fragments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_single_fragments.py

```bash
$ singularity exec <container> /usr/local/bin/map_single_fragments.py
$ podman run --it --rm --entrypoint /usr/local/bin/map_single_fragments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_single_fragments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_circos_plot.py

```bash
$ singularity exec <container> /usr/local/bin/plot_circos_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_circos_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_circos_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_regions_interactions.py

```bash
$ singularity exec <container> /usr/local/bin/plot_regions_interactions.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_regions_interactions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_regions_interactions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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