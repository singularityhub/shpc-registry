---
layout: container
name:  "quay.io/biocontainers/biotradis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biotradis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biotradis/container.yaml"
updated_at: "2025-04-25 03:17:32.273716"
latest: "1.4.5--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/biotradis"
aliases:
 - "add_tradis_tags"
 - "bacteria_tradis"
 - "basqcol"
 - "check_tradis_tags"
 - "combine_tradis_plots"
 - "fetchseq"
 - "filter_tradis_tags"
 - "mixreads"
 - "readstats"
 - "remove_tradis_tags"
 - "simqual"
 - "simread"
 - "smalt"
 - "splitmates"
 - "splitreads"
 - "tradis_comparison.R"
 - "tradis_essentiality.R"
 - "tradis_gene_insert_sites"
 - "tradis_merge_plots"
 - "tradis_plot"
 - "trunkreads"
 - "config_data"
 - "bam2bedgraph"
 - "bp_pairwise_kaks"
 - "bp_find-blast-matches.pl"
 - "t_coffee"
 - "baseml"
 - "basemlg"
 - "chi2"
 - "codeml"
 - "evolver"
versions:
 - "1.4.5--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for biotradis"
config: {"url": "https://biocontainers.pro/tools/biotradis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biotradis", "latest": {"1.4.5--hdfd78af_5": "sha256:c6abddaabd2c7cb244c14acc9b7c22ca04faa439bc4cd8e85a6551550ba91054"}, "tags": {"1.4.5--hdfd78af_5": "sha256:c6abddaabd2c7cb244c14acc9b7c22ca04faa439bc4cd8e85a6551550ba91054"}, "docker": "quay.io/biocontainers/biotradis", "aliases": {"add_tradis_tags": "/usr/local/bin/add_tradis_tags", "bacteria_tradis": "/usr/local/bin/bacteria_tradis", "basqcol": "/usr/local/bin/basqcol", "check_tradis_tags": "/usr/local/bin/check_tradis_tags", "combine_tradis_plots": "/usr/local/bin/combine_tradis_plots", "fetchseq": "/usr/local/bin/fetchseq", "filter_tradis_tags": "/usr/local/bin/filter_tradis_tags", "mixreads": "/usr/local/bin/mixreads", "readstats": "/usr/local/bin/readstats", "remove_tradis_tags": "/usr/local/bin/remove_tradis_tags", "simqual": "/usr/local/bin/simqual", "simread": "/usr/local/bin/simread", "smalt": "/usr/local/bin/smalt", "splitmates": "/usr/local/bin/splitmates", "splitreads": "/usr/local/bin/splitreads", "tradis_comparison.R": "/usr/local/bin/tradis_comparison.R", "tradis_essentiality.R": "/usr/local/bin/tradis_essentiality.R", "tradis_gene_insert_sites": "/usr/local/bin/tradis_gene_insert_sites", "tradis_merge_plots": "/usr/local/bin/tradis_merge_plots", "tradis_plot": "/usr/local/bin/tradis_plot", "trunkreads": "/usr/local/bin/trunkreads", "config_data": "/usr/local/bin/config_data", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bp_pairwise_kaks": "/usr/local/bin/bp_pairwise_kaks", "bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "t_coffee": "/usr/local/bin/t_coffee", "baseml": "/usr/local/bin/baseml", "basemlg": "/usr/local/bin/basemlg", "chi2": "/usr/local/bin/chi2", "codeml": "/usr/local/bin/codeml", "evolver": "/usr/local/bin/evolver"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biotradis.
shpc-registry automated BioContainers addition for biotradis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biotradis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biotradis:1.4.5--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biotradis/1.4.5--hdfd78af_5
$ module help quay.io/biocontainers/biotradis/1.4.5--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biotradis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biotradis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biotradis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biotradis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biotradis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biotradis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_tradis_tags

```bash
$ singularity exec <container> /usr/local/bin/add_tradis_tags
$ podman run --it --rm --entrypoint /usr/local/bin/add_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bacteria_tradis

```bash
$ singularity exec <container> /usr/local/bin/bacteria_tradis
$ podman run --it --rm --entrypoint /usr/local/bin/bacteria_tradis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bacteria_tradis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basqcol

```bash
$ singularity exec <container> /usr/local/bin/basqcol
$ podman run --it --rm --entrypoint /usr/local/bin/basqcol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basqcol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_tradis_tags

```bash
$ singularity exec <container> /usr/local/bin/check_tradis_tags
$ podman run --it --rm --entrypoint /usr/local/bin/check_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_tradis_plots

```bash
$ singularity exec <container> /usr/local/bin/combine_tradis_plots
$ podman run --it --rm --entrypoint /usr/local/bin/combine_tradis_plots   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_tradis_plots   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetchseq

```bash
$ singularity exec <container> /usr/local/bin/fetchseq
$ podman run --it --rm --entrypoint /usr/local/bin/fetchseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_tradis_tags

```bash
$ singularity exec <container> /usr/local/bin/filter_tradis_tags
$ podman run --it --rm --entrypoint /usr/local/bin/filter_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mixreads

```bash
$ singularity exec <container> /usr/local/bin/mixreads
$ podman run --it --rm --entrypoint /usr/local/bin/mixreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mixreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readstats

```bash
$ singularity exec <container> /usr/local/bin/readstats
$ podman run --it --rm --entrypoint /usr/local/bin/readstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_tradis_tags

```bash
$ singularity exec <container> /usr/local/bin/remove_tradis_tags
$ podman run --it --rm --entrypoint /usr/local/bin/remove_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simqual

```bash
$ singularity exec <container> /usr/local/bin/simqual
$ podman run --it --rm --entrypoint /usr/local/bin/simqual   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simqual   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simread

```bash
$ singularity exec <container> /usr/local/bin/simread
$ podman run --it --rm --entrypoint /usr/local/bin/simread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smalt

```bash
$ singularity exec <container> /usr/local/bin/smalt
$ podman run --it --rm --entrypoint /usr/local/bin/smalt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smalt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitmates

```bash
$ singularity exec <container> /usr/local/bin/splitmates
$ podman run --it --rm --entrypoint /usr/local/bin/splitmates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitmates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitreads

```bash
$ singularity exec <container> /usr/local/bin/splitreads
$ podman run --it --rm --entrypoint /usr/local/bin/splitreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tradis_comparison.R

```bash
$ singularity exec <container> /usr/local/bin/tradis_comparison.R
$ podman run --it --rm --entrypoint /usr/local/bin/tradis_comparison.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tradis_comparison.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tradis_essentiality.R

```bash
$ singularity exec <container> /usr/local/bin/tradis_essentiality.R
$ podman run --it --rm --entrypoint /usr/local/bin/tradis_essentiality.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tradis_essentiality.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tradis_gene_insert_sites

```bash
$ singularity exec <container> /usr/local/bin/tradis_gene_insert_sites
$ podman run --it --rm --entrypoint /usr/local/bin/tradis_gene_insert_sites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tradis_gene_insert_sites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tradis_merge_plots

```bash
$ singularity exec <container> /usr/local/bin/tradis_merge_plots
$ podman run --it --rm --entrypoint /usr/local/bin/tradis_merge_plots   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tradis_merge_plots   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tradis_plot

```bash
$ singularity exec <container> /usr/local/bin/tradis_plot
$ podman run --it --rm --entrypoint /usr/local/bin/tradis_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tradis_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trunkreads

```bash
$ singularity exec <container> /usr/local/bin/trunkreads
$ podman run --it --rm --entrypoint /usr/local/bin/trunkreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trunkreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config_data

```bash
$ singularity exec <container> /usr/local/bin/config_data
$ podman run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t_coffee

```bash
$ singularity exec <container> /usr/local/bin/t_coffee
$ podman run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baseml

```bash
$ singularity exec <container> /usr/local/bin/baseml
$ podman run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basemlg

```bash
$ singularity exec <container> /usr/local/bin/basemlg
$ podman run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chi2

```bash
$ singularity exec <container> /usr/local/bin/chi2
$ podman run --it --rm --entrypoint /usr/local/bin/chi2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chi2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codeml

```bash
$ singularity exec <container> /usr/local/bin/codeml
$ podman run --it --rm --entrypoint /usr/local/bin/codeml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codeml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evolver

```bash
$ singularity exec <container> /usr/local/bin/evolver
$ podman run --it --rm --entrypoint /usr/local/bin/evolver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evolver   -v ${PWD} -w ${PWD} <container> -c " $@"
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