---
layout: container
name:  "quay.io/biocontainers/bactopia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bactopia/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bactopia/container.yaml"
updated_at: "2022-10-27 00:18:38.402909"
latest: "2.1.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bactopia"
aliases:
 - "amr_report"
 - "amrfinder"
 - "amrfinder_update"
 - "ariba"
 - "bactopia"
 - "bactopia-citations.py"
 - "bactopia-datasets.py"
 - "bactopia-download.py"
 - "bactopia-prepare.py"
 - "bactopia-search.py"
 - "check-assembly-accession.py"
 - "check-fastqs.py"
 - "cleanup-coverage.py"
 - "dna_mutation"
 - "executor"
 - "fasta2parts"
 - "fasta_check"
 - "fasta_extract"
 - "gff_check"
 - "gimme_taxa.py"
 - "mamba-package"
 - "mask-consensus.py"
 - "merge-blast-json.py"
 - "mlst-blast.py"
 - "ncbi-genome-download"
 - "nextflow.bak"
 - "ngd"
 - "select-references.py"
 - "split-coverages.py"
 - "staphopia"
versions:
 - "2.1.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bactopia"
config: {"url": "https://biocontainers.pro/tools/bactopia", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bactopia", "latest": {"2.1.1--hdfd78af_0": "sha256:4febfb57515009b8a872666d0d541d942777afbfbdfd5b4d0b0e1a47987fbe51"}, "tags": {"2.1.1--hdfd78af_0": "sha256:4febfb57515009b8a872666d0d541d942777afbfbdfd5b4d0b0e1a47987fbe51"}, "docker": "quay.io/biocontainers/bactopia", "aliases": {"amr_report": "/usr/local/bin/amr_report", "amrfinder": "/usr/local/bin/amrfinder", "amrfinder_update": "/usr/local/bin/amrfinder_update", "ariba": "/usr/local/bin/ariba", "bactopia": "/usr/local/bin/bactopia", "bactopia-citations.py": "/usr/local/bin/bactopia-citations.py", "bactopia-datasets.py": "/usr/local/bin/bactopia-datasets.py", "bactopia-download.py": "/usr/local/bin/bactopia-download.py", "bactopia-prepare.py": "/usr/local/bin/bactopia-prepare.py", "bactopia-search.py": "/usr/local/bin/bactopia-search.py", "check-assembly-accession.py": "/usr/local/bin/check-assembly-accession.py", "check-fastqs.py": "/usr/local/bin/check-fastqs.py", "cleanup-coverage.py": "/usr/local/bin/cleanup-coverage.py", "dna_mutation": "/usr/local/bin/dna_mutation", "executor": "/usr/local/bin/executor", "fasta2parts": "/usr/local/bin/fasta2parts", "fasta_check": "/usr/local/bin/fasta_check", "fasta_extract": "/usr/local/bin/fasta_extract", "gff_check": "/usr/local/bin/gff_check", "gimme_taxa.py": "/usr/local/bin/gimme_taxa.py", "mamba-package": "/usr/local/bin/mamba-package", "mask-consensus.py": "/usr/local/bin/mask-consensus.py", "merge-blast-json.py": "/usr/local/bin/merge-blast-json.py", "mlst-blast.py": "/usr/local/bin/mlst-blast.py", "ncbi-genome-download": "/usr/local/bin/ncbi-genome-download", "nextflow.bak": "/usr/local/bin/nextflow.bak", "ngd": "/usr/local/bin/ngd", "select-references.py": "/usr/local/bin/select-references.py", "split-coverages.py": "/usr/local/bin/split-coverages.py", "staphopia": "/usr/local/bin/staphopia"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bactopia.
shpc-registry automated BioContainers addition for bactopia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bactopia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bactopia:2.1.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bactopia/2.1.1--hdfd78af_0
$ module help quay.io/biocontainers/bactopia/2.1.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bactopia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bactopia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bactopia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bactopia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bactopia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bactopia-inspect-deffile:

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


#### ariba

```bash
$ singularity exec <container> /usr/local/bin/ariba
$ podman run --it --rm --entrypoint /usr/local/bin/ariba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ariba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia

```bash
$ singularity exec <container> /usr/local/bin/bactopia
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia-citations.py

```bash
$ singularity exec <container> /usr/local/bin/bactopia-citations.py
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-citations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-citations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia-datasets.py

```bash
$ singularity exec <container> /usr/local/bin/bactopia-datasets.py
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-datasets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-datasets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia-download.py

```bash
$ singularity exec <container> /usr/local/bin/bactopia-download.py
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-download.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-download.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia-prepare.py

```bash
$ singularity exec <container> /usr/local/bin/bactopia-prepare.py
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-prepare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-prepare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia-search.py

```bash
$ singularity exec <container> /usr/local/bin/bactopia-search.py
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-search.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-search.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check-assembly-accession.py

```bash
$ singularity exec <container> /usr/local/bin/check-assembly-accession.py
$ podman run --it --rm --entrypoint /usr/local/bin/check-assembly-accession.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check-assembly-accession.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check-fastqs.py

```bash
$ singularity exec <container> /usr/local/bin/check-fastqs.py
$ podman run --it --rm --entrypoint /usr/local/bin/check-fastqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check-fastqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cleanup-coverage.py

```bash
$ singularity exec <container> /usr/local/bin/cleanup-coverage.py
$ podman run --it --rm --entrypoint /usr/local/bin/cleanup-coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cleanup-coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dna_mutation

```bash
$ singularity exec <container> /usr/local/bin/dna_mutation
$ podman run --it --rm --entrypoint /usr/local/bin/dna_mutation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dna_mutation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### executor

```bash
$ singularity exec <container> /usr/local/bin/executor
$ podman run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gimme_taxa.py

```bash
$ singularity exec <container> /usr/local/bin/gimme_taxa.py
$ podman run --it --rm --entrypoint /usr/local/bin/gimme_taxa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gimme_taxa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba-package

```bash
$ singularity exec <container> /usr/local/bin/mamba-package
$ podman run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mask-consensus.py

```bash
$ singularity exec <container> /usr/local/bin/mask-consensus.py
$ podman run --it --rm --entrypoint /usr/local/bin/mask-consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mask-consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-blast-json.py

```bash
$ singularity exec <container> /usr/local/bin/merge-blast-json.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge-blast-json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-blast-json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst-blast.py

```bash
$ singularity exec <container> /usr/local/bin/mlst-blast.py
$ podman run --it --rm --entrypoint /usr/local/bin/mlst-blast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst-blast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi-genome-download

```bash
$ singularity exec <container> /usr/local/bin/ncbi-genome-download
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow.bak

```bash
$ singularity exec <container> /usr/local/bin/nextflow.bak
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngd

```bash
$ singularity exec <container> /usr/local/bin/ngd
$ podman run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select-references.py

```bash
$ singularity exec <container> /usr/local/bin/select-references.py
$ podman run --it --rm --entrypoint /usr/local/bin/select-references.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select-references.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-coverages.py

```bash
$ singularity exec <container> /usr/local/bin/split-coverages.py
$ podman run --it --rm --entrypoint /usr/local/bin/split-coverages.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-coverages.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### staphopia

```bash
$ singularity exec <container> /usr/local/bin/staphopia
$ podman run --it --rm --entrypoint /usr/local/bin/staphopia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/staphopia   -v ${PWD} -w ${PWD} <container> -c " $@"
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