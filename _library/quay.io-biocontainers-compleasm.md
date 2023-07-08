---
layout: container
name:  "quay.io/biocontainers/compleasm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/compleasm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/compleasm/container.yaml"
updated_at: "2023-07-08 03:29:26.424224"
latest: "0.2.2--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/compleasm"
aliases:
 - "compleasm"
 - "hb-info"
 - "jwebserver"
 - "miniprot"
 - "run-sepp.sh"
 - "run_sepp.py"
 - "run_upp.py"
 - "seppJsonMerger.jar"
 - "split_sequences.py"
 - "hmmc2"
 - "hmmerfm-exactmatch"
 - "guppy"
 - "pplacer"
 - "dendropy-format"
 - "tjbench"
 - "sumlabels.py"
 - "sumtrees.py"
 - "jpackage"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "alimask"
 - "hmmconvert"
 - "hmmemit"
 - "hmmfetch"
 - "hmmlogo"
 - "hmmpgmd"
 - "hmmpress"
 - "hmmscan"
 - "hmmsearch"
 - "hmmsim"
 - "hmmstat"
 - "jackhmmer"
 - "makehmmerdb"
versions:
 - "0.2.2--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for compleasm"
config: {"url": "https://biocontainers.pro/tools/compleasm", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for compleasm", "latest": {"0.2.2--pyh7cba7a3_0": "sha256:f4e232d2e1861d9d3be59d61bc555b59f3308e57ae5054ee99287986152dad25"}, "tags": {"0.2.2--pyh7cba7a3_0": "sha256:f4e232d2e1861d9d3be59d61bc555b59f3308e57ae5054ee99287986152dad25"}, "docker": "quay.io/biocontainers/compleasm", "aliases": {"compleasm": "/usr/local/bin/compleasm", "hb-info": "/usr/local/bin/hb-info", "jwebserver": "/usr/local/bin/jwebserver", "miniprot": "/usr/local/bin/miniprot", "run-sepp.sh": "/usr/local/bin/run-sepp.sh", "run_sepp.py": "/usr/local/bin/run_sepp.py", "run_upp.py": "/usr/local/bin/run_upp.py", "seppJsonMerger.jar": "/usr/local/bin/seppJsonMerger.jar", "split_sequences.py": "/usr/local/bin/split_sequences.py", "hmmc2": "/usr/local/bin/hmmc2", "hmmerfm-exactmatch": "/usr/local/bin/hmmerfm-exactmatch", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer", "dendropy-format": "/usr/local/bin/dendropy-format", "tjbench": "/usr/local/bin/tjbench", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "jpackage": "/usr/local/bin/jpackage", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "alimask": "/usr/local/bin/alimask", "hmmconvert": "/usr/local/bin/hmmconvert", "hmmemit": "/usr/local/bin/hmmemit", "hmmfetch": "/usr/local/bin/hmmfetch", "hmmlogo": "/usr/local/bin/hmmlogo", "hmmpgmd": "/usr/local/bin/hmmpgmd", "hmmpress": "/usr/local/bin/hmmpress", "hmmscan": "/usr/local/bin/hmmscan", "hmmsearch": "/usr/local/bin/hmmsearch", "hmmsim": "/usr/local/bin/hmmsim", "hmmstat": "/usr/local/bin/hmmstat", "jackhmmer": "/usr/local/bin/jackhmmer", "makehmmerdb": "/usr/local/bin/makehmmerdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/compleasm.
singularity registry hpc automated addition for compleasm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/compleasm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/compleasm:0.2.2--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/compleasm/0.2.2--pyh7cba7a3_0
$ module help quay.io/biocontainers/compleasm/0.2.2--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### compleasm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### compleasm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### compleasm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### compleasm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### compleasm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### compleasm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compleasm

```bash
$ singularity exec <container> /usr/local/bin/compleasm
$ podman run --it --rm --entrypoint /usr/local/bin/compleasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compleasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniprot

```bash
$ singularity exec <container> /usr/local/bin/miniprot
$ podman run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-sepp.sh

```bash
$ singularity exec <container> /usr/local/bin/run-sepp.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run-sepp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-sepp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_sepp.py

```bash
$ singularity exec <container> /usr/local/bin/run_sepp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_sepp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_sepp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmconvert

```bash
$ singularity exec <container> /usr/local/bin/hmmconvert
$ podman run --it --rm --entrypoint /usr/local/bin/hmmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmemit

```bash
$ singularity exec <container> /usr/local/bin/hmmemit
$ podman run --it --rm --entrypoint /usr/local/bin/hmmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmfetch

```bash
$ singularity exec <container> /usr/local/bin/hmmfetch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmlogo

```bash
$ singularity exec <container> /usr/local/bin/hmmlogo
$ podman run --it --rm --entrypoint /usr/local/bin/hmmlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd

```bash
$ singularity exec <container> /usr/local/bin/hmmpgmd
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpgmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpgmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpress

```bash
$ singularity exec <container> /usr/local/bin/hmmpress
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmscan

```bash
$ singularity exec <container> /usr/local/bin/hmmscan
$ podman run --it --rm --entrypoint /usr/local/bin/hmmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmsearch

```bash
$ singularity exec <container> /usr/local/bin/hmmsearch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmsim

```bash
$ singularity exec <container> /usr/local/bin/hmmsim
$ podman run --it --rm --entrypoint /usr/local/bin/hmmsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmstat

```bash
$ singularity exec <container> /usr/local/bin/hmmstat
$ podman run --it --rm --entrypoint /usr/local/bin/hmmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jackhmmer

```bash
$ singularity exec <container> /usr/local/bin/jackhmmer
$ podman run --it --rm --entrypoint /usr/local/bin/jackhmmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jackhmmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makehmmerdb

```bash
$ singularity exec <container> /usr/local/bin/makehmmerdb
$ podman run --it --rm --entrypoint /usr/local/bin/makehmmerdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makehmmerdb   -v ${PWD} -w ${PWD} <container> -c " $@"
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