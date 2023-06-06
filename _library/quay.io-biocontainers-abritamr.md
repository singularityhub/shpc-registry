---
layout: container
name:  "quay.io/biocontainers/abritamr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abritamr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/abritamr/container.yaml"
updated_at: "2023-06-06 03:03:30.016035"
latest: "1.0.14--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/abritamr"
aliases:
 - "abriTAMR"
 - "abritamr"
 - "amr_report"
 - "amrfinder"
 - "amrfinder_update"
 - "dna_mutation"
 - "fasta2parts"
 - "fasta_check"
 - "fasta_extract"
 - "gff_check"
 - "vba_extract.py"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "align-columns"
 - "blst2tkns"
 - "csv2xml"
versions:
 - "1.0.9--hdfd78af_0"
 - "1.0.13--pyhdfd78af_0"
 - "1.0.14--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for abritamr"
config: {"url": "https://biocontainers.pro/tools/abritamr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for abritamr", "latest": {"1.0.14--pyhdfd78af_0": "sha256:1dc33feef2958332eef7b5ac1909ec99f6ba6ef306f35e22966e3b73faa4fab8"}, "tags": {"1.0.9--hdfd78af_0": "sha256:548ef2995e2e0ab8f09f81cc1f31e1d59463fcbf47494382d181fdbdc2fb8faf", "1.0.13--pyhdfd78af_0": "sha256:b9b76b502c1a391e4ef39fdc24ebfb7d95b66a85be5258091138059402793f6f", "1.0.14--pyhdfd78af_0": "sha256:1dc33feef2958332eef7b5ac1909ec99f6ba6ef306f35e22966e3b73faa4fab8"}, "docker": "quay.io/biocontainers/abritamr", "aliases": {"abriTAMR": "/usr/local/bin/abriTAMR", "abritamr": "/usr/local/bin/abritamr", "amr_report": "/usr/local/bin/amr_report", "amrfinder": "/usr/local/bin/amrfinder", "amrfinder_update": "/usr/local/bin/amrfinder_update", "dna_mutation": "/usr/local/bin/dna_mutation", "fasta2parts": "/usr/local/bin/fasta2parts", "fasta_check": "/usr/local/bin/fasta_check", "fasta_extract": "/usr/local/bin/fasta_extract", "gff_check": "/usr/local/bin/gff_check", "vba_extract.py": "/usr/local/bin/vba_extract.py", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abritamr.
shpc-registry automated BioContainers addition for abritamr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abritamr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abritamr:1.0.14--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abritamr/1.0.14--pyhdfd78af_0
$ module help quay.io/biocontainers/abritamr/1.0.14--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abritamr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abritamr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abritamr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abritamr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abritamr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abritamr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abriTAMR

```bash
$ singularity exec <container> /usr/local/bin/abriTAMR
$ podman run --it --rm --entrypoint /usr/local/bin/abriTAMR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abriTAMR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abritamr

```bash
$ singularity exec <container> /usr/local/bin/abritamr
$ podman run --it --rm --entrypoint /usr/local/bin/abritamr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abritamr   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blst2tkns

```bash
$ singularity exec <container> /usr/local/bin/blst2tkns
$ podman run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2xml

```bash
$ singularity exec <container> /usr/local/bin/csv2xml
$ podman run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
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