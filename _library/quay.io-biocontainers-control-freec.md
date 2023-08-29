---
layout: container
name:  "quay.io/biocontainers/control-freec"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/control-freec/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/control-freec/container.yaml"
updated_at: "2023-08-29 03:20:28.070124"
latest: "11.6--hdbdd923_3"
container_url: "https://biocontainers.pro/tools/control-freec"
aliases:
 - "_makeGraph_Chromosome.R"
 - "assess_significance.R"
 - "freec"
 - "freec2bed.pl"
 - "freec2circos.pl"
 - "get_fasta_lengths.pl"
 - "makeGraph.R"
 - "makeGraph.R~"
 - "makeGraph_Chromosome.R"
 - "vcf2snpFreec.pl"
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
 - "11.6--h87f3376_2"
 - "11.6--hdbdd923_3"
description: "shpc-registry automated BioContainers addition for control-freec"
config: {"url": "https://biocontainers.pro/tools/control-freec", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for control-freec", "latest": {"11.6--hdbdd923_3": "sha256:246def482a76fc7fc9faaa04499853f29acc16680500d5ade3fcce4eeb074611"}, "tags": {"11.6--h87f3376_2": "sha256:84662aa8c0eed3fd0209a4e84936ad3fe7cecddb1947992f2b45ab217ec27222", "11.6--hdbdd923_3": "sha256:246def482a76fc7fc9faaa04499853f29acc16680500d5ade3fcce4eeb074611"}, "docker": "quay.io/biocontainers/control-freec", "aliases": {"_makeGraph_Chromosome.R": "/usr/local/bin/_makeGraph_Chromosome.R", "assess_significance.R": "/usr/local/bin/assess_significance.R", "freec": "/usr/local/bin/freec", "freec2bed.pl": "/usr/local/bin/freec2bed.pl", "freec2circos.pl": "/usr/local/bin/freec2circos.pl", "get_fasta_lengths.pl": "/usr/local/bin/get_fasta_lengths.pl", "makeGraph.R": "/usr/local/bin/makeGraph.R", "makeGraph.R~": "/usr/local/bin/makeGraph.R~", "makeGraph_Chromosome.R": "/usr/local/bin/makeGraph_Chromosome.R", "vcf2snpFreec.pl": "/usr/local/bin/vcf2snpFreec.pl", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/control-freec.
shpc-registry automated BioContainers addition for control-freec
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/control-freec
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/control-freec:11.6--hdbdd923_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/control-freec/11.6--hdbdd923_3
$ module help quay.io/biocontainers/control-freec/11.6--hdbdd923_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### control-freec-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### control-freec-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### control-freec-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### control-freec-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### control-freec-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### control-freec-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _makeGraph_Chromosome.R

```bash
$ singularity exec <container> /usr/local/bin/_makeGraph_Chromosome.R
$ podman run --it --rm --entrypoint /usr/local/bin/_makeGraph_Chromosome.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_makeGraph_Chromosome.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assess_significance.R

```bash
$ singularity exec <container> /usr/local/bin/assess_significance.R
$ podman run --it --rm --entrypoint /usr/local/bin/assess_significance.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assess_significance.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freec

```bash
$ singularity exec <container> /usr/local/bin/freec
$ podman run --it --rm --entrypoint /usr/local/bin/freec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freec2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/freec2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/freec2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freec2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freec2circos.pl

```bash
$ singularity exec <container> /usr/local/bin/freec2circos.pl
$ podman run --it --rm --entrypoint /usr/local/bin/freec2circos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freec2circos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_fasta_lengths.pl

```bash
$ singularity exec <container> /usr/local/bin/get_fasta_lengths.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_fasta_lengths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_fasta_lengths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeGraph.R

```bash
$ singularity exec <container> /usr/local/bin/makeGraph.R
$ podman run --it --rm --entrypoint /usr/local/bin/makeGraph.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeGraph.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeGraph.R~

```bash
$ singularity exec <container> /usr/local/bin/makeGraph.R~
$ podman run --it --rm --entrypoint /usr/local/bin/makeGraph.R~   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeGraph.R~   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeGraph_Chromosome.R

```bash
$ singularity exec <container> /usr/local/bin/makeGraph_Chromosome.R
$ podman run --it --rm --entrypoint /usr/local/bin/makeGraph_Chromosome.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeGraph_Chromosome.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2snpFreec.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2snpFreec.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2snpFreec.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2snpFreec.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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