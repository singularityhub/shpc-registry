---
layout: container
name:  "quay.io/biocontainers/chira"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chira/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chira/container.yaml"
updated_at: "2023-10-24 02:42:49.662264"
latest: "1.4.3--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/chira"
aliases:
 - "CopomuS.py"
 - "IntaRNA"
 - "IntaRNA1"
 - "IntaRNA2"
 - "IntaRNA3"
 - "IntaRNA_CSV_p-value.R"
 - "IntaRNA_plotRegions.R"
 - "IntaRNAduplex"
 - "IntaRNAens"
 - "IntaRNAexact"
 - "IntaRNAhelix"
 - "IntaRNAsTar"
 - "IntaRNAseed"
 - "blockbuster.x"
 - "chira_collapse.py"
 - "chira_extract.py"
 - "chira_map.py"
 - "chira_merge.py"
 - "chira_quantify.py"
 - "chira_utilities.py"
 - "clan_annotate"
 - "clan_index"
 - "clan_output"
 - "clan_search"
 - "RNAdos"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
 - "b2ct"
 - "ct2db"
 - "kinwalker"
 - "popt"
 - "RNA2Dfold"
versions:
 - "1.4.3--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for chira"
config: {"url": "https://biocontainers.pro/tools/chira", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chira", "latest": {"1.4.3--hdfd78af_2": "sha256:fab0a27149cb985fca193e33b2c331f78558dc90e799e85fb912dcdc255898bd"}, "tags": {"1.4.3--hdfd78af_2": "sha256:fab0a27149cb985fca193e33b2c331f78558dc90e799e85fb912dcdc255898bd"}, "docker": "quay.io/biocontainers/chira", "aliases": {"CopomuS.py": "/usr/local/bin/CopomuS.py", "IntaRNA": "/usr/local/bin/IntaRNA", "IntaRNA1": "/usr/local/bin/IntaRNA1", "IntaRNA2": "/usr/local/bin/IntaRNA2", "IntaRNA3": "/usr/local/bin/IntaRNA3", "IntaRNA_CSV_p-value.R": "/usr/local/bin/IntaRNA_CSV_p-value.R", "IntaRNA_plotRegions.R": "/usr/local/bin/IntaRNA_plotRegions.R", "IntaRNAduplex": "/usr/local/bin/IntaRNAduplex", "IntaRNAens": "/usr/local/bin/IntaRNAens", "IntaRNAexact": "/usr/local/bin/IntaRNAexact", "IntaRNAhelix": "/usr/local/bin/IntaRNAhelix", "IntaRNAsTar": "/usr/local/bin/IntaRNAsTar", "IntaRNAseed": "/usr/local/bin/IntaRNAseed", "blockbuster.x": "/usr/local/bin/blockbuster.x", "chira_collapse.py": "/usr/local/bin/chira_collapse.py", "chira_extract.py": "/usr/local/bin/chira_extract.py", "chira_map.py": "/usr/local/bin/chira_map.py", "chira_merge.py": "/usr/local/bin/chira_merge.py", "chira_quantify.py": "/usr/local/bin/chira_quantify.py", "chira_utilities.py": "/usr/local/bin/chira_utilities.py", "clan_annotate": "/usr/local/bin/clan_annotate", "clan_index": "/usr/local/bin/clan_index", "clan_output": "/usr/local/bin/clan_output", "clan_search": "/usr/local/bin/clan_search", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chira.
shpc-registry automated BioContainers addition for chira
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chira
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chira:1.4.3--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chira/1.4.3--hdfd78af_2
$ module help quay.io/biocontainers/chira/1.4.3--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chira-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chira-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chira-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chira-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chira-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chira-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CopomuS.py

```bash
$ singularity exec <container> /usr/local/bin/CopomuS.py
$ podman run --it --rm --entrypoint /usr/local/bin/CopomuS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CopomuS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA1

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA1
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA2

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA2
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA3

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA3
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA_CSV_p-value.R

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA_CSV_p-value.R
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA_CSV_p-value.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA_CSV_p-value.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA_plotRegions.R

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA_plotRegions.R
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA_plotRegions.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA_plotRegions.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAduplex

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAduplex
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAens

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAens
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAens   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAens   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAexact

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAexact
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAexact   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAexact   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAhelix

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAhelix
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAhelix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAhelix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAsTar

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAsTar
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAsTar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAsTar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAseed

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAseed
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAseed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAseed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blockbuster.x

```bash
$ singularity exec <container> /usr/local/bin/blockbuster.x
$ podman run --it --rm --entrypoint /usr/local/bin/blockbuster.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blockbuster.x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chira_collapse.py

```bash
$ singularity exec <container> /usr/local/bin/chira_collapse.py
$ podman run --it --rm --entrypoint /usr/local/bin/chira_collapse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chira_collapse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chira_extract.py

```bash
$ singularity exec <container> /usr/local/bin/chira_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/chira_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chira_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chira_map.py

```bash
$ singularity exec <container> /usr/local/bin/chira_map.py
$ podman run --it --rm --entrypoint /usr/local/bin/chira_map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chira_map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chira_merge.py

```bash
$ singularity exec <container> /usr/local/bin/chira_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/chira_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chira_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chira_quantify.py

```bash
$ singularity exec <container> /usr/local/bin/chira_quantify.py
$ podman run --it --rm --entrypoint /usr/local/bin/chira_quantify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chira_quantify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chira_utilities.py

```bash
$ singularity exec <container> /usr/local/bin/chira_utilities.py
$ podman run --it --rm --entrypoint /usr/local/bin/chira_utilities.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chira_utilities.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clan_annotate

```bash
$ singularity exec <container> /usr/local/bin/clan_annotate
$ podman run --it --rm --entrypoint /usr/local/bin/clan_annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clan_annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clan_index

```bash
$ singularity exec <container> /usr/local/bin/clan_index
$ podman run --it --rm --entrypoint /usr/local/bin/clan_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clan_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clan_output

```bash
$ singularity exec <container> /usr/local/bin/clan_output
$ podman run --it --rm --entrypoint /usr/local/bin/clan_output   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clan_output   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clan_search

```bash
$ singularity exec <container> /usr/local/bin/clan_search
$ podman run --it --rm --entrypoint /usr/local/bin/clan_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clan_search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdos

```bash
$ singularity exec <container> /usr/local/bin/RNAdos
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseDists

```bash
$ singularity exec <container> /usr/local/bin/AnalyseDists
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseSeqs

```bash
$ singularity exec <container> /usr/local/bin/AnalyseSeqs
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAlocmin

```bash
$ singularity exec <container> /usr/local/bin/RNAlocmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNApvmin

```bash
$ singularity exec <container> /usr/local/bin/RNApvmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2ct

```bash
$ singularity exec <container> /usr/local/bin/b2ct
$ podman run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2db

```bash
$ singularity exec <container> /usr/local/bin/ct2db
$ podman run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinwalker

```bash
$ singularity exec <container> /usr/local/bin/kinwalker
$ podman run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### popt

```bash
$ singularity exec <container> /usr/local/bin/popt
$ podman run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNA2Dfold

```bash
$ singularity exec <container> /usr/local/bin/RNA2Dfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
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