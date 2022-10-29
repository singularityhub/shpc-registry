---
layout: container
name:  "quay.io/biocontainers/bakta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bakta/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bakta/container.yaml"
updated_at: "2022-10-29 05:39:50.861212"
latest: "1.5.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bakta"
aliases:
 - "amr_report"
 - "amrfinder"
 - "amrfinder_update"
 - "bakta"
 - "bakta_db"
 - "bakta_proteins"
 - "dna_mutation"
 - "fasta2parts"
 - "fasta_check"
 - "fasta_extract"
 - "gff_check"
 - "pilercr"
 - "2to3-3.10"
 - "EukHighConfidenceFilter"
 - "accn-at-a-time"
 - "align-columns"
 - "alimask"
 - "amino-acid-composition"
 - "aragorn"
 - "archive-pubmed"
 - "asn2xml"
 - "between-two-genes"
versions:
 - "1.5.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for bakta"
config: {"url": "https://biocontainers.pro/tools/bakta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bakta", "latest": {"1.5.1--pyhdfd78af_0": "sha256:4b6e6caef591f0caa658dff7db4d153abf4b3200948da0e3701dd65637adfdb0"}, "tags": {"1.5.1--pyhdfd78af_0": "sha256:4b6e6caef591f0caa658dff7db4d153abf4b3200948da0e3701dd65637adfdb0"}, "docker": "quay.io/biocontainers/bakta", "aliases": {"amr_report": "/usr/local/bin/amr_report", "amrfinder": "/usr/local/bin/amrfinder", "amrfinder_update": "/usr/local/bin/amrfinder_update", "bakta": "/usr/local/bin/bakta", "bakta_db": "/usr/local/bin/bakta_db", "bakta_proteins": "/usr/local/bin/bakta_proteins", "dna_mutation": "/usr/local/bin/dna_mutation", "fasta2parts": "/usr/local/bin/fasta2parts", "fasta_check": "/usr/local/bin/fasta_check", "fasta_extract": "/usr/local/bin/fasta_extract", "gff_check": "/usr/local/bin/gff_check", "pilercr": "/usr/local/bin/pilercr", "2to3-3.10": "/usr/local/bin/2to3-3.10", "EukHighConfidenceFilter": "/usr/local/bin/EukHighConfidenceFilter", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "align-columns": "/usr/local/bin/align-columns", "alimask": "/usr/local/bin/alimask", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "aragorn": "/usr/local/bin/aragorn", "archive-pubmed": "/usr/local/bin/archive-pubmed", "asn2xml": "/usr/local/bin/asn2xml", "between-two-genes": "/usr/local/bin/between-two-genes"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bakta.
shpc-registry automated BioContainers addition for bakta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bakta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bakta:1.5.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bakta/1.5.1--pyhdfd78af_0
$ module help quay.io/biocontainers/bakta/1.5.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bakta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bakta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bakta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bakta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bakta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bakta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amr_report

```bash
$ singularity exec <container> /usr/local/bin/amr_report
$ podman run --it --rm --entrypoint /usr/local/bin/amr_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amr_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrfinder

```bash
$ singularity exec <container> /usr/local/bin/amrfinder
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrfinder_update

```bash
$ singularity exec <container> /usr/local/bin/amrfinder_update
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bakta

```bash
$ singularity exec <container> /usr/local/bin/bakta
$ podman run --it --rm --entrypoint /usr/local/bin/bakta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bakta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bakta_db

```bash
$ singularity exec <container> /usr/local/bin/bakta_db
$ podman run --it --rm --entrypoint /usr/local/bin/bakta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bakta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bakta_proteins

```bash
$ singularity exec <container> /usr/local/bin/bakta_proteins
$ podman run --it --rm --entrypoint /usr/local/bin/bakta_proteins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bakta_proteins   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dna_mutation

```bash
$ singularity exec <container> /usr/local/bin/dna_mutation
$ podman run --it --rm --entrypoint /usr/local/bin/dna_mutation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dna_mutation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2parts

```bash
$ singularity exec <container> /usr/local/bin/fasta2parts
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2parts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2parts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_check

```bash
$ singularity exec <container> /usr/local/bin/fasta_check
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_extract

```bash
$ singularity exec <container> /usr/local/bin/fasta_extract
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff_check

```bash
$ singularity exec <container> /usr/local/bin/gff_check
$ podman run --it --rm --entrypoint /usr/local/bin/gff_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilercr

```bash
$ singularity exec <container> /usr/local/bin/pilercr
$ podman run --it --rm --entrypoint /usr/local/bin/pilercr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilercr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EukHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/EukHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aragorn

```bash
$ singularity exec <container> /usr/local/bin/aragorn
$ podman run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn2xml

```bash
$ singularity exec <container> /usr/local/bin/asn2xml
$ podman run --it --rm --entrypoint /usr/local/bin/asn2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### between-two-genes

```bash
$ singularity exec <container> /usr/local/bin/between-two-genes
$ podman run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
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