---
layout: container
name:  "quay.io/biocontainers/nanomonsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanomonsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanomonsv/container.yaml"
updated_at: "2023-10-18 03:04:00.453197"
latest: "0.7.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/nanomonsv"
aliases:
 - "DateRepeats"
 - "DupMasker"
 - "ProcessRepeats"
 - "RM2Bed.py"
 - "RepeatMasker"
 - "RepeatProteinMask"
 - "buildRMLibFromEMBL.pl"
 - "buildSummary.pl"
 - "calcDivergenceFromAlign.pl"
 - "createRepeatLandscape.pl"
 - "dupliconToSVG.pl"
 - "getRepeatMaskerBatch.pl"
 - "maskFile.pl"
 - "nanomonsv"
 - "rmOut2Fasta.pl"
 - "rmOutToGFF3.pl"
 - "rmToUCSCTables.pl"
 - "trfMask"
 - "wublastToCrossmatch.pl"
 - "rmblastn"
 - "trf4.10.0-rc.2.linux64.exe"
 - "trf"
 - "blast_report"
 - "blastdb_convert"
 - "blastdb_path"
 - "racon"
 - "rampler"
 - "racon_wrapper"
 - "certtool"
versions:
 - "0.5.0--pyhdfd78af_0"
 - "0.5.1--pyhdfd78af_0"
 - "0.7.0--pyhdfd78af_0"
 - "0.6.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for nanomonsv"
config: {"url": "https://biocontainers.pro/tools/nanomonsv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanomonsv", "latest": {"0.7.0--pyhdfd78af_0": "sha256:5dd81ccbdcee7f6346fc569bba75e37043248138c132cadd4d5abd1659ffba60"}, "tags": {"0.5.0--pyhdfd78af_0": "sha256:b6a2fee29c637f006eecf7a10f9a9f4190467441ed02a04bfe6d297636f6f793", "0.5.1--pyhdfd78af_0": "sha256:f236f81fa9690c90a829ed62f736e5353ed0be0518b2bdb45fcf849d30a0f4c6", "0.7.0--pyhdfd78af_0": "sha256:5dd81ccbdcee7f6346fc569bba75e37043248138c132cadd4d5abd1659ffba60", "0.6.0--pyhdfd78af_0": "sha256:aca64678939130537d6d36aa6adbd03684c31d31828e349a73ea161be05edd9a"}, "docker": "quay.io/biocontainers/nanomonsv", "aliases": {"DateRepeats": "/usr/local/bin/DateRepeats", "DupMasker": "/usr/local/bin/DupMasker", "ProcessRepeats": "/usr/local/bin/ProcessRepeats", "RM2Bed.py": "/usr/local/bin/RM2Bed.py", "RepeatMasker": "/usr/local/bin/RepeatMasker", "RepeatProteinMask": "/usr/local/bin/RepeatProteinMask", "buildRMLibFromEMBL.pl": "/usr/local/bin/buildRMLibFromEMBL.pl", "buildSummary.pl": "/usr/local/bin/buildSummary.pl", "calcDivergenceFromAlign.pl": "/usr/local/bin/calcDivergenceFromAlign.pl", "createRepeatLandscape.pl": "/usr/local/bin/createRepeatLandscape.pl", "dupliconToSVG.pl": "/usr/local/bin/dupliconToSVG.pl", "getRepeatMaskerBatch.pl": "/usr/local/bin/getRepeatMaskerBatch.pl", "maskFile.pl": "/usr/local/bin/maskFile.pl", "nanomonsv": "/usr/local/bin/nanomonsv", "rmOut2Fasta.pl": "/usr/local/bin/rmOut2Fasta.pl", "rmOutToGFF3.pl": "/usr/local/bin/rmOutToGFF3.pl", "rmToUCSCTables.pl": "/usr/local/bin/rmToUCSCTables.pl", "trfMask": "/usr/local/bin/trfMask", "wublastToCrossmatch.pl": "/usr/local/bin/wublastToCrossmatch.pl", "rmblastn": "/usr/local/bin/rmblastn", "trf4.10.0-rc.2.linux64.exe": "/usr/local/bin/trf4.10.0-rc.2.linux64.exe", "trf": "/usr/local/bin/trf", "blast_report": "/usr/local/bin/blast_report", "blastdb_convert": "/usr/local/bin/blastdb_convert", "blastdb_path": "/usr/local/bin/blastdb_path", "racon": "/usr/local/bin/racon", "rampler": "/usr/local/bin/rampler", "racon_wrapper": "/usr/local/bin/racon_wrapper", "certtool": "/usr/local/bin/certtool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanomonsv.
shpc-registry automated BioContainers addition for nanomonsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanomonsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanomonsv:0.7.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanomonsv/0.7.0--pyhdfd78af_0
$ module help quay.io/biocontainers/nanomonsv/0.7.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanomonsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanomonsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanomonsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanomonsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanomonsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanomonsv-inspect-deffile:

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


#### RM2Bed.py

```bash
$ singularity exec <container> /usr/local/bin/RM2Bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/RM2Bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RM2Bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### buildRMLibFromEMBL.pl

```bash
$ singularity exec <container> /usr/local/bin/buildRMLibFromEMBL.pl
$ podman run --it --rm --entrypoint /usr/local/bin/buildRMLibFromEMBL.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildRMLibFromEMBL.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSummary.pl

```bash
$ singularity exec <container> /usr/local/bin/buildSummary.pl
$ podman run --it --rm --entrypoint /usr/local/bin/buildSummary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSummary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### getRepeatMaskerBatch.pl

```bash
$ singularity exec <container> /usr/local/bin/getRepeatMaskerBatch.pl
$ podman run --it --rm --entrypoint /usr/local/bin/getRepeatMaskerBatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getRepeatMaskerBatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maskFile.pl

```bash
$ singularity exec <container> /usr/local/bin/maskFile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/maskFile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maskFile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanomonsv

```bash
$ singularity exec <container> /usr/local/bin/nanomonsv
$ podman run --it --rm --entrypoint /usr/local/bin/nanomonsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanomonsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### trfMask

```bash
$ singularity exec <container> /usr/local/bin/trfMask
$ podman run --it --rm --entrypoint /usr/local/bin/trfMask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trfMask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wublastToCrossmatch.pl

```bash
$ singularity exec <container> /usr/local/bin/wublastToCrossmatch.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wublastToCrossmatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wublastToCrossmatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### blast_report

```bash
$ singularity exec <container> /usr/local/bin/blast_report
$ podman run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_convert

```bash
$ singularity exec <container> /usr/local/bin/blastdb_convert
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_path

```bash
$ singularity exec <container> /usr/local/bin/blastdb_path
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon

```bash
$ singularity exec <container> /usr/local/bin/racon
$ podman run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rampler

```bash
$ singularity exec <container> /usr/local/bin/rampler
$ podman run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon_wrapper

```bash
$ singularity exec <container> /usr/local/bin/racon_wrapper
$ podman run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certtool

```bash
$ singularity exec <container> /usr/local/bin/certtool
$ podman run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
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