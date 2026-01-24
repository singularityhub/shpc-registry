---
layout: container
name:  "quay.io/biocontainers/vitap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vitap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vitap/container.yaml"
updated_at: "2026-01-24 04:09:01.687198"
latest: "1.10--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/vitap"
aliases:
 - "VITAP"
 - "VITAP_assignment_20240731.py"
 - "VITAP_upd_20240325.py"
 - "prodigal-gv"
 - "numpy-config"
 - "seqkit"
 - "blastn_vdb"
 - "tblastn_vdb"
 - "test_pcre"
 - "diamond"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "align-columns"
 - "blst2tkns"
 - "csv2xml"
 - "disambiguate-nucleotides"
 - "download-ncbi-software"
 - "ecommon.sh"
 - "find-in-gene"
 - "fuse-ranges"
 - "hgvs2spdi"
 - "json2xml"
 - "print-columns"
 - "snp2hgvs"
 - "snp2tbl"
versions:
 - "1.5--pyh7e72e81_0"
 - "1.7--pyh7e72e81_1"
 - "1.7.1--pyh7e72e81_0"
 - "1.10--pyhdfd78af_0"
description: "singularity registry hpc automated addition for vitap"
config: {"url": "https://biocontainers.pro/tools/vitap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vitap", "latest": {"1.10--pyhdfd78af_0": "sha256:dc5ae998f8bded2c8df70f23805e439fea875d9e755968f4ee86cee1847f6dd7"}, "tags": {"1.5--pyh7e72e81_0": "sha256:507c230b06028459c242790604f846e7dff693bbb255c0c725d317088424cc25", "1.7--pyh7e72e81_1": "sha256:97c23e032e2f31bcf1eed0a87402e42b6dcf0bd9f384cb7c3b3ac320de222442", "1.7.1--pyh7e72e81_0": "sha256:cf875d69407809b5f8a2d77519d4d896e58e89afbd29937117df309639830bb8", "1.10--pyhdfd78af_0": "sha256:dc5ae998f8bded2c8df70f23805e439fea875d9e755968f4ee86cee1847f6dd7"}, "docker": "quay.io/biocontainers/vitap", "aliases": {"VITAP": "/usr/local/bin/VITAP", "VITAP_assignment_20240731.py": "/usr/local/bin/VITAP_assignment_20240731.py", "VITAP_upd_20240325.py": "/usr/local/bin/VITAP_upd_20240325.py", "prodigal-gv": "/usr/local/bin/prodigal-gv", "numpy-config": "/usr/local/bin/numpy-config", "seqkit": "/usr/local/bin/seqkit", "blastn_vdb": "/usr/local/bin/blastn_vdb", "tblastn_vdb": "/usr/local/bin/tblastn_vdb", "test_pcre": "/usr/local/bin/test_pcre", "diamond": "/usr/local/bin/diamond", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml", "disambiguate-nucleotides": "/usr/local/bin/disambiguate-nucleotides", "download-ncbi-software": "/usr/local/bin/download-ncbi-software", "ecommon.sh": "/usr/local/bin/ecommon.sh", "find-in-gene": "/usr/local/bin/find-in-gene", "fuse-ranges": "/usr/local/bin/fuse-ranges", "hgvs2spdi": "/usr/local/bin/hgvs2spdi", "json2xml": "/usr/local/bin/json2xml", "print-columns": "/usr/local/bin/print-columns", "snp2hgvs": "/usr/local/bin/snp2hgvs", "snp2tbl": "/usr/local/bin/snp2tbl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vitap.
singularity registry hpc automated addition for vitap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vitap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vitap:1.10--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vitap/1.10--pyhdfd78af_0
$ module help quay.io/biocontainers/vitap/1.10--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vitap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vitap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vitap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vitap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vitap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vitap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### VITAP

```bash
$ singularity exec <container> /usr/local/bin/VITAP
$ podman run --it --rm --entrypoint /usr/local/bin/VITAP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VITAP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### VITAP_assignment_20240731.py

```bash
$ singularity exec <container> /usr/local/bin/VITAP_assignment_20240731.py
$ podman run --it --rm --entrypoint /usr/local/bin/VITAP_assignment_20240731.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VITAP_assignment_20240731.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### VITAP_upd_20240325.py

```bash
$ singularity exec <container> /usr/local/bin/VITAP_upd_20240325.py
$ podman run --it --rm --entrypoint /usr/local/bin/VITAP_upd_20240325.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VITAP_upd_20240325.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal-gv

```bash
$ singularity exec <container> /usr/local/bin/prodigal-gv
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/blastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/tblastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blst2tkns

```bash
$ singularity exec <container> /usr/local/bin/blst2tkns
$ podman run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2xml

```bash
$ singularity exec <container> /usr/local/bin/csv2xml
$ podman run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disambiguate-nucleotides

```bash
$ singularity exec <container> /usr/local/bin/disambiguate-nucleotides
$ podman run --it --rm --entrypoint /usr/local/bin/disambiguate-nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disambiguate-nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-ncbi-software

```bash
$ singularity exec <container> /usr/local/bin/download-ncbi-software
$ podman run --it --rm --entrypoint /usr/local/bin/download-ncbi-software   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-ncbi-software   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecommon.sh

```bash
$ singularity exec <container> /usr/local/bin/ecommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ecommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-in-gene

```bash
$ singularity exec <container> /usr/local/bin/find-in-gene
$ podman run --it --rm --entrypoint /usr/local/bin/find-in-gene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-in-gene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-ranges

```bash
$ singularity exec <container> /usr/local/bin/fuse-ranges
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-ranges   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-ranges   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hgvs2spdi

```bash
$ singularity exec <container> /usr/local/bin/hgvs2spdi
$ podman run --it --rm --entrypoint /usr/local/bin/hgvs2spdi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hgvs2spdi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### json2xml

```bash
$ singularity exec <container> /usr/local/bin/json2xml
$ podman run --it --rm --entrypoint /usr/local/bin/json2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/json2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print-columns

```bash
$ singularity exec <container> /usr/local/bin/print-columns
$ podman run --it --rm --entrypoint /usr/local/bin/print-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp2hgvs

```bash
$ singularity exec <container> /usr/local/bin/snp2hgvs
$ podman run --it --rm --entrypoint /usr/local/bin/snp2hgvs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp2hgvs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp2tbl

```bash
$ singularity exec <container> /usr/local/bin/snp2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/snp2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
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