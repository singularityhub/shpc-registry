---
layout: container
name:  "quay.io/biocontainers/annosine2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/annosine2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/annosine2/container.yaml"
updated_at: "2024-12-06 03:33:44.798698"
latest: "2.0.7--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/annosine2"
aliases:
 - "RM2Bed.py"
 - "annosine2"
 - "buildRMLibFromEMBL.pl"
 - "buildSummary.pl"
 - "corepack"
 - "h5tools_test_utils"
 - "irf"
 - "makeclusterdb"
 - "maskFile.pl"
 - "wublastToCrossmatch.pl"
 - "DateRepeats"
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
 - "npx"
 - "rmblastn"
 - "node"
 - "npm"
 - "blast_report"
 - "blastdb_convert"
 - "blastdb_path"
 - "trf"
 - "h5fuse.sh"
 - "FET.pl"
 - "cd-hit-clstr_2_blm8.pl"
 - "clstr_list.pl"
versions:
 - "1.0.4--pyh7cba7a3_0"
 - "2.0.7--pyh7cba7a3_0"
 - "1.0.5--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for annosine2"
config: {"url": "https://biocontainers.pro/tools/annosine2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for annosine2", "latest": {"2.0.7--pyh7cba7a3_0": "sha256:cb0162509ec72b4a746be6641f614681226cf21b0687d601d2532bec353f16f7"}, "tags": {"1.0.4--pyh7cba7a3_0": "sha256:d042ece3e1fc28b04a6ec70ef8ff3fdd1b625f41143a53c498a1d0ddfa4294ca", "2.0.7--pyh7cba7a3_0": "sha256:cb0162509ec72b4a746be6641f614681226cf21b0687d601d2532bec353f16f7", "1.0.5--pyh7cba7a3_0": "sha256:99a2c20d23999476c670d33a3566ff5a63fff17a37646dba45d53e0580eb7650"}, "docker": "quay.io/biocontainers/annosine2", "aliases": {"RM2Bed.py": "/usr/local/bin/RM2Bed.py", "annosine2": "/usr/local/bin/annosine2", "buildRMLibFromEMBL.pl": "/usr/local/bin/buildRMLibFromEMBL.pl", "buildSummary.pl": "/usr/local/bin/buildSummary.pl", "corepack": "/usr/local/bin/corepack", "h5tools_test_utils": "/usr/local/bin/h5tools_test_utils", "irf": "/usr/local/bin/irf", "makeclusterdb": "/usr/local/bin/makeclusterdb", "maskFile.pl": "/usr/local/bin/maskFile.pl", "wublastToCrossmatch.pl": "/usr/local/bin/wublastToCrossmatch.pl", "DateRepeats": "/usr/local/bin/DateRepeats", "DupMasker": "/usr/local/bin/DupMasker", "ProcessRepeats": "/usr/local/bin/ProcessRepeats", "RepeatMasker": "/usr/local/bin/RepeatMasker", "RepeatProteinMask": "/usr/local/bin/RepeatProteinMask", "calcDivergenceFromAlign.pl": "/usr/local/bin/calcDivergenceFromAlign.pl", "createRepeatLandscape.pl": "/usr/local/bin/createRepeatLandscape.pl", "dupliconToSVG.pl": "/usr/local/bin/dupliconToSVG.pl", "getRepeatMaskerBatch.pl": "/usr/local/bin/getRepeatMaskerBatch.pl", "rmOut2Fasta.pl": "/usr/local/bin/rmOut2Fasta.pl", "rmOutToGFF3.pl": "/usr/local/bin/rmOutToGFF3.pl", "rmToUCSCTables.pl": "/usr/local/bin/rmToUCSCTables.pl", "trfMask": "/usr/local/bin/trfMask", "npx": "/usr/local/bin/npx", "rmblastn": "/usr/local/bin/rmblastn", "node": "/usr/local/bin/node", "npm": "/usr/local/bin/npm", "blast_report": "/usr/local/bin/blast_report", "blastdb_convert": "/usr/local/bin/blastdb_convert", "blastdb_path": "/usr/local/bin/blastdb_path", "trf": "/usr/local/bin/trf", "h5fuse.sh": "/usr/local/bin/h5fuse.sh", "FET.pl": "/usr/local/bin/FET.pl", "cd-hit-clstr_2_blm8.pl": "/usr/local/bin/cd-hit-clstr_2_blm8.pl", "clstr_list.pl": "/usr/local/bin/clstr_list.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/annosine2.
singularity registry hpc automated addition for annosine2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/annosine2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/annosine2:2.0.7--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/annosine2/2.0.7--pyh7cba7a3_0
$ module help quay.io/biocontainers/annosine2/2.0.7--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### annosine2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### annosine2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### annosine2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### annosine2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### annosine2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### annosine2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RM2Bed.py

```bash
$ singularity exec <container> /usr/local/bin/RM2Bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/RM2Bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RM2Bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annosine2

```bash
$ singularity exec <container> /usr/local/bin/annosine2
$ podman run --it --rm --entrypoint /usr/local/bin/annosine2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annosine2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### corepack

```bash
$ singularity exec <container> /usr/local/bin/corepack
$ podman run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5tools_test_utils

```bash
$ singularity exec <container> /usr/local/bin/h5tools_test_utils
$ podman run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irf

```bash
$ singularity exec <container> /usr/local/bin/irf
$ podman run --it --rm --entrypoint /usr/local/bin/irf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irf   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### wublastToCrossmatch.pl

```bash
$ singularity exec <container> /usr/local/bin/wublastToCrossmatch.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wublastToCrossmatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wublastToCrossmatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### npx

```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmblastn

```bash
$ singularity exec <container> /usr/local/bin/rmblastn
$ podman run --it --rm --entrypoint /usr/local/bin/rmblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### node

```bash
$ singularity exec <container> /usr/local/bin/node
$ podman run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npm

```bash
$ singularity exec <container> /usr/local/bin/npm
$ podman run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h5fuse.sh

```bash
$ singularity exec <container> /usr/local/bin/h5fuse.sh
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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