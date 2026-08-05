---
layout: container
name:  "quay.io/biocontainers/roundabout"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/roundabout/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/roundabout/container.yaml"
updated_at: "2026-08-05 05:43:05.451236"
latest: "0.7.26160--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/roundabout"
aliases:
 - "amrfinder_index"
 - "bakta"
 - "bakta_db"
 - "bakta_io"
 - "bakta_plot"
 - "bakta_proteins"
 - "daisyblast"
 - "disruption2genesymbol"
 - "download-db.sh"
 - "gawk-5.4.1"
 - "heatcluster"
 - "minkemap"
 - "mutate"
 - "pgv-blast"
 - "pgv-download"
 - "pgv-gui"
 - "pgv-mmseqs"
 - "pgv-mummer"
 - "pgv-pmauve"
 - "pilercr"
 - "plasmidfinder.py"
 - "progressiveMauve"
 - "refseq-plasmid-dl"
 - "roundabout"
 - "skani"
 - "stx.prot"
 - "stxtyper"
 - "test_stxtyper.sh"
 - "MitoHighConfidenceFilter"
 - "amrfinder_update"
 - "dna_mutation"
 - "fasta2parts"
 - "amr_report"
 - "amrfinder"
 - "fasta_extract"
 - "gff_check"
 - "fasta_check"
 - "EukHighConfidenceFilter"
 - "covels-SE"
 - "coves-SE"
 - "eufindtRNA"
 - "fasta2gsi"
 - "sstofa"
 - "tRNAscan-SE"
 - "tRNAscan-SE.conf"
 - "trnascan-1.4"
 - "kma"
 - "kma_index"
 - "kma_shm"
 - "kma_update"
 - "pyrodigal"
 - "fc-genconf"
 - "archspec"
versions:
 - "0.7.26160--pyh106432d_0"
description: "singularity registry hpc automated addition for roundabout"
config: {"url": "https://biocontainers.pro/tools/roundabout", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for roundabout", "latest": {"0.7.26160--pyh106432d_0": "sha256:f41360a62f7713fef481e37b34a4af061383bdbf8a5b98a686b900c38046f98f"}, "tags": {"0.7.26160--pyh106432d_0": "sha256:f41360a62f7713fef481e37b34a4af061383bdbf8a5b98a686b900c38046f98f"}, "docker": "quay.io/biocontainers/roundabout", "aliases": {"amrfinder_index": "/usr/local/bin/amrfinder_index", "bakta": "/usr/local/bin/bakta", "bakta_db": "/usr/local/bin/bakta_db", "bakta_io": "/usr/local/bin/bakta_io", "bakta_plot": "/usr/local/bin/bakta_plot", "bakta_proteins": "/usr/local/bin/bakta_proteins", "daisyblast": "/usr/local/bin/daisyblast", "disruption2genesymbol": "/usr/local/bin/disruption2genesymbol", "download-db.sh": "/usr/local/bin/download-db.sh", "gawk-5.4.1": "/usr/local/bin/gawk-5.4.1", "heatcluster": "/usr/local/bin/heatcluster", "minkemap": "/usr/local/bin/minkemap", "mutate": "/usr/local/bin/mutate", "pgv-blast": "/usr/local/bin/pgv-blast", "pgv-download": "/usr/local/bin/pgv-download", "pgv-gui": "/usr/local/bin/pgv-gui", "pgv-mmseqs": "/usr/local/bin/pgv-mmseqs", "pgv-mummer": "/usr/local/bin/pgv-mummer", "pgv-pmauve": "/usr/local/bin/pgv-pmauve", "pilercr": "/usr/local/bin/pilercr", "plasmidfinder.py": "/usr/local/bin/plasmidfinder.py", "progressiveMauve": "/usr/local/bin/progressiveMauve", "refseq-plasmid-dl": "/usr/local/bin/refseq-plasmid-dl", "roundabout": "/usr/local/bin/roundabout", "skani": "/usr/local/bin/skani", "stx.prot": "/usr/local/bin/stx.prot", "stxtyper": "/usr/local/bin/stxtyper", "test_stxtyper.sh": "/usr/local/bin/test_stxtyper.sh", "MitoHighConfidenceFilter": "/usr/local/bin/MitoHighConfidenceFilter", "amrfinder_update": "/usr/local/bin/amrfinder_update", "dna_mutation": "/usr/local/bin/dna_mutation", "fasta2parts": "/usr/local/bin/fasta2parts", "amr_report": "/usr/local/bin/amr_report", "amrfinder": "/usr/local/bin/amrfinder", "fasta_extract": "/usr/local/bin/fasta_extract", "gff_check": "/usr/local/bin/gff_check", "fasta_check": "/usr/local/bin/fasta_check", "EukHighConfidenceFilter": "/usr/local/bin/EukHighConfidenceFilter", "covels-SE": "/usr/local/bin/covels-SE", "coves-SE": "/usr/local/bin/coves-SE", "eufindtRNA": "/usr/local/bin/eufindtRNA", "fasta2gsi": "/usr/local/bin/fasta2gsi", "sstofa": "/usr/local/bin/sstofa", "tRNAscan-SE": "/usr/local/bin/tRNAscan-SE", "tRNAscan-SE.conf": "/usr/local/bin/tRNAscan-SE.conf", "trnascan-1.4": "/usr/local/bin/trnascan-1.4", "kma": "/usr/local/bin/kma", "kma_index": "/usr/local/bin/kma_index", "kma_shm": "/usr/local/bin/kma_shm", "kma_update": "/usr/local/bin/kma_update", "pyrodigal": "/usr/local/bin/pyrodigal", "fc-genconf": "/usr/local/bin/fc-genconf", "archspec": "/usr/local/bin/archspec"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/roundabout.
singularity registry hpc automated addition for roundabout
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/roundabout
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/roundabout:0.7.26160--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/roundabout/0.7.26160--pyh106432d_0
$ module help quay.io/biocontainers/roundabout/0.7.26160--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### roundabout-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### roundabout-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### roundabout-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### roundabout-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### roundabout-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### roundabout-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amrfinder_index

```bash
$ singularity exec <container> /usr/local/bin/amrfinder_index
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder_index   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bakta_io

```bash
$ singularity exec <container> /usr/local/bin/bakta_io
$ podman run --it --rm --entrypoint /usr/local/bin/bakta_io   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bakta_io   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bakta_plot

```bash
$ singularity exec <container> /usr/local/bin/bakta_plot
$ podman run --it --rm --entrypoint /usr/local/bin/bakta_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bakta_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bakta_proteins

```bash
$ singularity exec <container> /usr/local/bin/bakta_proteins
$ podman run --it --rm --entrypoint /usr/local/bin/bakta_proteins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bakta_proteins   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### daisyblast

```bash
$ singularity exec <container> /usr/local/bin/daisyblast
$ podman run --it --rm --entrypoint /usr/local/bin/daisyblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/daisyblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disruption2genesymbol

```bash
$ singularity exec <container> /usr/local/bin/disruption2genesymbol
$ podman run --it --rm --entrypoint /usr/local/bin/disruption2genesymbol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disruption2genesymbol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-db.sh

```bash
$ singularity exec <container> /usr/local/bin/download-db.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download-db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### heatcluster

```bash
$ singularity exec <container> /usr/local/bin/heatcluster
$ podman run --it --rm --entrypoint /usr/local/bin/heatcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/heatcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minkemap

```bash
$ singularity exec <container> /usr/local/bin/minkemap
$ podman run --it --rm --entrypoint /usr/local/bin/minkemap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minkemap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutate

```bash
$ singularity exec <container> /usr/local/bin/mutate
$ podman run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-blast

```bash
$ singularity exec <container> /usr/local/bin/pgv-blast
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-download

```bash
$ singularity exec <container> /usr/local/bin/pgv-download
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-gui

```bash
$ singularity exec <container> /usr/local/bin/pgv-gui
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-mmseqs

```bash
$ singularity exec <container> /usr/local/bin/pgv-mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-mummer

```bash
$ singularity exec <container> /usr/local/bin/pgv-mummer
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-pmauve

```bash
$ singularity exec <container> /usr/local/bin/pgv-pmauve
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-pmauve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-pmauve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilercr

```bash
$ singularity exec <container> /usr/local/bin/pilercr
$ podman run --it --rm --entrypoint /usr/local/bin/pilercr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilercr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasmidfinder.py

```bash
$ singularity exec <container> /usr/local/bin/plasmidfinder.py
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidfinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidfinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### progressiveMauve

```bash
$ singularity exec <container> /usr/local/bin/progressiveMauve
$ podman run --it --rm --entrypoint /usr/local/bin/progressiveMauve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/progressiveMauve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refseq-plasmid-dl

```bash
$ singularity exec <container> /usr/local/bin/refseq-plasmid-dl
$ podman run --it --rm --entrypoint /usr/local/bin/refseq-plasmid-dl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refseq-plasmid-dl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roundabout

```bash
$ singularity exec <container> /usr/local/bin/roundabout
$ podman run --it --rm --entrypoint /usr/local/bin/roundabout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roundabout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skani

```bash
$ singularity exec <container> /usr/local/bin/skani
$ podman run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stx.prot

```bash
$ singularity exec <container> /usr/local/bin/stx.prot
$ podman run --it --rm --entrypoint /usr/local/bin/stx.prot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stx.prot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stxtyper

```bash
$ singularity exec <container> /usr/local/bin/stxtyper
$ podman run --it --rm --entrypoint /usr/local/bin/stxtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stxtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_stxtyper.sh

```bash
$ singularity exec <container> /usr/local/bin/test_stxtyper.sh
$ podman run --it --rm --entrypoint /usr/local/bin/test_stxtyper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_stxtyper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MitoHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/MitoHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/MitoHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MitoHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fasta_check

```bash
$ singularity exec <container> /usr/local/bin/fasta_check
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EukHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/EukHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### covels-SE

```bash
$ singularity exec <container> /usr/local/bin/covels-SE
$ podman run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coves-SE

```bash
$ singularity exec <container> /usr/local/bin/coves-SE
$ podman run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eufindtRNA

```bash
$ singularity exec <container> /usr/local/bin/eufindtRNA
$ podman run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2gsi

```bash
$ singularity exec <container> /usr/local/bin/fasta2gsi
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2gsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2gsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sstofa

```bash
$ singularity exec <container> /usr/local/bin/sstofa
$ podman run --it --rm --entrypoint /usr/local/bin/sstofa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sstofa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscan-SE

```bash
$ singularity exec <container> /usr/local/bin/tRNAscan-SE
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscan-SE.conf

```bash
$ singularity exec <container> /usr/local/bin/tRNAscan-SE.conf
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trnascan-1.4

```bash
$ singularity exec <container> /usr/local/bin/trnascan-1.4
$ podman run --it --rm --entrypoint /usr/local/bin/trnascan-1.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trnascan-1.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma

```bash
$ singularity exec <container> /usr/local/bin/kma
$ podman run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_index

```bash
$ singularity exec <container> /usr/local/bin/kma_index
$ podman run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_shm

```bash
$ singularity exec <container> /usr/local/bin/kma_shm
$ podman run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_update

```bash
$ singularity exec <container> /usr/local/bin/kma_update
$ podman run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archspec

```bash
$ singularity exec <container> /usr/local/bin/archspec
$ podman run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
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