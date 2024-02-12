---
layout: container
name:  "quay.io/biocontainers/arriba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arriba/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arriba/container.yaml"
updated_at: "2024-02-12 02:43:27.167394"
latest: "2.4.0--h0033a41_2"
container_url: "https://biocontainers.pro/tools/arriba"
aliases:
 - "arriba"
 - "convert_fusions_to_vcf.sh"
 - "draw_fusions.R"
 - "extract_fusion-supporting_alignments.sh"
 - "quantify_virus_expression.sh"
 - "run_arriba.sh"
 - "run_arriba_on_prealigned_bam.sh"
 - "STAR"
 - "STARlong"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "interpolate_sam.pl"
 - "maq2sam-long"
versions:
 - "2.3.0--ha04fe3b_1"
 - "2.4.0--h6b7c446_1"
 - "2.4.0--h0033a41_2"
description: "shpc-registry automated BioContainers addition for arriba"
config: {"url": "https://biocontainers.pro/tools/arriba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for arriba", "latest": {"2.4.0--h0033a41_2": "sha256:d4632bdaa59ba9619c4c72d897b7551ec993d79cd3acefa475169eba9bfc8d29"}, "tags": {"2.3.0--ha04fe3b_1": "sha256:0b46650c649f24856861dcddb21c1d78fbefaef437ea3619c9304f59b1de1ae5", "2.4.0--h6b7c446_1": "sha256:4e6d33c6d163b2b27185ba08312472e77cfab3d3a745bc2ef1eac90d32c4df9f", "2.4.0--h0033a41_2": "sha256:d4632bdaa59ba9619c4c72d897b7551ec993d79cd3acefa475169eba9bfc8d29"}, "docker": "quay.io/biocontainers/arriba", "aliases": {"arriba": "/usr/local/bin/arriba", "convert_fusions_to_vcf.sh": "/usr/local/bin/convert_fusions_to_vcf.sh", "draw_fusions.R": "/usr/local/bin/draw_fusions.R", "extract_fusion-supporting_alignments.sh": "/usr/local/bin/extract_fusion-supporting_alignments.sh", "quantify_virus_expression.sh": "/usr/local/bin/quantify_virus_expression.sh", "run_arriba.sh": "/usr/local/bin/run_arriba.sh", "run_arriba_on_prealigned_bam.sh": "/usr/local/bin/run_arriba_on_prealigned_bam.sh", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arriba.
shpc-registry automated BioContainers addition for arriba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arriba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arriba:2.4.0--h0033a41_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arriba/2.4.0--h0033a41_2
$ module help quay.io/biocontainers/arriba/2.4.0--h0033a41_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arriba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arriba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arriba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arriba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arriba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arriba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arriba

```bash
$ singularity exec <container> /usr/local/bin/arriba
$ podman run --it --rm --entrypoint /usr/local/bin/arriba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arriba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_fusions_to_vcf.sh

```bash
$ singularity exec <container> /usr/local/bin/convert_fusions_to_vcf.sh
$ podman run --it --rm --entrypoint /usr/local/bin/convert_fusions_to_vcf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_fusions_to_vcf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### draw_fusions.R

```bash
$ singularity exec <container> /usr/local/bin/draw_fusions.R
$ podman run --it --rm --entrypoint /usr/local/bin/draw_fusions.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/draw_fusions.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_fusion-supporting_alignments.sh

```bash
$ singularity exec <container> /usr/local/bin/extract_fusion-supporting_alignments.sh
$ podman run --it --rm --entrypoint /usr/local/bin/extract_fusion-supporting_alignments.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_fusion-supporting_alignments.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quantify_virus_expression.sh

```bash
$ singularity exec <container> /usr/local/bin/quantify_virus_expression.sh
$ podman run --it --rm --entrypoint /usr/local/bin/quantify_virus_expression.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quantify_virus_expression.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_arriba.sh

```bash
$ singularity exec <container> /usr/local/bin/run_arriba.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_arriba.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_arriba.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_arriba_on_prealigned_bam.sh

```bash
$ singularity exec <container> /usr/local/bin/run_arriba_on_prealigned_bam.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_arriba_on_prealigned_bam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_arriba_on_prealigned_bam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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