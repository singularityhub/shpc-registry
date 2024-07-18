---
layout: container
name:  "quay.io/biocontainers/proksee"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proksee/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proksee/container.yaml"
updated_at: "2024-07-18 03:07:34.594858"
latest: "1.0.0a6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/proksee"
aliases:
 - "icarus.py"
 - "metaquast"
 - "metaquast.py"
 - "proksee"
 - "quast"
 - "quast-download-busco"
 - "quast-download-gridss"
 - "quast-download-silva"
 - "quast-lg.py"
 - "quast.py"
 - "skesa"
 - "circos"
 - "circos.exe"
 - "compile.bat"
 - "compile.make"
 - "fastp"
 - "gddiag"
 - "glimmerhmm"
 - "glimmhmm.pl"
 - "list.modules"
 - "test.modules"
versions:
 - "1.0.0a4--pyhdfd78af_0"
 - "1.0.0a5--pyhdfd78af_0"
 - "1.0.0a6--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for proksee"
config: {"url": "https://biocontainers.pro/tools/proksee", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proksee", "latest": {"1.0.0a6--pyhdfd78af_0": "sha256:c8d4302b0da5aedbaf5fb6c4557dbe3e5cf7edcebc1e9f51475d3bdb86ddc6bd"}, "tags": {"1.0.0a4--pyhdfd78af_0": "sha256:fb811bb9bef452206126f7c68199a3c820064cae0d4a7b973da5f5c3500299ce", "1.0.0a5--pyhdfd78af_0": "sha256:5b48c4c8a99339f97a8c9795d82a3efd8902c8b6be660e1f5aa112ee87867fd5", "1.0.0a6--pyhdfd78af_0": "sha256:c8d4302b0da5aedbaf5fb6c4557dbe3e5cf7edcebc1e9f51475d3bdb86ddc6bd"}, "docker": "quay.io/biocontainers/proksee", "aliases": {"icarus.py": "/usr/local/bin/icarus.py", "metaquast": "/usr/local/bin/metaquast", "metaquast.py": "/usr/local/bin/metaquast.py", "proksee": "/usr/local/bin/proksee", "quast": "/usr/local/bin/quast", "quast-download-busco": "/usr/local/bin/quast-download-busco", "quast-download-gridss": "/usr/local/bin/quast-download-gridss", "quast-download-silva": "/usr/local/bin/quast-download-silva", "quast-lg.py": "/usr/local/bin/quast-lg.py", "quast.py": "/usr/local/bin/quast.py", "skesa": "/usr/local/bin/skesa", "circos": "/usr/local/bin/circos", "circos.exe": "/usr/local/bin/circos.exe", "compile.bat": "/usr/local/bin/compile.bat", "compile.make": "/usr/local/bin/compile.make", "fastp": "/usr/local/bin/fastp", "gddiag": "/usr/local/bin/gddiag", "glimmerhmm": "/usr/local/bin/glimmerhmm", "glimmhmm.pl": "/usr/local/bin/glimmhmm.pl", "list.modules": "/usr/local/bin/list.modules", "test.modules": "/usr/local/bin/test.modules"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proksee.
shpc-registry automated BioContainers addition for proksee
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proksee
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proksee:1.0.0a6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proksee/1.0.0a6--pyhdfd78af_0
$ module help quay.io/biocontainers/proksee/1.0.0a6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proksee-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proksee-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proksee-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proksee-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proksee-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proksee-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### proksee

```bash
$ singularity exec <container> /usr/local/bin/proksee
$ podman run --it --rm --entrypoint /usr/local/bin/proksee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proksee   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### skesa

```bash
$ singularity exec <container> /usr/local/bin/skesa
$ podman run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
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