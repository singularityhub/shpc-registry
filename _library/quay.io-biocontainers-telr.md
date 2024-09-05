---
layout: container
name:  "quay.io/biocontainers/telr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/telr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/telr/container.yaml"
updated_at: "2024-09-05 02:54:52.931734"
latest: "1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/telr"
aliases:
 - "DateRepeats"
 - "DupMasker"
 - "ProcessRepeats"
 - "RepeatMasker"
 - "RepeatProteinMask"
 - "calcDivergenceFromAlign.pl"
 - "createRepeatLandscape.pl"
 - "dupliconToSVG.pl"
 - "flye"
 - "flye-minimap2"
 - "flye-modules"
 - "flye-samtools"
 - "getRepeatMaskerBatch.pl"
 - "ngmlr"
 - "queryRepeatDatabase.pl"
 - "queryTaxonomyDatabase.pl"
 - "rmOut2Fasta.pl"
 - "rmOutToGFF3.pl"
 - "rmToUCSCTables.pl"
 - "sniffles"
 - "sniffles-debug"
 - "telr"
 - "trfMask"
 - "wtdbg-cns"
 - "wtdbg2"
 - "wtpoa-cns"
 - "rmblastn"
 - "trf4.10.0-rc.2.linux64.exe"
 - "trf"
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
 - "gnutls-serv"
 - "nettle-hash"
 - "nettle-lfib-stream"
 - "nettle-pbkdf2"
versions:
 - "0.2--pyhdfd78af_1"
 - "0.2--pyhdfd78af_2"
 - "1.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for telr"
config: {"url": "https://biocontainers.pro/tools/telr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for telr", "latest": {"1.1--pyhdfd78af_0": "sha256:732edeb283c5bb2d76c03cae72fccb2bc6e1ce6becfc924d0865b04c72dde995"}, "tags": {"0.2--pyhdfd78af_1": "sha256:747495fb7770dff6d91720f5236ce20d1d88c9ec036728c30796b292d887a6e1", "0.2--pyhdfd78af_2": "sha256:1605145779cd5aa45f94a3d7abb229dcd640e1a27a4f4b9819f90a50b116d3db", "1.1--pyhdfd78af_0": "sha256:732edeb283c5bb2d76c03cae72fccb2bc6e1ce6becfc924d0865b04c72dde995"}, "docker": "quay.io/biocontainers/telr", "aliases": {"DateRepeats": "/usr/local/bin/DateRepeats", "DupMasker": "/usr/local/bin/DupMasker", "ProcessRepeats": "/usr/local/bin/ProcessRepeats", "RepeatMasker": "/usr/local/bin/RepeatMasker", "RepeatProteinMask": "/usr/local/bin/RepeatProteinMask", "calcDivergenceFromAlign.pl": "/usr/local/bin/calcDivergenceFromAlign.pl", "createRepeatLandscape.pl": "/usr/local/bin/createRepeatLandscape.pl", "dupliconToSVG.pl": "/usr/local/bin/dupliconToSVG.pl", "flye": "/usr/local/bin/flye", "flye-minimap2": "/usr/local/bin/flye-minimap2", "flye-modules": "/usr/local/bin/flye-modules", "flye-samtools": "/usr/local/bin/flye-samtools", "getRepeatMaskerBatch.pl": "/usr/local/bin/getRepeatMaskerBatch.pl", "ngmlr": "/usr/local/bin/ngmlr", "queryRepeatDatabase.pl": "/usr/local/bin/queryRepeatDatabase.pl", "queryTaxonomyDatabase.pl": "/usr/local/bin/queryTaxonomyDatabase.pl", "rmOut2Fasta.pl": "/usr/local/bin/rmOut2Fasta.pl", "rmOutToGFF3.pl": "/usr/local/bin/rmOutToGFF3.pl", "rmToUCSCTables.pl": "/usr/local/bin/rmToUCSCTables.pl", "sniffles": "/usr/local/bin/sniffles", "sniffles-debug": "/usr/local/bin/sniffles-debug", "telr": "/usr/local/bin/telr", "trfMask": "/usr/local/bin/trfMask", "wtdbg-cns": "/usr/local/bin/wtdbg-cns", "wtdbg2": "/usr/local/bin/wtdbg2", "wtpoa-cns": "/usr/local/bin/wtpoa-cns", "rmblastn": "/usr/local/bin/rmblastn", "trf4.10.0-rc.2.linux64.exe": "/usr/local/bin/trf4.10.0-rc.2.linux64.exe", "trf": "/usr/local/bin/trf", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug", "gnutls-serv": "/usr/local/bin/gnutls-serv", "nettle-hash": "/usr/local/bin/nettle-hash", "nettle-lfib-stream": "/usr/local/bin/nettle-lfib-stream", "nettle-pbkdf2": "/usr/local/bin/nettle-pbkdf2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/telr.
shpc-registry automated BioContainers addition for telr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/telr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/telr:1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/telr/1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/telr/1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### telr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### telr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### telr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### telr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### telr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### telr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DateRepeats

```bash
$ singularity exec <container> /usr/local/bin/DateRepeats
$ podman run --it --rm --entrypoint /usr/local/bin/DateRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DateRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DupMasker

```bash
$ singularity exec <container> /usr/local/bin/DupMasker
$ podman run --it --rm --entrypoint /usr/local/bin/DupMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DupMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ProcessRepeats

```bash
$ singularity exec <container> /usr/local/bin/ProcessRepeats
$ podman run --it --rm --entrypoint /usr/local/bin/ProcessRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ProcessRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepeatMasker

```bash
$ singularity exec <container> /usr/local/bin/RepeatMasker
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepeatProteinMask

```bash
$ singularity exec <container> /usr/local/bin/RepeatProteinMask
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatProteinMask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatProteinMask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calcDivergenceFromAlign.pl

```bash
$ singularity exec <container> /usr/local/bin/calcDivergenceFromAlign.pl
$ podman run --it --rm --entrypoint /usr/local/bin/calcDivergenceFromAlign.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calcDivergenceFromAlign.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createRepeatLandscape.pl

```bash
$ singularity exec <container> /usr/local/bin/createRepeatLandscape.pl
$ podman run --it --rm --entrypoint /usr/local/bin/createRepeatLandscape.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createRepeatLandscape.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dupliconToSVG.pl

```bash
$ singularity exec <container> /usr/local/bin/dupliconToSVG.pl
$ podman run --it --rm --entrypoint /usr/local/bin/dupliconToSVG.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dupliconToSVG.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye

```bash
$ singularity exec <container> /usr/local/bin/flye
$ podman run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-minimap2

```bash
$ singularity exec <container> /usr/local/bin/flye-minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-modules

```bash
$ singularity exec <container> /usr/local/bin/flye-modules
$ podman run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-samtools

```bash
$ singularity exec <container> /usr/local/bin/flye-samtools
$ podman run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getRepeatMaskerBatch.pl

```bash
$ singularity exec <container> /usr/local/bin/getRepeatMaskerBatch.pl
$ podman run --it --rm --entrypoint /usr/local/bin/getRepeatMaskerBatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getRepeatMaskerBatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngmlr

```bash
$ singularity exec <container> /usr/local/bin/ngmlr
$ podman run --it --rm --entrypoint /usr/local/bin/ngmlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngmlr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### queryRepeatDatabase.pl

```bash
$ singularity exec <container> /usr/local/bin/queryRepeatDatabase.pl
$ podman run --it --rm --entrypoint /usr/local/bin/queryRepeatDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/queryRepeatDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### queryTaxonomyDatabase.pl

```bash
$ singularity exec <container> /usr/local/bin/queryTaxonomyDatabase.pl
$ podman run --it --rm --entrypoint /usr/local/bin/queryTaxonomyDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/queryTaxonomyDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmOut2Fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/rmOut2Fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rmOut2Fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmOut2Fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmOutToGFF3.pl

```bash
$ singularity exec <container> /usr/local/bin/rmOutToGFF3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rmOutToGFF3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmOutToGFF3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmToUCSCTables.pl

```bash
$ singularity exec <container> /usr/local/bin/rmToUCSCTables.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rmToUCSCTables.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmToUCSCTables.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sniffles

```bash
$ singularity exec <container> /usr/local/bin/sniffles
$ podman run --it --rm --entrypoint /usr/local/bin/sniffles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sniffles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sniffles-debug

```bash
$ singularity exec <container> /usr/local/bin/sniffles-debug
$ podman run --it --rm --entrypoint /usr/local/bin/sniffles-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sniffles-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### telr

```bash
$ singularity exec <container> /usr/local/bin/telr
$ podman run --it --rm --entrypoint /usr/local/bin/telr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/telr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trfMask

```bash
$ singularity exec <container> /usr/local/bin/trfMask
$ podman run --it --rm --entrypoint /usr/local/bin/trfMask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trfMask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtdbg-cns

```bash
$ singularity exec <container> /usr/local/bin/wtdbg-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtdbg2

```bash
$ singularity exec <container> /usr/local/bin/wtdbg2
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtpoa-cns

```bash
$ singularity exec <container> /usr/local/bin/wtpoa-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmblastn

```bash
$ singularity exec <container> /usr/local/bin/rmblastn
$ podman run --it --rm --entrypoint /usr/local/bin/rmblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trf4.10.0-rc.2.linux64.exe

```bash
$ singularity exec <container> /usr/local/bin/trf4.10.0-rc.2.linux64.exe
$ podman run --it --rm --entrypoint /usr/local/bin/trf4.10.0-rc.2.linux64.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trf4.10.0-rc.2.linux64.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trf

```bash
$ singularity exec <container> /usr/local/bin/trf
$ podman run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certtool

```bash
$ singularity exec <container> /usr/local/bin/certtool
$ podman run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli-debug

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli-debug
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-serv

```bash
$ singularity exec <container> /usr/local/bin/gnutls-serv
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-hash

```bash
$ singularity exec <container> /usr/local/bin/nettle-hash
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-lfib-stream

```bash
$ singularity exec <container> /usr/local/bin/nettle-lfib-stream
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-lfib-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-lfib-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-pbkdf2

```bash
$ singularity exec <container> /usr/local/bin/nettle-pbkdf2
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-pbkdf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-pbkdf2   -v ${PWD} -w ${PWD} <container> -c " $@"
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