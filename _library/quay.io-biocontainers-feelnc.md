---
layout: container
name:  "quay.io/biocontainers/feelnc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/feelnc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/feelnc/container.yaml"
updated_at: "2025-03-29 03:16:55.056135"
latest: "0.2--pl526_0"
container_url: "https://biocontainers.pro/tools/feelnc"
aliases:
 - "FEELnc_classifier.pl"
 - "FEELnc_classifier.pl.bak"
 - "FEELnc_codpot.pl"
 - "FEELnc_codpot.pl.bak"
 - "FEELnc_filter.pl"
 - "FEELnc_filter.pl.bak"
 - "FEELnc_pipeline.sh"
 - "FEELnc_tpLevel2gnLevelClassification.R"
 - "FEELnc_tpLevel2gnLevelClassification.R.bak"
 - "KmerInShort"
 - "fasta_ushuffle"
 - "ushuffle"
 - "gdlib-config"
 - "bam2bedgraph"
 - "bp_find-blast-matches.pl"
 - "ace.pl"
 - "ccconfig"
 - "SOAPsh.pl"
 - "map"
 - "mirrorMappings"
 - "mkCSGB2312"
 - "mkmapfile"
versions:
 - "0.2--pl526_0"
description: "shpc-registry automated BioContainers addition for feelnc"
config: {"url": "https://biocontainers.pro/tools/feelnc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for feelnc", "latest": {"0.2--pl526_0": "sha256:80753a45c717c2b2d1dededfe2732baa3cea54b12e8a73d1f48542bdef8480fd"}, "tags": {"0.2--pl526_0": "sha256:80753a45c717c2b2d1dededfe2732baa3cea54b12e8a73d1f48542bdef8480fd"}, "docker": "quay.io/biocontainers/feelnc", "aliases": {"FEELnc_classifier.pl": "/usr/local/bin/FEELnc_classifier.pl", "FEELnc_classifier.pl.bak": "/usr/local/bin/FEELnc_classifier.pl.bak", "FEELnc_codpot.pl": "/usr/local/bin/FEELnc_codpot.pl", "FEELnc_codpot.pl.bak": "/usr/local/bin/FEELnc_codpot.pl.bak", "FEELnc_filter.pl": "/usr/local/bin/FEELnc_filter.pl", "FEELnc_filter.pl.bak": "/usr/local/bin/FEELnc_filter.pl.bak", "FEELnc_pipeline.sh": "/usr/local/bin/FEELnc_pipeline.sh", "FEELnc_tpLevel2gnLevelClassification.R": "/usr/local/bin/FEELnc_tpLevel2gnLevelClassification.R", "FEELnc_tpLevel2gnLevelClassification.R.bak": "/usr/local/bin/FEELnc_tpLevel2gnLevelClassification.R.bak", "KmerInShort": "/usr/local/bin/KmerInShort", "fasta_ushuffle": "/usr/local/bin/fasta_ushuffle", "ushuffle": "/usr/local/bin/ushuffle", "gdlib-config": "/usr/local/bin/gdlib-config", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "ace.pl": "/usr/local/bin/ace.pl", "ccconfig": "/usr/local/bin/ccconfig", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "map": "/usr/local/bin/map", "mirrorMappings": "/usr/local/bin/mirrorMappings", "mkCSGB2312": "/usr/local/bin/mkCSGB2312", "mkmapfile": "/usr/local/bin/mkmapfile"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/feelnc.
shpc-registry automated BioContainers addition for feelnc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/feelnc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/feelnc:0.2--pl526_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/feelnc/0.2--pl526_0
$ module help quay.io/biocontainers/feelnc/0.2--pl526_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### feelnc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### feelnc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### feelnc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### feelnc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### feelnc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### feelnc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FEELnc_classifier.pl

```bash
$ singularity exec <container> /usr/local/bin/FEELnc_classifier.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FEELnc_classifier.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FEELnc_classifier.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FEELnc_classifier.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/FEELnc_classifier.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/FEELnc_classifier.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FEELnc_classifier.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FEELnc_codpot.pl

```bash
$ singularity exec <container> /usr/local/bin/FEELnc_codpot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FEELnc_codpot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FEELnc_codpot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FEELnc_codpot.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/FEELnc_codpot.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/FEELnc_codpot.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FEELnc_codpot.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FEELnc_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/FEELnc_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FEELnc_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FEELnc_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FEELnc_filter.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/FEELnc_filter.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/FEELnc_filter.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FEELnc_filter.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FEELnc_pipeline.sh

```bash
$ singularity exec <container> /usr/local/bin/FEELnc_pipeline.sh
$ podman run --it --rm --entrypoint /usr/local/bin/FEELnc_pipeline.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FEELnc_pipeline.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FEELnc_tpLevel2gnLevelClassification.R

```bash
$ singularity exec <container> /usr/local/bin/FEELnc_tpLevel2gnLevelClassification.R
$ podman run --it --rm --entrypoint /usr/local/bin/FEELnc_tpLevel2gnLevelClassification.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FEELnc_tpLevel2gnLevelClassification.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FEELnc_tpLevel2gnLevelClassification.R.bak

```bash
$ singularity exec <container> /usr/local/bin/FEELnc_tpLevel2gnLevelClassification.R.bak
$ podman run --it --rm --entrypoint /usr/local/bin/FEELnc_tpLevel2gnLevelClassification.R.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FEELnc_tpLevel2gnLevelClassification.R.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KmerInShort

```bash
$ singularity exec <container> /usr/local/bin/KmerInShort
$ podman run --it --rm --entrypoint /usr/local/bin/KmerInShort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerInShort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_ushuffle

```bash
$ singularity exec <container> /usr/local/bin/fasta_ushuffle
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_ushuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_ushuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ushuffle

```bash
$ singularity exec <container> /usr/local/bin/ushuffle
$ podman run --it --rm --entrypoint /usr/local/bin/ushuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ushuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccconfig

```bash
$ singularity exec <container> /usr/local/bin/ccconfig
$ podman run --it --rm --entrypoint /usr/local/bin/ccconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map

```bash
$ singularity exec <container> /usr/local/bin/map
$ podman run --it --rm --entrypoint /usr/local/bin/map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirrorMappings

```bash
$ singularity exec <container> /usr/local/bin/mirrorMappings
$ podman run --it --rm --entrypoint /usr/local/bin/mirrorMappings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirrorMappings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkCSGB2312

```bash
$ singularity exec <container> /usr/local/bin/mkCSGB2312
$ podman run --it --rm --entrypoint /usr/local/bin/mkCSGB2312   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkCSGB2312   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkmapfile

```bash
$ singularity exec <container> /usr/local/bin/mkmapfile
$ podman run --it --rm --entrypoint /usr/local/bin/mkmapfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkmapfile   -v ${PWD} -w ${PWD} <container> -c " $@"
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