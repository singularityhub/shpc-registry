---
layout: container
name:  "quay.io/biocontainers/asqcan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/asqcan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/asqcan/container.yaml"
updated_at: "2025-10-01 03:51:00.666651"
latest: "0.4--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/asqcan"
aliases:
 - "asqcan"
 - "blobtools"
 - "blobtools-build_nodesdb"
 - "icarus.py"
 - "metaquast"
 - "metaquast.py"
 - "quast"
 - "quast-download-busco"
 - "quast-download-gridss"
 - "quast-download-silva"
 - "quast-lg.py"
 - "quast.py"
 - "circos"
 - "circos.exe"
 - "compile.bat"
 - "compile.make"
 - "gddiag"
 - "glimmerhmm"
 - "glimmhmm.pl"
 - "list.modules"
 - "test.modules"
 - "trainGlimmerHMM"
versions:
 - "0.2--py_2"
 - "0.4--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for asqcan"
config: {"url": "https://biocontainers.pro/tools/asqcan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for asqcan", "latest": {"0.4--pyh7cba7a3_0": "sha256:fb23f81ef79c1278b6b8af402db28d2915ba2cb721abe13fdf3f214e649d17bc"}, "tags": {"0.2--py_2": "sha256:317d0aaf61b66dacad7198d62b47c2409038955645c1d8efe2415fbcf7918d7b", "0.4--pyh7cba7a3_0": "sha256:fb23f81ef79c1278b6b8af402db28d2915ba2cb721abe13fdf3f214e649d17bc"}, "docker": "quay.io/biocontainers/asqcan", "aliases": {"asqcan": "/usr/local/bin/asqcan", "blobtools": "/usr/local/bin/blobtools", "blobtools-build_nodesdb": "/usr/local/bin/blobtools-build_nodesdb", "icarus.py": "/usr/local/bin/icarus.py", "metaquast": "/usr/local/bin/metaquast", "metaquast.py": "/usr/local/bin/metaquast.py", "quast": "/usr/local/bin/quast", "quast-download-busco": "/usr/local/bin/quast-download-busco", "quast-download-gridss": "/usr/local/bin/quast-download-gridss", "quast-download-silva": "/usr/local/bin/quast-download-silva", "quast-lg.py": "/usr/local/bin/quast-lg.py", "quast.py": "/usr/local/bin/quast.py", "circos": "/usr/local/bin/circos", "circos.exe": "/usr/local/bin/circos.exe", "compile.bat": "/usr/local/bin/compile.bat", "compile.make": "/usr/local/bin/compile.make", "gddiag": "/usr/local/bin/gddiag", "glimmerhmm": "/usr/local/bin/glimmerhmm", "glimmhmm.pl": "/usr/local/bin/glimmhmm.pl", "list.modules": "/usr/local/bin/list.modules", "test.modules": "/usr/local/bin/test.modules", "trainGlimmerHMM": "/usr/local/bin/trainGlimmerHMM"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/asqcan.
shpc-registry automated BioContainers addition for asqcan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/asqcan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/asqcan:0.4--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/asqcan/0.4--pyh7cba7a3_0
$ module help quay.io/biocontainers/asqcan/0.4--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### asqcan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### asqcan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### asqcan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### asqcan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### asqcan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### asqcan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### asqcan

```bash
$ singularity exec <container> /usr/local/bin/asqcan
$ podman run --it --rm --entrypoint /usr/local/bin/asqcan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asqcan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blobtools

```bash
$ singularity exec <container> /usr/local/bin/blobtools
$ podman run --it --rm --entrypoint /usr/local/bin/blobtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blobtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blobtools-build_nodesdb

```bash
$ singularity exec <container> /usr/local/bin/blobtools-build_nodesdb
$ podman run --it --rm --entrypoint /usr/local/bin/blobtools-build_nodesdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blobtools-build_nodesdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### icarus.py

```bash
$ singularity exec <container> /usr/local/bin/icarus.py
$ podman run --it --rm --entrypoint /usr/local/bin/icarus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/icarus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### trainGlimmerHMM

```bash
$ singularity exec <container> /usr/local/bin/trainGlimmerHMM
$ podman run --it --rm --entrypoint /usr/local/bin/trainGlimmerHMM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trainGlimmerHMM   -v ${PWD} -w ${PWD} <container> -c " $@"
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