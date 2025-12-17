---
layout: container
name:  "quay.io/biocontainers/metawrap-reassemble-bins"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metawrap-reassemble-bins/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metawrap-reassemble-bins/container.yaml"
updated_at: "2025-12-17 15:48:11.106271"
latest: "1.3.0--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/metawrap-reassemble-bins"
aliases:
 - "config-metawrap"
 - "metaWRAP"
 - "metawrap"
 - "checkm"
 - "rppr"
 - "guppy"
 - "pplacer"
 - "spades-truseq-scfcorrection"
 - "truspades.py"
 - "spades-bwa"
 - "spades-core"
 - "spades-corrector-core"
 - "spades-gbuilder"
 - "spades-gmapper"
 - "spades-hammer"
 - "spades-ionhammer"
 - "spades-kmercount"
 - "metaspades.py"
 - "plasmidspades.py"
 - "rnaspades.py"
 - "spades.py"
 - "spades_init.py"
 - "dendropy-format"
 - "sumlabels.py"
 - "sumtrees.py"
 - "shmemrun"
 - "oshCC"
 - "oshc++"
versions:
 - "1.3.0--hdfd78af_3"
description: "singularity registry hpc automated addition for metawrap-reassemble-bins"
config: {"url": "https://biocontainers.pro/tools/metawrap-reassemble-bins", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metawrap-reassemble-bins", "latest": {"1.3.0--hdfd78af_3": "sha256:25b1c3868e4f5d84e572dcc3c0ba728a6828dce8c64173311a6e2f7add9934aa"}, "tags": {"1.3.0--hdfd78af_3": "sha256:25b1c3868e4f5d84e572dcc3c0ba728a6828dce8c64173311a6e2f7add9934aa"}, "docker": "quay.io/biocontainers/metawrap-reassemble-bins", "aliases": {"config-metawrap": "/usr/local/bin/config-metawrap", "metaWRAP": "/usr/local/bin/metaWRAP", "metawrap": "/usr/local/bin/metawrap", "checkm": "/usr/local/bin/checkm", "rppr": "/usr/local/bin/rppr", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer", "spades-truseq-scfcorrection": "/usr/local/bin/spades-truseq-scfcorrection", "truspades.py": "/usr/local/bin/truspades.py", "spades-bwa": "/usr/local/bin/spades-bwa", "spades-core": "/usr/local/bin/spades-core", "spades-corrector-core": "/usr/local/bin/spades-corrector-core", "spades-gbuilder": "/usr/local/bin/spades-gbuilder", "spades-gmapper": "/usr/local/bin/spades-gmapper", "spades-hammer": "/usr/local/bin/spades-hammer", "spades-ionhammer": "/usr/local/bin/spades-ionhammer", "spades-kmercount": "/usr/local/bin/spades-kmercount", "metaspades.py": "/usr/local/bin/metaspades.py", "plasmidspades.py": "/usr/local/bin/plasmidspades.py", "rnaspades.py": "/usr/local/bin/rnaspades.py", "spades.py": "/usr/local/bin/spades.py", "spades_init.py": "/usr/local/bin/spades_init.py", "dendropy-format": "/usr/local/bin/dendropy-format", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "shmemrun": "/usr/local/bin/shmemrun", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metawrap-reassemble-bins.
singularity registry hpc automated addition for metawrap-reassemble-bins
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metawrap-reassemble-bins
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metawrap-reassemble-bins:1.3.0--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metawrap-reassemble-bins/1.3.0--hdfd78af_3
$ module help quay.io/biocontainers/metawrap-reassemble-bins/1.3.0--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metawrap-reassemble-bins-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metawrap-reassemble-bins-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metawrap-reassemble-bins-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metawrap-reassemble-bins-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metawrap-reassemble-bins-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metawrap-reassemble-bins-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### config-metawrap

```bash
$ singularity exec <container> /usr/local/bin/config-metawrap
$ podman run --it --rm --entrypoint /usr/local/bin/config-metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config-metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaWRAP

```bash
$ singularity exec <container> /usr/local/bin/metaWRAP
$ podman run --it --rm --entrypoint /usr/local/bin/metaWRAP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaWRAP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metawrap

```bash
$ singularity exec <container> /usr/local/bin/metawrap
$ podman run --it --rm --entrypoint /usr/local/bin/metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkm

```bash
$ singularity exec <container> /usr/local/bin/checkm
$ podman run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rppr

```bash
$ singularity exec <container> /usr/local/bin/rppr
$ podman run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### spades-truseq-scfcorrection

```bash
$ singularity exec <container> /usr/local/bin/spades-truseq-scfcorrection
$ podman run --it --rm --entrypoint /usr/local/bin/spades-truseq-scfcorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-truseq-scfcorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### truspades.py

```bash
$ singularity exec <container> /usr/local/bin/truspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/truspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/truspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-bwa

```bash
$ singularity exec <container> /usr/local/bin/spades-bwa
$ podman run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-core

```bash
$ singularity exec <container> /usr/local/bin/spades-core
$ podman run --it --rm --entrypoint /usr/local/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-corrector-core

```bash
$ singularity exec <container> /usr/local/bin/spades-corrector-core
$ podman run --it --rm --entrypoint /usr/local/bin/spades-corrector-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-corrector-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gbuilder

```bash
$ singularity exec <container> /usr/local/bin/spades-gbuilder
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gmapper

```bash
$ singularity exec <container> /usr/local/bin/spades-gmapper
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-hammer

```bash
$ singularity exec <container> /usr/local/bin/spades-hammer
$ podman run --it --rm --entrypoint /usr/local/bin/spades-hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-ionhammer

```bash
$ singularity exec <container> /usr/local/bin/spades-ionhammer
$ podman run --it --rm --entrypoint /usr/local/bin/spades-ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmercount

```bash
$ singularity exec <container> /usr/local/bin/spades-kmercount
$ podman run --it --rm --entrypoint /usr/local/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/plasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades.py

```bash
$ singularity exec <container> /usr/local/bin/spades.py
$ podman run --it --rm --entrypoint /usr/local/bin/spades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades_init.py

```bash
$ singularity exec <container> /usr/local/bin/spades_init.py
$ podman run --it --rm --entrypoint /usr/local/bin/spades_init.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades_init.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### shmemrun

```bash
$ singularity exec <container> /usr/local/bin/shmemrun
$ podman run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshCC

```bash
$ singularity exec <container> /usr/local/bin/oshCC
$ podman run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshc++

```bash
$ singularity exec <container> /usr/local/bin/oshc++
$ podman run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
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