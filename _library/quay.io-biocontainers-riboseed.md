---
layout: container
name:  "quay.io/biocontainers/riboseed"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/riboseed/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/riboseed/container.yaml"
updated_at: "2024-10-13 11:07:53.270550"
latest: "0.4.90--py_0"
container_url: "https://biocontainers.pro/tools/riboseed"
aliases:
 - "bwa-spades"
 - "corrector"
 - "dipspades"
 - "dipspades.py"
 - "hammer"
 - "icarus.py"
 - "ionhammer"
 - "metaquast"
 - "metaquast.py"
 - "quast"
 - "quast-download-busco"
 - "quast-download-gridss"
 - "quast-download-silva"
 - "quast-lg.py"
 - "quast.py"
 - "ribo"
 - "scaffold_correction"
 - "seedRand.py"
 - "skesa"
 - "spades"
 - "prank"
 - "circos"
 - "circos.exe"
 - "compile.bat"
 - "compile.make"
 - "gddiag"
 - "glimmerhmm"
 - "glimmhmm.pl"
 - "list.modules"
 - "test.modules"
versions:
 - "0.4.90--py_0"
description: "shpc-registry automated BioContainers addition for riboseed"
config: {"url": "https://biocontainers.pro/tools/riboseed", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for riboseed", "latest": {"0.4.90--py_0": "sha256:fa2228d3f952cb968f6a09de4ce144055037b9cbf4834bce17861eadcaa045ec"}, "tags": {"0.4.90--py_0": "sha256:fa2228d3f952cb968f6a09de4ce144055037b9cbf4834bce17861eadcaa045ec"}, "docker": "quay.io/biocontainers/riboseed", "aliases": {"bwa-spades": "/usr/local/bin/bwa-spades", "corrector": "/usr/local/bin/corrector", "dipspades": "/usr/local/bin/dipspades", "dipspades.py": "/usr/local/bin/dipspades.py", "hammer": "/usr/local/bin/hammer", "icarus.py": "/usr/local/bin/icarus.py", "ionhammer": "/usr/local/bin/ionhammer", "metaquast": "/usr/local/bin/metaquast", "metaquast.py": "/usr/local/bin/metaquast.py", "quast": "/usr/local/bin/quast", "quast-download-busco": "/usr/local/bin/quast-download-busco", "quast-download-gridss": "/usr/local/bin/quast-download-gridss", "quast-download-silva": "/usr/local/bin/quast-download-silva", "quast-lg.py": "/usr/local/bin/quast-lg.py", "quast.py": "/usr/local/bin/quast.py", "ribo": "/usr/local/bin/ribo", "scaffold_correction": "/usr/local/bin/scaffold_correction", "seedRand.py": "/usr/local/bin/seedRand.py", "skesa": "/usr/local/bin/skesa", "spades": "/usr/local/bin/spades", "prank": "/usr/local/bin/prank", "circos": "/usr/local/bin/circos", "circos.exe": "/usr/local/bin/circos.exe", "compile.bat": "/usr/local/bin/compile.bat", "compile.make": "/usr/local/bin/compile.make", "gddiag": "/usr/local/bin/gddiag", "glimmerhmm": "/usr/local/bin/glimmerhmm", "glimmhmm.pl": "/usr/local/bin/glimmhmm.pl", "list.modules": "/usr/local/bin/list.modules", "test.modules": "/usr/local/bin/test.modules"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/riboseed.
shpc-registry automated BioContainers addition for riboseed
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/riboseed
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/riboseed:0.4.90--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/riboseed/0.4.90--py_0
$ module help quay.io/biocontainers/riboseed/0.4.90--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### riboseed-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### riboseed-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### riboseed-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### riboseed-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### riboseed-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### riboseed-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa-spades

```bash
$ singularity exec <container> /usr/local/bin/bwa-spades
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-spades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-spades   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corrector

```bash
$ singularity exec <container> /usr/local/bin/corrector
$ podman run --it --rm --entrypoint /usr/local/bin/corrector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corrector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dipspades

```bash
$ singularity exec <container> /usr/local/bin/dipspades
$ podman run --it --rm --entrypoint /usr/local/bin/dipspades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipspades   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dipspades.py

```bash
$ singularity exec <container> /usr/local/bin/dipspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/dipspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hammer

```bash
$ singularity exec <container> /usr/local/bin/hammer
$ podman run --it --rm --entrypoint /usr/local/bin/hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### icarus.py

```bash
$ singularity exec <container> /usr/local/bin/icarus.py
$ podman run --it --rm --entrypoint /usr/local/bin/icarus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/icarus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ionhammer

```bash
$ singularity exec <container> /usr/local/bin/ionhammer
$ podman run --it --rm --entrypoint /usr/local/bin/ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaquast

```bash
$ singularity exec <container> /usr/local/bin/metaquast
$ podman run --it --rm --entrypoint /usr/local/bin/metaquast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaquast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaquast.py

```bash
$ singularity exec <container> /usr/local/bin/metaquast.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaquast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaquast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast

```bash
$ singularity exec <container> /usr/local/bin/quast
$ podman run --it --rm --entrypoint /usr/local/bin/quast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-download-busco

```bash
$ singularity exec <container> /usr/local/bin/quast-download-busco
$ podman run --it --rm --entrypoint /usr/local/bin/quast-download-busco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-download-busco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-download-gridss

```bash
$ singularity exec <container> /usr/local/bin/quast-download-gridss
$ podman run --it --rm --entrypoint /usr/local/bin/quast-download-gridss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-download-gridss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-download-silva

```bash
$ singularity exec <container> /usr/local/bin/quast-download-silva
$ podman run --it --rm --entrypoint /usr/local/bin/quast-download-silva   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-download-silva   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-lg.py

```bash
$ singularity exec <container> /usr/local/bin/quast-lg.py
$ podman run --it --rm --entrypoint /usr/local/bin/quast-lg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-lg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast.py

```bash
$ singularity exec <container> /usr/local/bin/quast.py
$ podman run --it --rm --entrypoint /usr/local/bin/quast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ribo

```bash
$ singularity exec <container> /usr/local/bin/ribo
$ podman run --it --rm --entrypoint /usr/local/bin/ribo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ribo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scaffold_correction

```bash
$ singularity exec <container> /usr/local/bin/scaffold_correction
$ podman run --it --rm --entrypoint /usr/local/bin/scaffold_correction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scaffold_correction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seedRand.py

```bash
$ singularity exec <container> /usr/local/bin/seedRand.py
$ podman run --it --rm --entrypoint /usr/local/bin/seedRand.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seedRand.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skesa

```bash
$ singularity exec <container> /usr/local/bin/skesa
$ podman run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades

```bash
$ singularity exec <container> /usr/local/bin/spades
$ podman run --it --rm --entrypoint /usr/local/bin/spades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prank

```bash
$ singularity exec <container> /usr/local/bin/prank
$ podman run --it --rm --entrypoint /usr/local/bin/prank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circos

```bash
$ singularity exec <container> /usr/local/bin/circos
$ podman run --it --rm --entrypoint /usr/local/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circos.exe

```bash
$ singularity exec <container> /usr/local/bin/circos.exe
$ podman run --it --rm --entrypoint /usr/local/bin/circos.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circos.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile.bat

```bash
$ singularity exec <container> /usr/local/bin/compile.bat
$ podman run --it --rm --entrypoint /usr/local/bin/compile.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile.make

```bash
$ singularity exec <container> /usr/local/bin/compile.make
$ podman run --it --rm --entrypoint /usr/local/bin/compile.make   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile.make   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gddiag

```bash
$ singularity exec <container> /usr/local/bin/gddiag
$ podman run --it --rm --entrypoint /usr/local/bin/gddiag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gddiag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glimmerhmm

```bash
$ singularity exec <container> /usr/local/bin/glimmerhmm
$ podman run --it --rm --entrypoint /usr/local/bin/glimmerhmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glimmerhmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glimmhmm.pl

```bash
$ singularity exec <container> /usr/local/bin/glimmhmm.pl
$ podman run --it --rm --entrypoint /usr/local/bin/glimmhmm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glimmhmm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### list.modules

```bash
$ singularity exec <container> /usr/local/bin/list.modules
$ podman run --it --rm --entrypoint /usr/local/bin/list.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/list.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.modules

```bash
$ singularity exec <container> /usr/local/bin/test.modules
$ podman run --it --rm --entrypoint /usr/local/bin/test.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
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