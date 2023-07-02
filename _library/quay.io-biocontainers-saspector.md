---
layout: container
name:  "quay.io/biocontainers/saspector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/saspector/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/saspector/container.yaml"
updated_at: "2023-07-02 03:46:44.973091"
latest: "0.0.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/saspector"
aliases:
 - "SASpector"
 - "coverage.py"
 - "gene_predict.py"
 - "icarus.py"
 - "kmer.py"
 - "mapper.py"
 - "metaquast"
 - "metaquast.py"
 - "progressiveMauve"
 - "quast"
 - "quast-download-busco"
 - "quast-download-gridss"
 - "quast-download-silva"
 - "quast-lg.py"
 - "quast.py"
 - "quastunmap.py"
 - "select_mash.py"
 - "sourmash"
 - "summary.py"
 - "tandem_repeats.py"
 - "tbl2asn-test"
 - "fix-sqn-date"
 - "circos"
 - "circos.exe"
 - "compile.bat"
 - "compile.make"
 - "faketime"
 - "gddiag"
 - "glimmerhmm"
 - "glimmhmm.pl"
 - "list.modules"
versions:
 - "0.0.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for saspector"
config: {"url": "https://biocontainers.pro/tools/saspector", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for saspector", "latest": {"0.0.5--pyhdfd78af_0": "sha256:f31f4140479e99f4719863cd8bddfd4fd0c6c12ffa8d38a92e52d29943833f56"}, "tags": {"0.0.5--pyhdfd78af_0": "sha256:f31f4140479e99f4719863cd8bddfd4fd0c6c12ffa8d38a92e52d29943833f56"}, "docker": "quay.io/biocontainers/saspector", "aliases": {"SASpector": "/usr/local/bin/SASpector", "coverage.py": "/usr/local/bin/coverage.py", "gene_predict.py": "/usr/local/bin/gene_predict.py", "icarus.py": "/usr/local/bin/icarus.py", "kmer.py": "/usr/local/bin/kmer.py", "mapper.py": "/usr/local/bin/mapper.py", "metaquast": "/usr/local/bin/metaquast", "metaquast.py": "/usr/local/bin/metaquast.py", "progressiveMauve": "/usr/local/bin/progressiveMauve", "quast": "/usr/local/bin/quast", "quast-download-busco": "/usr/local/bin/quast-download-busco", "quast-download-gridss": "/usr/local/bin/quast-download-gridss", "quast-download-silva": "/usr/local/bin/quast-download-silva", "quast-lg.py": "/usr/local/bin/quast-lg.py", "quast.py": "/usr/local/bin/quast.py", "quastunmap.py": "/usr/local/bin/quastunmap.py", "select_mash.py": "/usr/local/bin/select_mash.py", "sourmash": "/usr/local/bin/sourmash", "summary.py": "/usr/local/bin/summary.py", "tandem_repeats.py": "/usr/local/bin/tandem_repeats.py", "tbl2asn-test": "/usr/local/bin/tbl2asn-test", "fix-sqn-date": "/usr/local/bin/fix-sqn-date", "circos": "/usr/local/bin/circos", "circos.exe": "/usr/local/bin/circos.exe", "compile.bat": "/usr/local/bin/compile.bat", "compile.make": "/usr/local/bin/compile.make", "faketime": "/usr/local/bin/faketime", "gddiag": "/usr/local/bin/gddiag", "glimmerhmm": "/usr/local/bin/glimmerhmm", "glimmhmm.pl": "/usr/local/bin/glimmhmm.pl", "list.modules": "/usr/local/bin/list.modules"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/saspector.
shpc-registry automated BioContainers addition for saspector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/saspector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/saspector:0.0.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/saspector/0.0.5--pyhdfd78af_0
$ module help quay.io/biocontainers/saspector/0.0.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### saspector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### saspector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### saspector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### saspector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### saspector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### saspector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SASpector

```bash
$ singularity exec <container> /usr/local/bin/SASpector
$ podman run --it --rm --entrypoint /usr/local/bin/SASpector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SASpector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage.py

```bash
$ singularity exec <container> /usr/local/bin/coverage.py
$ podman run --it --rm --entrypoint /usr/local/bin/coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_predict.py

```bash
$ singularity exec <container> /usr/local/bin/gene_predict.py
$ podman run --it --rm --entrypoint /usr/local/bin/gene_predict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_predict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### icarus.py

```bash
$ singularity exec <container> /usr/local/bin/icarus.py
$ podman run --it --rm --entrypoint /usr/local/bin/icarus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/icarus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer.py

```bash
$ singularity exec <container> /usr/local/bin/kmer.py
$ podman run --it --rm --entrypoint /usr/local/bin/kmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapper.py

```bash
$ singularity exec <container> /usr/local/bin/mapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/mapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### progressiveMauve

```bash
$ singularity exec <container> /usr/local/bin/progressiveMauve
$ podman run --it --rm --entrypoint /usr/local/bin/progressiveMauve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/progressiveMauve   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### quastunmap.py

```bash
$ singularity exec <container> /usr/local/bin/quastunmap.py
$ podman run --it --rm --entrypoint /usr/local/bin/quastunmap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quastunmap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_mash.py

```bash
$ singularity exec <container> /usr/local/bin/select_mash.py
$ podman run --it --rm --entrypoint /usr/local/bin/select_mash.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_mash.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sourmash

```bash
$ singularity exec <container> /usr/local/bin/sourmash
$ podman run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summary.py

```bash
$ singularity exec <container> /usr/local/bin/summary.py
$ podman run --it --rm --entrypoint /usr/local/bin/summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tandem_repeats.py

```bash
$ singularity exec <container> /usr/local/bin/tandem_repeats.py
$ podman run --it --rm --entrypoint /usr/local/bin/tandem_repeats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tandem_repeats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2asn-test

```bash
$ singularity exec <container> /usr/local/bin/tbl2asn-test
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix-sqn-date

```bash
$ singularity exec <container> /usr/local/bin/fix-sqn-date
$ podman run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### faketime

```bash
$ singularity exec <container> /usr/local/bin/faketime
$ podman run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
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