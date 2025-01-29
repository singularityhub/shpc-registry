---
layout: container
name:  "quay.io/biocontainers/metapop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metapop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metapop/container.yaml"
updated_at: "2025-01-29 03:26:41.475327"
latest: "1.0.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/metapop"
aliases:
 - "MetaPop.R"
 - "MetaPop_Call_SNPs.R"
 - "MetaPop_Codon_Bias_Separate.R"
 - "MetaPop_Codon_Bias_Viz.R"
 - "MetaPop_Macrodiversity.R"
 - "MetaPop_Microdiversity.R"
 - "MetaPop_Microdiversity_Visualizations.R"
 - "MetaPop_Mine_Reads.R"
 - "MetaPop_Preprocess.R"
 - "MetaPop_Preprocessing_Summaries.R"
 - "gff2gff.py"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
versions:
 - "1.0.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for metapop"
config: {"url": "https://biocontainers.pro/tools/metapop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metapop", "latest": {"1.0.2--hdfd78af_1": "sha256:b670034d0fe0d3cfac8ce98d0834dd30fa8834243c98ea871485a3608ae2c03c"}, "tags": {"1.0.2--hdfd78af_1": "sha256:b670034d0fe0d3cfac8ce98d0834dd30fa8834243c98ea871485a3608ae2c03c"}, "docker": "quay.io/biocontainers/metapop", "aliases": {"MetaPop.R": "/usr/local/bin/MetaPop.R", "MetaPop_Call_SNPs.R": "/usr/local/bin/MetaPop_Call_SNPs.R", "MetaPop_Codon_Bias_Separate.R": "/usr/local/bin/MetaPop_Codon_Bias_Separate.R", "MetaPop_Codon_Bias_Viz.R": "/usr/local/bin/MetaPop_Codon_Bias_Viz.R", "MetaPop_Macrodiversity.R": "/usr/local/bin/MetaPop_Macrodiversity.R", "MetaPop_Microdiversity.R": "/usr/local/bin/MetaPop_Microdiversity.R", "MetaPop_Microdiversity_Visualizations.R": "/usr/local/bin/MetaPop_Microdiversity_Visualizations.R", "MetaPop_Mine_Reads.R": "/usr/local/bin/MetaPop_Mine_Reads.R", "MetaPop_Preprocess.R": "/usr/local/bin/MetaPop_Preprocess.R", "MetaPop_Preprocessing_Summaries.R": "/usr/local/bin/MetaPop_Preprocessing_Summaries.R", "gff2gff.py": "/usr/local/bin/gff2gff.py", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metapop.
shpc-registry automated BioContainers addition for metapop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metapop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metapop:1.0.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metapop/1.0.2--hdfd78af_1
$ module help quay.io/biocontainers/metapop/1.0.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metapop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metapop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metapop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metapop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metapop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metapop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MetaPop.R

```bash
$ singularity exec <container> /usr/local/bin/MetaPop.R
$ podman run --it --rm --entrypoint /usr/local/bin/MetaPop.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaPop.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaPop_Call_SNPs.R

```bash
$ singularity exec <container> /usr/local/bin/MetaPop_Call_SNPs.R
$ podman run --it --rm --entrypoint /usr/local/bin/MetaPop_Call_SNPs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaPop_Call_SNPs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaPop_Codon_Bias_Separate.R

```bash
$ singularity exec <container> /usr/local/bin/MetaPop_Codon_Bias_Separate.R
$ podman run --it --rm --entrypoint /usr/local/bin/MetaPop_Codon_Bias_Separate.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaPop_Codon_Bias_Separate.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaPop_Codon_Bias_Viz.R

```bash
$ singularity exec <container> /usr/local/bin/MetaPop_Codon_Bias_Viz.R
$ podman run --it --rm --entrypoint /usr/local/bin/MetaPop_Codon_Bias_Viz.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaPop_Codon_Bias_Viz.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaPop_Macrodiversity.R

```bash
$ singularity exec <container> /usr/local/bin/MetaPop_Macrodiversity.R
$ podman run --it --rm --entrypoint /usr/local/bin/MetaPop_Macrodiversity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaPop_Macrodiversity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaPop_Microdiversity.R

```bash
$ singularity exec <container> /usr/local/bin/MetaPop_Microdiversity.R
$ podman run --it --rm --entrypoint /usr/local/bin/MetaPop_Microdiversity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaPop_Microdiversity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaPop_Microdiversity_Visualizations.R

```bash
$ singularity exec <container> /usr/local/bin/MetaPop_Microdiversity_Visualizations.R
$ podman run --it --rm --entrypoint /usr/local/bin/MetaPop_Microdiversity_Visualizations.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaPop_Microdiversity_Visualizations.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaPop_Mine_Reads.R

```bash
$ singularity exec <container> /usr/local/bin/MetaPop_Mine_Reads.R
$ podman run --it --rm --entrypoint /usr/local/bin/MetaPop_Mine_Reads.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaPop_Mine_Reads.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaPop_Preprocess.R

```bash
$ singularity exec <container> /usr/local/bin/MetaPop_Preprocess.R
$ podman run --it --rm --entrypoint /usr/local/bin/MetaPop_Preprocess.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaPop_Preprocess.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaPop_Preprocessing_Summaries.R

```bash
$ singularity exec <container> /usr/local/bin/MetaPop_Preprocessing_Summaries.R
$ podman run --it --rm --entrypoint /usr/local/bin/MetaPop_Preprocessing_Summaries.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaPop_Preprocessing_Summaries.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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