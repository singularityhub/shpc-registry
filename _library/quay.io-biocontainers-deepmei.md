---
layout: container
name:  "quay.io/biocontainers/deepmei"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepmei/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deepmei/container.yaml"
updated_at: "2025-12-09 03:46:21.016475"
latest: "1.6.24--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/deepmei"
aliases:
 - "bigRmskAlignBed.as"
 - "bigRmskBed.as"
 - "combineRMFiles.pl"
 - "deepmeiv1"
 - "makeclusterdb"
 - "maskFile.pl"
 - "renumberRMFiles.pl"
 - "rmToTrackHub.pl"
 - "RM2Bed.py"
 - "buildRMLibFromEMBL.pl"
 - "buildSummary.pl"
 - "wublastToCrossmatch.pl"
 - "DupMasker"
 - "ProcessRepeats"
 - "RepeatMasker"
 - "RepeatProteinMask"
 - "calcDivergenceFromAlign.pl"
 - "createRepeatLandscape.pl"
 - "dupliconToSVG.pl"
 - "getRepeatMaskerBatch.pl"
 - "rmOut2Fasta.pl"
 - "rmOutToGFF3.pl"
 - "rmToUCSCTables.pl"
 - "trfMask"
 - "rmblastn"
 - "trf4.10.0-rc.2.linux64.exe"
 - "blast_report"
 - "blastdb_convert"
 - "blastdb_path"
 - "trf"
 - "metadata_conda_debug.yaml"
 - "import_pb_to_tensorboard"
 - "estimator_ckpt_converter"
versions:
 - "1.0.0--hdfd78af_0"
 - "1.6.24--hdfd78af_0"
 - "1.6.24--hdfd78af_1"
description: "singularity registry hpc automated addition for deepmei"
config: {"url": "https://biocontainers.pro/tools/deepmei", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for deepmei", "latest": {"1.6.24--hdfd78af_1": "sha256:a24fefb9b24255d0cd26b3e7b2a8bc7c862f9ba95027483cac0ac82926053056"}, "tags": {"1.0.0--hdfd78af_0": "sha256:2cea61072003ce9db519391639e938db5674b3f4014a799293e5fd222e31a24a", "1.6.24--hdfd78af_0": "sha256:0b5634471eaeb0ab3e487647d95e2d8276bbca14aa3a0e4730a69c8867fc6c9a", "1.6.24--hdfd78af_1": "sha256:a24fefb9b24255d0cd26b3e7b2a8bc7c862f9ba95027483cac0ac82926053056"}, "docker": "quay.io/biocontainers/deepmei", "aliases": {"bigRmskAlignBed.as": "/usr/local/bin/bigRmskAlignBed.as", "bigRmskBed.as": "/usr/local/bin/bigRmskBed.as", "combineRMFiles.pl": "/usr/local/bin/combineRMFiles.pl", "deepmeiv1": "/usr/local/bin/deepmeiv1", "makeclusterdb": "/usr/local/bin/makeclusterdb", "maskFile.pl": "/usr/local/bin/maskFile.pl", "renumberRMFiles.pl": "/usr/local/bin/renumberRMFiles.pl", "rmToTrackHub.pl": "/usr/local/bin/rmToTrackHub.pl", "RM2Bed.py": "/usr/local/bin/RM2Bed.py", "buildRMLibFromEMBL.pl": "/usr/local/bin/buildRMLibFromEMBL.pl", "buildSummary.pl": "/usr/local/bin/buildSummary.pl", "wublastToCrossmatch.pl": "/usr/local/bin/wublastToCrossmatch.pl", "DupMasker": "/usr/local/bin/DupMasker", "ProcessRepeats": "/usr/local/bin/ProcessRepeats", "RepeatMasker": "/usr/local/bin/RepeatMasker", "RepeatProteinMask": "/usr/local/bin/RepeatProteinMask", "calcDivergenceFromAlign.pl": "/usr/local/bin/calcDivergenceFromAlign.pl", "createRepeatLandscape.pl": "/usr/local/bin/createRepeatLandscape.pl", "dupliconToSVG.pl": "/usr/local/bin/dupliconToSVG.pl", "getRepeatMaskerBatch.pl": "/usr/local/bin/getRepeatMaskerBatch.pl", "rmOut2Fasta.pl": "/usr/local/bin/rmOut2Fasta.pl", "rmOutToGFF3.pl": "/usr/local/bin/rmOutToGFF3.pl", "rmToUCSCTables.pl": "/usr/local/bin/rmToUCSCTables.pl", "trfMask": "/usr/local/bin/trfMask", "rmblastn": "/usr/local/bin/rmblastn", "trf4.10.0-rc.2.linux64.exe": "/usr/local/bin/trf4.10.0-rc.2.linux64.exe", "blast_report": "/usr/local/bin/blast_report", "blastdb_convert": "/usr/local/bin/blastdb_convert", "blastdb_path": "/usr/local/bin/blastdb_path", "trf": "/usr/local/bin/trf", "metadata_conda_debug.yaml": "/usr/local/bin/metadata_conda_debug.yaml", "import_pb_to_tensorboard": "/usr/local/bin/import_pb_to_tensorboard", "estimator_ckpt_converter": "/usr/local/bin/estimator_ckpt_converter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepmei.
singularity registry hpc automated addition for deepmei
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepmei
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepmei:1.6.24--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepmei/1.6.24--hdfd78af_1
$ module help quay.io/biocontainers/deepmei/1.6.24--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepmei-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepmei-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepmei-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepmei-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepmei-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepmei-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigRmskAlignBed.as

```bash
$ singularity exec <container> /usr/local/bin/bigRmskAlignBed.as
$ podman run --it --rm --entrypoint /usr/local/bin/bigRmskAlignBed.as   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigRmskAlignBed.as   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigRmskBed.as

```bash
$ singularity exec <container> /usr/local/bin/bigRmskBed.as
$ podman run --it --rm --entrypoint /usr/local/bin/bigRmskBed.as   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigRmskBed.as   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineRMFiles.pl

```bash
$ singularity exec <container> /usr/local/bin/combineRMFiles.pl
$ podman run --it --rm --entrypoint /usr/local/bin/combineRMFiles.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineRMFiles.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deepmeiv1

```bash
$ singularity exec <container> /usr/local/bin/deepmeiv1
$ podman run --it --rm --entrypoint /usr/local/bin/deepmeiv1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepmeiv1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeclusterdb

```bash
$ singularity exec <container> /usr/local/bin/makeclusterdb
$ podman run --it --rm --entrypoint /usr/local/bin/makeclusterdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeclusterdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maskFile.pl

```bash
$ singularity exec <container> /usr/local/bin/maskFile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/maskFile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maskFile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### renumberRMFiles.pl

```bash
$ singularity exec <container> /usr/local/bin/renumberRMFiles.pl
$ podman run --it --rm --entrypoint /usr/local/bin/renumberRMFiles.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renumberRMFiles.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmToTrackHub.pl

```bash
$ singularity exec <container> /usr/local/bin/rmToTrackHub.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rmToTrackHub.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmToTrackHub.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RM2Bed.py

```bash
$ singularity exec <container> /usr/local/bin/RM2Bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/RM2Bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RM2Bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### wublastToCrossmatch.pl

```bash
$ singularity exec <container> /usr/local/bin/wublastToCrossmatch.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wublastToCrossmatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wublastToCrossmatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### getRepeatMaskerBatch.pl

```bash
$ singularity exec <container> /usr/local/bin/getRepeatMaskerBatch.pl
$ podman run --it --rm --entrypoint /usr/local/bin/getRepeatMaskerBatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getRepeatMaskerBatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### trf

```bash
$ singularity exec <container> /usr/local/bin/trf
$ podman run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metadata_conda_debug.yaml

```bash
$ singularity exec <container> /usr/local/bin/metadata_conda_debug.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### import_pb_to_tensorboard

```bash
$ singularity exec <container> /usr/local/bin/import_pb_to_tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimator_ckpt_converter

```bash
$ singularity exec <container> /usr/local/bin/estimator_ckpt_converter
$ podman run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
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