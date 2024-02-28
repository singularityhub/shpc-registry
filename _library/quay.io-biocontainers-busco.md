---
layout: container
name:  "quay.io/biocontainers/busco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/busco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/busco/container.yaml"
updated_at: "2024-02-28 02:27:10.847654"
latest: "4.1.2--py37r40_0"
container_url: "https://biocontainers.pro/tools/busco"
aliases:
 - "busco"
 - "busco_configurator.py"
 - "find"
 - "generate_plot.py"
 - "hmmc2"
 - "hmmerfm-exactmatch"
 - "locate"
 - "run-sepp.sh"
 - "run_abundance.py"
 - "run_sepp.py"
 - "run_tipp.py"
 - "run_tipp_tool.py"
 - "run_upp.py"
 - "seppJsonMerger.jar"
 - "split_sequences.py"
 - "updatedb"
 - "xargs"
 - "augustus"
 - "bam2hints"
 - "etraining"
 - "fastBlockSearch"
 - "filterBam"
 - "homGeneMapping"
 - "joingenes"
 - "prepareAlign"
 - "guppy"
 - "pplacer"
versions:
 - "4.1.2--py37r40_0"
description: "shpc-registry automated BioContainers addition for busco"
config: {"url": "https://biocontainers.pro/tools/busco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for busco", "latest": {"4.1.2--py37r40_0": "sha256:2a1a14f4584c43dd172b1b3501b533ebb7e21b039c69c9ee02b8425abf462ea1"}, "tags": {"4.1.2--py37r40_0": "sha256:2a1a14f4584c43dd172b1b3501b533ebb7e21b039c69c9ee02b8425abf462ea1"}, "docker": "quay.io/biocontainers/busco", "aliases": {"busco": "/usr/local/bin/busco", "busco_configurator.py": "/usr/local/bin/busco_configurator.py", "find": "/usr/local/bin/find", "generate_plot.py": "/usr/local/bin/generate_plot.py", "hmmc2": "/usr/local/bin/hmmc2", "hmmerfm-exactmatch": "/usr/local/bin/hmmerfm-exactmatch", "locate": "/usr/local/bin/locate", "run-sepp.sh": "/usr/local/bin/run-sepp.sh", "run_abundance.py": "/usr/local/bin/run_abundance.py", "run_sepp.py": "/usr/local/bin/run_sepp.py", "run_tipp.py": "/usr/local/bin/run_tipp.py", "run_tipp_tool.py": "/usr/local/bin/run_tipp_tool.py", "run_upp.py": "/usr/local/bin/run_upp.py", "seppJsonMerger.jar": "/usr/local/bin/seppJsonMerger.jar", "split_sequences.py": "/usr/local/bin/split_sequences.py", "updatedb": "/usr/local/bin/updatedb", "xargs": "/usr/local/bin/xargs", "augustus": "/usr/local/bin/augustus", "bam2hints": "/usr/local/bin/bam2hints", "etraining": "/usr/local/bin/etraining", "fastBlockSearch": "/usr/local/bin/fastBlockSearch", "filterBam": "/usr/local/bin/filterBam", "homGeneMapping": "/usr/local/bin/homGeneMapping", "joingenes": "/usr/local/bin/joingenes", "prepareAlign": "/usr/local/bin/prepareAlign", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/busco.
shpc-registry automated BioContainers addition for busco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/busco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/busco:4.1.2--py37r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/busco/4.1.2--py37r40_0
$ module help quay.io/biocontainers/busco/4.1.2--py37r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### busco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### busco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### busco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### busco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### busco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### busco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### busco

```bash
$ singularity exec <container> /usr/local/bin/busco
$ podman run --it --rm --entrypoint /usr/local/bin/busco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/busco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### busco_configurator.py

```bash
$ singularity exec <container> /usr/local/bin/busco_configurator.py
$ podman run --it --rm --entrypoint /usr/local/bin/busco_configurator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/busco_configurator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find

```bash
$ singularity exec <container> /usr/local/bin/find
$ podman run --it --rm --entrypoint /usr/local/bin/find   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_plot.py

```bash
$ singularity exec <container> /usr/local/bin/generate_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmc2

```bash
$ singularity exec <container> /usr/local/bin/hmmc2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerfm-exactmatch

```bash
$ singularity exec <container> /usr/local/bin/hmmerfm-exactmatch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locate

```bash
$ singularity exec <container> /usr/local/bin/locate
$ podman run --it --rm --entrypoint /usr/local/bin/locate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-sepp.sh

```bash
$ singularity exec <container> /usr/local/bin/run-sepp.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run-sepp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-sepp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_abundance.py

```bash
$ singularity exec <container> /usr/local/bin/run_abundance.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_sepp.py

```bash
$ singularity exec <container> /usr/local/bin/run_sepp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_sepp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_sepp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_tipp.py

```bash
$ singularity exec <container> /usr/local/bin/run_tipp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_tipp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_tipp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_tipp_tool.py

```bash
$ singularity exec <container> /usr/local/bin/run_tipp_tool.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_tipp_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_tipp_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_upp.py

```bash
$ singularity exec <container> /usr/local/bin/run_upp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_upp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_upp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seppJsonMerger.jar

```bash
$ singularity exec <container> /usr/local/bin/seppJsonMerger.jar
$ podman run --it --rm --entrypoint /usr/local/bin/seppJsonMerger.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seppJsonMerger.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_sequences.py

```bash
$ singularity exec <container> /usr/local/bin/split_sequences.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### updatedb

```bash
$ singularity exec <container> /usr/local/bin/updatedb
$ podman run --it --rm --entrypoint /usr/local/bin/updatedb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/updatedb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xargs

```bash
$ singularity exec <container> /usr/local/bin/xargs
$ podman run --it --rm --entrypoint /usr/local/bin/xargs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xargs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### augustus

```bash
$ singularity exec <container> /usr/local/bin/augustus
$ podman run --it --rm --entrypoint /usr/local/bin/augustus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/augustus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2hints

```bash
$ singularity exec <container> /usr/local/bin/bam2hints
$ podman run --it --rm --entrypoint /usr/local/bin/bam2hints   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2hints   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### etraining

```bash
$ singularity exec <container> /usr/local/bin/etraining
$ podman run --it --rm --entrypoint /usr/local/bin/etraining   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/etraining   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastBlockSearch

```bash
$ singularity exec <container> /usr/local/bin/fastBlockSearch
$ podman run --it --rm --entrypoint /usr/local/bin/fastBlockSearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastBlockSearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterBam

```bash
$ singularity exec <container> /usr/local/bin/filterBam
$ podman run --it --rm --entrypoint /usr/local/bin/filterBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### homGeneMapping

```bash
$ singularity exec <container> /usr/local/bin/homGeneMapping
$ podman run --it --rm --entrypoint /usr/local/bin/homGeneMapping   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/homGeneMapping   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### joingenes

```bash
$ singularity exec <container> /usr/local/bin/joingenes
$ podman run --it --rm --entrypoint /usr/local/bin/joingenes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/joingenes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepareAlign

```bash
$ singularity exec <container> /usr/local/bin/prepareAlign
$ podman run --it --rm --entrypoint /usr/local/bin/prepareAlign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepareAlign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guppy

```bash
$ singularity exec <container> /usr/local/bin/guppy
$ podman run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pplacer

```bash
$ singularity exec <container> /usr/local/bin/pplacer
$ podman run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
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