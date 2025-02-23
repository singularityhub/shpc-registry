---
layout: container
name:  "quay.io/biocontainers/eukfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eukfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eukfinder/container.yaml"
updated_at: "2025-02-23 03:34:47.214662"
latest: "1.2.3--py36hdbdd923_0"
container_url: "https://biocontainers.pro/tools/eukfinder"
aliases:
 - "Eukfinder.py"
 - "acc2tax"
 - "centrifuge"
 - "centrifuge-BuildSharedSequence.pl"
 - "centrifuge-RemoveEmptySequence.pl"
 - "centrifuge-RemoveN.pl"
 - "centrifuge-build"
 - "centrifuge-build-bin"
 - "centrifuge-class"
 - "centrifuge-compress.pl"
 - "centrifuge-download"
 - "centrifuge-inspect"
 - "centrifuge-inspect-bin"
 - "centrifuge-kreport"
 - "centrifuge-sort-nt.pl"
 - "centrifuge_evaluate.py"
 - "centrifuge_simulate_reads.py"
 - "eukfinder"
 - "plast"
 - "coronaspades.py"
 - "metaplasmidspades.py"
 - "metaviralspades.py"
 - "rnaviralspades.py"
 - "seqkit"
 - "cds-mapping-stats"
 - "cds-subgraphs"
 - "mag-improve"
 - "spades-convert-bin-to-fasta"
 - "spades-gsimplifier"
 - "spades-kmer-estimating"
 - "spades-read-filter"
 - "spaligner"
 - "spades-bwa"
 - "spades-core"
 - "spades-corrector-core"
 - "spades-gbuilder"
 - "spades-gmapper"
 - "spades-hammer"
 - "spades-ionhammer"
 - "spades-kmercount"
 - "spades-truseq-scfcorrection"
 - "trimmomatic"
 - "metaspades.py"
 - "plasmidspades.py"
versions:
 - "1.2.3--py36hdbdd923_0"
description: "singularity registry hpc automated addition for eukfinder"
config: {"url": "https://biocontainers.pro/tools/eukfinder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for eukfinder", "latest": {"1.2.3--py36hdbdd923_0": "sha256:f4ebd933e98662c8f41c9a4479dbea1f8e1031ac427e99fe786a0e3ea2941dd1"}, "tags": {"1.2.3--py36hdbdd923_0": "sha256:f4ebd933e98662c8f41c9a4479dbea1f8e1031ac427e99fe786a0e3ea2941dd1"}, "docker": "quay.io/biocontainers/eukfinder", "aliases": {"Eukfinder.py": "/usr/local/bin/Eukfinder.py", "acc2tax": "/usr/local/bin/acc2tax", "centrifuge": "/usr/local/bin/centrifuge", "centrifuge-BuildSharedSequence.pl": "/usr/local/bin/centrifuge-BuildSharedSequence.pl", "centrifuge-RemoveEmptySequence.pl": "/usr/local/bin/centrifuge-RemoveEmptySequence.pl", "centrifuge-RemoveN.pl": "/usr/local/bin/centrifuge-RemoveN.pl", "centrifuge-build": "/usr/local/bin/centrifuge-build", "centrifuge-build-bin": "/usr/local/bin/centrifuge-build-bin", "centrifuge-class": "/usr/local/bin/centrifuge-class", "centrifuge-compress.pl": "/usr/local/bin/centrifuge-compress.pl", "centrifuge-download": "/usr/local/bin/centrifuge-download", "centrifuge-inspect": "/usr/local/bin/centrifuge-inspect", "centrifuge-inspect-bin": "/usr/local/bin/centrifuge-inspect-bin", "centrifuge-kreport": "/usr/local/bin/centrifuge-kreport", "centrifuge-sort-nt.pl": "/usr/local/bin/centrifuge-sort-nt.pl", "centrifuge_evaluate.py": "/usr/local/bin/centrifuge_evaluate.py", "centrifuge_simulate_reads.py": "/usr/local/bin/centrifuge_simulate_reads.py", "eukfinder": "/usr/local/bin/eukfinder", "plast": "/usr/local/bin/plast", "coronaspades.py": "/usr/local/bin/coronaspades.py", "metaplasmidspades.py": "/usr/local/bin/metaplasmidspades.py", "metaviralspades.py": "/usr/local/bin/metaviralspades.py", "rnaviralspades.py": "/usr/local/bin/rnaviralspades.py", "seqkit": "/usr/local/bin/seqkit", "cds-mapping-stats": "/usr/local/bin/cds-mapping-stats", "cds-subgraphs": "/usr/local/bin/cds-subgraphs", "mag-improve": "/usr/local/bin/mag-improve", "spades-convert-bin-to-fasta": "/usr/local/bin/spades-convert-bin-to-fasta", "spades-gsimplifier": "/usr/local/bin/spades-gsimplifier", "spades-kmer-estimating": "/usr/local/bin/spades-kmer-estimating", "spades-read-filter": "/usr/local/bin/spades-read-filter", "spaligner": "/usr/local/bin/spaligner", "spades-bwa": "/usr/local/bin/spades-bwa", "spades-core": "/usr/local/bin/spades-core", "spades-corrector-core": "/usr/local/bin/spades-corrector-core", "spades-gbuilder": "/usr/local/bin/spades-gbuilder", "spades-gmapper": "/usr/local/bin/spades-gmapper", "spades-hammer": "/usr/local/bin/spades-hammer", "spades-ionhammer": "/usr/local/bin/spades-ionhammer", "spades-kmercount": "/usr/local/bin/spades-kmercount", "spades-truseq-scfcorrection": "/usr/local/bin/spades-truseq-scfcorrection", "trimmomatic": "/usr/local/bin/trimmomatic", "metaspades.py": "/usr/local/bin/metaspades.py", "plasmidspades.py": "/usr/local/bin/plasmidspades.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eukfinder.
singularity registry hpc automated addition for eukfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eukfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eukfinder:1.2.3--py36hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eukfinder/1.2.3--py36hdbdd923_0
$ module help quay.io/biocontainers/eukfinder/1.2.3--py36hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eukfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eukfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eukfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eukfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eukfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eukfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Eukfinder.py

```bash
$ singularity exec <container> /usr/local/bin/Eukfinder.py
$ podman run --it --rm --entrypoint /usr/local/bin/Eukfinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Eukfinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acc2tax

```bash
$ singularity exec <container> /usr/local/bin/acc2tax
$ podman run --it --rm --entrypoint /usr/local/bin/acc2tax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acc2tax   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge

```bash
$ singularity exec <container> /usr/local/bin/centrifuge
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-BuildSharedSequence.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-BuildSharedSequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-BuildSharedSequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-BuildSharedSequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-RemoveEmptySequence.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-RemoveEmptySequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveEmptySequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveEmptySequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-RemoveN.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-RemoveN.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveN.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveN.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-build

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-build
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-build-bin

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-build-bin
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-build-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-build-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-class

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-class
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-class   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-class   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-compress.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-compress.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-compress.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-compress.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-download

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-download
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-inspect

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-inspect-bin

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-inspect-bin
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-kreport

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-kreport
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-sort-nt.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-sort-nt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-sort-nt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-sort-nt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge_evaluate.py

```bash
$ singularity exec <container> /usr/local/bin/centrifuge_evaluate.py
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge_evaluate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge_evaluate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge_simulate_reads.py

```bash
$ singularity exec <container> /usr/local/bin/centrifuge_simulate_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eukfinder

```bash
$ singularity exec <container> /usr/local/bin/eukfinder
$ podman run --it --rm --entrypoint /usr/local/bin/eukfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eukfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plast

```bash
$ singularity exec <container> /usr/local/bin/plast
$ podman run --it --rm --entrypoint /usr/local/bin/plast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coronaspades.py

```bash
$ singularity exec <container> /usr/local/bin/coronaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaplasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaplasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-mapping-stats

```bash
$ singularity exec <container> /usr/local/bin/cds-mapping-stats
$ podman run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-subgraphs

```bash
$ singularity exec <container> /usr/local/bin/cds-subgraphs
$ podman run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mag-improve

```bash
$ singularity exec <container> /usr/local/bin/mag-improve
$ podman run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-convert-bin-to-fasta

```bash
$ singularity exec <container> /usr/local/bin/spades-convert-bin-to-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gsimplifier

```bash
$ singularity exec <container> /usr/local/bin/spades-gsimplifier
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmer-estimating

```bash
$ singularity exec <container> /usr/local/bin/spades-kmer-estimating
$ podman run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-read-filter

```bash
$ singularity exec <container> /usr/local/bin/spades-read-filter
$ podman run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaligner

```bash
$ singularity exec <container> /usr/local/bin/spaligner
$ podman run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-bwa

```bash
$ singularity exec <container> /usr/local/bin/spades-bwa
$ podman run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-core

```bash
$ singularity exec <container> /usr/local/bin/spades-core
$ podman run --it --rm --entrypoint /usr/local/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-corrector-core

```bash
$ singularity exec <container> /usr/local/bin/spades-corrector-core
$ podman run --it --rm --entrypoint /usr/local/bin/spades-corrector-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-corrector-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gbuilder

```bash
$ singularity exec <container> /usr/local/bin/spades-gbuilder
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gmapper

```bash
$ singularity exec <container> /usr/local/bin/spades-gmapper
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-hammer

```bash
$ singularity exec <container> /usr/local/bin/spades-hammer
$ podman run --it --rm --entrypoint /usr/local/bin/spades-hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-ionhammer

```bash
$ singularity exec <container> /usr/local/bin/spades-ionhammer
$ podman run --it --rm --entrypoint /usr/local/bin/spades-ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmercount

```bash
$ singularity exec <container> /usr/local/bin/spades-kmercount
$ podman run --it --rm --entrypoint /usr/local/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-truseq-scfcorrection

```bash
$ singularity exec <container> /usr/local/bin/spades-truseq-scfcorrection
$ podman run --it --rm --entrypoint /usr/local/bin/spades-truseq-scfcorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-truseq-scfcorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmomatic

```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/plasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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