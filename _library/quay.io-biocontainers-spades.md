---
layout: container
name:  "quay.io/biocontainers/spades"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spades/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spades/container.yaml"
updated_at: "2023-06-12 02:57:10.196826"
latest: "3.15.4--h95f258a_0"
container_url: "https://biocontainers.pro/tools/spades"
aliases:
 - "2to3-3.5"
 - "bwa-spades"
 - "cds-mapping-stats"
 - "cds-subgraphs"
 - "coronaspades.py"
 - "corrector"
 - "dipspades.py"
 - "dipspades"
 - "hammer"
 - "idle3.5"
 - "ionhammer"
 - "mag-improve"
 - "metaplasmidspades.py"
 - "metaspades.py"
 - "metaviralspades.py"
 - "plasmidspades.py"
 - "pydoc3.5"
 - "python3.5-config"
 - "python3.5"
 - "python3.5m-config"
 - "python3.5m"
 - "pyvenv-3.5"
 - "pyvenv"
 - "rnaspades.py"
 - "rnaviralspades.py"
 - "scaffold_correction"
 - "spades-bwa"
 - "spades-convert-bin-to-fasta"
 - "spades-core"
 - "spades-corrector-core"
 - "spades-gbuilder"
 - "spades-gmapper"
 - "spades-gsimplifier"
 - "spades-hammer"
 - "spades-ionhammer"
 - "spades-kmer-estimating"
 - "spades-kmercount"
 - "spades-read-filter"
 - "spades-truseq-scfcorrection"
 - "spades.py"
 - "spades"
 - "spades_init.py"
 - "spaligner"
 - "truspades.py"
versions:
 - "3.15.4--h95f258a_0"
description: "shpc-registry automated BioContainers addition for spades"
config: {"url": "https://biocontainers.pro/tools/spades", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spades", "latest": {"3.15.4--h95f258a_0": "sha256:7dfda44ae2535ba1ccc7c60c2ec265f8672cfd45885f458a964daf1b839a7ec1"}, "tags": {"3.15.4--h95f258a_0": "sha256:7dfda44ae2535ba1ccc7c60c2ec265f8672cfd45885f458a964daf1b839a7ec1"}, "docker": "quay.io/biocontainers/spades", "aliases": {"2to3-3.5": "/usr/local/bin/2to3-3.5", "bwa-spades": "/usr/local/bin/bwa-spades", "cds-mapping-stats": "/usr/local/bin/cds-mapping-stats", "cds-subgraphs": "/usr/local/bin/cds-subgraphs", "coronaspades.py": "/usr/local/bin/coronaspades.py", "corrector": "/usr/local/bin/corrector", "dipspades.py": "/usr/local/bin/dipspades.py", "dipspades": "/usr/local/bin/dipspades", "hammer": "/usr/local/bin/hammer", "idle3.5": "/usr/local/bin/idle3.5", "ionhammer": "/usr/local/bin/ionhammer", "mag-improve": "/usr/local/bin/mag-improve", "metaplasmidspades.py": "/usr/local/bin/metaplasmidspades.py", "metaspades.py": "/usr/local/bin/metaspades.py", "metaviralspades.py": "/usr/local/bin/metaviralspades.py", "plasmidspades.py": "/usr/local/bin/plasmidspades.py", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5-config": "/usr/local/bin/python3.5-config", "python3.5": "/usr/local/bin/python3.5", "python3.5m-config": "/usr/local/bin/python3.5m-config", "python3.5m": "/usr/local/bin/python3.5m", "pyvenv-3.5": "/usr/local/bin/pyvenv-3.5", "pyvenv": "/usr/local/bin/pyvenv", "rnaspades.py": "/usr/local/bin/rnaspades.py", "rnaviralspades.py": "/usr/local/bin/rnaviralspades.py", "scaffold_correction": "/usr/local/bin/scaffold_correction", "spades-bwa": "/usr/local/bin/spades-bwa", "spades-convert-bin-to-fasta": "/usr/local/bin/spades-convert-bin-to-fasta", "spades-core": "/usr/local/bin/spades-core", "spades-corrector-core": "/usr/local/bin/spades-corrector-core", "spades-gbuilder": "/usr/local/bin/spades-gbuilder", "spades-gmapper": "/usr/local/bin/spades-gmapper", "spades-gsimplifier": "/usr/local/bin/spades-gsimplifier", "spades-hammer": "/usr/local/bin/spades-hammer", "spades-ionhammer": "/usr/local/bin/spades-ionhammer", "spades-kmer-estimating": "/usr/local/bin/spades-kmer-estimating", "spades-kmercount": "/usr/local/bin/spades-kmercount", "spades-read-filter": "/usr/local/bin/spades-read-filter", "spades-truseq-scfcorrection": "/usr/local/bin/spades-truseq-scfcorrection", "spades.py": "/usr/local/bin/spades.py", "spades": "/usr/local/bin/spades", "spades_init.py": "/usr/local/bin/spades_init.py", "spaligner": "/usr/local/bin/spaligner", "truspades.py": "/usr/local/bin/truspades.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spades.
shpc-registry automated BioContainers addition for spades
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spades
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spades:3.15.4--h95f258a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spades/3.15.4--h95f258a_0
$ module help quay.io/biocontainers/spades/3.15.4--h95f258a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spades-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spades-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spades-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spades-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spades-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spades-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-spades

```bash
$ singularity exec <container> /usr/local/bin/bwa-spades
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-spades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-spades   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### coronaspades.py

```bash
$ singularity exec <container> /usr/local/bin/coronaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corrector

```bash
$ singularity exec <container> /usr/local/bin/corrector
$ podman run --it --rm --entrypoint /usr/local/bin/corrector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corrector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dipspades.py

```bash
$ singularity exec <container> /usr/local/bin/dipspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/dipspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dipspades

```bash
$ singularity exec <container> /usr/local/bin/dipspades
$ podman run --it --rm --entrypoint /usr/local/bin/dipspades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipspades   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hammer

```bash
$ singularity exec <container> /usr/local/bin/hammer
$ podman run --it --rm --entrypoint /usr/local/bin/hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.5

```bash
$ singularity exec <container> /usr/local/bin/idle3.5
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ionhammer

```bash
$ singularity exec <container> /usr/local/bin/ionhammer
$ podman run --it --rm --entrypoint /usr/local/bin/ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mag-improve

```bash
$ singularity exec <container> /usr/local/bin/mag-improve
$ podman run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaplasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaplasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/plasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.5

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5

```bash
$ singularity exec <container> /usr/local/bin/python3.5
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m

```bash
$ singularity exec <container> /usr/local/bin/python3.5m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.5

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scaffold_correction

```bash
$ singularity exec <container> /usr/local/bin/scaffold_correction
$ podman run --it --rm --entrypoint /usr/local/bin/scaffold_correction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scaffold_correction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-bwa

```bash
$ singularity exec <container> /usr/local/bin/spades-bwa
$ podman run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-convert-bin-to-fasta

```bash
$ singularity exec <container> /usr/local/bin/spades-convert-bin-to-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### spades-gsimplifier

```bash
$ singularity exec <container> /usr/local/bin/spades-gsimplifier
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### spades-kmer-estimating

```bash
$ singularity exec <container> /usr/local/bin/spades-kmer-estimating
$ podman run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmercount

```bash
$ singularity exec <container> /usr/local/bin/spades-kmercount
$ podman run --it --rm --entrypoint /usr/local/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-read-filter

```bash
$ singularity exec <container> /usr/local/bin/spades-read-filter
$ podman run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-truseq-scfcorrection

```bash
$ singularity exec <container> /usr/local/bin/spades-truseq-scfcorrection
$ podman run --it --rm --entrypoint /usr/local/bin/spades-truseq-scfcorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-truseq-scfcorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades.py

```bash
$ singularity exec <container> /usr/local/bin/spades.py
$ podman run --it --rm --entrypoint /usr/local/bin/spades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades

```bash
$ singularity exec <container> /usr/local/bin/spades
$ podman run --it --rm --entrypoint /usr/local/bin/spades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades_init.py

```bash
$ singularity exec <container> /usr/local/bin/spades_init.py
$ podman run --it --rm --entrypoint /usr/local/bin/spades_init.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades_init.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaligner

```bash
$ singularity exec <container> /usr/local/bin/spaligner
$ podman run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### truspades.py

```bash
$ singularity exec <container> /usr/local/bin/truspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/truspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/truspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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