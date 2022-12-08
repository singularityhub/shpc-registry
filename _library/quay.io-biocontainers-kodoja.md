---
layout: container
name:  "quay.io/biocontainers/kodoja"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kodoja/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kodoja/container.yaml"
updated_at: "2022-12-08 03:27:47.557011"
latest: "0.0.10--0"
container_url: "https://biocontainers.pro/tools/kodoja"
aliases:
 - "addTaxonNames"
 - "convertNR"
 - "convert_mar_to_kaiju.py"
 - "database_modules.py"
 - "diagnostic_modules.py"
 - "gbk2faa.pl"
 - "kaiju"
 - "kaiju2krona"
 - "kaijuReport"
 - "kaijup"
 - "kaijux"
 - "kodoja_build.py"
 - "kodoja_retrieve.py"
 - "kodoja_search.py"
 - "kraken"
 - "kraken-build"
 - "kraken-filter"
 - "kraken-mpa-report"
 - "kraken-report"
 - "kraken-translate"
 - "makeDB.sh"
 - "mergeOutputs"
 - "mkbwt"
 - "mkfmi"
 - "ncbi-genome-download"
 - "ngd"
 - "taxonlist.tsv"
 - "conv-template"
 - "from-template"
 - "fastqc"
 - "trimmomatic"
 - "jellyfish"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
versions:
 - "0.0.9--0"
 - "0.0.10--0"
description: "shpc-registry automated BioContainers addition for kodoja"
config: {"url": "https://biocontainers.pro/tools/kodoja", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kodoja", "latest": {"0.0.10--0": "sha256:9f5fd786ee3e5a77f8a7159243c08ff64778dcadb534981b47683287cc7b92a5"}, "tags": {"0.0.9--0": "sha256:5d1c1cc0e1793497e177e0241945e7de65c3897239305a1bee21970e5d3c8db9", "0.0.10--0": "sha256:9f5fd786ee3e5a77f8a7159243c08ff64778dcadb534981b47683287cc7b92a5"}, "docker": "quay.io/biocontainers/kodoja", "aliases": {"addTaxonNames": "/usr/local/bin/addTaxonNames", "convertNR": "/usr/local/bin/convertNR", "convert_mar_to_kaiju.py": "/usr/local/bin/convert_mar_to_kaiju.py", "database_modules.py": "/usr/local/bin/database_modules.py", "diagnostic_modules.py": "/usr/local/bin/diagnostic_modules.py", "gbk2faa.pl": "/usr/local/bin/gbk2faa.pl", "kaiju": "/usr/local/bin/kaiju", "kaiju2krona": "/usr/local/bin/kaiju2krona", "kaijuReport": "/usr/local/bin/kaijuReport", "kaijup": "/usr/local/bin/kaijup", "kaijux": "/usr/local/bin/kaijux", "kodoja_build.py": "/usr/local/bin/kodoja_build.py", "kodoja_retrieve.py": "/usr/local/bin/kodoja_retrieve.py", "kodoja_search.py": "/usr/local/bin/kodoja_search.py", "kraken": "/usr/local/bin/kraken", "kraken-build": "/usr/local/bin/kraken-build", "kraken-filter": "/usr/local/bin/kraken-filter", "kraken-mpa-report": "/usr/local/bin/kraken-mpa-report", "kraken-report": "/usr/local/bin/kraken-report", "kraken-translate": "/usr/local/bin/kraken-translate", "makeDB.sh": "/usr/local/bin/makeDB.sh", "mergeOutputs": "/usr/local/bin/mergeOutputs", "mkbwt": "/usr/local/bin/mkbwt", "mkfmi": "/usr/local/bin/mkfmi", "ncbi-genome-download": "/usr/local/bin/ncbi-genome-download", "ngd": "/usr/local/bin/ngd", "taxonlist.tsv": "/usr/local/bin/taxonlist.tsv", "conv-template": "/usr/local/bin/conv-template", "from-template": "/usr/local/bin/from-template", "fastqc": "/usr/local/bin/fastqc", "trimmomatic": "/usr/local/bin/trimmomatic", "jellyfish": "/usr/local/bin/jellyfish", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kodoja.
shpc-registry automated BioContainers addition for kodoja
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kodoja
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kodoja:0.0.10--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kodoja/0.0.10--0
$ module help quay.io/biocontainers/kodoja/0.0.10--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kodoja-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kodoja-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kodoja-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kodoja-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kodoja-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kodoja-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addTaxonNames

```bash
$ singularity exec <container> /usr/local/bin/addTaxonNames
$ podman run --it --rm --entrypoint /usr/local/bin/addTaxonNames   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addTaxonNames   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertNR

```bash
$ singularity exec <container> /usr/local/bin/convertNR
$ podman run --it --rm --entrypoint /usr/local/bin/convertNR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertNR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_mar_to_kaiju.py

```bash
$ singularity exec <container> /usr/local/bin/convert_mar_to_kaiju.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_mar_to_kaiju.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_mar_to_kaiju.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### database_modules.py

```bash
$ singularity exec <container> /usr/local/bin/database_modules.py
$ podman run --it --rm --entrypoint /usr/local/bin/database_modules.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/database_modules.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diagnostic_modules.py

```bash
$ singularity exec <container> /usr/local/bin/diagnostic_modules.py
$ podman run --it --rm --entrypoint /usr/local/bin/diagnostic_modules.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diagnostic_modules.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbk2faa.pl

```bash
$ singularity exec <container> /usr/local/bin/gbk2faa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gbk2faa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbk2faa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju

```bash
$ singularity exec <container> /usr/local/bin/kaiju
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju2krona

```bash
$ singularity exec <container> /usr/local/bin/kaiju2krona
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju2krona   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju2krona   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaijuReport

```bash
$ singularity exec <container> /usr/local/bin/kaijuReport
$ podman run --it --rm --entrypoint /usr/local/bin/kaijuReport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaijuReport   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### kodoja_build.py

```bash
$ singularity exec <container> /usr/local/bin/kodoja_build.py
$ podman run --it --rm --entrypoint /usr/local/bin/kodoja_build.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kodoja_build.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kodoja_retrieve.py

```bash
$ singularity exec <container> /usr/local/bin/kodoja_retrieve.py
$ podman run --it --rm --entrypoint /usr/local/bin/kodoja_retrieve.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kodoja_retrieve.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kodoja_search.py

```bash
$ singularity exec <container> /usr/local/bin/kodoja_search.py
$ podman run --it --rm --entrypoint /usr/local/bin/kodoja_search.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kodoja_search.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken

```bash
$ singularity exec <container> /usr/local/bin/kraken
$ podman run --it --rm --entrypoint /usr/local/bin/kraken   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-build

```bash
$ singularity exec <container> /usr/local/bin/kraken-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-filter

```bash
$ singularity exec <container> /usr/local/bin/kraken-filter
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-mpa-report

```bash
$ singularity exec <container> /usr/local/bin/kraken-mpa-report
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-report

```bash
$ singularity exec <container> /usr/local/bin/kraken-report
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-translate

```bash
$ singularity exec <container> /usr/local/bin/kraken-translate
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeDB.sh

```bash
$ singularity exec <container> /usr/local/bin/makeDB.sh
$ podman run --it --rm --entrypoint /usr/local/bin/makeDB.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeDB.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeOutputs

```bash
$ singularity exec <container> /usr/local/bin/mergeOutputs
$ podman run --it --rm --entrypoint /usr/local/bin/mergeOutputs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeOutputs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkbwt

```bash
$ singularity exec <container> /usr/local/bin/mkbwt
$ podman run --it --rm --entrypoint /usr/local/bin/mkbwt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkbwt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkfmi

```bash
$ singularity exec <container> /usr/local/bin/mkfmi
$ podman run --it --rm --entrypoint /usr/local/bin/mkfmi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkfmi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi-genome-download

```bash
$ singularity exec <container> /usr/local/bin/ncbi-genome-download
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngd

```bash
$ singularity exec <container> /usr/local/bin/ngd
$ podman run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonlist.tsv

```bash
$ singularity exec <container> /usr/local/bin/taxonlist.tsv
$ podman run --it --rm --entrypoint /usr/local/bin/taxonlist.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonlist.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conv-template

```bash
$ singularity exec <container> /usr/local/bin/conv-template
$ podman run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from-template

```bash
$ singularity exec <container> /usr/local/bin/from-template
$ podman run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmomatic

```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhat

```bash
$ singularity exec <container> /usr/local/bin/jhat
$ podman run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsadebugd

```bash
$ singularity exec <container> /usr/local/bin/jsadebugd
$ podman run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
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