---
layout: container
name:  "quay.io/biocontainers/ltr_retriever"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ltr_retriever/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ltr_retriever/container.yaml"
updated_at: "2024-05-05 03:07:03.105800"
latest: "2.9.9--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/ltr_retriever"
aliases:
 - "DateRepeats"
 - "DupMasker"
 - "LAI"
 - "LTR_retriever"
 - "ProcessRepeats"
 - "RM2Bed.py"
 - "RepeatMasker"
 - "RepeatProteinMask"
 - "buildRMLibFromEMBL.pl"
 - "buildSummary.pl"
 - "calcDivergenceFromAlign.pl"
 - "convert_MGEScan3.0.pl"
 - "convert_ltr_struc.pl"
 - "convert_ltrdetector.pl"
 - "createRepeatLandscape.pl"
 - "dupliconToSVG.pl"
 - "getRepeatMaskerBatch.pl"
 - "queryRepeatDatabase.pl"
 - "queryTaxonomyDatabase.pl"
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
 - "FET.pl"
 - "cd-hit-clstr_2_blm8.pl"
 - "certtool"
 - "clstr_list.pl"
versions:
 - "2.9.0--hdfd78af_1"
 - "2.9.4--hdfd78af_0"
 - "2.9.5--hdfd78af_0"
 - "2.9.9--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for ltr_retriever"
config: {"url": "https://biocontainers.pro/tools/ltr_retriever", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ltr_retriever", "latest": {"2.9.9--hdfd78af_0": "sha256:934751219619c0c32b8be554c73f877090c5404037714a40674d6b10d5dc573c"}, "tags": {"2.9.0--hdfd78af_1": "sha256:881fbf91a576048b71c7f9328609e4a9554bbe283400af3931a25250206c2b58", "2.9.4--hdfd78af_0": "sha256:cffaf84a6f668d21f8c7b2e21befc6b1b7eb2c151a5706a662209248319d6918", "2.9.5--hdfd78af_0": "sha256:00026a3c90d23a584e2b31577e6c5781095a0788ed44d91555b22b365ca698e6", "2.9.9--hdfd78af_0": "sha256:934751219619c0c32b8be554c73f877090c5404037714a40674d6b10d5dc573c"}, "docker": "quay.io/biocontainers/ltr_retriever", "aliases": {"DateRepeats": "/usr/local/bin/DateRepeats", "DupMasker": "/usr/local/bin/DupMasker", "LAI": "/usr/local/bin/LAI", "LTR_retriever": "/usr/local/bin/LTR_retriever", "ProcessRepeats": "/usr/local/bin/ProcessRepeats", "RM2Bed.py": "/usr/local/bin/RM2Bed.py", "RepeatMasker": "/usr/local/bin/RepeatMasker", "RepeatProteinMask": "/usr/local/bin/RepeatProteinMask", "buildRMLibFromEMBL.pl": "/usr/local/bin/buildRMLibFromEMBL.pl", "buildSummary.pl": "/usr/local/bin/buildSummary.pl", "calcDivergenceFromAlign.pl": "/usr/local/bin/calcDivergenceFromAlign.pl", "convert_MGEScan3.0.pl": "/usr/local/bin/convert_MGEScan3.0.pl", "convert_ltr_struc.pl": "/usr/local/bin/convert_ltr_struc.pl", "convert_ltrdetector.pl": "/usr/local/bin/convert_ltrdetector.pl", "createRepeatLandscape.pl": "/usr/local/bin/createRepeatLandscape.pl", "dupliconToSVG.pl": "/usr/local/bin/dupliconToSVG.pl", "getRepeatMaskerBatch.pl": "/usr/local/bin/getRepeatMaskerBatch.pl", "queryRepeatDatabase.pl": "/usr/local/bin/queryRepeatDatabase.pl", "queryTaxonomyDatabase.pl": "/usr/local/bin/queryTaxonomyDatabase.pl", "rmOut2Fasta.pl": "/usr/local/bin/rmOut2Fasta.pl", "rmOutToGFF3.pl": "/usr/local/bin/rmOutToGFF3.pl", "rmToUCSCTables.pl": "/usr/local/bin/rmToUCSCTables.pl", "trfMask": "/usr/local/bin/trfMask", "wublastToCrossmatch.pl": "/usr/local/bin/wublastToCrossmatch.pl", "rmblastn": "/usr/local/bin/rmblastn", "trf4.10.0-rc.2.linux64.exe": "/usr/local/bin/trf4.10.0-rc.2.linux64.exe", "trf": "/usr/local/bin/trf", "blast_report": "/usr/local/bin/blast_report", "blastdb_convert": "/usr/local/bin/blastdb_convert", "blastdb_path": "/usr/local/bin/blastdb_path", "FET.pl": "/usr/local/bin/FET.pl", "cd-hit-clstr_2_blm8.pl": "/usr/local/bin/cd-hit-clstr_2_blm8.pl", "certtool": "/usr/local/bin/certtool", "clstr_list.pl": "/usr/local/bin/clstr_list.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ltr_retriever.
shpc-registry automated BioContainers addition for ltr_retriever
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ltr_retriever
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ltr_retriever:2.9.9--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ltr_retriever/2.9.9--hdfd78af_0
$ module help quay.io/biocontainers/ltr_retriever/2.9.9--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ltr_retriever-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ltr_retriever-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ltr_retriever-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ltr_retriever-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ltr_retriever-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ltr_retriever-inspect-deffile:

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


#### LAI

```bash
$ singularity exec <container> /usr/local/bin/LAI
$ podman run --it --rm --entrypoint /usr/local/bin/LAI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LTR_retriever

```bash
$ singularity exec <container> /usr/local/bin/LTR_retriever
$ podman run --it --rm --entrypoint /usr/local/bin/LTR_retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LTR_retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### convert_MGEScan3.0.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_MGEScan3.0.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_MGEScan3.0.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_MGEScan3.0.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_ltr_struc.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_ltr_struc.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_ltr_struc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_ltr_struc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_ltrdetector.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_ltrdetector.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_ltrdetector.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_ltrdetector.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### FET.pl

```bash
$ singularity exec <container> /usr/local/bin/FET.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-clstr_2_blm8.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-clstr_2_blm8.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certtool

```bash
$ singularity exec <container> /usr/local/bin/certtool
$ podman run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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