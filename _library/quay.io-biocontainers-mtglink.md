---
layout: container
name:  "quay.io/biocontainers/mtglink"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mtglink/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mtglink/container.yaml"
updated_at: "2025-05-08 03:17:38.613533"
latest: "2.4.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/mtglink"
aliases:
 - "LRez"
 - "MindTheGap"
 - "ProgDynOptim.py"
 - "barcodesExtraction.py"
 - "bed2gfa.py"
 - "dbgh5"
 - "dbginfo"
 - "fasta2bed.py"
 - "gapFilling.py"
 - "gfa1tofasta.py"
 - "gfa2tofasta.py"
 - "gfapy-convert"
 - "gfapy-mergelinear"
 - "gfapy-renumber"
 - "gfapy-validate"
 - "helpers.py"
 - "localAssemblyDBG.py"
 - "localAssemblyIRO.py"
 - "main.py"
 - "matrix2gfa.py"
 - "mergegfa.py"
 - "mtglink.py"
 - "pathos_connect"
 - "paths2gfa.py"
 - "portpicker"
 - "pox"
 - "ppserver"
 - "qualitativeEvaluation.py"
 - "readsRetrieval.py"
 - "stats_alignment.py"
 - "test.py"
 - "vcf2gfa.py"
 - "get_objgraph"
 - "undill"
 - "mapview"
 - "mgaps"
 - "run-mummer1"
 - "run-mummer3"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
versions:
 - "2.4.0--hdfd78af_0"
 - "2.4.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for mtglink"
config: {"url": "https://biocontainers.pro/tools/mtglink", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mtglink", "latest": {"2.4.1--hdfd78af_0": "sha256:bf26656ece9ef96a36f621c7fa17a25afa347d672030287ebe6811b6e5f7c933"}, "tags": {"2.4.0--hdfd78af_0": "sha256:d7a0abed2bf58e7fe86ff4cd49fab3a9218dbef663f4845aa92e97338e1702e2", "2.4.1--hdfd78af_0": "sha256:bf26656ece9ef96a36f621c7fa17a25afa347d672030287ebe6811b6e5f7c933"}, "docker": "quay.io/biocontainers/mtglink", "aliases": {"LRez": "/usr/local/bin/LRez", "MindTheGap": "/usr/local/bin/MindTheGap", "ProgDynOptim.py": "/usr/local/bin/ProgDynOptim.py", "barcodesExtraction.py": "/usr/local/bin/barcodesExtraction.py", "bed2gfa.py": "/usr/local/bin/bed2gfa.py", "dbgh5": "/usr/local/bin/dbgh5", "dbginfo": "/usr/local/bin/dbginfo", "fasta2bed.py": "/usr/local/bin/fasta2bed.py", "gapFilling.py": "/usr/local/bin/gapFilling.py", "gfa1tofasta.py": "/usr/local/bin/gfa1tofasta.py", "gfa2tofasta.py": "/usr/local/bin/gfa2tofasta.py", "gfapy-convert": "/usr/local/bin/gfapy-convert", "gfapy-mergelinear": "/usr/local/bin/gfapy-mergelinear", "gfapy-renumber": "/usr/local/bin/gfapy-renumber", "gfapy-validate": "/usr/local/bin/gfapy-validate", "helpers.py": "/usr/local/bin/helpers.py", "localAssemblyDBG.py": "/usr/local/bin/localAssemblyDBG.py", "localAssemblyIRO.py": "/usr/local/bin/localAssemblyIRO.py", "main.py": "/usr/local/bin/main.py", "matrix2gfa.py": "/usr/local/bin/matrix2gfa.py", "mergegfa.py": "/usr/local/bin/mergegfa.py", "mtglink.py": "/usr/local/bin/mtglink.py", "pathos_connect": "/usr/local/bin/pathos_connect", "paths2gfa.py": "/usr/local/bin/paths2gfa.py", "portpicker": "/usr/local/bin/portpicker", "pox": "/usr/local/bin/pox", "ppserver": "/usr/local/bin/ppserver", "qualitativeEvaluation.py": "/usr/local/bin/qualitativeEvaluation.py", "readsRetrieval.py": "/usr/local/bin/readsRetrieval.py", "stats_alignment.py": "/usr/local/bin/stats_alignment.py", "test.py": "/usr/local/bin/test.py", "vcf2gfa.py": "/usr/local/bin/vcf2gfa.py", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "mapview": "/usr/local/bin/mapview", "mgaps": "/usr/local/bin/mgaps", "run-mummer1": "/usr/local/bin/run-mummer1", "run-mummer3": "/usr/local/bin/run-mummer3", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mtglink.
shpc-registry automated BioContainers addition for mtglink
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mtglink
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mtglink:2.4.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mtglink/2.4.1--hdfd78af_0
$ module help quay.io/biocontainers/mtglink/2.4.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mtglink-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mtglink-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mtglink-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mtglink-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mtglink-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mtglink-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LRez

```bash
$ singularity exec <container> /usr/local/bin/LRez
$ podman run --it --rm --entrypoint /usr/local/bin/LRez   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LRez   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MindTheGap

```bash
$ singularity exec <container> /usr/local/bin/MindTheGap
$ podman run --it --rm --entrypoint /usr/local/bin/MindTheGap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MindTheGap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ProgDynOptim.py

```bash
$ singularity exec <container> /usr/local/bin/ProgDynOptim.py
$ podman run --it --rm --entrypoint /usr/local/bin/ProgDynOptim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ProgDynOptim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barcodesExtraction.py

```bash
$ singularity exec <container> /usr/local/bin/barcodesExtraction.py
$ podman run --it --rm --entrypoint /usr/local/bin/barcodesExtraction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barcodesExtraction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed2gfa.py

```bash
$ singularity exec <container> /usr/local/bin/bed2gfa.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed2gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbgh5

```bash
$ singularity exec <container> /usr/local/bin/dbgh5
$ podman run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbginfo

```bash
$ singularity exec <container> /usr/local/bin/dbginfo
$ podman run --it --rm --entrypoint /usr/local/bin/dbginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2bed.py

```bash
$ singularity exec <container> /usr/local/bin/fasta2bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gapFilling.py

```bash
$ singularity exec <container> /usr/local/bin/gapFilling.py
$ podman run --it --rm --entrypoint /usr/local/bin/gapFilling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gapFilling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfa1tofasta.py

```bash
$ singularity exec <container> /usr/local/bin/gfa1tofasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/gfa1tofasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfa1tofasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfa2tofasta.py

```bash
$ singularity exec <container> /usr/local/bin/gfa2tofasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/gfa2tofasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfa2tofasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-convert

```bash
$ singularity exec <container> /usr/local/bin/gfapy-convert
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-mergelinear

```bash
$ singularity exec <container> /usr/local/bin/gfapy-mergelinear
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-mergelinear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-mergelinear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-renumber

```bash
$ singularity exec <container> /usr/local/bin/gfapy-renumber
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-renumber   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-renumber   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-validate

```bash
$ singularity exec <container> /usr/local/bin/gfapy-validate
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### helpers.py

```bash
$ singularity exec <container> /usr/local/bin/helpers.py
$ podman run --it --rm --entrypoint /usr/local/bin/helpers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/helpers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### localAssemblyDBG.py

```bash
$ singularity exec <container> /usr/local/bin/localAssemblyDBG.py
$ podman run --it --rm --entrypoint /usr/local/bin/localAssemblyDBG.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/localAssemblyDBG.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### localAssemblyIRO.py

```bash
$ singularity exec <container> /usr/local/bin/localAssemblyIRO.py
$ podman run --it --rm --entrypoint /usr/local/bin/localAssemblyIRO.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/localAssemblyIRO.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### main.py

```bash
$ singularity exec <container> /usr/local/bin/main.py
$ podman run --it --rm --entrypoint /usr/local/bin/main.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/main.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matrix2gfa.py

```bash
$ singularity exec <container> /usr/local/bin/matrix2gfa.py
$ podman run --it --rm --entrypoint /usr/local/bin/matrix2gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matrix2gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergegfa.py

```bash
$ singularity exec <container> /usr/local/bin/mergegfa.py
$ podman run --it --rm --entrypoint /usr/local/bin/mergegfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergegfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mtglink.py

```bash
$ singularity exec <container> /usr/local/bin/mtglink.py
$ podman run --it --rm --entrypoint /usr/local/bin/mtglink.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mtglink.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathos_connect

```bash
$ singularity exec <container> /usr/local/bin/pathos_connect
$ podman run --it --rm --entrypoint /usr/local/bin/pathos_connect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathos_connect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paths2gfa.py

```bash
$ singularity exec <container> /usr/local/bin/paths2gfa.py
$ podman run --it --rm --entrypoint /usr/local/bin/paths2gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paths2gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### portpicker

```bash
$ singularity exec <container> /usr/local/bin/portpicker
$ podman run --it --rm --entrypoint /usr/local/bin/portpicker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/portpicker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pox

```bash
$ singularity exec <container> /usr/local/bin/pox
$ podman run --it --rm --entrypoint /usr/local/bin/pox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppserver

```bash
$ singularity exec <container> /usr/local/bin/ppserver
$ podman run --it --rm --entrypoint /usr/local/bin/ppserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualitativeEvaluation.py

```bash
$ singularity exec <container> /usr/local/bin/qualitativeEvaluation.py
$ podman run --it --rm --entrypoint /usr/local/bin/qualitativeEvaluation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualitativeEvaluation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readsRetrieval.py

```bash
$ singularity exec <container> /usr/local/bin/readsRetrieval.py
$ podman run --it --rm --entrypoint /usr/local/bin/readsRetrieval.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readsRetrieval.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stats_alignment.py

```bash
$ singularity exec <container> /usr/local/bin/stats_alignment.py
$ podman run --it --rm --entrypoint /usr/local/bin/stats_alignment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stats_alignment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.py

```bash
$ singularity exec <container> /usr/local/bin/test.py
$ podman run --it --rm --entrypoint /usr/local/bin/test.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2gfa.py

```bash
$ singularity exec <container> /usr/local/bin/vcf2gfa.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapview

```bash
$ singularity exec <container> /usr/local/bin/mapview
$ podman run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgaps

```bash
$ singularity exec <container> /usr/local/bin/mgaps
$ podman run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer1

```bash
$ singularity exec <container> /usr/local/bin/run-mummer1
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer3

```bash
$ singularity exec <container> /usr/local/bin/run-mummer3
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
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