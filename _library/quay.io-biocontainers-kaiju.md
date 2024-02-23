---
layout: container
name:  "quay.io/biocontainers/kaiju"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kaiju/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kaiju/container.yaml"
updated_at: "2024-02-23 02:41:37.883407"
latest: "1.10.0--h43eeafb_0"
container_url: "https://biocontainers.pro/tools/kaiju"
aliases:
 - "kaiju"
 - "kaiju-addTaxonNames"
 - "kaiju-convertMAR.py"
 - "kaiju-convertNR"
 - "kaiju-excluded-accessions.txt"
 - "kaiju-gbk2faa.pl"
 - "kaiju-makedb"
 - "kaiju-mergeOutputs"
 - "kaiju-mkbwt"
 - "kaiju-mkfmi"
 - "kaiju-multi"
 - "kaiju-taxonlistEuk.tsv"
 - "kaiju2krona"
 - "kaiju2table"
 - "kaijup"
 - "kaijux"
 - "idn2"
 - "wget"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.9.0--h5b5514e_1"
 - "1.9.2--h5b5514e_0"
 - "1.9.2--h43eeafb_2"
 - "1.9.2--h43eeafb_3"
 - "1.10.0--h43eeafb_0"
description: "shpc-registry automated BioContainers addition for kaiju"
config: {"url": "https://biocontainers.pro/tools/kaiju", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kaiju", "latest": {"1.10.0--h43eeafb_0": "sha256:7553f49894e08b77295a9c5791b262209c69903dedf758b0fa90fa659775c8d0"}, "tags": {"1.9.0--h5b5514e_1": "sha256:4131bb30e4ee9edcec5abfb9d90ad5f09b6acf6c7361bc10cac781805a474c27", "1.9.2--h5b5514e_0": "sha256:6ec9778b106ff52005c83e1876c3227c3fd8be8c39131413b43a735ffed3055a", "1.9.2--h43eeafb_2": "sha256:35cd0f5755916855575235644a9fd293adddcb9432993dbce114b6895dad974e", "1.9.2--h43eeafb_3": "sha256:ac63491b7a20e60658bf8247e53e107cecae1cddc40769d2b0c9f9317da63c27", "1.10.0--h43eeafb_0": "sha256:7553f49894e08b77295a9c5791b262209c69903dedf758b0fa90fa659775c8d0"}, "docker": "quay.io/biocontainers/kaiju", "aliases": {"kaiju": "/usr/local/bin/kaiju", "kaiju-addTaxonNames": "/usr/local/bin/kaiju-addTaxonNames", "kaiju-convertMAR.py": "/usr/local/bin/kaiju-convertMAR.py", "kaiju-convertNR": "/usr/local/bin/kaiju-convertNR", "kaiju-excluded-accessions.txt": "/usr/local/bin/kaiju-excluded-accessions.txt", "kaiju-gbk2faa.pl": "/usr/local/bin/kaiju-gbk2faa.pl", "kaiju-makedb": "/usr/local/bin/kaiju-makedb", "kaiju-mergeOutputs": "/usr/local/bin/kaiju-mergeOutputs", "kaiju-mkbwt": "/usr/local/bin/kaiju-mkbwt", "kaiju-mkfmi": "/usr/local/bin/kaiju-mkfmi", "kaiju-multi": "/usr/local/bin/kaiju-multi", "kaiju-taxonlistEuk.tsv": "/usr/local/bin/kaiju-taxonlistEuk.tsv", "kaiju2krona": "/usr/local/bin/kaiju2krona", "kaiju2table": "/usr/local/bin/kaiju2table", "kaijup": "/usr/local/bin/kaijup", "kaijux": "/usr/local/bin/kaijux", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kaiju.
shpc-registry automated BioContainers addition for kaiju
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kaiju
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kaiju:1.10.0--h43eeafb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kaiju/1.10.0--h43eeafb_0
$ module help quay.io/biocontainers/kaiju/1.10.0--h43eeafb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kaiju-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kaiju-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kaiju-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kaiju-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kaiju-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kaiju-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kaiju

```bash
$ singularity exec <container> /usr/local/bin/kaiju
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-addTaxonNames

```bash
$ singularity exec <container> /usr/local/bin/kaiju-addTaxonNames
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-addTaxonNames   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-addTaxonNames   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-convertMAR.py

```bash
$ singularity exec <container> /usr/local/bin/kaiju-convertMAR.py
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-convertMAR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-convertMAR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-convertNR

```bash
$ singularity exec <container> /usr/local/bin/kaiju-convertNR
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-convertNR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-convertNR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-excluded-accessions.txt

```bash
$ singularity exec <container> /usr/local/bin/kaiju-excluded-accessions.txt
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-excluded-accessions.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-excluded-accessions.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-gbk2faa.pl

```bash
$ singularity exec <container> /usr/local/bin/kaiju-gbk2faa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-gbk2faa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-gbk2faa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-makedb

```bash
$ singularity exec <container> /usr/local/bin/kaiju-makedb
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-makedb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-makedb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-mergeOutputs

```bash
$ singularity exec <container> /usr/local/bin/kaiju-mergeOutputs
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-mergeOutputs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-mergeOutputs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-mkbwt

```bash
$ singularity exec <container> /usr/local/bin/kaiju-mkbwt
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-mkbwt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-mkbwt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-mkfmi

```bash
$ singularity exec <container> /usr/local/bin/kaiju-mkfmi
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-mkfmi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-mkfmi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-multi

```bash
$ singularity exec <container> /usr/local/bin/kaiju-multi
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju-taxonlistEuk.tsv

```bash
$ singularity exec <container> /usr/local/bin/kaiju-taxonlistEuk.tsv
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju-taxonlistEuk.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju-taxonlistEuk.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju2krona

```bash
$ singularity exec <container> /usr/local/bin/kaiju2krona
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju2krona   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju2krona   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju2table

```bash
$ singularity exec <container> /usr/local/bin/kaiju2table
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju2table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju2table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaijup

```bash
$ singularity exec <container> /usr/local/bin/kaijup
$ podman run --it --rm --entrypoint /usr/local/bin/kaijup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaijup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaijux

```bash
$ singularity exec <container> /usr/local/bin/kaijux
$ podman run --it --rm --entrypoint /usr/local/bin/kaijux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaijux   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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